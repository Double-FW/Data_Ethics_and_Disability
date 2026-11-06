# AGENTS.md — Operating guidance for agents

## Purpose and scope

This repository provides policy, research, and governance guidance for the ethical use of data relating to disabled people. These instructions apply to any human or automated agent that reads, edits, applies, or operationalises this repository's material—including work in data ethics, accessibility, research, HR, product and service management, procurement, analytics, AI, communications, customer support, and other business processes that may affect people.

Use the repository's substantive documents as companion guidance:

- `Ethical and Inclusive Use of Data Relating to Disabled People.md` — core principles for dignity, equivalence, data minimisation, aggregation, privacy, and governance.
- `Nothing_About_Us_Without_Us.md` — inclusive mainstream research, meaningful participation, proportional coverage, and influence on decisions.
- `Assistive_Technology_Data_Flows_Risks_and_Review.md` — data-flow review, assistive-technology and AI risks, referral triggers, and access continuity.
- `CUSTOMER RESEARCH FRAMEWORK.md` — a structure for analysing customer and organisational knowledge. Its proposed personas, datasets, knowledge graphs, RAG records, or training data are not permission to collect, link, infer, share, or reuse personal data.

These documents are guidance, not legal advice, a substitute for applicable law or standards, or automatic approval for a particular project. Check current authoritative requirements and obtain qualified human review when needed. Do not silently turn a recommendation, example, or research prompt into a legal requirement or a validated scoring system.

## Non-negotiable principles

1. **Nothing about people without meaningful involvement.** Involve affected Deaf, disabled, and neurodivergent people early enough to shape questions, interpretation, design, and decisions. Make participation accessible, voluntary, appropriately supported, and fairly compensated. Attendance alone is not influence; document what changed and what did not.
2. **Improve barriers, not profiles.** Seek evidence about barriers, service outcomes, and user-chosen preferences. Do not identify, track, classify, or build persistent profiles of disabled people where aggregate or less intrusive evidence can answer the question.
3. **Equivalence includes dignity and agency.** Assess functional and informational access as well as comparable confidence, privacy, safety, independence, respect, and satisfaction. Task completion alone does not demonstrate an equivalent experience.
4. **Minimise and protect data.** Define a specific purpose before collection; collect only what is necessary; separate identity, recruitment/access arrangements, and research findings where practical; restrict access; set retention and deletion; and prefer safe aggregation. Pseudonymised data is not necessarily anonymous. Small groups, quotations, timestamps, and joined attributes can re-identify people.
5. **Do not infer disability or health from proxies.** Accessibility settings, assistive-technology use, interaction patterns, voice, gaze, or behaviour are not proof of a diagnosis or identity. Do not use them for advertising, eligibility, pricing, hiring, performance, discipline, or other consequential treatment.
6. **Access must not be conditional on surveillance.** Do not make an accommodation, assistive feature, or basic service contingent on optional tracking, marketing, analytics, or model-training reuse. Address privacy risks without removing effective access; provide an accessible alternative and involve affected users.
7. **Be transparent about uncertainty and power.** Distinguish observed facts, participant accounts, interpretations, hypotheses, supplier claims, and verified behaviour. State evidence limits, disagreements, missing perspectives, and possible harms. Never present uncertain findings as universal truths about a group.
8. **Human accountability.** Agents may organise evidence, draft options, and identify review triggers. A named, authorised human owner must make and document decisions that affect people's rights, access, employment, safety, or significant opportunities. An agent must not claim legal, clinical, HR, or accessibility clearance.

## Required workflow for work that may affect people

Before recommending or taking action:

1. **Define the decision and benefit.** State the business or user problem, who may benefit or be harmed, affected groups (including non-users and people excluded by current processes), the intended outcome, and why data or automation is needed. Consider a non-data or less intrusive alternative.
2. **Map people, process, and authority.** Identify the service or employment context, decision owner, affected people, data sources, recipients, systems, vendors, integrations, and any downstream decisions. Check whether information could flow between research, customer, HR, performance, marketing, analytics, or AI systems.
3. **Map data and evidence.** For each data element, record purpose, source, sensitivity, collection method, identifiers and linkage, access, processing location, recipients/subprocessors, retention, deletion, secondary use, and evidence source/date/scope. Mark each material fact `yes`, `no`, `unknown`, or `conflicting`. Unknown is not evidence of safety or approval.
4. **Plan meaningful participation and access.** Include affected people in mainstream research, not only specialist accessibility studies. Use an appropriate audience benchmark for quantitative targets or a reasoned breadth plan for qualitative work; do not invent universal percentages. Provide accessible recruitment, consent, materials, communication, scheduling, breaks, payment, and withdrawal information. Record coverage gaps and how they constrain conclusions.
5. **Assess outcomes and alternatives.** Examine access, task success, information parity, effort, agency, dignity, confidence, safety, trust, and satisfaction across relevant needs and contexts. Check for trade-offs between groups, non-response, abandonment, and harms caused by the proposed mitigation itself.
6. **Apply controls and route concerns.** Minimise, separate, aggregate, restrict, secure, and time-limit data. For unknown or conflicting flows, sensitive data, re-identification, profiling, AI reuse, monitoring, inaccessible controls, or consequential decisions, pause the affected processing or decision and route to the relevant human specialists (privacy/data protection, security, accessibility, research ethics, HR, legal, procurement, clinical/psychometric, safeguarding, or service owner). Apply all relevant referrals; do not let an agent resolve its own escalation.
7. **Make and record a human decision.** Record the accountable owner, evidence and its limits, affected perspectives, options considered, rationale, safeguards, residual risks, interim action, approval conditions, review/expiry date, and appeal or correction route. “Reviewed” or “low risk” is not legal clearance.
8. **Monitor and revisit.** Validate with affected people and appropriate technical checks before and after deployment. Reassess after changes to feature, model, supplier, contract, configuration, region, data flow, purpose, or business process. Track adverse outcomes and barriers, not just aggregate completion. Report incidents through approved channels.

