# Phase 6 — Provider-Neutral Expert Boundary

<a id="kiko-035"></a>
### KIKO-035 — Define tutoring expert request and result contracts

- Checkpoint kind: implementation
- Observable outcome: Tutor Core has validated provider-neutral request/result shapes for one tutoring interaction.
- Why it matters: Codex must remain replaceable and unable to own pedagogy or durable state.
- Prerequisites: KIKO-026 and KIKO-027C.
- Known concepts: Versioned contracts, validation, bounded context, and tagged interaction types.
- New concepts and syntax: Provider DTOs and explicit proposed-versus-accepted fields.
- Learner task: Define one tutoring request/result contract and validate required/forbidden fields.
- Verification: `.venv/bin/python -m unittest tests.test_expert_contracts.TutoringContractTests -v`
- Expected behavior: Valid proposals pass; source-write actions, direct progress updates, and malformed results fail.
- Edge case: Unknown optional provider metadata is ignored without becoming learner-facing state.
- Not included: Provider classes, subprocesses, or network/model calls.
- Exit condition: Tutoring request/result, unsafe action, malformed result, and inert-proposal fixtures enforce Tutor ownership.

<a id="kiko-035a"></a>
### KIKO-035A — Define planning expert request and result contracts

- Checkpoint kind: implementation
- Observable outcome: Candidate, critique, and repair expert requests/results use explicit provider-neutral planning shapes.
- Why it matters: Planning stages need different required fields while preserving the same Tutor authority boundary.
- Prerequisites: KIKO-033B, KIKO-034A, and KIKO-035.
- Known concepts: Tutoring contracts, plan validation, critique findings, candidate lineage, and accepted-plan state.
- New concepts and syntax: Planning-purpose tagged request/result variants.
- Learner task: Define and validate planning contract variants without adding provider behavior.
- Verification: `.venv/bin/python -m unittest tests.test_expert_contracts.PlanningContractTests -v`
- Expected behavior: Candidate/critique/repair variants accept only their required fields and cannot claim user acceptance.
- Edge case: Critique/repair references unknown candidate or checkpoint IDs fail precisely.
- Not included: Provider interface, fake/live model calls, or project-file writes.
- Exit condition: Candidate, critique, repair, malformed, unknown-lineage, and authority-boundary fixtures pass.

<a id="kiko-036"></a>
### KIKO-036 — Introduce the single ExpertProvider operation

- Checkpoint kind: implementation
- Observable outcome: Tutor Core calls one `ask(expert_request)` boundary without knowing provider details.
- Why it matters: Fake, Codex, and future local experts must be interchangeable behind one seam.
- Prerequisites: KIKO-035A.
- Known concepts: Functions, request/result contracts, and module boundaries.
- New concepts and syntax: Python protocols or abstract interfaces and dependency injection.
- Learner task: Define the provider seam and inject it into one Core operation.
- Verification: `.venv/bin/python -m unittest tests.test_expert_provider -v`
- Expected behavior: A minimal stub satisfying `ask` works; an incompatible provider fails clearly.
- Edge case: Provider exceptions become controlled expert errors rather than raw tracebacks.
- Not included: Codex process lifecycle or provider selection UI.
- Exit condition: Tutor Core executes against a replaceable stub through only the documented operation.

<a id="kiko-037"></a>
### KIKO-037 — Prove tutoring with a deterministic fake expert

- Checkpoint kind: integration
- Observable outcome: A fake provider returns valid tutoring proposals for success and controlled failure fixtures.
- Why it matters: Tutor behavior must be testable without Codex, authentication, latency, or cost.
- Prerequisites: KIKO-036 and KIKO-027C.
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
- Prerequisites: KIKO-033B, KIKO-034A, and KIKO-036.
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
