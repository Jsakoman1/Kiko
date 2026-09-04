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
### KIKO-024 — Select interaction intent and assistance level

- Checkpoint kind: implementation
- Observable outcome: Kiko deterministically chooses teach, remind, hint, review, debug, or unblock plus a help level.
- Why it matters: The model must not decide how much assistance the learner receives.
- Prerequisites: KIKO-023.
- Known concepts: Conditions, functions, dictionaries, and validated inputs.
- New concepts and syntax: Lookup tables and explicit fallback priority.
- Learner task: Map request signals and stored preference to one interaction intent/help decision.
- Verification: `.venv/bin/python -m unittest tests.test_help_policy -v`
- Expected behavior: Each supported intent and explicit/default preference produces the documented decision.
- Edge case: A side question retains the active checkpoint and does not become a new lesson.
- Not included: Natural-language model classification or response generation.
- Exit condition: The complete decision table passes deterministic tests.

<a id="kiko-025"></a>
### KIKO-025 — Build and audit Syntax preflight

- Checkpoint kind: implementation
- Observable outcome: Kiko separates relevant known, required new, and deliberately excluded syntax.
- Why it matters: Learners must never encounter unexplained constructs inside examples or tasks.
- Prerequisites: KIKO-011, KIKO-022, and KIKO-024.
- Known concepts: Concept selection, personal reference, lists, and validation.
- New concepts and syntax: Set-style membership reasoning and a syntax-usage audit contract.
- Learner task: Build one Syntax preflight and reject an example containing an undeclared construct.
- Verification: `.venv/bin/python -m unittest tests.test_syntax_preflight -v`
- Expected behavior: Declared examples pass; an unannounced-method fixture fails with the method name.
- Edge case: Only task-relevant known syntax appears, not the entire reference.
- Not included: Parsing every programming language or inferring competence from reference entries.
- Exit condition: Known/new/excluded selection and no-unannounced-syntax audit pass.

<a id="kiko-026"></a>
### KIKO-026 — Compile bounded Tutor context

- Checkpoint kind: implementation
- Observable outcome: One request produces the smallest context needed for its active checkpoint.
- Why it matters: Privacy, relevance, model cost, and teaching quality degrade when all state/history is sent.
- Prerequisites: KIKO-018B, KIKO-023, KIKO-024, and KIKO-025.
- Known concepts: Separate state ownership, selection functions, and validated dictionaries.
- New concepts and syntax: Context projection and explicit allowlists.
- Learner task: Combine only the active objective, request, selected concepts/reference, decisions, and safe file summaries.
- Verification: `.venv/bin/python -m unittest tests.test_context_compiler -v`
- Expected behavior: Required fields appear; unrelated concepts, full reference, transcript, and unsafe files do not.
- Edge case: Context-size limits truncate or reject safely without cutting structured fields silently.
- Not included: Sending context to an expert or rendering a learner response.
- Exit condition: Inclusion, exclusion, safety, and size-bound fixtures pass.

<a id="kiko-027"></a>
### KIKO-027 — Build the canonical new-checkpoint interaction

- Checkpoint kind: implementation
- Observable outcome: One `new_checkpoint` interaction uses the semantic fields and order from `LESSON_SPEC.md`.
- Why it matters: Chat, CLI, and VS Code must present the same pedagogy consistently.
- Prerequisites: KIKO-024, KIKO-025, and KIKO-026.
- Known concepts: Structured dictionaries, validation, intent types, and Syntax preflight.
- New concepts and syntax: Tagged interaction data and presenter-independent content.
- Learner task: Create and validate one `new_checkpoint` interaction before rendering it.
- Verification: `.venv/bin/python -m unittest tests.test_tutor_interactions.NewCheckpointTests -v`
- Expected behavior: Complete new lesson passes; missing progress/problem/syntax/task/verification or wrong order fails.
- Edge case: An undeclared syntax item prevents interaction validation.
- Not included: CLI styling, VS Code HTML, localization files, or expert generation.
- Exit condition: New-checkpoint success and missing/reordered-field fixtures pass.

<a id="kiko-027a"></a>
### KIKO-027A — Validate reminder and hint interactions

