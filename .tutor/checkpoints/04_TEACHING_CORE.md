# Phase 4 — Deterministic Teaching Core

<a id="kiko-023"></a>
### KIKO-023 — Represent and validate one learner request

- Checkpoint kind: implementation
- Observable outcome: Tutor Core accepts one question/help request with a validated in-memory shape.
- Why it matters: Teaching decisions need explicit input before any model call or UI rendering.
- Prerequisites: KIKO-014 and KIKO-022.
- Known concepts: Dictionaries, validation, return values, and tests.
- New concepts and syntax: Enumerated string values and whitespace normalization with `strip()`.
- Learner task: Build and validate one learner-request value containing text and requested help.
- Verification: `.venv/bin/python -m unittest tests.test_tutor_requests -v`
- Expected behavior: Valid text is normalized; empty text and unsupported help values return controlled errors.
- Edge case: The request remains in memory and raw conversation is not persisted.
- Not included: Intent classification, model calls, or UI input.
- Exit condition: Valid, empty, whitespace-only, and invalid-help fixtures pass.

<a id="kiko-024"></a>
### KIKO-024 — Select the interaction intent

- Checkpoint kind: implementation
- Observable outcome: Kiko deterministically chooses teach, remind, hint, review, debug, or unblock for one validated request.
- Why it matters: The model must not decide which pedagogical interaction is taking place.
- Prerequisites: KIKO-023.
- Known concepts: Conditions, functions, dictionaries, and validated inputs.
- New concepts and syntax: Intent lookup table and explicit fallback priority.
- Learner task: Map request signals to exactly one interaction intent while preserving the active checkpoint for side questions.
- Verification: `.venv/bin/python -m unittest tests.test_help_policy.IntentSelectionTests -v`
- Expected behavior: Every supported signal produces the documented intent; ambiguous/unsupported signals use one safe fallback.
- Edge case: A side question retains the active checkpoint and does not become a new lesson.
- Not included: Assistance-level selection, natural-language model classification, or response generation.
- Exit condition: The complete intent decision table passes deterministic tests.

<a id="kiko-024a"></a>
### KIKO-024A — Select the assistance level

- Checkpoint kind: implementation
- Observable outcome: A selected intent receives one deterministic help level from explicit request, stored preference, and retry state.
- Why it matters: Kiko, not the model, controls how much solution detail the learner receives.
- Prerequisites: KIKO-024.
- Known concepts: Intent values, preferences, conditions, lookup tables, and validated requests.
- New concepts and syntax: Progressive-help level transition and explicit-request priority.
- Learner task: Select one help level without changing the interaction intent or project progress.
- Verification: `.venv/bin/python -m unittest tests.test_help_policy.AssistanceLevelTests -v`
- Expected behavior: Explicit level wins; otherwise preference applies and a genuine retry increases at most one level.
- Edge case: Full solution is not selected unless explicitly requested or the maximum documented retry condition is met.
- Not included: Rendering help, model calls, or storing competence evidence.
- Exit condition: Explicit, default, retry, maximum, and no-progress-change fixtures pass.

<a id="kiko-025"></a>
### KIKO-025 — Build and audit a code-syntax preflight

- Checkpoint kind: implementation
- Observable outcome: Kiko separates known, new, and excluded code syntax and rejects an example/task containing undeclared syntax.
- Why it matters: Learners must never encounter unexplained code constructs in a lesson.
- Prerequisites: KIKO-011, KIKO-022, and KIKO-024A.
- Known concepts: Concept selection, personal reference, lists, and validation.
- New concepts and syntax: Set-style membership reasoning and declared-versus-used syntax audit.
- Learner task: Select relevant known/new/excluded code syntax and validate one lesson example/task against it.
- Verification: `.venv/bin/python -m unittest tests.test_syntax_preflight.CodeSyntaxTests -v`
- Expected behavior: Fully declared code passes; an unannounced import, method, operator, or shorthand fails by name.
- Edge case: Only task-relevant known syntax appears, not the entire reference.
- Not included: Configuration formats, parsing every language, or inferring competence from reference entries.
- Exit condition: Known/new/excluded selection and no-unannounced-code-syntax fixtures pass.

<a id="kiko-025a"></a>
### KIKO-025A — Build and audit a configuration-format preflight

