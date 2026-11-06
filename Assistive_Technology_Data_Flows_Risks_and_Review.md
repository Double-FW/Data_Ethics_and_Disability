# Assistive Technology, Data Gathering and Return Paths

## Opportunities, risks and specialist review triggers for accessibility programmes

**Double FW Ltd · Version 1.0 · Research checked 6 November 2026**  
**Companion guidance for Data Ethics and Disability**

## Purpose and relationship to existing guidance

Assistive technology can enable independence, communication, learning and participation. Some features process information entirely on a device; others transmit text, images, audio, interaction events or diagnostics to another service. A useful access feature may therefore also create a route by which personal, corporate or third-party information leaves its original context.

This document helps accessibility programmes identify those routes, evaluate benefits and recognise when privacy, security, assessment, clinical or legal expertise is needed. It provides operational guidance and referral prompts, not legal advice, a compliance determination or an assessment of any named supplier's lawfulness.

Read it alongside:

- [Ethical and Inclusive Use of Data Relating to Disabled People](./Ethical%20and%20Inclusive%20Use%20of%20Data%20Relating%20to%20Disabled%20People.md): the governing principles of dignity, equivalence, minimum necessary collection, aggregation, accessibility signals and responsible AI use.
- [Nothing About Us Without Us](./Nothing_About_Us_Without_Us.md): inclusive recruitment, meaningful influence and functional and emotional outcomes.
- [CUSTOMER RESEARCH FRAMEWORK](./CUSTOMER%20RESEARCH%20FRAMEWORK.md): structures for insight and organisational intelligence. Its proposed datasets do not themselves authorise participant-data reuse.

This guidance interprets the ethical framework's examples of unacceptable recording and extraction in their stated context of involuntary collection and misuse. It does not prohibit properly governed, voluntary research sessions or access-enabling transcription. Such activities still need a defined purpose, suitable permissions, proportionality and safeguards.

**Review the feature, deployment and data flow. The label “assistive”, “accessibility”, “anonymous”, “enterprise” or “AI-powered” is not evidence that a particular data use is safe.**

## 1. What a return path means

Here, a **return path** is a route by which information from an interaction, device or environment is sent back to a supplier, employer, service provider, researcher or other recipient. It can be essential to delivering a feature, optional telemetry, remote support, continuous monitoring or a secondary use such as training.

Separate the following questions:

| Stage | What to establish | Common misunderstanding |
| --- | --- | --- |
| Access | What can the feature read, hear, observe or control? | Permission to access a screen does not prove that its contents are uploaded |
| Processing | Does computation happen locally, remotely or through both? | “No training” does not mean “no transmission” |
| Transmission | What payload and metadata leave, to which endpoints, and when? | Encryption protects transit; the intended recipient still processes the content |
| Retention | What is kept, where, for how long, including logs, caches and backups? | No saved recording does not establish that no temporary processing occurs |
| Linkage | Which account, cookie, token, device or contextual details can identify someone? | Removing a name does not necessarily anonymise a record |
| Access and onward use | Can administrators, support staff, reviewers, subprocessors or integrations use it? | “Not public” does not mean “not shared” |
| Training and evaluation | Does any party use inputs, outputs, feedback or derived data to improve models? | An external model provider's no-training promise may not cover the tool supplier |
| Deletion | What can be removed, and what downstream effects remain? | Deleting a source file does not necessarily reverse earlier model learning |

Distinguish a technical capability, a vendor's stated practice, a contractual commitment and behaviour observed in a test. None is a substitute for the others. Treat the examples below as evidence about specific documented features, not proof about every version or deployment.

## 2. Third-party JavaScript, overlays and embedded accessibility tools

### Underlying issue

A single script reference can load a substantial externally maintained application. Code executing in the page can, within its execution context and browser controls, access page content and interaction events and send information elsewhere. This is a general third-party script risk; it is not unique to accessibility overlays. OWASP describes the trust and supply-chain implications. [S01]

Potentially exposed material includes account-specific page content, form text, URLs containing identifiers, image locations, clicks and selected accessibility preferences. What a particular tool actually accesses and transmits must be established. A script does not automatically gain access to all browser data, other applications or every cross-origin frame.

**Documented example:** accessiBe's help article, updated 31 August 2026, says accessWidget processes IP addresses and page URLs in real time without storing them, and that mouse movements and clicks remain local. Its broader privacy notice describes server receipt of image and link URLs, HTML structure, CSS attributes, clicks, interactions and page views. Those statements require written reconciliation for the intended configuration; this review does not determine which applies. [S02, S03]

