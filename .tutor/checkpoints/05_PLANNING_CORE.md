# Phase 5 — Idea Discovery and Planning Core

<a id="kiko-029"></a>
### KIKO-029 — Classify facts, decisions, assumptions, and future ideas

- Checkpoint kind: implementation
- Observable outcome: A broad app idea becomes four separate collections with source and status.
- Why it matters: Codex must not hide unresolved product choices inside a plausible roadmap.
- Prerequisites: KIKO-023 and KIKO-027F.
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
- Observable outcome: Kiko selects no more than three highest-priority unanswered blocking questions.
- Why it matters: Discovery must be thorough without forcing a beginner through a technical questionnaire.
- Prerequisites: KIKO-029.
- Known concepts: Lists, ordering, conditions, and decision records.
- New concepts and syntax: Priority selection and recommended-default metadata.
- Learner task: Produce the next question round from confirmed and open decision fixtures without applying answers.
- Verification: `.venv/bin/python -m unittest tests.test_discovery.DiscoveryRoundTests -v`
- Expected behavior: The highest-impact unanswered questions appear once with reason and safe default when available.
- Edge case: Already answered questions never appear again in a later round.
- Not included: Codex plan generation or writing project files.
- Exit condition: Question limit, reuse, ordering, reason, and safe-default fixtures pass.

<a id="kiko-030a"></a>
### KIKO-030A — Apply one discovery answer safely

- Checkpoint kind: implementation
- Observable outcome: One answer confirms a decision or records “I am not sure” as a visible reversible assumption without repeating the question.
- Why it matters: Discovery state must preserve user answers without hiding uncertainty or entering a question loop.
- Prerequisites: KIKO-030.
- Known concepts: Decision records, question rounds, blocking/deferrable classes, and explicit defaults.
- New concepts and syntax: Answer-source record and unsure-to-assumption transition.
- Learner task: Apply answered, corrected, and unsure responses to one discovery record.
- Verification: `.venv/bin/python -m unittest tests.test_discovery.DiscoveryAnswerTests -v`
- Expected behavior: Confirmed answer closes the question; unsure records a visible default; correction replaces only that decision.
- Edge case: A blocking choice cannot become confirmed solely from Kiko's proposed default.
- Not included: Selecting the next round, brief readiness, or plan generation.
- Exit condition: Answer, unsure, correction, blocking-default, and no-repeat fixtures pass.

<a id="kiko-031"></a>
### KIKO-031 — Enforce brief readiness

- Checkpoint kind: implementation
- Observable outcome: Kiko blocks planning until all required brief dimensions are confirmed and reports exact blockers.
- Why it matters: A model cannot compensate reliably for missing product ownership decisions.
- Prerequisites: KIKO-030A.
- Known concepts: Validation, decisions, conditions, and explicit user actions.
- New concepts and syntax: Readiness predicates and blocker findings.
- Learner task: Validate one brief candidate and expose exact remaining blockers.
- Verification: `.venv/bin/python -m unittest tests.test_planning_readiness -v`
- Expected behavior: A complete brief is ready for confirmation; missing dimensions remain blocked with exact findings.
- Edge case: Deferrable decisions include a latest-resolution checkpoint.
- Not included: Brief acceptance, producing a roadmap, or plan acceptance.
- Exit condition: Complete, incomplete, and deferred-deadline readiness fixtures pass.

<a id="kiko-031a"></a>
### KIKO-031A — Record separate brief acceptance

- Checkpoint kind: implementation
- Observable outcome: A ready brief becomes plan-draft eligible only after explicit user acceptance.
- Why it matters: Readiness is a Kiko validation result; acceptance is a separate user decision.
- Prerequisites: KIKO-031.
- Known concepts: Ready brief, user actions, state transitions, and validation findings.
- New concepts and syntax: Brief-acceptance receipt and revocation transition.
- Learner task: Apply accept, revise, and revoke actions to one ready brief without creating a plan.
- Verification: `.venv/bin/python -m unittest tests.test_planning_readiness.BriefAcceptanceTests -v`
- Expected behavior: Accept records the confirmed brief version; revise/revoke returns it to non-accepted state.
- Edge case: Editing a product-defining answer invalidates only the related acceptance, not preserved answers.
- Not included: Plan generation, plan acceptance, or project-file creation.
- Exit condition: Accept, revise, revoke, stale-version, and preserved-answer fixtures pass.