- Checkpoint kind: implementation
- Observable outcome: Every configuration section, punctuation rule, type, field owner, default, effect, and project mapping used by a task is explained first.
- Why it matters: TOML, YAML, manifests, and schemas must not appear as opaque blocks to copy.
- Prerequisites: KIKO-025.
- Known concepts: Code-syntax preflight, required fields, lists, validation, and lesson examples.
- New concepts and syntax: Declarative-format hierarchy/field descriptors and no-opaque-field audit.
- Learner task: Validate one TOML-style format preflight and reject an unexplained section or field used by its task.
- Verification: `.venv/bin/python -m unittest tests.test_syntax_preflight.ConfigurationFormatTests -v`
- Expected behavior: Complete format explanation passes; missing consumer, hierarchy, punctuation, type, effect, mapping, or error fails precisely.
- Edge case: The audit includes only the format features used by the current task.
- Not included: Full TOML/YAML parsers or configuration rendering.
- Exit condition: Complete, missing-section, missing-field, missing-mapping, and unused-detail fixtures pass.

<a id="kiko-026"></a>
### KIKO-026 — Compile allowed Tutor context

- Checkpoint kind: implementation
- Observable outcome: One request includes only the allowed state and repository fields needed for its active checkpoint.
- Why it matters: Privacy, relevance, model cost, and teaching quality degrade when all state/history is sent.
- Prerequisites: KIKO-018C, KIKO-023, KIKO-024A, and KIKO-025A.
- Known concepts: Separate state ownership, selection functions, and validated dictionaries.
- New concepts and syntax: Context projection and explicit field allowlist.
- Learner task: Combine only the active objective, request, selected concepts/reference, decisions, and safe file summaries.
- Verification: `.venv/bin/python -m unittest tests.test_context_compiler -v`
- Expected behavior: Required allowed fields appear; unrelated concepts, full reference, transcript, and unsafe files do not.
- Edge case: An unknown source field is excluded by default rather than copied through.
- Not included: Sending context to an expert or rendering a learner response.
- Exit condition: Inclusion, exclusion, unsafe-source, unknown-field, and owner-boundary fixtures pass.

<a id="kiko-026a"></a>
### KIKO-026A — Enforce the Tutor-context size boundary

- Checkpoint kind: implementation
- Observable outcome: Allowed Tutor context stays within a deterministic size budget without silently cutting structured fields.
- Why it matters: Privacy, cost, and reliability still degrade when relevant allowed context is unbounded.
- Prerequisites: KIKO-026.
- Known concepts: Allowed context projection, structured fields, controlled errors, and tests.
- New concepts and syntax: Context-size budget and whole-field include/reject decision.
- Learner task: Enforce one deterministic context budget after allowlist projection.
- Verification: `.venv/bin/python -m unittest tests.test_context_compiler.SizeBoundaryTests -v`
- Expected behavior: Within-budget context passes; oversized optional items are omitted by policy or the request is rejected with guidance.
- Edge case: Required structured fields are never silently truncated in the middle.
- Not included: Token or price estimation, provider calls, or UI rendering.
- Exit condition: Within, exact-limit, optional-overflow, required-overflow, and no-partial-field fixtures pass.

<a id="kiko-027"></a>
### KIKO-027 — Build the canonical new-checkpoint interaction

- Checkpoint kind: implementation
- Observable outcome: One `new_checkpoint` interaction uses the semantic fields and order from `LESSON_SPEC.md`.
- Why it matters: Chat, CLI, and VS Code must present the same pedagogy consistently.
- Prerequisites: KIKO-024A, KIKO-025A, and KIKO-026A.
- Known concepts: Structured dictionaries, validation, intent types, and Syntax preflight.
- New concepts and syntax: Tagged interaction data and presenter-independent content.
- Learner task: Create and validate one `new_checkpoint` interaction before rendering it.
- Verification: `.venv/bin/python -m unittest tests.test_tutor_interactions.NewCheckpointTests -v`
- Expected behavior: Complete new lesson passes; missing progress/problem/syntax/task/verification or wrong order fails.
- Edge case: An undeclared syntax item prevents interaction validation.
- Not included: CLI styling, VS Code HTML, localization files, or expert generation.
- Exit condition: New-checkpoint success and missing/reordered-field fixtures pass.

<a id="kiko-027a"></a>
### KIKO-027A — Validate reminder interactions

- Checkpoint kind: implementation
- Observable outcome: A reminder uses its small stable contract without repeating a full lesson.
- Why it matters: Recalling known syntax should be concise while keeping the current task visible.
- Prerequisites: KIKO-027.
- Known concepts: Tagged interaction data, progress header, personal reference, and required-field validation.
- New concepts and syntax: Reminder-specific required/forbidden fields.
- Learner task: Validate one reminder fixture against the reminder contract.
- Verification: `.venv/bin/python -m unittest tests.test_tutor_interactions.ReminderTests -v`
- Expected behavior: A concise reminder passes; missing current task/verification or full-lesson duplication fails.
- Edge case: Reminder changes neither checkpoint status nor competence.
- Not included: Hints, reviews, debugging, or durable updates.
- Exit condition: Valid, missing-field, duplicated-lesson, and no-state-change reminder fixtures pass.

