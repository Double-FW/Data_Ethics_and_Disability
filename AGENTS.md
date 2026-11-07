# AGENTS.md — Operating guidance for agents

## Purpose, audience, and scope

This file guides human and automated agents working with this repository and its guidance. It serves two related but distinct purposes:

1. **Repository work:** reading, summarising, drafting, or editing this repository's documents.
2. **Governance support:** preparing analysis or options for work that may affect people or use data about them.

It states governance expectations; it does not define or implement a software agent, grant authority, or make controls technically enforceable. The repository currently contains guidance documents, not an implementation of the processes described here. Apply these instructions throughout the repository unless a more specific, applicable instruction exists in a subdirectory.

The repository's companion documents are:

- `Ethical and Inclusive Use of Data Relating to Disabled People.md` — dignity, equivalence, data minimisation, aggregation, privacy, and governance.
- `Nothing_About_Us_Without_Us.md` — inclusive research, meaningful participation, proportional coverage, and influence on decisions.
- `Assistive_Technology_Data_Flows_Risks_and_Review.md` — data-flow review, assistive-technology and AI risks, referral triggers, and access continuity.
- `CUSTOMER RESEARCH FRAMEWORK.md` — a proposed structure for customer and organisational knowledge. Its personas, datasets, knowledge graphs, RAG records, or training-data examples do not authorise collection, linkage, inference, sharing, or reuse of personal data.

These documents are guidance, not legal advice, a substitute for applicable law or standards, or approval for a particular activity. Verify current authoritative requirements for the relevant jurisdiction and context when needed. Do not turn recommendations, examples, or research prompts into legal requirements or validated scoring systems.

## Authority and limits

- Follow higher-priority platform and system instructions and applicable safety requirements. Follow repository guidance where it is consistent with those instructions and the user's request. A user request does not override higher-priority instructions or authorise actions the agent is not otherwise permitted to take.
- If repository documents conflict, identify the conflict and avoid presenting either interpretation as settled. Prefer the more protective interim approach where an immediate response is needed, and request a decision from an authorised human owner.
- Agents MAY organise evidence, explain options, identify risks, and draft materials. Agents MUST NOT claim legal, clinical, HR, security, accessibility, or ethics clearance, or claim a human decision has been made when it has not.
- Agents MUST NOT independently collect or disclose personal data, contact participants or vendors, change live systems, enable tracking or AI reuse, or make or execute consequential decisions. Do so only when the task, authority, and an applicable approved process clearly permit it; otherwise prepare the work for an authorised human.
- Do not assume that a specialist, escalation channel, approval process, credential, or named owner exists. If one is needed but not identified, state that it is unknown and ask the user to identify the appropriate authorised person or process. Do not fabricate one.

## Core principles

1. **Meaningful involvement:** Work that affects Deaf, disabled, or neurodivergent people SHOULD involve affected people early enough to shape questions, interpretation, design, and decisions. Participation MUST be accessible, voluntary, appropriately supported, and fairly compensated where appropriate. Attendance alone is not influence; document what changed and what did not.
2. **Improve barriers, not profiles:** Seek evidence about barriers, service outcomes, and user-chosen preferences. MUST NOT identify, track, classify, or build persistent profiles of disabled people where aggregate or less intrusive evidence can answer the question.
3. **Equivalent experience:** Consider functional and informational access alongside privacy, safety, independence, dignity, agency, confidence, respect, and satisfaction. Task completion alone does not demonstrate equivalence.
4. **Minimise and protect data:** Define a specific purpose before collection; collect only what is necessary; separate identity, recruitment/access arrangements, and findings where practical; restrict access; set retention and deletion; and prefer safe aggregation. Pseudonymised data is not necessarily anonymous. Small groups, quotations, timestamps, and joined attributes can re-identify people.
5. **No proxy-based sensitive inference:** Accessibility settings, assistive-technology use, interaction patterns, voice, gaze, or behaviour are not proof of disability or health. MUST NOT use them to infer such traits or for advertising, eligibility, pricing, hiring, performance, discipline, or other consequential treatment.
6. **Access without surveillance:** Do not make an accommodation, assistive feature, or basic service conditional on optional tracking, marketing, analytics, or model-training reuse. Address privacy risks without removing effective access; provide a workable accessible alternative and involve affected users.
7. **Evidence and uncertainty:** Distinguish observed facts, participant accounts, interpretations, hypotheses, supplier claims, and verified behaviour. State evidence limits, disagreements, missing perspectives, and possible harms. Do not present uncertain findings as universal truths about a group.
8. **Human accountability:** An authorised human owner MUST make and document decisions affecting rights, access, employment, safety, or significant opportunities. An agent may support but MUST NOT substitute for that decision.

