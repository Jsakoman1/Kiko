# Phase 6 — Provider-Neutral Expert Boundary

<a id="kiko-035"></a>
### KIKO-035 — Define tutoring expert request and result contracts

- Checkpoint kind: implementation
- Observable outcome: Tutor Core has validated provider-neutral request/result shapes for one tutoring interaction.
- Why it matters: Codex must remain replaceable and unable to own pedagogy or durable state.
- Prerequisites: KIKO-026A and KIKO-027F.
- Known concepts: Versioned contracts, validation, bounded context, and tagged interaction types.
- New concepts and syntax: Provider DTOs and explicit proposed-versus-accepted fields.
- Learner task: Define one tutoring request/result contract and validate required/forbidden fields.
- Verification: `.venv/bin/python -m unittest tests.test_expert_contracts.TutoringContractTests -v`
- Expected behavior: Valid proposals pass; source-write actions, direct progress updates, and malformed results fail.
- Edge case: Unknown optional provider metadata is ignored without becoming learner-facing state.
- Not included: Provider classes, subprocesses, or network/model calls.
- Exit condition: Tutoring request/result, unsafe action, malformed result, and inert-proposal fixtures enforce Tutor ownership.

<a id="kiko-035a"></a>
### KIKO-035A — Define candidate-plan expert contracts

- Checkpoint kind: implementation
- Observable outcome: A confirmed brief uses provider-neutral request/result shapes for one non-canonical candidate plan.
- Why it matters: Codex may propose a roadmap but cannot declare it valid or user-accepted.
- Prerequisites: KIKO-033F, KIKO-034C, and KIKO-035.
- Known concepts: Tutoring contracts, confirmed briefs, candidate validation, and accepted-plan ownership.
- New concepts and syntax: Candidate-planning purpose tag and candidate correlation ID.
- Learner task: Define/validate candidate-plan request and result shapes without provider behavior.
- Verification: `.venv/bin/python -m unittest tests.test_expert_contracts.CandidatePlanContractTests -v`
- Expected behavior: Valid candidate proposal passes; missing brief/lineage or claimed acceptance fails.
- Edge case: Unknown optional provider metadata remains inert.
- Not included: Provider interface, fake/live model calls, or project-file writes.
- Exit condition: Valid, malformed, unknown-lineage, claimed-acceptance, and optional-metadata fixtures pass.

<a id="kiko-035b"></a>
### KIKO-035B — Define plan-critique expert contracts

- Checkpoint kind: implementation
- Observable outcome: A critique request/result references one candidate and returns structured findings without changing it.
- Why it matters: Plan critique has different authority and required fields from candidate generation.
- Prerequisites: KIKO-035A.
- Known concepts: Candidate contract, correlation IDs, coverage/atomicity findings, and provider-neutral shapes.
- New concepts and syntax: Critique-purpose tag and finding-category payload.
- Learner task: Define/validate critique request/result shapes and forbid candidate mutation or acceptance.
- Verification: `.venv/bin/python -m unittest tests.test_expert_contracts.CritiqueContractTests -v`
- Expected behavior: Known candidate/findings pass; unknown lineage, malformed findings, or mutation claims fail.
- Edge case: Scope-expansion finding stays labeled rather than becoming a new requirement.
- Not included: Repair contracts, provider calls, or project writes.
- Exit condition: Valid, malformed, unknown-lineage, mutation, and scope-expansion fixtures pass.

<a id="kiko-035c"></a>
### KIKO-035C — Define plan-repair expert contracts

- Checkpoint kind: implementation
- Observable outcome: A repair request/result links critique findings to a revised candidate or an unresolved decision.
- Why it matters: Codex may repair implementation detail but cannot invent blocking product facts.
- Prerequisites: KIKO-035B.
- Known concepts: Candidate/critique lineage, findings, discovery blockers, and provider-neutral shapes.
- New concepts and syntax: Repair-purpose tag and affected-section mapping.
- Learner task: Define/validate repaired-candidate and reopen-decision result variants.
- Verification: `.venv/bin/python -m unittest tests.test_expert_contracts.RepairContractTests -v`
- Expected behavior: Valid repair/reopen variants pass; unknown findings, unrelated sections, or acceptance claims fail.
- Edge case: Reopen result preserves confirmed answers and identifies only the blocking decision.
- Not included: Provider calls, applying repairs, or project-file writes.
- Exit condition: Repair, reopen, malformed-lineage, unrelated-section, and authority-boundary fixtures pass.

<a id="kiko-036"></a>
### KIKO-036 — Define the single ExpertProvider operation

- Checkpoint kind: implementation
- Observable outcome: One provider interface exposes only `ask(expert_request) -> expert_result`.
- Why it matters: Fake, Codex, and future local experts need one explicit replaceable seam before Core uses it.
- Prerequisites: KIKO-035C.
- Known concepts: Functions, request/result contracts, and module boundaries.
- New concepts and syntax: Python `Protocol` (or chosen abstract interface) and method contract.
- Learner task: Define the provider seam and validate a compatible/incompatible stub structurally.
- Verification: `.venv/bin/python -m unittest tests.test_expert_provider.ProviderContractTests -v`
- Expected behavior: A minimal `ask` stub satisfies the seam; extra provider details do not enter Tutor Core.
- Edge case: A provider missing `ask` fails clearly before a real request.
- Not included: Codex process lifecycle or provider selection UI.
- Exit condition: Compatible, missing-method, wrong-result, and no-provider-detail fixtures pass.