<a id="kiko-027b"></a>
### KIKO-027B — Validate hint interactions

- Checkpoint kind: implementation
- Observable outcome: A hint exposes exactly one progressive help level and one next learner attempt.
- Why it matters: Kiko must help without revealing more than the learner requested.
- Prerequisites: KIKO-027A.
- Known concepts: Tagged variants, progress header, assistance levels, and required-field validation.
- New concepts and syntax: Hint-specific next-attempt field and one-level help transition.
- Learner task: Validate first/repeated hint fixtures without changing the active task.
- Verification: `.venv/bin/python -m unittest tests.test_tutor_interactions.HintTests -v`
- Expected behavior: Each hint adds at most one help level and retains the original verification.
- Edge case: Explicit stronger-help request may skip only to the requested level, never beyond it.
- Not included: Reminders, reviews, debug, or durable progress changes.
- Exit condition: First, repeated, explicit-level, over-help, and no-progress-change hint fixtures pass.

<a id="kiko-027c"></a>
### KIKO-027C — Validate failed-review interactions

- Checkpoint kind: implementation
- Observable outcome: A failed review reports observed checks, the first issue, one next correction, and exact re-verification without state updates.
- Why it matters: Failed work needs actionable guidance without false completion or competence.
- Prerequisites: KIKO-027B.
- Known concepts: Tagged interactions, verification observations, assistance level, and unchanged-state policy.
- New concepts and syntax: Failed-review verdict and first-actionable-issue fields.
- Learner task: Validate one failed-review interaction and reject any proposed progress/evidence update.
- Verification: `.venv/bin/python -m unittest tests.test_tutor_interactions.FailedReviewTests -v`
- Expected behavior: Failure contains correction/re-verification and no durable update or next lesson body.
- Edge case: Expert-proposed replacement code cannot be labeled learner-authored evidence.
- Not included: Passing review, executing checks, or persistence.
- Exit condition: Valid failure, missing observation, false update, and authorship fixtures pass.

<a id="kiko-027d"></a>
### KIKO-027D — Validate passing-review interactions

- Checkpoint kind: implementation
- Observable outcome: A passing review contains accepted learner behavior, help used, proposed updates, and only the next title.
- Why it matters: Verified learner work is the sole point where progress/evidence updates may be proposed.
- Prerequisites: KIKO-027C.
- Known concepts: Failed reviews, verification observations, evidence boundaries, and help levels.
- New concepts and syntax: Passing-review verdict and proposed state-update payload.
- Learner task: Validate one passing-review interaction without applying its proposed updates.
- Verification: `.venv/bin/python -m unittest tests.test_tutor_interactions.PassingReviewTests -v`
- Expected behavior: Complete verified proposal passes; false pass or missing authorship/help/evidence fails.
- Edge case: Naming the next checkpoint is allowed, but beginning its lesson is rejected.
- Not included: Persisting updates or executing the next lesson.
- Exit condition: Valid pass, false-pass, missing-evidence, and next-lesson-leak fixtures pass.

<a id="kiko-027e"></a>
### KIKO-027E — Validate debug interactions

- Checkpoint kind: implementation
- Observable outcome: A debug response separates expected/observed evidence from a confirmed cause or labeled hypothesis.
- Why it matters: Diagnosis must not present guesses as facts or complete a checkpoint.
- Prerequisites: KIKO-027D.
- Known concepts: Tagged interactions, observations, progress status, and next verification.
- New concepts and syntax: Optional hypothesis field and cause-evidence requirement.
- Learner task: Validate confirmed-cause and hypothesis debug fixtures.
- Verification: `.venv/bin/python -m unittest tests.test_tutor_interactions.DebugTests -v`
- Expected behavior: Evidence-backed cause or labeled hypothesis passes; unsupported cause and completion claim fail.
- Edge case: Debugging alone cannot set checkpoint status to verified.
- Not included: Running diagnostics, reviews, handoffs, or state writes.
- Exit condition: Confirmed, hypothesis, unsupported-cause, and false-completion fixtures pass.

<a id="kiko-027f"></a>
### KIKO-027F — Validate completion-handoff interactions