<a id="kiko-032"></a>
### KIKO-032 — Validate required checkpoint fields

- Checkpoint kind: implementation
- Observable outcome: A candidate checkpoint passes only when all standard contract fields are present in the required order.
- Why it matters: Missing or reordered fields force the Tutor to invent lesson information later.
- Prerequisites: KIKO-031A.
- Known concepts: Validation, lists, IDs, and checkpoint contract fields.
- New concepts and syntax: Ordered required-field validation.
- Learner task: Validate one checkpoint's field presence and order without checking ID uniqueness.
- Verification: `.venv/bin/python -m unittest tests.test_plan_structure.RequiredFieldTests -v`
- Expected behavior: Complete ordered fields pass; missing, empty, or reordered fields fail precisely.
- Edge case: A pending checkpoint can be reordered without changing its stable ID.
- Not included: ID uniqueness, prerequisite order, semantic size, coverage, or Codex calls.
- Exit condition: Complete, missing, empty, and reordered-field fixtures return deterministic findings.

<a id="kiko-032a"></a>
### KIKO-032A — Validate unique stable checkpoint IDs

- Checkpoint kind: implementation
- Observable outcome: Every candidate checkpoint has one unique stable ID that remains unchanged when pending work is reordered.
- Why it matters: Duplicate or mutable identities make progress, dependencies, and review evidence ambiguous.
- Prerequisites: KIKO-032.
- Known concepts: Required checkpoint fields, lists, IDs, and validation findings.
- New concepts and syntax: Uniqueness set and duplicate-ID finding.
- Learner task: Reject duplicate/missing IDs while allowing a pending checkpoint to move without renaming.
- Verification: `.venv/bin/python -m unittest tests.test_plan_structure.UniqueIdTests -v`
- Expected behavior: Unique IDs pass; duplicate/empty IDs fail with the exact collision.
- Edge case: Reordering pending items preserves their accepted IDs.
- Not included: Prerequisite references, semantic size, or product coverage.
- Exit condition: Unique, duplicate, empty, and reorder-stability fixtures pass.

<a id="kiko-032b"></a>
### KIKO-032B — Validate prerequisite references and ordering

- Checkpoint kind: implementation
- Observable outcome: Every prerequisite names an existing earlier checkpoint.
- Why it matters: Learners cannot implement a dependency that is missing or scheduled in the future.
- Prerequisites: KIKO-032A.
- Known concepts: Stable IDs, list order, dictionaries, and validation findings.
- New concepts and syntax: ID-to-position lookup and forward-dependency validation.
- Learner task: Reject unknown, self, later, and duplicate prerequisite references.
- Verification: `.venv/bin/python -m unittest tests.test_plan_structure.PrerequisiteTests -v`
- Expected behavior: Earlier prerequisites pass; unknown/self/later references fail with exact IDs.
- Edge case: Strict earlier-only prerequisites make dependency cycles impossible without a separate graph algorithm.
- Not included: Semantic checkpoint size or product coverage.
- Exit condition: Valid, unknown, self, later, and repeated prerequisite fixtures pass.

<a id="kiko-032c"></a>
### KIKO-032C — Reject vague or multi-outcome checkpoints

- Checkpoint kind: implementation
- Observable outcome: Candidate checkpoints exceeding the complexity budget return a split requirement.
- Why it matters: One lesson must remain comparable to the learner's recent successful workload.
- Prerequisites: KIKO-032B.
- Known concepts: Atomic checkpoint contract, product outcomes, learner tasks, and validation findings.
- New concepts and syntax: Complexity-budget classification and structured split proposals.
- Learner task: Classify keep/split/integration fixtures and report independent outcomes or mental models.
- Verification: `.venv/bin/python -m unittest tests.test_plan_structure.AtomicityTests -v`
- Expected behavior: One-behavior implementation and one-question integration pass; vague/multi-boundary work requests a split.
- Edge case: Acceptance may verify many existing behaviors but cannot introduce unrelated implementation; a historical size audit remains valid as covered checkpoints complete.
- Not included: Product requirement coverage or automatic plan rewriting.
- Exit condition: Keep, split, integration, acceptance, vague-language, and completed-audit-history fixtures pass.

