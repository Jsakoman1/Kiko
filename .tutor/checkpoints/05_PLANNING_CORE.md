# Phase 5 — Idea Discovery and Planning Core

<a id="kiko-029"></a>
### KIKO-029 — Classify facts, decisions, assumptions, and future ideas

- Checkpoint kind: implementation
- Observable outcome: A broad app idea becomes four separate collections with source and status.
- Why it matters: Codex must not hide unresolved product choices inside a plausible roadmap.
- Prerequisites: KIKO-023 and KIKO-027C.
- Known concepts: Dictionaries, lists, validation, and tagged request types.
- New concepts and syntax: Decision records and blocking/deferrable/future classification.
- Learner task: Classify one fixed idea fixture according to `PLANNING_SPEC.md`.
- Verification: `.venv/bin/python -m unittest tests.test_discovery.DecisionClassificationTests -v`
- Expected behavior: Product-changing uncertainty remains blocking; reversible implementation choices remain visible assumptions.
- Edge case: A privacy/cost/deployment choice cannot be silently defaulted.
- Not included: Asking questions or generating a roadmap.
- Exit condition: Confirmed, blocking, assumed, and future fixtures classify deterministically.

<a id="kiko-030"></a>
### KIKO-030 — Run beginner-friendly discovery rounds

- Checkpoint kind: implementation
- Observable outcome: Kiko selects no more than three next blocking questions and preserves previous answers.
- Why it matters: Discovery must be thorough without forcing a beginner through a technical questionnaire.
- Prerequisites: KIKO-029.
- Known concepts: Lists, ordering, conditions, and decision records.
- New concepts and syntax: Priority selection, round state, and recommended-default metadata.
- Learner task: Produce the next question round from confirmed and open decision fixtures.
- Verification: `.venv/bin/python -m unittest tests.test_discovery.DiscoveryRoundTests -v`
- Expected behavior: The highest-impact unanswered questions appear once with reason and safe default when available.
- Edge case: “I am not sure” creates a visible reversible assumption instead of looping the same question.
- Not included: Codex plan generation or writing project files.
- Exit condition: Question limit, reuse, ordering, and unsure-answer fixtures pass.

<a id="kiko-031"></a>
### KIKO-031 — Enforce brief readiness and separate acceptance

- Checkpoint kind: implementation
- Observable outcome: Kiko blocks planning until all required brief dimensions are confirmed.
- Why it matters: A model cannot compensate reliably for missing product ownership decisions.
- Prerequisites: KIKO-030.
- Known concepts: Validation, decisions, conditions, and explicit user actions.
- New concepts and syntax: Readiness predicates and separate brief/plan acceptance states.
- Learner task: Validate one brief candidate and expose exact remaining blockers.
- Verification: `.venv/bin/python -m unittest tests.test_planning_readiness -v`
- Expected behavior: Complete accepted brief becomes plan-ready; missing or unaccepted dimensions remain blocked.
- Edge case: Deferrable decisions include a latest-resolution checkpoint.
- Not included: Producing or accepting a roadmap.
- Exit condition: Complete, incomplete, deferred, and revoked-acceptance fixtures pass.

<a id="kiko-032"></a>
### KIKO-032 — Validate checkpoint fields and unique IDs

- Checkpoint kind: implementation
- Observable outcome: A candidate roadmap passes only when every checkpoint has the complete standard contract and a unique stable ID.
- Why it matters: Missing fields or duplicate identities make teaching, progress, and review ambiguous.
- Prerequisites: KIKO-031.
- Known concepts: Validation, lists, IDs, and checkpoint contract fields.
- New concepts and syntax: Uniqueness sets and ordered required-field validation.
- Learner task: Validate all required fields/order and reject duplicate checkpoint IDs.
- Verification: `.venv/bin/python -m unittest tests.test_plan_structure.FieldAndIdTests -v`
- Expected behavior: Complete unique checkpoints pass; missing/reordered/duplicate fields or IDs fail precisely.
- Edge case: A pending checkpoint can be reordered without changing its stable ID.
- Not included: Judging product coverage or calling Codex.
- Exit condition: Required-field and unique-ID fixtures return deterministic repair findings.

<a id="kiko-032a"></a>
### KIKO-032A — Validate prerequisite references and ordering

- Checkpoint kind: implementation
- Observable outcome: Every prerequisite names an existing earlier checkpoint.
- Why it matters: Learners cannot implement a dependency that is missing or scheduled in the future.
- Prerequisites: KIKO-032.
- Known concepts: Stable IDs, list order, dictionaries, and validation findings.
- New concepts and syntax: ID-to-position lookup and forward-dependency validation.
- Learner task: Reject unknown, self, later, and duplicate prerequisite references.
- Verification: `.venv/bin/python -m unittest tests.test_plan_structure.PrerequisiteTests -v`
- Expected behavior: Earlier prerequisites pass; unknown/self/later references fail with exact IDs.
- Edge case: Strict earlier-only prerequisites make dependency cycles impossible without a separate graph algorithm.
- Not included: Semantic checkpoint size or product coverage.
- Exit condition: Valid, unknown, self, later, and repeated prerequisite fixtures pass.

<a id="kiko-032b"></a>
### KIKO-032B — Reject vague or multi-outcome checkpoints

- Checkpoint kind: implementation
- Observable outcome: Candidate checkpoints exceeding the complexity budget return a split requirement.
- Why it matters: One lesson must remain comparable to the learner's recent successful workload.
- Prerequisites: KIKO-032A.
- Known concepts: Atomic checkpoint contract, product outcomes, learner tasks, and validation findings.
- New concepts and syntax: Complexity-budget classification and structured split proposals.
- Learner task: Classify keep/split/integration fixtures and report independent outcomes or mental models.
- Verification: `.venv/bin/python -m unittest tests.test_plan_structure.AtomicityTests -v`
- Expected behavior: One-behavior implementation and one-question integration pass; vague/multi-boundary work requests a split.
- Edge case: Acceptance may verify many existing behaviors but cannot introduce unrelated implementation.
- Not included: Product requirement coverage or automatic plan rewriting.
- Exit condition: Keep, split, integration, acceptance, and vague-language fixtures pass.