### Opportunity and programme response

User-controlled presentation preferences can help some people. Prefer implementation patterns that preserve choice without creating unnecessary identity records. Evaluate accessibility effectiveness separately from privacy.

Before use on logged-in, employee, payment, health or confidential pages, obtain a field-level data-flow description and inspect a synthetic test journey. Check outbound calls, payloads, storage, tag-manager dependencies, script updates and behaviour before a user opens the tool. Ask whether capture rules cover dynamic content and whether the feature remains usable when optional analytics are declined.

Security specialists should assess script integrity, execution isolation, endpoint restrictions and update controls. Content Security Policy and subresource integrity may be relevant, but neither independently establishes privacy, and integrity pinning needs a workable update process. Refer unresolved capture scope, conflicting supplier statements or sensitive transmission for review. [S01]

## 3. Online forms: identity can enter through several routes

### Underlying issue

Forms are valuable for inclusive research, access requests and satisfaction measurement. Their privacy depends on the complete workflow, not just whether the questionnaire asks for a name.

| Linkage route | What can connect responses to a person | What to verify |
| --- | --- | --- |
| Authentication or SSO | Account ID, organisational identity or an explicit name/email field | Whether identity authenticates eligibility only, is stored with answers, or can be joined later |
| Individual invitations | Recipient-specific URL, contact-list entry, completion record or token | Whether invitation tracking and answer content are separated, and who can access each |
| URL parameters and hidden fields | Employee/customer ID, campaign token, CRM fields or embedded data | What is populated, logged, exported or forwarded to integrations |
| Browser and network metadata | Cookies, IP address, device identifiers and timestamps | Which layer collects them and whether they can actually be linked to answers |
| Operational systems | Webhooks, spreadsheets, CRM, HR systems, audit logs and notifications | Who receives answers and whether a stable key permits joining |
| Response content | Name, location, job role, rare condition, uploaded document or distinctive narrative | Whether the content identifies someone without a technical identifier |
| Small populations | Team, location, grade, impairment and time combinations | Re-identification risk in dashboards, filters and repeated reporting |

Login is not proof that researchers receive named responses. Equally, a name-free export is not proof that the whole collection process is anonymous.

**Documented examples:** Microsoft Forms supports response settings that do not record names; organisational restrictions and name recording are configurable. Qualtrics distinguishes shared anonymous links from personal links and explains that default anonymous-link responses may include IP/location data unless anonymisation is enabled. Its security guidance warns that embedded directory fields can defeat anonymity. [S04–S06]

### Opportunity and programme response

Separate two purposes: **anonymous experience research** and **identified case handling**. A person requesting an adjustment may need follow-up; explain the identified workflow rather than promising anonymity. Offer a separate, optional contact route for research follow-up without silently reconnecting anonymous answers.

Test invitations, authentication, completion reminders, partial responses, exports and every downstream integration using dummy accounts. Define exactly what “anonymous” means: anonymous to the analyst, to the employer, or not reasonably identifiable anywhere in the intended data flow. Prefer “confidential” when identities are known but restricted. Do not infer the existence of a hidden join merely because both systems have logs; verify whether linkage is feasible and accessible.

Use minimum necessary attributes and safe reporting rules. Refer an anonymity claim that cannot be substantiated, sensitive HR/customer linkage, or a new cross-system join to privacy and research governance specialists.

## 4. Behaviour tracking, condition inference and profiling

### Underlying issue

Navigation paths, reading pace, error patterns, pointer movement, keystrokes, voice, gaze or accessibility settings can be used to construct predictions about an individual. An observed interaction difficulty has several possible causes: fatigue, language, context, unfamiliarity, technology or disability. The signal alone is not a diagnosis.

Distinguish:

- **Barrier evidence:** people struggle with this step, so improve it.
- **A chosen preference:** this person asks for captions or a simpler presentation.
- **An inferred trait:** the system assigns a disability, neurotype, cognitive or health label.
- **A consequential profile:** that label changes recruitment, price, eligibility, monitoring, support or access.

The final two create substantially different risks from barrier measurement. ICO guidance explains that intentional health inference, or intentionally treating someone differently on such an inference, can engage special-category data protections even when the inference is uncertain or wrong. This is a referral trigger, not a legal determination for a particular system. [S07]