<a id="kiko-032d"></a>
### KIKO-032D — Require lesson readiness for every final checkpoint

- Checkpoint kind: implementation
- Observable outcome: Every final post-split checkpoint proves it can render a complete lesson without inventing syntax, task, or verification detail.
- Why it matters: Atomicity must be checked after splitting, not only on the original large checkpoint when the next lesson is loaded.
- Prerequisites: KIKO-025A and KIKO-032C.
- Known concepts: Checkpoint fields, atomicity classification, syntax/configuration preflights, and lesson contract.
- New concepts and syntax: Post-split readiness record and lesson dry-run gate.
- Learner task: Validate one final checkpoint for one outcome, one responsibility, bounded concepts/syntax, exact verification, exclusions, and renderable lesson fields.
- Verification: `.venv/bin/python -m unittest tests.test_plan_structure.LessonReadinessTests -v`
- Expected behavior: Every final checkpoint has a readiness record; missing syntax detail, mixed responsibility, or invented lesson content fails before plan acceptance.
- Edge case: Integration/acceptance may remain broader only when it adds no unrelated implementation and answers one explicit release question.
- Not included: Rendering the real lesson or automatically rewriting a rejected checkpoint.
- Exit condition: Ready, missing-preflight, multi-responsibility, integration-exception, and post-split-coverage fixtures pass.

<a id="kiko-033"></a>
### KIKO-033 — Trace requirements to implementation and verification

- Checkpoint kind: implementation
- Observable outcome: Every confirmed requirement maps to implementation and verification, and every checkpoint maps back to an accepted reason.
- Why it matters: Structurally valid steps can still omit requirements or introduce speculative scope.
- Prerequisites: KIKO-032D.
- Known concepts: Requirement lists, checkpoint IDs, and validation reports.
- New concepts and syntax: Bidirectional traceability matrix.
- Learner task: Validate requirement-to-checkpoint/test and checkpoint-to-reason links.
- Verification: `.venv/bin/python -m unittest tests.test_plan_coverage.TraceabilityTests -v`
- Expected behavior: Complete bidirectional map passes; uncovered requirement and ungrounded checkpoint fail.
- Edge case: A proposed checkpoint without a confirmed requirement/risk/learning need is flagged as scope expansion.
- Not included: Model critique wording or user presentation.
- Exit condition: Requirement/checkpoint/test traceability fixtures pass without speculative scope.

<a id="kiko-033a"></a>
### KIKO-033A — Audit user-experience coverage

- Checkpoint kind: implementation
- Observable outcome: Candidate plan covers the primary workflow and applicable empty/loading/success/error/cancel/retry/restart/resume states.
- Why it matters: A feature list can omit the states users actually encounter.
- Prerequisites: KIKO-033.
- Known concepts: Traceability findings, product journeys, data owners, and external boundaries.
- New concepts and syntax: User-journey state coverage rules.
- Learner task: Audit one plan fixture and list uncovered user-visible states.
- Verification: `.venv/bin/python -m unittest tests.test_plan_coverage.UserExperienceTests -v`
- Expected behavior: Complete journey passes; each missing applicable user state fails precisely.
- Edge case: A non-applicable category is excluded only with an explicit brief reason.
- Not included: Data, integrations, engineering, release, teaching, or critique prose.
- Exit condition: Every applicable user-visible state has traceable implementation and verification.

<a id="kiko-033b"></a>
### KIKO-033B — Audit data-lifecycle coverage

- Checkpoint kind: implementation
- Observable outcome: Candidate plan covers applicable data ownership, schema, validation, persistence, backup, migration, export, retention, and deletion.
- Why it matters: User data can be lost or leaked even when the happy-path feature works.
- Prerequisites: KIKO-033A.
- Known concepts: Traceability, data owners, state contracts, and explicit applicability reasons.
- New concepts and syntax: Data-lifecycle coverage rules.
- Learner task: Audit one plan fixture and report each missing applicable data-lifecycle stage.
- Verification: `.venv/bin/python -m unittest tests.test_plan_coverage.DataLifecycleTests -v`
- Expected behavior: Complete owner lifecycle passes; each omitted applicable stage produces one finding.
- Edge case: A lifecycle stage is non-applicable only with a confirmed brief reason.
- Not included: External integrations, engineering/release/teaching coverage, or plan repair.
- Exit condition: Every applicable data owner and lifecycle stage maps to implementation and verification.

