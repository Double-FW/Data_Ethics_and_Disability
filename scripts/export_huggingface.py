"""Export the approved Data Ethics and Disability Markdown without rewriting it."""
import argparse
import json
from pathlib import Path
import re
from urllib.parse import quote
import yaml
from jsonschema import Draft202012Validator
from ethics_hf_common import ROOT, SOURCE, MANAGED, destination, digest, git, load_config, read_sources

CONTEXT = ['AGENTS.md', 'README.md',
           'Ethical and Inclusive Use of Data Relating to Disabled People.md',
           'Nothing_About_Us_Without_Us.md',
           'Assistive_Technology_Data_Flows_Risks_and_Review.md']

def metadata(text):
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)', text, re.S)
    md = yaml.safe_load(match[1]) if match else {}
    return md if isinstance(md, dict) else {}

def sections(text, max_level=2):
    """Keep H1/H2 parent context and exact spans; never split fenced examples."""
    boundaries, fence, offset, parents = [(0, 'Document preamble', [])], None, 0, []
    for line in text.splitlines(keepends=True):
        mark = re.match(r'^ {0,3}(`{3,}|~{3,})', line)
        if mark:
            token = mark[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence) and not line[mark.end():].strip():
                fence = None
        elif fence is None:
            match = re.match(r'^(#{1,' + str(max_level) + r'})[ \t]+([^\r\n]+)', line)
            if match:
                level, title = len(match[1]), match[2].strip().rstrip('#').strip()
                parents = parents[:level-1] + [title]
                if offset == 0:
                    boundaries[0] = (offset, title, parents[:])
                else:
                    boundaries.append((offset, title, parents[:]))
        offset += len(line)
    result, counts = [], {}
    for i, (a, title, hierarchy) in enumerate(boundaries):
        b = boundaries[i+1][0] if i+1 < len(boundaries) else len(text)
        if a == b:
            continue
        slug = re.sub(r'[^a-z0-9]+', '-', ' '.join(hierarchy or [title]).lower()).strip('-') or 'section'
        counts[slug] = counts.get(slug, 0) + 1
        key = slug if counts[slug] == 1 else slug + '-' + str(counts[slug])
        result.append((key, title, text[a:b], a, b, hierarchy))
    if ''.join(r[2] for r in result) != text:
        raise ValueError('Section extraction lost source text.')
    return result