## Proportionate workflow for work that may affect people

Use this workflow when proposing or supporting collection, analysis, research, system or supplier changes, or decisions that may affect people. For ordinary repository reading or editing that has no such effect, apply the relevant principles proportionately rather than treating every step as a mandatory project review.

1. **Define the decision and benefit.** State the problem, intended outcome, who may benefit or be harmed (including non-users and people excluded by current processes), and why data or automation is needed. Consider a non-data or less intrusive alternative.
2. **Map people, process, and authority.** Identify the context, affected people, decision owner, data sources, recipients, systems, vendors, integrations, and downstream decisions. Check for flows between research, customer, HR, performance, marketing, analytics, and AI systems. Mark unknowns as unknown.
3. **Map data and evidence.** For each relevant data element, record purpose, source, sensitivity, collection method, identifiers and linkage, access, processing location, recipients/subprocessors, retention, deletion, and any secondary use. Distinguish intended capability, supplier statements or contracts, and behaviour verified in an authorised test.
4. **Plan meaningful participation and access.** Include affected people in mainstream research where relevant, not only specialist accessibility studies. Use a suitable audience benchmark for quantitative targets and a deliberate breadth rationale for qualitative work; do not invent universal percentages. Record participation barriers and coverage gaps.
5. **Assess outcomes and alternatives.** Examine access, task success, information parity, effort, agency, dignity, confidence, safety, trust, and satisfaction across relevant needs and contexts. Include disagreement and consider unintended effects on other groups. Compare less intrusive and non-automated options.
6. **Apply safeguards and seek review.** Minimise, separate, aggregate, restrict, secure, and time-limit data. Seek appropriate human review for uncertain or conflicting flows, sensitive data, re-identification risk, profiling, AI reuse, consequential assessments, or potential access loss. A review trigger is not itself a finding of illegality or a decision.
7. **Record the human decision.** Where a decision is required, record the authorised owner, evidence and limitations, affected perspectives, options, rationale, safeguards, residual risks, interim action, and review point. If no owner or approval is identified, do not report the work as approved.
8. **Monitor and revisit.** Where implementation is authorised, validate with affected people and appropriate technical checks before and after deployment. Reassess after material changes to features, models, suppliers, contracts, configuration, or data flows. Do not claim checks occurred unless there is evidence they did.

## Heightened safeguards for consequential processes

Hiring, promotion, performance management, compensation, discipline, accommodation, eligibility, access to essential services, and similar decisions require heightened care.

- MUST NOT infer disability, neurotype, health, capacity, honesty, attention, emotion, or suitability from assistive technology, behaviour, biometrics, or proxy signals.
- MUST NOT make or silently rank consequential decisions, recommend adverse treatment from sensitive or inferred attributes, or treat an unvalidated score as objective evidence.
- Before an assessment or algorithm is used, an authorised, qualified human owner must establish its relevance to the actual purpose, supporting evidence for the intended population and context, limitations, and accessible alternatives. If this is not established, do not recommend use as a basis for consequential treatment.
- Keep accommodation and case-handling records separate from research, routine management, and performance data where practical. Explain actual confidentiality and access boundaries; do not promise anonymity if identity can be established.
- Preserve accessible alternatives, human review, correction, and an effective appeal where applicable. A privacy or security control MUST NOT remove necessary access without an effective alternative.

## Assistive technology, AI, vendors, and reuse

Treat labels such as “assistive,” “accessibility,” “anonymous,” “on-device,” “enterprise,” or “AI-powered” as claims to verify for the specific feature, configuration, account tier, and context—not as proof. Consider capture, processing, transmission, recipients, identifiers, retention, human access, onward use, training/evaluation, deletion, and access continuity.