<a id="kiko-033c"></a>
### KIKO-033C — Audit external-integration coverage

- Checkpoint kind: implementation
- Observable outcome: Every external boundary covers authentication, unavailability, timeout, cancellation, malformed response, compatibility, and cleanup where applicable.
- Why it matters: External tools fail independently and must not leave Kiko hanging or corrupt state.
- Prerequisites: KIKO-033B.
- Known concepts: Traceability, external boundaries, error states, and applicability reasons.
- New concepts and syntax: Integration-failure coverage rules.
- Learner task: Audit one plan fixture and report missing failure handling for each external system.
- Verification: `.venv/bin/python -m unittest tests.test_plan_coverage.ExternalIntegrationTests -v`
- Expected behavior: Complete boundaries pass; each missing applicable auth/timeout/cancel/malformed/cleanup path fails.
- Edge case: A project without an external system excludes the category only through the confirmed brief.
- Not included: Engineering, delivery, teaching, or model critique prose.
- Exit condition: Every external boundary has traceable happy/failure-path implementation and verification.

<a id="kiko-033d"></a>
### KIKO-033D — Audit engineering-quality coverage

- Checkpoint kind: implementation
- Observable outcome: Candidate plan covers applicable unit/integration/protocol/e2e tests, diagnostics, security, privacy, and accessibility.
- Why it matters: Feature behavior without quality controls is not a dependable product.
- Prerequisites: KIKO-033C.
- Known concepts: Coverage categories, traceability, test layers, and product quality gates.
- New concepts and syntax: Engineering-quality coverage rules.
- Learner task: Audit one plan fixture and report each missing applicable engineering-quality category.
- Verification: `.venv/bin/python -m unittest tests.test_plan_coverage.EngineeringQualityTests -v`
- Expected behavior: Complete quality plan passes; each missing applicable category returns one actionable finding.
- Edge case: A deliberately excluded category must link to a confirmed scope reason.
- Not included: Packaging, upgrade/uninstall, documentation, teaching order, or plan repair.
- Exit condition: Every applicable engineering-quality category maps to implementation and proof.

<a id="kiko-033e"></a>
### KIKO-033E — Audit delivery and lifecycle coverage

- Checkpoint kind: implementation
- Observable outcome: Candidate plan covers packaging/deployment, onboarding, configuration, upgrade/rollback, uninstall, documentation, and clean-environment acceptance.
- Why it matters: A repository demo is not a finished usable product.
- Prerequisites: KIKO-033D.
- Known concepts: Release boundary, artifacts, traceability, and explicit exclusions.
- New concepts and syntax: Delivery/lifecycle coverage rules.
- Learner task: Audit one plan fixture and report missing applicable delivery or lifecycle work.
- Verification: `.venv/bin/python -m unittest tests.test_plan_coverage.DeliveryLifecycleTests -v`
- Expected behavior: Finished-product fixture passes; each omitted applicable concern produces one finding.
- Edge case: Publication can remain excluded while an installable artifact and instructions stay required.
- Not included: Teaching order, plan repair, or user presentation.
- Exit condition: Every applicable delivery/lifecycle concern maps to implementation and acceptance evidence.

<a id="kiko-033f"></a>
### KIKO-033F — Audit teaching-order coverage

- Checkpoint kind: implementation
- Observable outcome: Candidate plan introduces prerequisites and syntax before use and never treats explanation as competence.
- Why it matters: A complete product roadmap can still be unteachable for its learner.
- Prerequisites: KIKO-033E.
- Known concepts: Lesson readiness, prerequisites, concept stages, and traceability.
- New concepts and syntax: Teaching-order coverage rules.
- Learner task: Audit one plan fixture for prerequisite order, syntax disclosure, workload growth, verification accessibility, and competence boundaries.
- Verification: `.venv/bin/python -m unittest tests.test_plan_coverage.TeachingOrderTests -v`
- Expected behavior: Teachable plan passes; premature syntax, missing prerequisite, size jump, or false competence fails.
- Edge case: Later work may grow moderately only when prior checkpoints establish the needed concepts.
- Not included: Generating repairs or presenting the plan.
- Exit condition: Every teaching-order and learning-evidence gate passes.