<a id="kiko-036a"></a>
### KIKO-036A — Inject and call an ExpertProvider

- Checkpoint kind: implementation
- Observable outcome: One Tutor Core operation receives a provider and calls only its documented `ask` method.
- Why it matters: Defining an interface does not prove Core is actually independent from provider implementation.
- Prerequisites: KIKO-036.
- Known concepts: Provider interface, request/result contracts, function arguments, and controlled errors.
- New concepts and syntax: Constructor/function dependency injection and provider-exception mapping.
- Learner task: Inject a stub provider into one Core call and convert provider failure to a controlled expert error.
- Verification: `.venv/bin/python -m unittest tests.test_expert_provider.ProviderInjectionTests -v`
- Expected behavior: Two compatible stubs are interchangeable; one failing stub yields the same controlled boundary error.
- Edge case: Raw provider exception details do not leak into learner-facing data.
- Not included: Fake scenario catalog, Codex processes, or provider selection UI.
- Exit condition: First/second stub, one-call-only, controlled-error, and no-detail-leak fixtures pass.

<a id="kiko-037"></a>
### KIKO-037 — Prove tutoring with a deterministic fake expert

- Checkpoint kind: integration
- Observable outcome: A fake provider returns valid tutoring proposals for success and controlled failure fixtures.
- Why it matters: Tutor behavior must be testable without Codex, authentication, latency, or cost.
- Prerequisites: KIKO-036A and KIKO-027F.
- Known concepts: Dependency injection, fixed fixtures, validation, and canonical interactions.
- New concepts and syntax: Test doubles and deterministic provider scenarios.
- Learner task: Implement a fake provider response and pass it through Tutor validation/presentation.
- Verification: `.venv/bin/python -m unittest tests.integration.test_fake_tutoring -v`
- Expected behavior: Valid fake response becomes TutorInteraction; invalid/unsupported response becomes a controlled error.
- Edge case: Proposed knowledge signals do not update evidence without learner review.
- Not included: Live Codex, streaming, or process events.
- Exit condition: Help and error flows work end to end against the fake provider.

<a id="kiko-038"></a>
### KIKO-038 — Produce a fake candidate plan

- Checkpoint kind: implementation
- Observable outcome: A fake provider returns one structured candidate plan for a confirmed brief.
- Why it matters: Planning policy must be proven before live model variability is introduced.
- Prerequisites: KIKO-033F, KIKO-034C, and KIKO-036A.
- Known concepts: Candidate plans, coverage findings, fake providers, and user acceptance.
- New concepts and syntax: Planning-purpose provider fixture and candidate correlation ID.
- Learner task: Return and validate one incomplete-but-structured fake candidate without accepting it.
- Verification: `.venv/bin/python -m unittest tests.integration.test_fake_planning.CandidateTests -v`
- Expected behavior: Candidate remains non-canonical and structural/coverage findings remain available.
- Edge case: Malformed provider result becomes a controlled error without changing the accepted plan.
- Not included: Live Codex planning or writing real project files.
- Exit condition: Valid, incomplete, malformed, and provider-error candidate fixtures pass.

<a id="kiko-038a"></a>
### KIKO-038A — Critique a fake candidate plan

- Checkpoint kind: integration
- Observable outcome: A separate fake critique reports coverage, atomicity, unsafe assumptions, and scope-expansion findings.
- Why it matters: The provider that drafted a plan cannot make it canonical without an explicit quality pass.
- Prerequisites: KIKO-038.
- Known concepts: Candidate plans, structural/coverage validators, provider fixtures, and correlation IDs.
- New concepts and syntax: Separate critique-purpose request/result and finding categories.
- Learner task: Send one candidate to a fake critic and validate its structured findings.
- Verification: `.venv/bin/python -m unittest tests.integration.test_fake_planning.CritiqueTests -v`
- Expected behavior: Known gaps are found; unrelated new features are flagged as scope expansion.
- Edge case: Critique cannot modify the candidate or declare user acceptance.
- Not included: Repairing the plan or live Codex.
- Exit condition: Complete, missing-coverage, vague-step, unsafe-assumption, and scope-expansion critiques pass.

<a id="kiko-038b"></a>
### KIKO-038B — Repair or reopen a fake plan

- Checkpoint kind: integration
- Observable outcome: Critique findings produce a revalidated repaired candidate or reopen a blocking user decision.
- Why it matters: Quality repair must not silently invent product choices.
- Prerequisites: KIKO-038A.
- Known concepts: Critique findings, plan validation, discovery blockers, and plan review.
- New concepts and syntax: Repair lineage and affected-section invalidation.
- Learner task: Apply one fake repair and route one ambiguity finding back to discovery.
- Verification: `.venv/bin/python -m unittest tests.integration.test_fake_planning.RepairTests -v`
- Expected behavior: Valid repair awaits user acceptance; product ambiguity blocks and preserves confirmed answers.
- Edge case: Cancel preserves the last accepted plan and removes only the pending candidate.
- Not included: Live Codex or writing project files.
- Exit condition: Repair, revalidation, ambiguity-reopen, cancel, and acceptance-boundary fixtures pass.