## Additional safeguards for HR and other consequential processes

Hiring, promotion, performance management, compensation, discipline, accommodation, eligibility, access to essential services, and similar decisions require heightened care.

- Never infer disability, neurotype, health, capacity, honesty, attention, emotion, or suitability from assistive technology, behaviour, biometrics, or proxy signals.
- Do not let an agent make or silently rank consequential decisions, recommend adverse treatment from sensitive or inferred attributes, or treat an unvalidated score as objective evidence. Do not use disability data to screen people out.
- Before any assessment or algorithm is used, require a qualified human owner to establish that the measure is relevant to the actual role or purpose, supported for the intended population and conditions, and appropriate with assistive technology and reasonable adjustments. Refer psychometric questions to a qualified psychologist/psychometrician and employment questions to HR, accessibility/equality, privacy, and legal specialists as applicable.
- Separate accommodation and case-handling records from research, routine management, and performance data. Explain the actual confidentiality and access boundaries; do not promise anonymity if identities can be linked.
- Offer accessible alternatives, human review, correction, and an effective appeal. A privacy or security control must not remove necessary access without an equivalent workable option.

## Assistive technology, AI, vendors, and data reuse

Treat labels such as “assistive,” “accessibility,” “anonymous,” “on-device,” “enterprise,” or “AI-powered” as claims to verify, not proof. For each feature and deployed configuration, establish what it can access; what is processed locally or remotely; what leaves the device; recipients and subprocessors; identifiers; human access; logs and retention; training/evaluation use; deletion limits; and changes by account tier, region, or integration.

Use synthetic data and authorised testing for data-flow checks. Do not covertly monitor employees or customers, fingerprint assistive technology, capture real sensitive screens or meetings for testing, or upload confidential data to unapproved AI tools. Encryption, removal of names, a vendor assurance, or a “no training” statement alone does not establish anonymity, absence of transmission, or suitability. Obtain feature- and contract-specific evidence.

Participation consent does not automatically authorise publication, onward sharing, model training, or a new purpose. Do not put identifiable or sensitive participant material into external AI systems or broadly accessible repositories without the required permissions, safeguards, and specialist review. Never promise that withdrawal can undo model learning or eliminate every copy unless that is substantiated.

## Stop, escalate, and preserve access

Stop the proposed collection, linkage, disclosure, automated recommendation, or consequential decision and escalate when any of the following applies:

- The purpose, data flow, recipient, retention, legal/ethical basis, or decision owner is unknown or disputed.
- Data may reveal disability, health, identity, confidential employment/customer information, or a person's identity through small-group reporting or linkage.
- A system infers a sensitive trait, monitors people, uses biometrics, or affects hiring, performance, eligibility, pricing, discipline, or essential access.
- Research participation is inaccessible, coerced, unpaid where payment is appropriate, or lacks meaningful influence; evidence gaps are being hidden or overstated.
- A vendor's actual feature, subprocessor, region, configuration, or reuse differs from what was reviewed; data appears in an unexpected destination; or an incident may have occurred.
- A proposed privacy, security, or operational response could remove effective access, accommodation, communication, or support.

Escalation is not an instruction to abandon people who rely on an existing service. Involve the accessibility owner and affected users promptly, contain the specific risk through approved processes, and provide a safe, accessible alternative while specialists review. Do not conceal or independently investigate a suspected incident; use the organisation's incident and reporting channels.

## Documentation and repository contribution rules

When creating or changing guidance, templates, policies, or workflows:

- Preserve the repository's principles and cross-link relevant companion documents using correct relative paths.
- Label recommendations, examples, hypothetical scenarios, supplier statements, verified observations, legal requirements, and research findings distinctly. Cite sources with dates and scope; qualify jurisdictional claims and note uncertainty.
- Do not fabricate participant findings, vendor behaviour, standards requirements, sample sizes, or outcomes. Do not treat illustrative records, risk triggers, or maturity/persona scores as validated instruments.
- Use respectful, specific language; do not homogenise disabled people or imply that one participant represents a whole group. Keep identity, functional need, preference, and context distinct.
- Avoid publishing personal or confidential information. Use fictional/synthetic examples; review quotations and small-cell breakdowns for re-identification risk.
- Make documents and forms accessible: meaningful headings, descriptive links, readable tables, plain language where suitable, and accessible alternatives for any essential process.
- For a proposed change, explain the rationale, evidence, audience, safeguards, owner, unresolved questions, and review date. Do not weaken an existing safeguard without documenting the trade-off and obtaining appropriate human review.

## Quick review checklist

Before an agent's work is used, confirm:

- [ ] A defined benefit and purpose justify the proposed action and data.
- [ ] Affected people can influence the work and participate accessibly.
- [ ] Collection, linkage, access, retention, sharing, and AI use are minimised and evidenced.
- [ ] No disability or other sensitive trait is inferred or used for consequential treatment.
- [ ] Outcomes include dignity, agency, privacy, safety, information parity, and experience—not only task completion.
- [ ] Evidence gaps, disagreement, uncertainty, and re-identification risk are explicit.
- [ ] Relevant specialists and an accountable human decision owner are identified.
- [ ] Effective access, accommodation, human review, and appeal remain available.
- [ ] Decisions, controls, residual risks, actions, and review timing are documented.

If a material answer is no, unknown, or conflicting, do not represent the work as approved or complete; take the least harmful safe interim action and escalate to the accountable human owner.