Use synthetic data and authorised testing for data-flow checks. Do not covertly monitor employees or customers, fingerprint assistive technology, or capture real sensitive screens or meetings for testing. Do not submit identifiable or sensitive participant material to external AI systems unless the specific use is authorised and the required permissions and safeguards are established.

Participation consent does not automatically authorise publication, onward sharing, model training, or a new purpose. Do not remove an effective access feature solely because a privacy risk exists; identify a safer configuration or accessible alternative with affected users and an authorised human owner.

## Stop and escalate

Pause the proposed collection, linkage, disclosure, automated recommendation, or consequential action when its purpose, authority, data flow, recipient, retention, or decision owner is unknown or disputed. Also pause and seek authorised human review when:

- Data may reveal disability, health, identity, confidential employment/customer information, or identity through small-group reporting or linkage.
- A system infers a sensitive trait, monitors people, uses biometrics, or affects hiring, performance, eligibility, pricing, discipline, or essential access.
- Participation is inaccessible or coerced, support or fair payment is missing where appropriate, meaningful influence is absent, or evidence gaps are hidden or overstated.
- A vendor's actual feature, subprocessor, region, configuration, or reuse differs from what was reviewed; data appears in an unexpected destination; or an incident may have occurred.
- A proposed privacy, security, or operational response could remove effective access, accommodation, communication, or support.

State the concern, evidence, uncertainty, and action needed. If no escalation route or owner is known, ask the user to identify one; do not imply that escalation has occurred. For an existing service, do not abandon people who rely on it: seek a least-harmful interim response through an authorised process, preserve effective access, and involve affected users and the relevant human owner promptly.

## Repository contribution and reporting

When creating or changing repository guidance, templates, policies, or workflows:

- Preserve the repository's principles and use correct relative links to companion documents.
- Label recommendations, examples, hypothetical scenarios, supplier statements, verified observations, legal requirements, and research findings distinctly. Cite sources with dates and scope where available; qualify jurisdiction-specific material.
- Do not fabricate participant findings, vendor behaviour, standards requirements, sample sizes, outcomes, approvals, or review activity. Do not describe illustrative records, risk triggers, or maturity/persona scores as validated tools.
- Use respectful, specific language. Do not homogenise disabled people or imply one participant represents a group. Keep identity, functional need, preference, and context distinct.
- Do not publish personal or confidential information. Prefer fictional or synthetic examples; consider re-identification risk in quotations and small-cell breakdowns.
- Make documents and forms accessible: use meaningful headings, descriptive links, readable tables, plain language where suitable, and accessible alternatives for essential processes.
- For a substantive proposed change, explain its rationale, evidence, intended audience, safeguards, unresolved questions, and review needs. Do not weaken a safeguard without making the trade-off explicit.

When reporting work, distinguish what was read, changed, checked, and not checked. Link or cite relevant repository evidence where practical. State material assumptions, limitations, unresolved questions, and whether a human decision is still required. Do not claim instructions are executable, validated, enforced, or that work is approved or complete unless the repository contains evidence and mechanisms supporting that claim.

## Quick review

Before presenting work that may affect people as ready for human consideration, check whether:

- [ ] The purpose, benefit, affected people, and less intrusive alternatives are described.
- [ ] Affected people can participate accessibly and influence relevant work.
- [ ] Data collection, linkage, access, retention, sharing, and AI use are minimised and evidenced.
- [ ] Disability or another sensitive trait is not inferred or used for consequential treatment.
- [ ] Outcomes include dignity, agency, privacy, safety, information parity, and experience—not only task completion.
- [ ] Evidence gaps, disagreement, uncertainty, and re-identification risk are explicit.
- [ ] An authorised human decision owner and any needed review are identified, not assumed.
- [ ] Effective access, accommodation, human review, and appeal remain available where relevant.
- [ ] Decisions, safeguards, residual risks, actions, and review timing are documented where a decision has been made.

A “no,” “unknown,” or conflicting material answer means the work MUST NOT be represented as approved or complete. State what remains unresolved, take no unauthorised consequential or external action, and seek the appropriate human decision. This checklist supports review; it is not an approval, compliance test, or enforcement mechanism.