<a id="kiko-033"></a>
### KIKO-033 — Trace requirements to implementation and verification

- Checkpoint kind: implementation
- Observable outcome: Every confirmed requirement maps to implementation and verification, and every checkpoint maps back to an accepted reason.
- Why it matters: Structurally valid steps can still omit requirements or introduce speculative scope.
- Prerequisites: KIKO-032B.
- Known concepts: Requirement lists, checkpoint IDs, and validation reports.
- New concepts and syntax: Bidirectional traceability matrix.
- Learner task: Validate requirement-to-checkpoint/test and checkpoint-to-reason links.
- Verification: `.venv/bin/python -m unittest tests.test_plan_coverage.TraceabilityTests -v`
- Expected behavior: Complete bidirectional map passes; uncovered requirement and ungrounded checkpoint fail.
- Edge case: A proposed checkpoint without a confirmed requirement/risk/learning need is flagged as scope expansion.
- Not included: Model critique wording or user presentation.
- Exit condition: Requirement/checkpoint/test traceability fixtures pass without speculative scope.

<a id="kiko-033a"></a>
### KIKO-033A — Audit product, data, and integration coverage

- Checkpoint kind: implementation
- Observable outcome: Candidate plan covers primary/alternate UX, data lifecycle, and every external-boundary failure.
- Why it matters: A feature list can omit empty/error/retry/resume behavior or data ownership.
- Prerequisites: KIKO-033.
- Known concepts: Traceability findings, product journeys, data owners, and external boundaries.
- New concepts and syntax: Coverage-category rules for UX, data, and integrations.
- Learner task: Audit one plan fixture and list uncovered user/data/integration requirements.
- Verification: `.venv/bin/python -m unittest tests.test_plan_coverage.ProductDataIntegrationTests -v`
- Expected behavior: Complete fixture passes; missing state, lifecycle, auth, timeout, or recovery category fails precisely.
- Edge case: A non-applicable category is excluded only with an explicit brief reason.
- Not included: Test/release/teaching coverage or model critique prose.
- Exit condition: Applicable UX, data, and integration categories have traceable implementation and verification.

<a id="kiko-033b"></a>
### KIKO-033B — Audit engineering, release, and teaching coverage

- Checkpoint kind: implementation
- Observable outcome: Candidate plan covers tests, diagnostics, security, packaging/deployment, upgrade/uninstall, docs, and teaching order.
- Why it matters: “Feature complete” is not a finished or teachable product.
- Prerequisites: KIKO-033A.
- Known concepts: Coverage categories, release boundary, lesson contract, and traceability.
- New concepts and syntax: Engineering/release/teaching coverage rules.
- Learner task: Audit one plan fixture and list uncovered quality, delivery, or learning prerequisites.
- Verification: `.venv/bin/python -m unittest tests.test_plan_coverage.EngineeringReleaseTeachingTests -v`
- Expected behavior: Complete fixture passes; each omitted applicable category produces one actionable finding.
- Edge case: A deliberately excluded release concern must point to the confirmed brief exclusion.
- Not included: Generating missing checkpoints or user plan presentation.
- Exit condition: Applicable quality, delivery, and teaching categories all map to checkpoints/tests.

<a id="kiko-034"></a>
### KIKO-034 — Present a plan without overwhelming beginners

- Checkpoint kind: implementation
- Observable outcome: Kiko shows release increments, assumptions, risks, plan size, first checkpoint, and full-plan option.
- Why it matters: Beginners need informed control without reading the full technical roadmap immediately.
- Prerequisites: KIKO-031, KIKO-032B, KIKO-033B, and KIKO-027C.
- Known concepts: Canonical interactions, user confirmation, and validated plan records.
- New concepts and syntax: Progressive disclosure and expandable plan-detail view model.
- Learner task: Build the plan-summary interaction without applying any plan decision.
- Verification: `.venv/bin/python -m unittest tests.test_plan_review.PresentationTests -v`
- Expected behavior: Summary shows required scope/size/risk/first step; expand shows the same validated candidate in full.
- Edge case: Beginner summary hides implementation noise without hiding assumptions, exclusions, or blockers.
- Not included: Codex generation or filesystem templates.
- Exit condition: Summary, expand, simplify-language, missing-required-summary, and no-state-change fixtures pass.

<a id="kiko-034a"></a>
### KIKO-034A — Apply plan accept, revise, expand, and cancel decisions

- Checkpoint kind: implementation
- Observable outcome: User decision moves a validated candidate to accepted, revision, expanded view, or cancelled state predictably.
- Why it matters: Plan presentation and durable plan authority must remain separate.
- Prerequisites: KIKO-034.
- Known concepts: Plan summary, candidate state, user confirmation, and accepted-plan ownership.
- New concepts and syntax: Plan decision transition and accepted-plan version metadata.
- Learner task: Apply one explicit plan decision without writing project files yet.
- Verification: `.venv/bin/python -m unittest tests.test_plan_review.DecisionTests -v`
- Expected behavior: Accept records candidate version; revise returns findings; expand changes only view; cancel preserves old plan.
- Edge case: Changed product decision invalidates only affected pending sections and reopens brief confirmation.
- Not included: Codex generation or transactional Tutor-file creation.
- Exit condition: Accept, revise, expand, cancel, invalid-transition, and scope-change fixtures pass.
