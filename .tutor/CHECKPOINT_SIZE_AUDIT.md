# Kiko Checkpoint Size Audit

## Audit basis

Date: 2026-09-04

Baseline: KIKO-005 introduced one mental model, one learner-owned refactor, and
one observable behavior-preservation check. Later implementation checkpoints may
be moderately larger, but should stay within roughly two to four baseline-sized
changes. Integration and acceptance checkpoints may verify several existing
behaviors when they introduce no unrelated feature.

Decision meanings:

- `keep`: one sufficiently coherent implementation/decision behavior
- `split`: contained independently teachable or verifiable behaviors
- `integration`: combines existing components to answer one integration question
- `acceptance`: validates one release outcome without adding product behavior

## Audit of all originally pending checkpoints

| Original | Decision | Normalized result | Reason |
| --- | --- | --- | --- |
| KIKO-011 | keep | KIKO-011 | One read-only reference-loading behavior. |
| KIKO-012 | split | KIKO-012, KIKO-012A, KIKO-012B | Environment creation, Python package structure, and packaging metadata/editable install are independently learnable. |
| KIKO-013 | keep | KIKO-013 | One progress-ownership correction. |
| KIKO-014 | split | KIKO-014, KIKO-014A | First unittest structure and filesystem isolation/mocking are separate mental models. |
| KIKO-015 | split | KIKO-015, KIKO-015A, KIKO-015B, KIKO-015C, KIKO-015D, KIKO-015E | Root/version, nested project fields, loading, and each remaining state owner are separate learning boundaries. |
| KIKO-016 | split | KIKO-016, KIKO-016A, KIKO-016B, KIKO-016C | Atomic replacement, backup preservation, restore, and schema migration are separate failure models. |
| KIKO-017 | split | KIKO-017, KIKO-017A, KIKO-017B, KIKO-017C | Request/success, error, progress, and cancellation messages have separate semantics. |
| KIKO-018 | split | KIKO-018, KIKO-018A, KIKO-018B, KIKO-018C | Path containment, bounded text, secret filtering, and untrusted labeling are distinct controls. |
| KIKO-019 | keep | KIKO-019 | One pure evidence record. |
| KIKO-020 | keep | KIKO-020 | One conservative concept-update rule. |
| KIKO-021 | keep | KIKO-021 | One accepted-review learner-state transaction. |
| KIKO-022 | keep | KIKO-022 | One idempotent personal-reference update. |
| KIKO-023 | keep | KIKO-023 | One learner-request value and validation boundary. |
| KIKO-024 | split | KIKO-024, KIKO-024A | Interaction intent and assistance strength are independent policy axes. |
| KIKO-025 | split | KIKO-025, KIKO-025A | Code syntax and declarative configuration require different preflight contracts. |
| KIKO-026 | split | KIKO-026, KIKO-026A | Context field selection and context-size enforcement are independent controls. |
| KIKO-027 | split | KIKO-027, KIKO-027A, KIKO-027B, KIKO-027C, KIKO-027D, KIKO-027E, KIKO-027F | Every interaction type now has its own independently testable contract. |
| KIKO-028 | split | KIKO-028, KIKO-028A, KIKO-028B, KIKO-028C | Classification, immediate repair, sanitization, and deduplication are separate effects. |
| KIKO-029 | keep | KIKO-029 | One uncertainty-classification model. |
| KIKO-030 | split | KIKO-030, KIKO-030A | Selecting questions and applying answers/default uncertainty are separate state effects. |
| KIKO-031 | split | KIKO-031, KIKO-031A | Deterministic readiness and explicit user acceptance are different authorities. |
| KIKO-032 | split | KIKO-032, KIKO-032A, KIKO-032B, KIKO-032C, KIKO-032D | Fields, IDs, prerequisites, atomicity, and final lesson readiness are independent gates. |
| KIKO-033 | split | KIKO-033, KIKO-033A, KIKO-033B, KIKO-033C, KIKO-033D, KIKO-033E, KIKO-033F | Traceability, UX, data, integrations, engineering, delivery, and teaching each receive a focused audit. |
| KIKO-034 | split | KIKO-034, KIKO-034A, KIKO-034B, KIKO-034C | Presentation, acceptance, revision/scope reopen, and cancellation have different state effects. |
| KIKO-035 | split | KIKO-035, KIKO-035A, KIKO-035B, KIKO-035C | Tutoring, candidate, critique, and repair provider contracts carry different authority and fields. |
| KIKO-036 | split | KIKO-036, KIKO-036A | Defining the provider interface and injecting/calling it are separate learning steps. |
| KIKO-037 | integration | KIKO-037 | One fake-expert tutoring flow using existing Core behavior. |
| KIKO-038 | split | KIKO-038, KIKO-038A, KIKO-038B | Candidate, critique, and repair/reopen are separate provider stages. |
| KIKO-039 | keep | KIKO-039 | One process-lifecycle boundary. |
| KIKO-040 | keep | KIKO-040 | One protocol handshake. |
| KIKO-041 | split | KIKO-041, KIKO-041A | Starting a new provider thread and resuming/falling back are separate operations. |
| KIKO-042 | split | KIKO-042, KIKO-042A, KIKO-042B | Line correlation, event dispatch, and terminal timeout/cancel paths are distinct. |
| KIKO-043 | integration | KIKO-043 | One complete read-only tutoring turn. |
| KIKO-044 | split | KIKO-044, KIKO-044A, KIKO-044B | Live plan candidate, critique, and repair/reopen are separate turns. |
| KIKO-045 | integration | KIKO-045 | One enforcement proof over previously defined repository controls. |
| KIKO-046 | keep | KIKO-046 | One parser/dispatch skeleton; command workflows remain separate. |
| KIKO-047 | integration | KIKO-047 | One complete help interaction. |
| KIKO-048 | split | KIKO-048, KIKO-048A | Failed-review guidance and passing-review state transaction have different effects. |
| KIKO-049 | split | KIKO-049, KIKO-049A, KIKO-049B, KIKO-049C | Discovery/brief, plan review, file staging, and commit/rollback are separate commitments/effects. |
| KIKO-050 | split | KIKO-050, KIKO-050A, KIKO-050B | CLI repair/preview, candidate retention decisions, and export have separate effects. |
| KIKO-051 | split | KIKO-051, KIKO-051A | The new TypeScript toolchain precedes VS Code activation/sidebar concepts. |
| KIKO-052 | split | KIKO-052, KIKO-052A, KIKO-052B | Core process ownership, request correlation, and error/cancel disposal are distinct. |
| KIKO-053 | split | KIKO-053, KIKO-053A, KIKO-053B | Setup/ready, response/review, and error/blocked views have separate UI behavior. |
| KIKO-054 | split | KIKO-054, KIKO-054A, KIKO-054B, KIKO-054C, KIKO-054D | Help, review, planning, cancel/retry, and Tutor-feedback actions are independent. |
| KIKO-055 | integration | KIKO-055 | One extension-host proof against fake Core. |
| KIKO-056 | acceptance | KIKO-056 | One v0.1 vertical-slice release question. |
| KIKO-057 | keep | KIKO-057 | One diagnostic report with homogeneous capability entries. |
| KIKO-058 | split | KIKO-058, KIKO-058A, KIKO-058B | Workspace recognition, discovery/approval, and transactional creation/resume are distinct. |
| KIKO-059 | split | KIKO-059, KIKO-059A | Error taxonomy and cross-surface recovery presentation are separate. |
| KIKO-060 | split | KIKO-060, KIKO-060A, KIKO-060B, KIKO-060C | Inspection, export, reset, and delete have distinct effects and safety boundaries. |
| KIKO-061 | split | KIKO-061, KIKO-061A, KIKO-061B | Localization, keyboard/focus semantics, and visual/text access are independent quality domains. |
| KIKO-062 | integration | KIKO-062 | One aggregate deterministic verification gate. |
| KIKO-063 | decision | KIKO-063 | One distribution decision backed by a spike. |
| KIKO-064 | split | KIKO-064, KIKO-064A, KIKO-064B, KIKO-064C | Artifact build, notices, signing, and isolated smoke are separate release concerns. |
| KIKO-065 | integration | KIKO-065 | One installable VSIX outcome over established Core/extension behavior. |
| KIKO-066 | integration | KIKO-066 | One reproducible release-candidate output. |
| KIKO-067 | integration | KIKO-067 | One read-only invariant proof. |
| KIKO-068 | split | KIKO-068, KIKO-068A | State-writer locking and process cancellation/shutdown are separate lifecycles. |
| KIKO-069 | split | KIKO-069, KIKO-069A, KIKO-069B, KIKO-069C | State migration, protocol upgrade, rollback, and downgrade/future guards are separate outcomes. |
| KIKO-070 | integration | KIKO-070 | One compatibility-matrix gate. |
| KIKO-071 | split | KIKO-071, KIKO-071A, KIKO-071B, KIKO-071C, KIKO-071D, KIKO-071E | Context/tokens, cost, latency, memory, retries, and diagnostic logs have different controls. |
| KIKO-072 | acceptance | KIKO-072 | One clean-machine installation question. |
| KIKO-073 | acceptance | KIKO-073 | One real learning-journey question. |
| KIKO-074 | split | KIKO-074, KIKO-074A | Cross-project isolation and injected failure recovery are separate release questions. |
| KIKO-075 | split | KIKO-075, KIKO-075A | Upgrade preservation and uninstall/data control are independently reversible flows. |
| KIKO-076 | acceptance | KIKO-076 | One final release-record decision. |