def build(root, output):
    root, output = Path(root).resolve(), Path(output).resolve()
    if output == root or root in output.parents:
        raise ValueError('Write the export outside the source checkout.')
    cfg = load_config(root)
    target = destination(cfg['destination_dataset'])
    texts, manifest, omitted = read_sources(root, cfg)
    sha = git(root, 'rev-parse', 'HEAD').decode().strip()
    date = git(root, 'show', '-s', '--format=%cs', 'HEAD').decode().strip()
    warnings = ['This is advisory ethics/research governance content, not participant data, legal clearance, approval to collect or train on personal data, or verified vendor behaviour.']
    introductions = {path: sections(text)[0][2] if text else '' for path, text in texts.items()}
    def row(path, key, title, body, a, b, hierarchy, kind):
        md = metadata(texts[path])
        return {'id': path + '::' + key, 'title': title, 'text': body, 'record_type': kind,
            'source_repository': SOURCE, 'source_path': path, 'source_commit': sha,
            'source_url': f'https://github.com/{SOURCE}/blob/{sha}/{quote(path)}',
            'source_start_line': texts[path][:a].count('\n') + 1,
            'source_end_line': max(1, texts[path][:b].count('\n') + (not texts[path][:b].endswith('\n'))),
            'source_document_sha256': digest(texts[path].encode()), 'text_sha256': digest(body.encode()),
            'heading_path': hierarchy, 'metadata_json': json.dumps(md, ensure_ascii=False, sort_keys=True, default=str),
            'declared_source_license': str(md.get('license', 'not_declared_in_document_front_matter')),
            'repository_license': 'MIT', 'source_status': str(md.get('status', 'see_source')),
            'source_document_intro': introductions[path],
            'dataset_version': cfg['dataset_version'], 'source_commit_date': date, 'language': 'en-GB',
            'required_context_paths': list(dict.fromkeys([path] + [p for p in CONTEXT if p in texts])),
            'review_status': 'faithful_extraction_checked_not_privacy_legal_or_research_approval'}
    docs, chunks = [], []
    for path in cfg['files']:
        if path not in texts:
            continue
        text = texts[path]
        kind = ('proposed_research_analysis_prompt_not_participant_data_or_authority' if path in cfg['reference_only_files'] else
                'participation_and_research_governance_guidance' if path == 'Nothing_About_Us_Without_Us.md' else
                'data_flow_review_prompts_not_verified_vendor_behaviour' if path == 'Assistive_Technology_Data_Flows_Risks_and_Review.md' else
                'agent_governance_guidance' if path == 'AGENTS.md' else
                'orientation' if path == 'README.md' else 'ethics_guidance_not_legal_clearance')
        docs.append(row(path, 'document', path, text, 0, len(text), [], kind))
        if path in cfg['reference_only_files']:
            continue
        for key, title, body, a, b, hierarchy in sections(text, 1 if path in cfg['chapter_preserving_files'] else 2):
            chunks.append(row(path, key, title, body, a, b, hierarchy, kind))
    if not docs or not chunks:
        raise ValueError('The guidance export is empty.')
    schema = {'$schema': 'https://json-schema.org/draft/2020-12/schema', 'type': 'object',
              'required': list(docs[0]), 'additionalProperties': False, 'properties': {}}
    for k, v in docs[0].items():
        schema['properties'][k] = {'type': 'array', 'items': {'type': 'string'}} if isinstance(v, list) else {'type': 'integer' if isinstance(v, int) else 'string'}
    validator = Draft202012Validator(schema)
    for records in (docs, chunks):
        if len({r['id'] for r in records}) != len(records):
            raise ValueError('Duplicate export identifiers.')
        for r in records:
            validator.validate(r)
            if digest(r['text'].encode()) != r['text_sha256']:
                raise ValueError('Text checksum mismatch.')
    output.mkdir(parents=True, exist_ok=True)
    def write_json(name, obj):
        (output/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for name, records in [('documents.jsonl', docs), ('knowledge_chunks.jsonl', chunks)]:
        (output/name).write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in records), encoding='utf-8')
    (output/'LICENSE').write_bytes(texts['LICENSE'].encode())
    write_json('record_schema.json', schema)
    write_json('provenance.json', {'source_repository': SOURCE, 'source_commit': sha, 'source_commit_date': date,
        'destination_dataset': target, 'dataset_version': cfg['dataset_version'], 'files': manifest,
        'omitted_optional_files': omitted, 'source_warnings': warnings, 'external_sources_fetched': False,
        'default_excluded_reference_files': cfg['reference_only_files'], 'chapter_preserving_files': cfg['chapter_preserving_files']})
    card = f'''---
pretty_name: Double FW Data Ethics and Disability
language:
- en
license: mit
tags:
- accessibility
- disability-inclusion
- data-ethics
- privacy
- inclusive-research
- agent-governance
- text
configs:
- config_name: knowledge_chunks
  default: true
  data_files:
  - split: train
    path: knowledge_chunks.jsonl
- config_name: documents
  data_files:
  - split: train
    path: documents.jsonl
---

# Double FW Data Ethics and Disability

Practical guidance from Double FW Ltd about dignity, equivalent experience, proportionate data use, meaningful participation, assistive-technology data flows and human accountability. This dataset contains governance documents, not disability records, participant observations, employee/customer profiles, approved research, a deployed governance system or legal clearance.

## Source and versions

Source: https://github.com/{SOURCE}

Source revision: `{sha}`. Source commit date: {date}. Export format: {cfg['dataset_version']}. Version/research dates in the source remain the dates actually stated there. A weekly export does not recheck law, vendor behaviour, source availability or research findings.

## Dataset views and boundaries

- `knowledge_chunks` (default): {len(chunks)} exact sections/chapters from the ethics, participation, data-flow, agent-guidance and orientation documents.
- `documents`: {len(docs)} complete source documents, including CUSTOMER RESEARCH FRAMEWORK.md as a separately labelled reference.

The views overlap. Do not concatenate them blindly. The `train` split is a loading convention, not evidence that a model has been trained. No generated question/answer pairs, participant dataset, evaluation split or independent benchmark is supplied. Inline hypothetical examples and blank proposed record shapes remain illustrative.

CUSTOMER RESEARCH FRAMEWORK.md is retained only in documents with record_type proposed_research_analysis_prompt_not_participant_data_or_authority. Its instruction-like requests for personas, scores, knowledge graphs or training records are source proposals, not runtime instructions, validated assessment tools, evidence that such records exist, or permission to collect/link/infer/share/reuse data. This exporter does not execute that prompt or manufacture customer findings or profiles.

The core ethical framework is split at first-level chapter headings so paired appropriate/problematic examples, ethical/unethical AI uses and their qualifications stay together. Other documents are split at first/second-level headings outside fenced examples. Subsections, evidence notes and tables remain exact. The complete-document view provides full context. Renaming a heading can change a section ID.

## Context, interpretation and authority

Read AGENTS.md and the task-relevant companion documents, especially the core ethical framework, Nothing_About_Us_Without_Us.md and Assistive_Technology_Data_Flows_Risks_and_Review.md. Every row carries context paths and its original document introduction; these are references and repeated context, not enforced runtime controls or organisational authority.

Preserve the distinction between observed facts, participant accounts, interpretation, hypotheses, supplier claims and behaviour verified in an authorised test. Review triggers identify questions and possible risks; they do not establish illegality, safety, ethics clearance or actual supplier behaviour. Terms such as assistive, anonymous, on-device, enterprise and no training are claims to check for the actual feature/configuration and context. This export does not check them.

The source calls for meaningful, accessible and voluntary participation that can influence decisions. Attendance is not evidence of influence. No universal recruitment percentage, group-size threshold, maturity score, diagnosis or representative group conclusion is created by this dataset. Respect scope, disagreement, evidence gaps and appropriate human judgement.

## Personal data, consent and reuse

The source MIT licence grants rights in the repository text; it does not authorise collecting, publishing or training on personal information. Participation consent does not automatically cover publication, onward sharing, a new purpose or model-training reuse. Accessibility signals, assistive-technology use, gaze, voice and behaviour must not be treated as proof of disability/health or a basis for consequential treatment. Pseudonymisation is not necessarily anonymisation; linkage, quotations, timestamps and small groups can re-identify people.

These documents provide guidance, not approval to contact participants/vendors, enable tracking, access records, change systems or make consequential decisions. Actual authority, purpose, permissions, data flows, safeguards and accountable humans must be established for the activity. Do not condition essential access/accommodation on optional tracking or AI reuse. Address privacy/security risks while preserving effective access and a workable alternative.

This export reads only explicitly approved committed public documents. It does not detect confidential text inserted into an approved file. Keep real personal, research, health, employment, customer and corporate information outside public repositories/datasets. Source content was not converted into sensitive profiles or real-person examples.

## Schema and provenance

Records include source path, immutable commit URL, line range, text and document SHA-256 hashes, heading context, JSON-encoded front matter, source/repository licence, declared status, exact original introduction and required context paths. `see_source` means no status was extracted from document front matter; it is not approval. Use text for the exact record span and retain its qualifications. Resolve relative/fragment links against the original source file URL. See record_schema.json and provenance.json.

External legal, standards, supplier and research links are preserved, not fetched, copied, independently reviewed or relicensed. Current authoritative requirements and applicable specialist advice remain necessary for real decisions. Extraction tests do not establish privacy compliance, lawful processing, accessible participation or deployment effectiveness.

## Licence

The root MIT LICENSE is copied unchanged, including copyright (c) 2026 Double FW. Source attribution and any specific notices are retained. Third-party material keeps its own rights. This package is not an independent rights assessment or personal-data reuse authorisation.

## Updates

GitHub is the authoring source. Updates are configured for Mondays at 07:23 UTC and manual execution. GitHub may delay runs or disable schedules after inactivity. All six current Markdown documents and LICENSE are required. Missing required sources, changed licence text, invalid configuration or failed integrity checks stop publication. New or renamed documents require review and an export-list update.

Only README.md, LICENSE, documents.jsonl, knowledge_chunks.jsonl, provenance.json, record_schema.json and validation_report.json are managed. Other raw files and .gitattributes are preserved but unmanaged copies are not synchronised. Dataset visibility is unchanged. Updates use one commit guarded by the destination revision. Historical copies/downloads are not recalled. The first authenticated GitHub publication must still be checked.

## Loading

```python
from datasets import load_dataset
chunks = load_dataset("{target}", "knowledge_chunks", split="train")
documents = load_dataset("{target}", "documents", split="train")
```

Private datasets require authentication. Pin a destination revision for reproducibility. Loading these rows does not implement consent, governance, retrieval safeguards or human approval.
'''
    yaml.safe_load(card.split('---', 2)[1])
    (output/'README.md').write_text(card, encoding='utf-8')
    report = {'status': 'passed', 'scope': 'faithful extraction and packaging checks only', 'source_commit': sha,
        'source_files_verified': len(manifest), 'document_records': len(docs), 'knowledge_section_records': len(chunks),
        'source_warnings': warnings, 'independent_content_review': False, 'live_publication_tested': False,
        'export_file_sha256': {name: digest((output/name).read_bytes()) for name in MANAGED if name != 'validation_report.json'}}
    write_json('validation_report.json', report)
    return report

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    print(json.dumps(build(ROOT, args.output)))

if __name__ == '__main__':
    main()