### Opportunity and programme response

Use aggregate task evidence to remove barriers and offer broadly available options. Let people select support without assigning a condition. Avoid cross-session condition scores or advertising audiences built from access needs. W3C identifies configuration-based fingerprinting as a route to identification and tracking; this does not mean websites can reliably detect every screen reader or disability. [S08]

Ask what the model is predicting, why, against what independently established evidence, with what error rates, and with what consequences. Check false positives, false negatives, proxy variables, subgroup performance, correction and challenge routes. Refer health or neurotype inference to privacy and relevant clinical specialists, and consequential decisions to equality, HR and legal specialists. Calling an output “wellbeing”, “fit”, “risk” or “support needs” does not settle its meaning.

## 5. Psychometrics and assessments that exclude relevant populations

### Underlying issue

An accessible interface does not establish that a measure is valid for the population, purpose or administration conditions. A timed task might reflect motor or reading demands instead of the intended skill. Personality or behavioural items may confound neurodivergent communication with competence or motivation. A general satisfaction scale may also miss relevant experiences.

Do not assume all psychometrics were designed only for non-disabled or neurotypical people. Obtain evidence about the actual instrument: its construct, normative sample, validation, subgroup coverage and intended interpretation.

BPS guidance cautions that arbitrary changes to timing or administration can invalidate standard score comparisons and recommends specialist advice on adaptations. US DOJ guidance provides examples of hiring tools measuring disability-related demands rather than relevant job skills. The latter is US guidance; its examples are useful risk evidence, not a statement of UK legal duties. [S09, S10]

### Opportunity and programme response

Inclusive assessment can produce more useful evidence about actual ability. Ask a suitably qualified psychologist or psychometrician to evaluate:

- Relevance of the construct to the task or decision.
- Normative and validation evidence for the intended users and language.
- Measurement equivalence, item bias and relevant subgroup uncertainty.
- Effects of assistive technology, extra time, readers, scribes or alternative formats.
- Whether an alternative work sample or method is more appropriate.
- Whether an adapted result can still use standard norms or requires different interpretation.

Refer before using unsupported scores for selection, promotion, performance, service eligibility or claims about a condition. Do not “correct” scores using an assumed disability label, or diagnose from a test that was not validated for that purpose. Provide an access-adjustment route without forcing unnecessary medical disclosure.

**Evidence limitation:** the BPS PDF's indexed passages were available during research, but direct retrieval returned an access error. This document uses only those passages, concerning adaptations and interpretation; it does not claim a full review of the publication.

## 6. Desktop assistive technology, screen access and remote AI

### Underlying issue

Screen readers, magnifiers, dictation, OCR, image description and cognitive support may need broad access to the user's working material. Broad local access is not itself evidence of remote scraping. Review optional cloud features, extensions, diagnostics, remote support and integrations separately from the core tool.

The relevant content could include a selected image, active window, whole desktop, document, clipboard, notification, accessibility-tree text or audio. In a corporate setting it may contain customer records, credentials, legal advice, unreleased designs or health and personnel information.

**Documented examples:** Freedom Scientific describes Picture Smart AI as submitting images for description. Its privacy policy states that it and its AI partners do not store or train on submitted Picture Smart images. This still describes remote processing. Microsoft describes Voice access speech processing as on-device, demonstrating that cloud transmission is not intrinsic to an assistive function. [S11, S12]

### Opportunity and programme response

AI descriptions and OCR can make inaccessible content available without human assistance. Preserve that benefit through approved configurations, local options or suitable contractual processing boundaries.

Document capture scope, invocation, preview, accidental activation, endpoint, retention and human access. Test notifications, secondary monitors and unrelated windows with synthetic data. Do not assume that a password mask or a local sensitive-content filter protects every confidential document. Check virtual-desktop and remote-session boundaries, clipboard sync, crash reports and support bundles.

Use feature-level controls, accessible training and restricted destinations where justified. If a cloud feature is unsuitable for a specific class of information, provide an effective alternative and validate it with the user. Avoid a blanket screen-reader ban or making the employee responsible for procurement failures. Refer sensitive outbound content or unknown scope to security and privacy specialists.

## 7. Meeting note takers, recorders, captions and summaries

### Underlying issue

Live access, persistent recording, transcription, speaker identification, summarisation and training are different activities. A meeting bot can introduce another recipient, automatic calendar joining, screenshots, searchable archives, follow-up emails and integrations.