- Checkpoint kind: implementation
- Observable outcome: A completion handoff reports only verified evidence/updates and the next checkpoint title.
- Why it matters: Finishing one checkpoint must not silently begin another or obscure what changed.
- Prerequisites: KIKO-027E.
- Known concepts: Passing review, verified progress, state owners, and tagged interactions.
- New concepts and syntax: Verified handoff summary and deliberate-unchanged fields.
- Learner task: Validate one completion-handoff fixture and its stop boundary.
- Verification: `.venv/bin/python -m unittest tests.test_tutor_interactions.CompletionHandoffTests -v`
- Expected behavior: Evidence/changed/unchanged/reference/next-title fields pass; next lesson body fails.
- Edge case: No reference addition is represented explicitly rather than omitted ambiguously.
- Not included: Starting the next lesson or applying unverified updates.
- Exit condition: Complete, missing-update, deliberate-unchanged, and stop-boundary fixtures pass.

<a id="kiko-028"></a>
### KIKO-028 — Classify Tutor-quality feedback

- Checkpoint kind: implementation
- Observable outcome: An unclear/format/help report is classified as learner, project, shared-skill, runtime, or ordinary difficulty.
- Why it matters: Tutor defects must be separated from learner difficulty before any repair or durable candidate is chosen.
- Prerequisites: KIKO-015E and KIKO-027F.
- Known concepts: Intent selection, structured data, privacy boundaries, and user confirmation.
- New concepts and syntax: Multi-scope classification and ordinary-difficulty exclusion.
- Learner task: Classify fixed feedback signals without repairing or persisting them.
- Verification: `.venv/bin/python -m unittest tests.test_tutor_feedback.ClassificationTests -v`
- Expected behavior: Reusable/project/learner/runtime fixtures classify correctly; ordinary difficulty remains a help request.
- Edge case: Ordinary learner difficulty remains a help request rather than a Tutor-defect finding.
- Not included: Repairing interactions, creating candidates, self-modification, or telemetry.
- Exit condition: Every classification and no-state-change fixture passes.

<a id="kiko-028a"></a>
### KIKO-028A — Repair the current interaction

- Checkpoint kind: implementation
- Observable outcome: A classified Tutor defect selects one corrected interaction/help response while preserving progress and competence.
- Why it matters: The learner needs an immediate usable correction before product feedback processing continues.
- Prerequisites: KIKO-028.
- Known concepts: Feedback classifications, canonical interactions, help levels, and state boundaries.
- New concepts and syntax: Classification-to-repair-action mapping.
- Learner task: Select and validate the corrected interaction for one classified feedback fixture.
- Verification: `.venv/bin/python -m unittest tests.test_tutor_feedback.RepairTests -v`
- Expected behavior: Corrected guidance matches the violated contract and retains the same active checkpoint.
- Edge case: Repairing a Tutor defect never lowers competence or records learner difficulty.
- Not included: Candidate sanitization, persistence, skill edits, or telemetry.
- Exit condition: Syntax, format, help-level, progress, and unchanged-competence repair fixtures pass.

<a id="kiko-028b"></a>
### KIKO-028B — Sanitize a feedback candidate

- Checkpoint kind: implementation
- Observable outcome: Reusable/project/runtime feedback becomes one optional candidate containing only allowed summary fields.
- Why it matters: Product improvement records must exclude private interaction/source data and duplicate policy.
- Prerequisites: KIKO-028A.
- Known concepts: Feedback classification, privacy allowlists, user confirmation, and separate state ownership.
- New concepts and syntax: Candidate sanitization allowlist.
- Learner task: Build one sanitized candidate and remove every forbidden raw-content field.
- Verification: `.venv/bin/python -m unittest tests.test_tutor_feedback.SanitizationTests -v`
- Expected behavior: Allowed summary fields remain; raw prompt, source, secret, and hidden-reasoning fields are absent.
- Edge case: A candidate with no safe useful observation is rejected rather than storing raw context.
- Not included: Shared skill/code mutation or remote telemetry.
- Exit condition: Allowed, forbidden, empty-after-sanitize, and competence-isolation fixtures pass.

<a id="kiko-028c"></a>
### KIKO-028C — Deduplicate feedback candidates

- Checkpoint kind: implementation
- Observable outcome: A sanitized repeated finding updates one candidate instead of creating duplicate policy records.
- Why it matters: Repeated Tutor problems need traceability without a noisy feedback store.
- Prerequisites: KIKO-028B.
- Known concepts: Sanitized candidates, lists, identifiers, and separate feedback ownership.
- New concepts and syntax: Stable deduplication key and occurrence update.
- Learner task: Merge one repeated sanitized candidate while leaving distinct findings separate.
- Verification: `.venv/bin/python -m unittest tests.test_tutor_feedback.DeduplicationTests -v`
- Expected behavior: Same rule/scope/regression target merges; a materially different finding remains separate.
- Edge case: Deduplication changes neither learner competence nor project progress.
- Not included: Keep/discard/export UI, persistence, skill edits, or telemetry.
- Exit condition: New, duplicate, distinct, stable-key, and state-isolation fixtures pass.