<a id="kiko-034"></a>
### KIKO-034 — Present a plan without overwhelming beginners

- Checkpoint kind: implementation
- Observable outcome: Kiko shows release increments, assumptions, risks, plan size, first checkpoint, and full-plan option.
- Why it matters: Beginners need informed control without reading the full technical roadmap immediately.
- Prerequisites: KIKO-031A, KIKO-032D, KIKO-033F, and KIKO-027F.
- Known concepts: Canonical interactions, user confirmation, and validated plan records.
- New concepts and syntax: Progressive disclosure and expandable plan-detail view model.
- Learner task: Build the plan-summary interaction without applying any plan decision.
- Verification: `.venv/bin/python -m unittest tests.test_plan_review.PresentationTests -v`
- Expected behavior: Summary shows required scope/size/risk/first step; expand shows the same validated candidate in full.
- Edge case: Beginner summary hides implementation noise without hiding assumptions, exclusions, or blockers.
- Not included: Codex generation or filesystem templates.
- Exit condition: Summary, expand, simplify-language, missing-required-summary, and no-state-change fixtures pass.

<a id="kiko-034a"></a>
### KIKO-034A — Accept one validated plan candidate

- Checkpoint kind: implementation
- Observable outcome: Explicit user acceptance promotes exactly one validated candidate version to accepted-plan state.
- Why it matters: Plan presentation and durable plan authority must remain separate.
- Prerequisites: KIKO-034.
- Known concepts: Plan summary, candidate state, user confirmation, and accepted-plan ownership.
- New concepts and syntax: Accepted-plan version receipt.
- Learner task: Accept one current validated candidate without writing project files.
- Verification: `.venv/bin/python -m unittest tests.test_plan_review.AcceptPlanTests -v`
- Expected behavior: Acceptance records exact candidate/brief versions and preserves prior accepted plan for recovery.
- Edge case: Stale or unvalidated candidate cannot be accepted.
- Not included: Codex generation or transactional Tutor-file creation.
- Exit condition: Accept, stale-candidate, invalid-candidate, version-receipt, and prior-plan-preservation fixtures pass.

<a id="kiko-034b"></a>
### KIKO-034B — Revise or reopen a plan candidate

- Checkpoint kind: implementation
- Observable outcome: Revision findings return a candidate for repair, while a product-changing answer reopens only affected brief/plan sections.
- Why it matters: Technical repair and changed user scope have different authorities and invalidation boundaries.
- Prerequisites: KIKO-034A.
- Known concepts: Candidate findings, accepted-plan versions, brief acceptance, and affected-section mapping.
- New concepts and syntax: Revision transition and scoped invalidation record.
- Learner task: Route one technical revision and one product-scope change to the correct state.
- Verification: `.venv/bin/python -m unittest tests.test_plan_review.RevisePlanTests -v`
- Expected behavior: Technical revise preserves brief; scope change reopens confirmation and only affected pending sections.
- Edge case: Completed valid work remains preserved unless its requirement was explicitly invalidated.
- Not included: Provider repair calls, project-file writes, or cancellation.
- Exit condition: Technical revise, scope reopen, affected-only invalidation, and completed-work fixtures pass.

<a id="kiko-034c"></a>
### KIKO-034C — Cancel a plan candidate safely

- Checkpoint kind: implementation
- Observable outcome: Cancelling review discards only the pending candidate and preserves confirmed answers plus the last accepted plan.
- Why it matters: A user must be able to leave planning without losing trusted project state.
- Prerequisites: KIKO-034B.
- Known concepts: Candidate/accepted versions, explicit user actions, and state ownership.
- New concepts and syntax: Cancel transition and preserved-state receipt.
- Learner task: Cancel one pending/revision candidate without writing Tutor files.
- Verification: `.venv/bin/python -m unittest tests.test_plan_review.CancelPlanTests -v`
- Expected behavior: Pending candidate disappears; confirmed brief, answers, application source, and old plan remain unchanged.
- Edge case: Repeated cancel is idempotent and reports no pending candidate.
- Not included: Project-file creation or provider calls.
- Exit condition: Cancel, repeated-cancel, confirmed-answer, old-plan, and source-unchanged fixtures pass.