Discussions may include health, adjustments, grievances, safeguarding, legal strategy, customer information or a colleague's family circumstances. Approval by the person using the tool does not resolve how everyone else's information should be handled.

**Documented examples:** Microsoft distinguishes Teams live captions, which its support page says are deleted after the meeting, from retained transcription stored in OneDrive/SharePoint. Otter's privacy policy describes proprietary training using de-identified audio and transcriptions that may contain personal information, while its security page separately says external AI providers do not train on customer data. These statements address different actors and must not be collapsed into a single “no training” claim. [S13–S16]

### Opportunity and programme response

Captions, transcripts and notes can support Deaf participants, memory, fatigue and processing needs. Determine the access outcome first: live captions may meet one need, while another person needs retained notes.

Establish who can start capture, what notification is accessible, whether a bot can autojoin, what happens in breakout or private discussions, who receives the output and how corrections work. Review calendar/contact access, external sharing, default retention, search indexing and access after a participant leaves the organisation. Distinguish processing of sound from using voice characteristics for identity recognition; do not label every audio recording as biometric identification.

For sensitive meetings, plan approved access support in advance. Pausing recording without another access method may exclude someone. Offer appropriate alternatives, such as approved live captioning, an authorised human note taker or a restricted record. Do not promise that a meeting banner or everyone's apparent agreement establishes a sufficient legal basis. ICO highlights the power imbalance in employment consent and the intrusiveness of continuous audio monitoring. [S17]

Refer sensitive persistent capture, uncertain participation choices, speaker biometrics or proposed reuse for performance monitoring to the relevant specialists.

## 8. Smart glasses and environmental recording

### Underlying issue

Wearable cameras and microphones may capture people, documents, screens, locations and conversations outside a conventional computer interface. The wearer may need visual assistance while bystanders have no account, no accessible notice and no practical way to inspect or delete the capture.

Separate ordinary camera capture, an AI image query, live video assistance, translation, voice interaction and background activation. Each may have different recipients and settings.

**Documented examples:** Ray-Ban's FAQ describes an AI image-query flow involving cloud processing, retention, training and reviewers. The same page contains feature and regional qualifications; it is not evidence that every UK feature has identical terms. Meta's responsible-innovation page explains that deleting a voice recording does not immediately alter a model that already learned from it. These sources justify feature- and region-specific verification, not a claim that every recording from all smart glasses becomes training data. [S18, S19]

### Opportunity and programme response

Wearables may support reading, orientation, translation and remote assistance. Assess an agreed use case with the wearer and affected people rather than treating the device as either harmless or inherently unacceptable.

Check field of view, activation, buffering, accidental triggers, offline queues, phone/cloud synchronisation, retention, training, human review, location information and account linkage. A recording light is not sufficient notice for someone who cannot see it, and awareness of recording does not explain downstream training. Establish practical boundaries for clinical, HR, safeguarding, legal, secure and domestic spaces while supplying alternative access support.

Ask whether people incidentally captured can obtain information, object or seek deletion, and whether the supplier can honour those requests across copies and downstream uses. The wearer's agreement cannot by itself resolve other people's interests or corporate confidentiality. Refer unresolved bystander capture, sensitive settings or training reuse to privacy, security, safeguarding and legal specialists as appropriate.

## 9. Inclusive training data: benefits and limits

Inclusion in model development may improve recognition of atypical speech, non-standard interactions and visual-assistance needs. People should be able to contribute knowingly without having to surrender unrelated information to obtain access.

**Documented example:** Be My Eyes' September 2026 policy distinguishes stored assistance videos that may be shared for research and AI development from Be My AI submissions, which it says neither it nor its AI providers use for model training. It also warns that removing file metadata does not guarantee removal of personal information spoken or visible within videos. This demonstrates why product-feature boundaries matter. [S20]

For proposed data contribution, specify inputs and outputs, recipient models, evaluation and training purposes, commercial use, human review, onward licensing, retention, and withdrawal limits. Prefer purpose-built, voluntary datasets, synthetic examples where appropriate and minimised samples over harvesting everyday assistance. Synthetic data also needs validation and privacy review; it is not automatically representative or anonymous.

“No training” should cover the supplier and its subprocessors, the relevant account tier and feature, and inputs, outputs and feedback. Where learning has occurred, do not promise guaranteed removal from model weights. Ask specialists what deletion and objection can accomplish in the specific architecture.

