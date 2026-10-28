# CUSTOMER RESEARCH FRAMEWORK

Analyse the repository as a source of customer, user, stakeholder, or organisational intelligence.

The objective is to identify knowledge that can improve AI understanding of customer needs, accessibility requirements, decision-making processes, governance challenges, and operational realities.

## CUSTOMER IDENTIFICATION

Identify all customer types represented within the repository.

For each customer type provide:

- Customer Name
- Customer Category
- Description
- Primary Objectives
- Success Measures
- Pain Points
- Constraints
- Risks
- Accessibility Considerations

Possible customer categories include:

- End Users
- Customers
- Employees
- Managers
- Executives
- Governance Leaders
- Compliance Teams
- Accessibility Specialists
- Product Owners
- Procurement Teams
- Developers
- Support Teams
- Regulatory Bodies
- Third-Party Suppliers

## PERSONA EXTRACTION

Identify explicit or implied personas.

For each persona generate:

{ "persona_name": "", "role": "", "goals": \[\], "motivations": \[\], "frustrations": \[\], "barriers": \[\], "decision_authority": "", "accessibility_requirements": \[\], "success_metrics": \[\] }

## JOBS TO BE DONE (JTBD)

Identify all Jobs To Be Done.

For each job provide:

When... I want to... So that...

Example:

When evaluating AI tools, I want to assess accessibility impacts, So that disabled employees are not excluded.

Categorise each job as:

- Functional
- Emotional
- Social
- Compliance
- Governance
- Operational
- Strategic

## CUSTOMER JOURNEY MAPPING

Identify customer journeys contained within the repository.

For each journey identify:

1. Trigger
2. Discovery
3. Evaluation
4. Decision
5. Implementation
6. Adoption
7. Review
8. Optimisation

For every stage record:

- Activities
- Decisions
- Pain Points
- Risks
- Accessibility Challenges
- Opportunities

## DECISION FRAMEWORK ANALYSIS

Identify how customers make decisions.

Extract:

- Decision Criteria
- Evaluation Models
- Approval Processes
- Risk Thresholds
- Escalation Paths
- Governance Controls

Represent decision logic as:

{ "decision": "", "criteria": \[\], "required_evidence": \[\], "approval_authority": "", "outcomes": \[\] }

## PAIN POINT ANALYSIS

Identify all customer pain points.

For each pain point provide:

- Description
- Root Cause
- Stakeholders Affected
- Severity
- Frequency
- Business Impact
- Accessibility Impact
- Potential Solutions

Assign scores:

- Impact (1-5)
- Frequency (1-5)
- Strategic Importance (1-5)

## ACCESSIBILITY NEEDS ANALYSIS

Identify accessibility-related customer needs.

Categorise into:

- Physical Accessibility
- Cognitive Accessibility
- Sensory Accessibility
- Neurodiversity
- Assistive Technology Support
- Language Accessibility
- Digital Accessibility

For each need identify:

- User group
- Risk if unmet
- Relevant standards
- Suggested mitigations

## CUSTOMER KNOWLEDGE GRAPH

Create entities and relationships for:

Customer → Goal

Customer → Pain Point

Pain Point → Solution

Customer → Journey

Journey → Decision

Decision → Outcome

Accessibility Need → Control

Control → Standard

Generate graph schema.

## TRAINING DATA OPPORTUNITIES

Identify opportunities to convert customer research into:

**RAG Data**

{ "customer_type": "", "pain_point": "", "context": "", "recommended_action": "" }

**Instruction Data**

{ "instruction": "How should an organisation address accessibility concerns during AI procurement?", "input": "", "output": "" }

**Agent Training Data**

{ "task": "", "customer_context": "", "analysis_steps": \[\], "recommendation": "" }

## CUSTOMER INSIGHT EXTRACTION

Generate a structured insight catalogue.

For each insight:

{ "insight_id": "", "stakeholder": "", "observation": "", "evidence": "", "impact": "", "confidence": "", "recommended_action": "" }

## VOICE OF THE CUSTOMER DATASET

Convert findings into machine-readable records.

Example:

{ "customer_segment": "", "challenge": "", "desired_outcome": "", "barriers": \[\], "requirements": \[\], "recommended_solution": "" }

## CUSTOMER MATURITY MODEL

If the repository contains frameworks, governance approaches, operating models, or assessment methodologies:

Identify customer maturity indicators.

Create maturity levels describing how customer needs are:

- Understood
- Measured
- Governed
- Prioritised
- Operationalised

Produce a Customer Experience Maturity Framework.