## Final post-split learning-readiness audit

This second pass audits every final pending checkpoint, including children
created by an earlier split. A row is `ready` only when its detailed
contract has one named outcome, one responsibility boundary, a bounded concept
family, one exact primary verification, an edge case from the same behavior,
explicit exclusions, and enough information to render the standard lesson
without inventing new syntax or scope.

Integration and acceptance rows may combine already-built behavior only when
they introduce no unrelated implementation and answer one explicit integration
or release question. Any later material replan must regenerate this table for
all final pending IDs; auditing only the original parent rows is insufficient.
This final-readiness table is pending-only: a completion handoff removes the
completed row while preserving the historical original-checkpoint audit above.

| Final checkpoint | Kind | Single learning focus | Bounded new concepts/syntax | Exact primary verification | Verdict |
| --- | --- | --- | --- | --- | --- |
| `KIKO-016` | implementation | Write state through atomic replacement | Temporary files, flush/close ordering, and atomic `Path.replace`. | `.venv/bin/python -m unittest tests.test_state_persistence.AtomicWriteTests -v` | ready |
| `KIKO-016A` | implementation | Preserve a recoverable state backup | Backup naming, copy semantics, and backup validation. | `.venv/bin/python -m unittest tests.test_state_persistence.BackupTests -v` | ready |
| `KIKO-016B` | implementation | Restore a validated state backup | Backup restore decision and restore receipt. | `.venv/bin/python -m unittest tests.test_state_persistence.RestoreBackupTests -v` | ready |
| `KIKO-016C` | implementation | Migrate a supported state schema version | Migration functions and ordered schema-version transitions. | `.venv/bin/python -m unittest tests.test_state_persistence.MigrationTests -v` | ready |
| `KIKO-017` | implementation | Define the versioned JSONL request/result envelope | JSON Lines framing, request IDs, and tagged request/result messages. | `.venv/bin/python -m unittest tests.test_local_protocol -v` | ready |
| `KIKO-017A` | implementation | Define the protocol error result | Tagged error payload and stable error-code field. | `.venv/bin/python -m unittest tests.test_local_protocol.ErrorResultTests -v` | ready |
| `KIKO-017B` | implementation | Define protocol progress events | Non-terminal notification semantics and bounded progress payload. | `.venv/bin/python -m unittest tests.test_local_protocol.ProgressEventTests -v` | ready |
| `KIKO-017C` | implementation | Define protocol cancellation messages | Cancel command and cancelled terminal-result semantics. | `.venv/bin/python -m unittest tests.test_local_protocol.CancellationMessageTests -v` | ready |
| `KIKO-018` | implementation | Enforce workspace file containment | `Path.resolve`, containment checks, regular-file checks, and symlink escape reasoning. | `.venv/bin/python -m unittest tests.test_repository_safety.PathContainmentTests -v` | ready |
| `KIKO-018A` | implementation | Accept only bounded repository text | Byte-size limit and explicit text-decoding failure. | `.venv/bin/python -m unittest tests.test_repository_safety.BoundedTextTests -v` | ready |
| `KIKO-018B` | implementation | Filter likely repository secrets | Conservative secret-name and credential-pattern heuristics. | `.venv/bin/python -m unittest tests.test_repository_safety.SecretFilterTests -v` | ready |
| `KIKO-018C` | implementation | Label repository text as untrusted model data | Trust labels, immutable instruction/data separation, and provenance fields. | `.venv/bin/python -m unittest tests.test_repository_safety.UntrustedContentTests -v` | ready |
| `KIKO-019` | implementation | Create one minimal evidence record | `date.today().isoformat()` for a stable local date string. | `.venv/bin/python -m unittest tests.test_evidence.EvidenceRecordTests -v` | ready |
| `KIKO-020` | implementation | Update one encountered concept conservatively | Sentinel value `None` for “not found” and identity check `is None`. | `.venv/bin/python -m unittest tests.test_learner_state.ConceptUpdateTests -v` | ready |
| `KIKO-021` | implementation | Save learner state without losing unrelated data | Copy-before-update behavior and injected storage paths. | `.venv/bin/python -m unittest tests.test_learner_state.LearnerSaveTests -v` | ready |
| `KIKO-022` | implementation | Add a used syntax entry to the personal reference | Text membership checks and newline-safe append behavior. | `.venv/bin/python -m unittest tests.test_reference.ReferenceUpdateTests -v` | ready |
| `KIKO-023` | implementation | Represent and validate one learner request | Enumerated string values and whitespace normalization with `strip()`. | `.venv/bin/python -m unittest tests.test_tutor_requests -v` | ready |
| `KIKO-024` | implementation | Select the interaction intent | Intent lookup table and explicit fallback priority. | `.venv/bin/python -m unittest tests.test_help_policy.IntentSelectionTests -v` | ready |
| `KIKO-024A` | implementation | Select the assistance level | Progressive-help level transition and explicit-request priority. | `.venv/bin/python -m unittest tests.test_help_policy.AssistanceLevelTests -v` | ready |
| `KIKO-025` | implementation | Build and audit a code-syntax preflight | Set-style membership reasoning and declared-versus-used syntax audit. | `.venv/bin/python -m unittest tests.test_syntax_preflight.CodeSyntaxTests -v` | ready |
| `KIKO-025A` | implementation | Build and audit a configuration-format preflight | Declarative-format hierarchy/field descriptors and no-opaque-field audit. | `.venv/bin/python -m unittest tests.test_syntax_preflight.ConfigurationFormatTests -v` | ready |
| `KIKO-026` | implementation | Compile allowed Tutor context | Context projection and explicit field allowlist. | `.venv/bin/python -m unittest tests.test_context_compiler -v` | ready |
| `KIKO-026A` | implementation | Enforce the Tutor-context size boundary | Context-size budget and whole-field include/reject decision. | `.venv/bin/python -m unittest tests.test_context_compiler.SizeBoundaryTests -v` | ready |
| `KIKO-027` | implementation | Build the canonical new-checkpoint interaction | Tagged interaction data and presenter-independent content. | `.venv/bin/python -m unittest tests.test_tutor_interactions.NewCheckpointTests -v` | ready |
| `KIKO-027A` | implementation | Validate reminder interactions | Reminder-specific required/forbidden fields. | `.venv/bin/python -m unittest tests.test_tutor_interactions.ReminderTests -v` | ready |
| `KIKO-027B` | implementation | Validate hint interactions | Hint-specific next-attempt field and one-level help transition. | `.venv/bin/python -m unittest tests.test_tutor_interactions.HintTests -v` | ready |
| `KIKO-027C` | implementation | Validate failed-review interactions | Failed-review verdict and first-actionable-issue fields. | `.venv/bin/python -m unittest tests.test_tutor_interactions.FailedReviewTests -v` | ready |
| `KIKO-027D` | implementation | Validate passing-review interactions | Passing-review verdict and proposed state-update payload. | `.venv/bin/python -m unittest tests.test_tutor_interactions.PassingReviewTests -v` | ready |
| `KIKO-027E` | implementation | Validate debug interactions | Optional hypothesis field and cause-evidence requirement. | `.venv/bin/python -m unittest tests.test_tutor_interactions.DebugTests -v` | ready |
| `KIKO-027F` | implementation | Validate completion-handoff interactions | Verified handoff summary and deliberate-unchanged fields. | `.venv/bin/python -m unittest tests.test_tutor_interactions.CompletionHandoffTests -v` | ready |
| `KIKO-028` | implementation | Classify Tutor-quality feedback | Multi-scope classification and ordinary-difficulty exclusion. | `.venv/bin/python -m unittest tests.test_tutor_feedback.ClassificationTests -v` | ready |
| `KIKO-028A` | implementation | Repair the current interaction | Classification-to-repair-action mapping. | `.venv/bin/python -m unittest tests.test_tutor_feedback.RepairTests -v` | ready |
| `KIKO-028B` | implementation | Sanitize a feedback candidate | Candidate sanitization allowlist. | `.venv/bin/python -m unittest tests.test_tutor_feedback.SanitizationTests -v` | ready |
| `KIKO-028C` | implementation | Deduplicate feedback candidates | Stable deduplication key and occurrence update. | `.venv/bin/python -m unittest tests.test_tutor_feedback.DeduplicationTests -v` | ready |
| `KIKO-029` | implementation | Classify facts, decisions, assumptions, and future ideas | Decision records and blocking/deferrable/future classification. | `.venv/bin/python -m unittest tests.test_discovery.DecisionClassificationTests -v` | ready |
| `KIKO-030` | implementation | Run beginner-friendly discovery rounds | Priority selection and recommended-default metadata. | `.venv/bin/python -m unittest tests.test_discovery.DiscoveryRoundTests -v` | ready |
| `KIKO-030A` | implementation | Apply one discovery answer safely | Answer-source record and unsure-to-assumption transition. | `.venv/bin/python -m unittest tests.test_discovery.DiscoveryAnswerTests -v` | ready |
| `KIKO-031` | implementation | Enforce brief readiness | Readiness predicates and blocker findings. | `.venv/bin/python -m unittest tests.test_planning_readiness -v` | ready |
| `KIKO-031A` | implementation | Record separate brief acceptance | Brief-acceptance receipt and revocation transition. | `.venv/bin/python -m unittest tests.test_planning_readiness.BriefAcceptanceTests -v` | ready |
| `KIKO-032` | implementation | Validate required checkpoint fields | Ordered required-field validation. | `.venv/bin/python -m unittest tests.test_plan_structure.RequiredFieldTests -v` | ready |
| `KIKO-032A` | implementation | Validate unique stable checkpoint IDs | Uniqueness set and duplicate-ID finding. | `.venv/bin/python -m unittest tests.test_plan_structure.UniqueIdTests -v` | ready |
| `KIKO-032B` | implementation | Validate prerequisite references and ordering | ID-to-position lookup and forward-dependency validation. | `.venv/bin/python -m unittest tests.test_plan_structure.PrerequisiteTests -v` | ready |
| `KIKO-032C` | implementation | Reject vague or multi-outcome checkpoints | Complexity-budget classification and structured split proposals. | `.venv/bin/python -m unittest tests.test_plan_structure.AtomicityTests -v` | ready |
| `KIKO-032D` | implementation | Require lesson readiness for every final checkpoint | Post-split readiness record and lesson dry-run gate. | `.venv/bin/python -m unittest tests.test_plan_structure.LessonReadinessTests -v` | ready |
| `KIKO-033` | implementation | Trace requirements to implementation and verification | Bidirectional traceability matrix. | `.venv/bin/python -m unittest tests.test_plan_coverage.TraceabilityTests -v` | ready |
| `KIKO-033A` | implementation | Audit user-experience coverage | User-journey state coverage rules. | `.venv/bin/python -m unittest tests.test_plan_coverage.UserExperienceTests -v` | ready |
| `KIKO-033B` | implementation | Audit data-lifecycle coverage | Data-lifecycle coverage rules. | `.venv/bin/python -m unittest tests.test_plan_coverage.DataLifecycleTests -v` | ready |
| `KIKO-033C` | implementation | Audit external-integration coverage | Integration-failure coverage rules. | `.venv/bin/python -m unittest tests.test_plan_coverage.ExternalIntegrationTests -v` | ready |
| `KIKO-033D` | implementation | Audit engineering-quality coverage | Engineering-quality coverage rules. | `.venv/bin/python -m unittest tests.test_plan_coverage.EngineeringQualityTests -v` | ready |
| `KIKO-033E` | implementation | Audit delivery and lifecycle coverage | Delivery/lifecycle coverage rules. | `.venv/bin/python -m unittest tests.test_plan_coverage.DeliveryLifecycleTests -v` | ready |
| `KIKO-033F` | implementation | Audit teaching-order coverage | Teaching-order coverage rules. | `.venv/bin/python -m unittest tests.test_plan_coverage.TeachingOrderTests -v` | ready |
| `KIKO-034` | implementation | Present a plan without overwhelming beginners | Progressive disclosure and expandable plan-detail view model. | `.venv/bin/python -m unittest tests.test_plan_review.PresentationTests -v` | ready |
| `KIKO-034A` | implementation | Accept one validated plan candidate | Accepted-plan version receipt. | `.venv/bin/python -m unittest tests.test_plan_review.AcceptPlanTests -v` | ready |
| `KIKO-034B` | implementation | Revise or reopen a plan candidate | Revision transition and scoped invalidation record. | `.venv/bin/python -m unittest tests.test_plan_review.RevisePlanTests -v` | ready |
| `KIKO-034C` | implementation | Cancel a plan candidate safely | Cancel transition and preserved-state receipt. | `.venv/bin/python -m unittest tests.test_plan_review.CancelPlanTests -v` | ready |
| `KIKO-035` | implementation | Define tutoring expert request and result contracts | Provider DTOs and explicit proposed-versus-accepted fields. | `.venv/bin/python -m unittest tests.test_expert_contracts.TutoringContractTests -v` | ready |
| `KIKO-035A` | implementation | Define candidate-plan expert contracts | Candidate-planning purpose tag and candidate correlation ID. | `.venv/bin/python -m unittest tests.test_expert_contracts.CandidatePlanContractTests -v` | ready |
| `KIKO-035B` | implementation | Define plan-critique expert contracts | Critique-purpose tag and finding-category payload. | `.venv/bin/python -m unittest tests.test_expert_contracts.CritiqueContractTests -v` | ready |
| `KIKO-035C` | implementation | Define plan-repair expert contracts | Repair-purpose tag and affected-section mapping. | `.venv/bin/python -m unittest tests.test_expert_contracts.RepairContractTests -v` | ready |
| `KIKO-036` | implementation | Define the single ExpertProvider operation | Python `Protocol` (or chosen abstract interface) and method contract. | `.venv/bin/python -m unittest tests.test_expert_provider.ProviderContractTests -v` | ready |
| `KIKO-036A` | implementation | Inject and call an ExpertProvider | Constructor/function dependency injection and provider-exception mapping. | `.venv/bin/python -m unittest tests.test_expert_provider.ProviderInjectionTests -v` | ready |
| `KIKO-037` | integration | Prove tutoring with a deterministic fake expert | Test doubles and deterministic provider scenarios. | `.venv/bin/python -m unittest tests.integration.test_fake_tutoring -v` | ready |
| `KIKO-038` | implementation | Produce a fake candidate plan | Planning-purpose provider fixture and candidate correlation ID. | `.venv/bin/python -m unittest tests.integration.test_fake_planning.CandidateTests -v` | ready |
| `KIKO-038A` | integration | Critique a fake candidate plan | Separate critique-purpose request/result and finding categories. | `.venv/bin/python -m unittest tests.integration.test_fake_planning.CritiqueTests -v` | ready |
| `KIKO-038B` | integration | Repair or reopen a fake plan | Repair lineage and affected-section invalidation. | `.venv/bin/python -m unittest tests.integration.test_fake_planning.RepairTests -v` | ready |
| `KIKO-039` | implementation | Start and stop the App Server process | `subprocess.Popen`, pipes, process lifetime, and context-managed cleanup. | `.venv/bin/python -m unittest tests.integration.test_app_server_process -v` | ready |
| `KIKO-040` | implementation | Complete the initialize handshake | JSON-RPC request/response correlation and notification messages. | `.venv/bin/python -m unittest tests.integration.test_app_server_initialize -v` | ready |
| `KIKO-041` | implementation | Start one project thread | Session-only thread identifier. | `.venv/bin/python -m unittest tests.integration.test_app_server_thread.StartThreadTests -v` | ready |
| `KIKO-041A` | implementation | Resume or replace one project thread | Resume request and explicit stale-session fallback result. | `.venv/bin/python -m unittest tests.integration.test_app_server_thread.ResumeThreadTests -v` | ready |
| `KIKO-042` | implementation | Read and correlate JSONL messages | Background line reader, pending-request map, and response correlation. | `.venv/bin/python -m unittest tests.integration.test_app_server_events.CorrelationTests -v` | ready |
| `KIKO-042A` | implementation | Dispatch known and unknown App Server events | Event dispatch table and unknown-notification fallback. | `.venv/bin/python -m unittest tests.integration.test_app_server_events.DispatchTests -v` | ready |
| `KIKO-042B` | implementation | Terminate timeout, cancel, and process-exit paths | Deadline state, cancellation token, and terminal-state guard. | `.venv/bin/python -m unittest tests.integration.test_app_server_events.TerminalTests -v` | ready |
| `KIKO-043` | integration | Complete one validated read-only tutoring turn | Structured output schema and turn completion aggregation. | `.venv/bin/python -m unittest tests.integration.test_codex_tutoring_turn -v` | ready |
| `KIKO-044` | implementation | Generate one live candidate plan | Planning-purpose turn and candidate-version correlation. | `.venv/bin/python -m unittest tests.integration.test_codex_planning_flow.CandidateTurnTests -v` | ready |
| `KIKO-044A` | integration | Run one live plan critique turn | Critique-specific structured output schema. | `.venv/bin/python -m unittest tests.integration.test_codex_planning_flow.CritiqueTurnTests -v` | ready |
| `KIKO-044B` | integration | Repair or reopen a live plan candidate | Repair-purpose turn and affected-section mapping. | `.venv/bin/python -m unittest tests.integration.test_codex_planning_flow.RepairTurnTests -v` | ready |
| `KIKO-045` | integration | Defend the expert boundary from unsafe repository content | Trust labels, content delimiters, secret-pattern filtering, and provenance metadata. | `.venv/bin/python -m unittest tests.security.test_expert_boundary -v` | ready |
| `KIKO-046` | implementation | Add stable learner-facing CLI commands | `argparse` subcommands and exit codes. | Run `.venv/bin/kiko --help`, then `.venv/bin/kiko --version`. | ready |
| `KIKO-047` | integration | Connect the complete help interaction | CLI provider selection and presenter functions. | `.venv/bin/kiko ask --provider fake "Explain the current step"` | ready |
| `KIKO-048` | implementation | Render one failed CLI review | Review check-result adapter. | `.venv/bin/python -m unittest tests.integration.test_cli_review.FailedReviewTests -v` | ready |
| `KIKO-048A` | integration | Persist one passing review transaction | Multi-owner review transaction and idempotency key. | `.venv/bin/python -m unittest tests.integration.test_cli_review.PassingReviewTests -v` | ready |
| `KIKO-049` | integration | Complete CLI discovery and brief acceptance | Resumable discovery session record. | `.venv/bin/python -m unittest tests.integration.test_cli_planning.DiscoveryBriefTests -v` | ready |
| `KIKO-049A` | integration | Generate and review a CLI plan candidate | CLI plan-review state and expandable detail presentation. | `.venv/bin/python -m unittest tests.integration.test_cli_planning.PlanReviewTests -v` | ready |
| `KIKO-049B` | integration | Stage and validate accepted Tutor files | Multi-file staging directory and document-manifest validation. | `.venv/bin/python -m unittest tests.integration.test_cli_planning.ProjectStagingTests -v` | ready |
| `KIKO-049C` | integration | Commit or roll back Tutor-file creation | Multi-file commit receipt and rollback/resume journal. | `.venv/bin/python -m unittest tests.integration.test_cli_planning.ProjectCommitTests -v` | ready |
| `KIKO-050` | integration | Repair feedback and preview its CLI candidate | CLI feedback preview presenter. | `.venv/bin/python -m unittest tests.integration.test_cli_feedback.PreviewTests -v` | ready |
| `KIKO-050A` | integration | Keep, edit, or discard a CLI feedback candidate | Local feedback repository and candidate decision transition. | `.venv/bin/python -m unittest tests.integration.test_cli_feedback.CandidateDecisionTests -v` | ready |
| `KIKO-050B` | integration | Export a sanitized feedback candidate | Versioned feedback export envelope. | `.venv/bin/python -m unittest tests.integration.test_cli_feedback.ExportTests -v` | ready |
| `KIKO-051` | implementation | Create the TypeScript extension development environment | `package.json`, `tsconfig.json`, npm development dependencies/scripts, and TypeScript compiler check. | Run `npm --prefix extension install`, then `npm --prefix extension run check` and `npm --prefix extension test`. | ready |
| `KIKO-051A` | implementation | Activate a static Kiko sidebar | Extension activation, contribution points, command registration, and view provider lifecycle. | Run `npm --prefix extension run check`, then `npm --prefix extension test -- --runInBand activation`. | ready |
| `KIKO-052` | implementation | Start and stop Core from the extension | Node child process spawn and VS Code disposable lifecycle. | `npm --prefix extension test -- --runInBand core-process` | ready |
| `KIKO-052A` | implementation | Correlate one extension/Core JSONL request | Stream line buffering and pending-promise map. | `npm --prefix extension test -- --runInBand core-protocol` | ready |
| `KIKO-052B` | implementation | Handle extension/Core cancel and failure disposal | Promise rejection mapping, cancellation token, and bounded timeout. | `npm --prefix extension test -- --runInBand core-failures` | ready |
| `KIKO-053` | implementation | Render setup, ready, and working states | Webview state rendering, safe text escaping, and initial focus management. | `npm --prefix extension test -- --runInBand initial-views` | ready |
| `KIKO-053A` | implementation | Render response and review sidebar states | Interaction-section rendering and review-verdict styling. | `npm --prefix extension test -- --runInBand response-review-views` | ready |
| `KIKO-053B` | implementation | Render recoverable-error and blocked states | Error-code-to-view mapping and conditional action availability. | `npm --prefix extension test -- --runInBand error-views` | ready |
| `KIKO-054` | implementation | Connect sidebar help and hint actions | Action correlation and working-to-response transition. | `npm --prefix extension test -- --runInBand help-actions` | ready |
| `KIKO-054A` | integration | Connect the sidebar review action | Review preview/confirm action correlation. | `npm --prefix extension test -- --runInBand review-action` | ready |
| `KIKO-054B` | integration | Connect the sidebar planning action | Multi-turn planning view state correlation. | `npm --prefix extension test -- --runInBand planning-action` | ready |
| `KIKO-054C` | integration | Connect cancel and retry actions | Cancel/retry action correlation. | `npm --prefix extension test -- --runInBand cancel-retry-actions` | ready |
| `KIKO-054D` | integration | Connect the unclear-feedback action | Feedback-action correlation and candidate-control rendering. | `npm --prefix extension test -- --runInBand feedback-action` | ready |
| `KIKO-055` | integration | Test the extension against a fake Core | VS Code extension-host integration harness and fixture process control. | `npm --prefix extension test` | ready |
| `KIKO-056` | acceptance | Pass the v0.1 end-to-end vertical proof | End-to-end scenario orchestration and evidence capture. | `.venv/bin/python -m unittest tests.e2e.test_v01_vertical_slice -v` | ready |
| `KIKO-057` | implementation | Diagnose dependencies and authentication | Version comparison, capability checks, and sanitized diagnostics. | `.venv/bin/python -m unittest tests.test_doctor -v` | ready |
| `KIKO-058` | implementation | Recognize workspace and show setup readiness | Project-recognition result and onboarding entry-state mapping. | `.venv/bin/python -m unittest tests.e2e.test_onboarding.WorkspaceRecognitionTests -v` | ready |
| `KIKO-058A` | integration | Complete onboarding discovery and approvals | Onboarding-stage presenter state and persisted draft-session pointer. | `.venv/bin/python -m unittest tests.e2e.test_onboarding.DiscoveryApprovalTests -v` | ready |
| `KIKO-058B` | integration | Create or resume the project transactionally | Onboarding completion receipt and reopen validation. | `.venv/bin/python -m unittest tests.e2e.test_onboarding.CreateResumeTests -v` | ready |
| `KIKO-059` | implementation | Define stable product error codes and recovery mapping | Error taxonomy and code-to-recovery-action table. | `.venv/bin/python -m unittest tests.test_error_taxonomy -v` | ready |
| `KIKO-059A` | integration | Present recovery actions consistently across surfaces | Cross-surface error fixture and recovery receipt. | `.venv/bin/python -m unittest tests.e2e.test_error_recovery -v` | ready |
| `KIKO-060` | implementation | Inspect learner and feedback data | Owner-specific read-only inspection view. | `.venv/bin/python -m unittest tests.e2e.test_data_control.InspectTests -v` | ready |
| `KIKO-060A` | implementation | Export learner and feedback data | Export manifest and owner-specific export entries. | `.venv/bin/python -m unittest tests.e2e.test_data_control.ExportTests -v` | ready |
| `KIKO-060B` | implementation | Reset one selected local data owner | Destructive-action target receipt and typed confirmation phrase/action. | `.venv/bin/python -m unittest tests.e2e.test_data_control.ResetTests -v` | ready |
| `KIKO-060C` | implementation | Delete one selected local data owner | Delete-specific confirmation and absent-after-delete receipt. | `.venv/bin/python -m unittest tests.e2e.test_data_control.DeleteTests -v` | ready |
| `KIKO-061` | implementation | Localize headings without changing technical literals | Localization keys and fallback locale. | `npm --prefix extension test -- --runInBand localization` | ready |
| `KIKO-061A` | integration | Verify keyboard, labels, and focus | ARIA labels, keyboard focus order, and focus assertions. | `npm --prefix extension test -- --runInBand keyboard-accessibility` | ready |
| `KIKO-061B` | integration | Verify visual and text accessibility | Contrast assertions, non-color status cues, and selectable-text checks. | `npm --prefix extension test -- --runInBand visual-text-accessibility` | ready |
| `KIKO-062` | integration | Aggregate one full product verification command | Build orchestration target and test-stage reporting. | `make verify` | ready |
| `KIKO-063` | decision | Choose and prove the macOS Core distribution | Distribution tradeoff record, standalone executable or managed-runtime proof. | Follow the recorded clean-profile spike command in `ARCHITECTURE.md` and run `kiko --version` outside the repository. | ready |
| `KIKO-064` | implementation | Build the versioned Core and CLI artifact | Build artifact metadata and selected distribution build command. | `make package-core` | ready |
| `KIKO-064A` | implementation | Bundle Core licenses and notices | License/notice inventory and notice-manifest validation. | `make verify-core-notices` | ready |
| `KIKO-064B` | implementation | Sign and verify the Core artifact | Code-signing identity, signature verification, and notarization status when required. | `make verify-core-signature` | ready |
| `KIKO-064C` | integration | Smoke-test the Core artifact in isolation | Isolated artifact smoke matrix. | `make smoke-core-artifact` | ready |
| `KIKO-065` | integration | Package an installable VS Code VSIX | VSIX packaging, bundled/located Core strategy, and extension release metadata. | Run `npm --prefix extension run package`, then `npm --prefix extension run smoke:vsix`. | ready |
| `KIKO-066` | integration | Produce reproducible versioned release output | Release manifest, checksum generation, and version-consistency check. | `make release-candidate` | ready |
| `KIKO-067` | integration | Enforce the read-only learning boundary | Capability denylist/allowlist and invariant tests over file hashes. | `.venv/bin/python -m unittest tests.security.test_read_only_invariant -v` | ready |
| `KIKO-068` | implementation | Prevent concurrent state writers | File lock, lock metadata, and stale-lock validation. | `.venv/bin/python -m unittest tests.integration.test_process_lifecycle.StateLockTests -v` | ready |
| `KIKO-068A` | integration | Cancel and shut down the full process tree | Signal propagation and bounded process-tree shutdown sequence. | `.venv/bin/python -m unittest tests.integration.test_process_lifecycle.ShutdownTests -v` | ready |
| `KIKO-069` | implementation | Upgrade supported state-owner versions | Multi-owner migration order and post-migration contract validation. | `.venv/bin/python -m unittest tests.e2e.test_upgrade_recovery.StateOwnerUpgradeTests -v` | ready |
| `KIKO-069A` | implementation | Upgrade the supported local protocol | Protocol-version negotiation and supported-adapter selection. | `.venv/bin/python -m unittest tests.e2e.test_upgrade_recovery.ProtocolUpgradeTests -v` | ready |
| `KIKO-069B` | integration | Roll back a failed multi-owner migration | Multi-owner rollback receipt. | `.venv/bin/python -m unittest tests.e2e.test_upgrade_recovery.RollbackTests -v` | ready |
| `KIKO-069C` | integration | Protect future-version and downgrade paths | Downgrade write guard and compatibility receipt. | `.venv/bin/python -m unittest tests.e2e.test_upgrade_recovery.DowngradeGuardTests -v` | ready |
| `KIKO-070` | integration | Establish the supported compatibility matrix | Compatibility matrix fixtures and minimum/maximum capability gates. | `make compatibility-check` | ready |
| `KIKO-071` | implementation | Bound context and token estimates | Budget configuration and conservative token estimation. | `.venv/bin/python -m unittest tests.performance.test_product_budgets.ContextCostTests -v` | ready |
| `KIKO-071A` | implementation | Report estimated model cost conservatively | Versioned pricing input and estimated-cost range. | `.venv/bin/python -m unittest tests.performance.test_product_budgets.CostEstimateTests -v` | ready |
| `KIKO-071B` | integration | Measure and bound lifecycle latency | Monotonic timing and latency threshold report. | `.venv/bin/python -m unittest tests.performance.test_product_budgets.LatencyTests -v` | ready |
| `KIKO-071C` | integration | Measure and bound process memory | Child-process memory sampling and aggregate-memory report. | `.venv/bin/python -m unittest tests.performance.test_product_budgets.MemoryTests -v` | ready |
| `KIKO-071D` | implementation | Bound automatic retries | Retry-attempt budget and bounded backoff schedule. | `.venv/bin/python -m unittest tests.performance.test_product_budgets.RetryTests -v` | ready |
| `KIKO-071E` | implementation | Sanitize and bound retained diagnostic logs | Diagnostic-log retention/rotation rule. | `.venv/bin/python -m unittest tests.performance.test_product_budgets.DiagnosticLogTests -v` | ready |
| `KIKO-072` | acceptance | Install on a clean supported macOS profile | Release acceptance record and installation evidence capture. | Follow `docs/install.md`, then run `kiko doctor` and the VS Code activation smoke. | ready |
| `KIKO-073` | acceptance | Complete and resume a real learning journey | Manual usability evidence rubric. | Run the release acceptance script in `docs/release-acceptance.md`. | ready |
| `KIKO-074` | acceptance | Prove cross-project knowledge and progress isolation | Cross-project release acceptance record. | `make release-cross-project-acceptance` | ready |
| `KIKO-074A` | acceptance | Prove release failure and feedback recovery | Failure-injection release acceptance matrix. | `make release-failure-acceptance` | ready |
| `KIKO-075` | acceptance | Prove packaged upgrade without data loss | Packaged upgrade acceptance manifest. | Follow the upgrade part of `docs/upgrade-and-uninstall.md`, then run `make smoke-upgrade`. | ready |
| `KIKO-075A` | acceptance | Prove uninstall and data-retention choices | Uninstall acceptance manifest. | Follow the uninstall part of `docs/upgrade-and-uninstall.md`, then run `make smoke-uninstall`. | ready |
| `KIKO-076` | acceptance | Create the v1.0 release record | Release sign-off checklist and known-limitations record. | `make release-audit` | ready |

## Result

- Originally pending checkpoints audited: 66
- Kept implementation checkpoints: 12
- Decision checkpoints kept: 1
- Integration/acceptance checkpoints kept intentionally broader: 14
- Original checkpoints split: 39
- New split checkpoints added: 92
- Normalized roadmap total after the full post-split audit: 168 checkpoints
- Verified historical checkpoints: 10
- Normalized checkpoints originating from the originally pending set: 158

Current completion/pending status remains only in `LEARNING_PLAN.md` and is not
duplicated in this historical size audit.