## 10. Other issues programmes should include

The following are review scenarios and engineering deductions from the data-flow model, not claims that all products perform these activities.

| Scenario | Underlying risk | Useful response or opportunity |
| --- | --- | --- |
| Session replay and interaction analytics | Sensitive DOM text, URLs, console output or network payloads may escape inadequate capture rules; behavioural traces may be joined to accounts | Inspect each capture channel. Fullstory documents distinct exclusion, masking, header and network controls; configuration matters [S21] |
| Add-ons and remote assistance | Extensions can change trusted software's behaviour; remote support may expose content or permit control | Govern extensions and support sessions without blocking core access. NV Access notes add-ons do not undergo human security audits [S22] |
| Speech, gaze and movement analysis | A feature introduced for access may become an identity, attention, emotion or productivity measure | Keep access functionality separate from inferred internal states. ICO warns about emotion-analysis risks and describes behavioural biometric techniques [S23] |
| Proctoring and anti-fraud checks | Unusual gaze, pauses, keyboard patterns or assistive software may be misread as suspicious | Test legitimate access patterns, provide an appeal and alternative assessment route; treat flags as uncertain evidence [S10] |
| Accessibility dashboards and adjustment records | Small populations or repeated filtering may reveal individuals; support information may migrate into performance or marketing systems | Separate case handling from aggregate service insight; restrict joins, access and reporting |
| Human assistance, interpreters and transcription suppliers | Additional humans, subcontractors or home-working environments can expose information | Confirm confidentiality, scope, working conditions, storage and access; human processing is a data flow too |
| Spoken or displayed output | TTS, braille, captions, shared screens and notifications can reveal information without any network transmission | Support headphones, private output, notification controls and participant choice; keep access usable |
| Agent actions and document instructions | An AI reading a page or document may also have connectors or action permissions; malicious content may influence unintended disclosure | Separate reading from acting, limit connector permissions and test hostile synthetic content with security specialists |
| Local screen-history archives | Even without an outbound path, a searchable archive can create a new sensitive dataset on a shared or compromised endpoint | Microsoft describes Recall snapshots as opt-in and locally processed/stored; assess archive access, exclusions and deletion separately from cloud upload [S26] |
| Synchronisation, exports and deletion | Personal accounts, mobile backups, downloads and integrations create copies outside the original retention rule | Map all copies and account transitions, including staff departure and device replacement |
| Accessible privacy controls | An inaccessible consent, pause, deletion or opt-out interface removes meaningful choice | Test privacy tasks with users and assistive technology; provide an equivalent accessible route [S24] |

A documented adjacent case illustrates the consequences of secondary use: the FTC's BetterHelp order concerned allegations about disclosure of health-questionnaire information and identifiers for advertising. It is not an assistive-technology case and does not prove similar conduct by the suppliers discussed here. It demonstrates why forms, identifiers and advertising integrations should be reviewed together. [S25]

## 11. A practical review workflow

### Step 1: Record benefit and context

Describe the task, access need, intended benefit, affected people, environment, information sensitivity and consequences of failure. Involve Deaf, disabled and neurodivergent people in decisions about acceptable configurations and alternatives.

### Step 2: Map the actual flow

Record device/app, feature/version, account tier, region, trigger, capture scope, recipients, subprocessors, identifiers, retention, logs, exports, training, human access and deletion. Mark each fact as verified, supplier-stated, observed, conflicting or unknown. Local processing can still require security and retention controls.

### Step 3: Gather evidence safely

Obtain the relevant terms, data-processing agreement, feature-specific notices, configuration screenshots and supplier answers. Ask security staff to inspect traffic and payloads in an authorised synthetic environment. Protect test traces: they may contain tokens or identifiers. Network observation alone cannot establish downstream retention or training, and a quiet test cannot prove there is no delayed upload.

Do not investigate by covertly monitoring employees, fingerprinting customers' assistive technology or uploading real confidential data. Ask for the relevant configuration and use controlled tests.

### Step 4: Route concerns using the matrix below

Referral rules are **Double FW programme recommendations**, not statutory thresholds. Apply all matching rules. The decision belongs to the named human owner, supported by specialists.

### Step 5: Preserve access while addressing the concern