- Checkpoint kind: implementation
- Observable outcome: Reminder and hint responses use their smaller stable contracts without repeating a full lesson.
- Why it matters: Consistency must not force unnecessary information into short help interactions.
- Prerequisites: KIKO-027.
- Known concepts: Tagged interaction data, progress header, help levels, and personal reference.
- New concepts and syntax: Variant-required fields and incremental help-level state.
- Learner task: Validate one reminder and one hint fixture against their specific required fields.
- Verification: `.venv/bin/python -m unittest tests.test_tutor_interactions.ShortHelpTests -v`
- Expected behavior: Correct variants pass; full-lesson duplication or missing next attempt/verification fails.
- Edge case: Repeated hint increases at most one help level unless stronger help is explicitly requested.
- Not included: Review evidence, debugging hypotheses, or durable progress changes.
- Exit condition: Reminder, first hint, repeated hint, and over-help fixtures pass.

<a id="kiko-027b"></a>
### KIKO-027B — Validate failed and passing review interactions

- Checkpoint kind: implementation
- Observable outcome: Failed and passing reviews expose different verdict/state fields and preserve learner authorship.
- Why it matters: Only passing observed learner work may propose progress/evidence updates.
- Prerequisites: KIKO-027A.
- Known concepts: Tagged variants, verification observations, evidence boundaries, and help levels.
- New concepts and syntax: Review verdict variants and proposed state-update payloads.
- Learner task: Validate one failed and one passing review interaction.
- Verification: `.venv/bin/python -m unittest tests.test_tutor_interactions.ReviewTests -v`
- Expected behavior: Failure has next correction/no update; pass has accepted behavior/help/update proposal/next title.
- Edge case: Passing review that begins the next lesson is rejected.
- Not included: Executing review checks or persisting the proposed update.
- Exit condition: Failed, passing, false-pass, and next-lesson-leak fixtures pass.

<a id="kiko-027c"></a>
### KIKO-027C — Validate debug and completion handoff interactions

- Checkpoint kind: implementation
- Observable outcome: Debug responses distinguish evidence/hypothesis while handoffs report only verified updates and next title.
- Why it matters: Diagnosis and completion have different truth and state boundaries.
- Prerequisites: KIKO-027B.
- Known concepts: Tagged variants, progress status, observations, and proposed updates.
- New concepts and syntax: Optional hypothesis field and verified handoff summary.
- Learner task: Validate one debug and one completion-handoff fixture.
- Verification: `.venv/bin/python -m unittest tests.test_tutor_interactions.DebugHandoffTests -v`
- Expected behavior: Unsupported cause claims fail; verified handoff lists evidence/updates and stops before next lesson.
- Edge case: Debugging alone cannot set checkpoint status to verified.
- Not included: Running diagnostics or writing state.
- Exit condition: Confirmed-cause, hypothesis, invalid-debug-completion, and handoff-stop fixtures pass.

<a id="kiko-028"></a>
### KIKO-028 — Classify feedback and repair the current interaction

- Checkpoint kind: implementation
- Observable outcome: An unclear/format/help report is classified and produces an immediate corrected interaction without progress change.
- Why it matters: Tutor defects must improve the product without being blamed on learner competence.
- Prerequisites: KIKO-027C.
- Known concepts: Intent selection, structured data, privacy boundaries, and user confirmation.
- New concepts and syntax: Multi-scope classification and repair-action selection.
- Learner task: Classify one feedback signal and select the corrected interaction/help response.
- Verification: `.venv/bin/python -m unittest tests.test_tutor_feedback.ClassificationRepairTests -v`
- Expected behavior: Reusable and learner-specific fixtures classify differently; both repair guidance and preserve checkpoint/competence.
- Edge case: Ordinary learner difficulty remains a help request rather than a Tutor-defect finding.
- Not included: Self-modifying code, automatic skill edits, or remote telemetry.
- Exit condition: Classification, immediate recovery, learner-difficulty, and no-state-change fixtures pass.

<a id="kiko-028a"></a>
### KIKO-028A — Sanitize and deduplicate feedback candidates

- Checkpoint kind: implementation
- Observable outcome: Reusable/project/runtime feedback becomes one optional sanitized candidate under user control.
- Why it matters: Product improvement records must exclude private interaction/source data and duplicate policy.
- Prerequisites: KIKO-028.
- Known concepts: Feedback classification, privacy allowlists, user confirmation, and separate state ownership.
- New concepts and syntax: Candidate sanitization allowlist and deduplication key.
- Learner task: Build, deduplicate, keep, or discard one structured feedback candidate.
- Verification: `.venv/bin/python -m unittest tests.test_tutor_feedback.CandidateTests -v`
- Expected behavior: Allowed summary fields remain; raw prompt/source/secret fields are absent; duplicate updates one candidate.
- Edge case: Discard writes nothing and never changes learner competence/reference.
- Not included: Shared skill/code mutation or remote telemetry.
- Exit condition: Sanitize, duplicate, keep, discard, forbidden-field, and competence-isolation fixtures pass.