For a planned deployment, resolve high-risk unknowns before enabling the proposed capture or reuse. For an existing service, urgently involve the accessibility owner and incident/security team as appropriate. Restrict the concerning feature or destination where possible and provide effective alternative support; do not automatically disable essential assistive technology.

### Step 6: Reassess changes and outcomes

Repeat review after material feature, model, supplier, region, permission, integration or policy changes. Record residual risks, decisions, expiry/review date and access outcomes, including dignity, independence, confidence and satisfaction. A previous review does not cover a new return path by default.

## 12. Referral matrix for people and automated systems

**Possible statuses:** `needs_evidence`, `specialist_review_required`, `incident_review_required`, `reviewed_with_conditions`. None means legal clearance. Missing evidence is not a negative finding or an automatic pass.

| Rule | Observable or declared trigger | Route and suggested status |
| --- | --- | --- |
| ATD-01 | Capture/transmission scope, recipient, retention or reuse is unknown or conflicting | Security + privacy + procurement; needs_evidence |
| ATD-02 | Screens, documents, forms, audio or video may send sensitive personal or corporate information outside an approved boundary | Security + privacy; specialist_review_required |
| ATD-03 | An “anonymous” response has a joinable identity key, or the anonymity claim is unverified | Research governance + privacy; needs_evidence |
| ATD-04 | Behaviour, voice, gaze or access preferences are used to infer a condition, neurotype or health risk | Privacy + relevant clinical expertise; specialist_review_required |
| ATD-05 | A profile or score affects hiring, performance, eligibility, pricing, discipline or another consequential outcome | HR/service owner + equality + legal + privacy; specialist_review_required |
| ATD-06 | A psychometric instrument lacks evidence for its population/purpose, or administration is adapted without supported interpretation | Qualified psychologist/psychometrician + HR/research lead; specialist_review_required |
| ATD-07 | Persistent recording involves health, adjustments, grievances, safeguarding, legal or confidential client discussions | Privacy + security + subject owner; add legal/safeguarding expertise where relevant; specialist_review_required |
| ATD-08 | Bystanders, children or people unable to receive meaningful notice may be captured | Privacy + safeguarding where relevant; specialist_review_required |
| ATD-09 | Inputs, outputs, feedback or recordings may be used for training, evaluation, onward licensing or human review beyond the approved purpose | Privacy + procurement + legal + research governance; specialist_review_required |
| ATD-10 | Access support is conditional on optional monitoring, marketing or model-training reuse, or meaningful refusal is doubtful | Accessibility + privacy + HR where relevant; specialist_review_required |
| ATD-11 | External endpoints, subprocessors, regions, account tiers or connectors differ from the reviewed configuration | Security + privacy + procurement; needs_evidence |
| ATD-12 | Raw content or identifiers unexpectedly appear in telemetry, exports, public/shared links or supplier systems | Security incident team + privacy + information owner; incident_review_required |
| ATD-13 | A deletion/withdrawal claim omits copies, backups, derived records or prior training | Privacy + security + supplier owner; needs_evidence |
| ATD-14 | Voice/gaze/behaviour is used for unique identity recognition, emotion inference or employee monitoring | Privacy + security + HR + relevant scientific expertise; specialist_review_required |
| ATD-15 | A proposed restriction would remove effective access, or privacy controls themselves are inaccessible | Accessibility owner + affected users + security/privacy; specialist_review_required |
| ATD-16 | Small-group reporting or data linkage makes identification reasonably plausible | Research governance + privacy; specialist_review_required |

### Applying the rules in software or agent workflows

Use procurement answers, approved configuration inventories, data-flow manifests and authorised test evidence as inputs. Keyword matches such as “AI training” or “anonymous” can request evidence; they must not alone establish a fact. Do not collect additional disability data just to run the rules.

Represent facts as `yes`, `no`, `unknown` or `conflicting`, with source, date and scope. Route unknown or conflicting facts to ATD-01 and any applicable subject-specific rule. Preserve all triggered rules; an apparent low-risk feature does not cancel another rule. Require a human to resolve consequential questions.

An illustrative record, using fictional information:

```json
{
  "record_id": "ATD-EXAMPLE-001",
  "feature": "Cloud image description",
  "deployment": {
    "version": "not_yet_confirmed",
    "account_tier": "not_yet_confirmed",
    "region": "UK"
  },
  "facts": {
    "content_sent_off_device": {
      "value": "yes",
      "evidence": "supplier_feature_documentation",
      "checked_on": "2026-11-06"
    },
    "sensitive_content_possible": {
      "value": "yes",
      "evidence": "intended_workflow_inventory",
      "checked_on": "2026-11-06"
    },
    "training_reuse": {
      "value": "unknown",
      "evidence": "no_feature_specific_answer",
      "checked_on": "2026-11-06"
    }
  },
  "triggered_rules": ["ATD-01", "ATD-02", "ATD-09"],
  "status": "specialist_review_required",
  "decision_owner": "accessibility_programme_owner",
  "reviewers": ["security", "privacy", "procurement"],
  "interim_action": "Use approved alternative for sensitive material",
  "access_continuity_checked": false,
  "human_decision": null,
  "review_due": null
}
```

This is a record template, not executable decision logic or a validated risk-scoring model. Its facts and referrals need human checking. Test any implementation against synthetic cases: on-device processing with no remote reuse; cloud processing with no training; supposedly anonymous surveys with embedded IDs; adapted psychometrics; sensitive transcripts; and bystander camera capture. It should distinguish these cases and preserve uncertainty.

## 13. Questions to put to suppliers

1. Which exact feature, version, region and contract do your answers cover?
2. What can it access, and which data fields and metadata leave the device?
3. What triggers capture, including background activity, accidental activation and offline upload?
4. Which organisation receives each flow and which subprocessors, staff or reviewers can access it?
5. Which identifiers permit linkage to a user, account, device, employer or third party?
6. What is stored for inference, logs, troubleshooting, human review, evaluation and training, separately?
7. Does “no training” cover your own models and every downstream provider, including feedback and outputs?
8. Are consumer and enterprise defaults different? Can administrators enforce the intended settings?
9. What retention, deletion, backup and onward-use limits apply? What cannot be reversed?
10. How are changes communicated, and how can we test the deployment with synthetic information?
11. How do you support accessible notice, refusal, correction and deletion for users and people incidentally captured?
12. Which access functions continue when optional data contribution or analytics are disabled?

Record documentary evidence and unresolved answers. Certification, a security badge or a general assurance does not replace feature-specific answers.

## 14. Source register and evidence limits

All links below were researched on 6 November 2026. Vendor sources describe stated practices, not independent technical verification. Product terms, geography, tiers and defaults change. Regulatory material provides issue-spotting context; obtain current jurisdiction-specific advice for decisions. Some ICO pages flag revision following the Data (Use and Access) Act 2025; this document avoids prescribing a lawful basis or interpreting automated-decision rules.

| ID | Primary source | Contribution and limit |
| --- | --- | --- |
| S01 | [OWASP: Third Party JavaScript Management](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html) | Script trust, data access and security controls; not an overlay product audit |
| S02 | [accessiBe: Does accessWidget use cookies or collect personal data?](https://support.accessibe.com/hc/en-us/articles/37847421167506-Does-accessWidget-use-cookies-or-collect-personal-data) | Feature-specific supplier claims; updated 31 August 2026 |
| S03 | [accessiBe Privacy Notice](https://accessibe.com/privacy-notice) | Broader server data description; reconcile with S02 and deployment contract |
| S04 | [Microsoft Forms: collecting responses without recorded names](https://support.microsoft.com/en-us/forms/set-up-your-survey-so-names-aren-t-recorded-when-collecting-responses) | Name-recording settings; not proof of anonymity across an entire enterprise workflow |
| S05 | [Qualtrics: Anonymous Link](https://www.qualtrics.com/support/survey-platform/distributions-module/web-distribution/anonymous-link/) | Shared links, IP/location collection and distribution choices |
| S06 | [Qualtrics: Security Survey Options](https://www.qualtrics.com/support/survey-platform/survey-module/survey-options/survey-protection/) | Anonymisation settings and embedded-data caveats |
| S07 | [ICO: Special category data](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/a-guide-to-lawful-basis/special-category-data) | Updated October 2026; intentional sensitive inference and differential treatment |
| S08 | [W3C: Mitigating Browser Fingerprinting](https://www.w3.org/TR/fingerprinting-guidance/) | Configuration-based tracking threats; Group Note, not a claim of universal AT detection |
| S09 | [BPS: Neurodiversity and Psychometric Testing](https://cms.bps.org.uk/sites/default/files/2024-11/Neurodiversity%20and%20Psychometric%20Testing.pdf) | Indexed passages on adaptations and interpretation; full direct retrieval unavailable |
| S10 | [US DOJ: Algorithms, AI and Disability Discrimination in Hiring](https://www.ada.gov/resources/ai-guidance/) | Assessment examples and job-skill relevance; US jurisdiction |
| S11 | [Freedom Scientific Data Privacy Policy](https://support.freedomscientific.com/privacy-policy/enu/) and [Picture Smart AI](https://www.freedomscientific.com/training/jaws/picture-smart-ai/) | Remote image submission and feature-specific no-storage/no-training statements; policy dated 8 April 2025 |
| S12 | [Microsoft: Improve speech recognition with Voice access](https://support.microsoft.com/en-us/accessibility/windows/voice-access/improve-speech-recognition-with-voice-access) | Example of stated on-device speech processing |
| S13 | [Microsoft Teams: Use live captions](https://support.microsoft.com/en-gb/teams/meetings/use-live-captions-in-microsoft-teams-meetings) | Live-caption processing and deletion; distinct from recording/transcription |
| S14 | [Microsoft Learn: Manage transcription and captions](https://learn.microsoft.com/en-us/microsoftteams/meeting-transcription-captions) | Retained transcripts and OneDrive/SharePoint storage |
| S15 | [Otter Privacy Policy](https://otter.ai/privacy-policy) | Effective 16 June 2026; content, integrations and proprietary training uses |
| S16 | [Otter Privacy and Security](https://otter.ai/privacy-security) | Separate external-provider training and human-access statements; check contractual scope |
| S17 | [ICO: Data protection and monitoring workers](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/employment/monitoring-workers/data-protection-and-monitoring-workers/) and [specific monitoring methods](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/employment/monitoring-workers/specific-data-protection-considerations-for-different-ways-or-methods-of-monitoring-workers/) | Employment power imbalance and audio-monitoring issues; referral context |
| S18 | [Ray-Ban Meta FAQ](https://www.ray-ban.com/uk/c/frequently-asked-questions-ray-ban-meta-smart-glasses) | AI image flow, reviewers and training statements; regional/feature qualifications require confirmation |
| S19 | [Meta: Responsible Innovation](https://www.meta.com/actions/responsible-innovation/) | Bystanders and limits of deletion after training; supplier statements |
| S20 | [Be My Eyes Privacy Policy](https://www.bemyeyes.com/privacy-policy/) | Effective 1 September 2026; distinct assistance-video and Be My AI purposes and sharing |
| S21 | [Fullstory: Privacy protections](https://help.fullstory.com/hc/en-us/articles/360020623574-How-do-I-protect-my-users-privacy-in-Fullstory) and [Privacy settings](https://help.fullstory.com/hc/en-us/articles/34807885576215-Privacy-Settings-in-Fullstory) | Capture exclusion/masking and distinct network/header rules; defaults vary |
| S22 | [NV Access: Add-on datastore](https://github.com/nvaccess/addon-datastore) | Explicit limits of add-on security auditing; not a claim that all add-ons are unsafe |
| S23 | [ICO: Biometrics technologies](https://ico.org.uk/about-the-ico/research-reports-impact-and-evaluation/research-and-reports/technology-and-innovation/tech-horizons-and-ico-tech-futures/biometrics-technologies/) and [Biometric recognition](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/biometric-data-guidance-biometric-recognition/biometric-recognition/) | Emotion-analysis concerns and behavioural recognition examples |
| S24 | [W3C: Privacy Principles](https://www.w3.org/TR/privacy-principles/) | Privacy design principles and consideration of accessibility |
| S25 | [FTC: Final BetterHelp order, July 2023](https://www.ftc.gov/news-events/news/press-releases/2023/07/ftc-gives-final-approval-order-banning-betterhelp-sharing-sensitive-health-data-advertising) | Adjacent enforcement example about health information, identifiers and advertising; allegations and order, not AT-sector evidence |
| S26 | [Microsoft: Privacy and control over Recall](https://support.microsoft.com/en-gb/windows/privacy/privacy-and-control-over-your-recall-experience) | Adjacent screen-history example; opt-in and local processing/storage, not evidence of AT cloud scraping |

**Repository integration:** Place this file in the root alongside the linked guidance. Suggested README entry: `Assistive_Technology_Data_Flows_Risks_and_Review.md — evidence-led guidance on assistive technology return paths, forms, profiling, assessments, recordings, wearables, supplier questions and specialist review triggers.`
