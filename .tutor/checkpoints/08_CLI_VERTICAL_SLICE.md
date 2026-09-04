# Phase 8 — Standalone CLI Vertical Slice

<a id="kiko-046"></a>
### KIKO-046 — Add stable learner-facing CLI commands

- Checkpoint kind: implementation
- Observable outcome: Installed CLI exposes `init`, `status`, `ask`, `hint`, `review`, `feedback`, `doctor`, `show`, and `--version` usage.
- Why it matters: Tutor Core must remain usable and diagnosable without the editor extension.
- Prerequisites: KIKO-017C, KIKO-027F, KIKO-034C, and KIKO-036A.
- Known concepts: CLI arguments, functions, validation, and package entry points.
- New concepts and syntax: `argparse` subcommands and exit codes.
- Learner task: Add one parser with clear help and dispatch without implementing command internals twice.
- Verification: Run `.venv/bin/kiko --help`, then `.venv/bin/kiko --version`.
- Expected behavior: Commands and concise usage display; unknown/missing arguments exit non-zero with guidance.
- Edge case: Help/version work without starting Codex or loading a project.
- Not included: Full workflows or shell completion.
- Exit condition: Parser and dispatch tests cover every command and malformed input.

<a id="kiko-047"></a>
### KIKO-047 — Connect the complete help interaction

- Checkpoint kind: integration
- Observable outcome: `kiko ask` loads context, calls fake/live provider, validates, and renders one canonical interaction.
- Why it matters: This proves the core teaching loop outside VS Code.
- Prerequisites: KIKO-037, KIKO-043, and KIKO-046.
- Known concepts: Context compilation, provider injection, TutorInteraction, and CLI dispatch.
- New concepts and syntax: CLI provider selection and presenter functions.
- Learner task: Connect one ask command end to end without moving pedagogy into the CLI layer.
- Verification: `.venv/bin/kiko ask --provider fake "Explain the current step"`
- Expected behavior: Stable progress/problem/syntax/task/verification content renders in the documented order.
- Edge case: Empty question or provider failure returns a controlled exit code and no state update.
- Not included: Review persistence, planning, or interactive shell sessions.
- Exit condition: Fake ask, live-smoke, invalid-input, and provider-error tests pass.

<a id="kiko-048"></a>
### KIKO-048 — Render one failed CLI review

- Checkpoint kind: implementation
- Observable outcome: `kiko review` renders checks, observations, first issue, next learner change, and re-verification for a failed review.
- Why it matters: Working software and demonstrated learning must remain distinct.
- Prerequisites: KIKO-027C, KIKO-037, KIKO-043, and KIKO-046.
- Known concepts: Failed-review interaction, provider results, CLI rendering, and unchanged-state policy.
- New concepts and syntax: Review check-result adapter.
- Learner task: Connect one fake failing review from expert result to CLI output.
- Verification: `.venv/bin/python -m unittest tests.integration.test_cli_review.FailedReviewTests -v`
- Expected behavior: First actionable issue and exact retry appear; no project/learner/reference state changes.
- Edge case: Expert-proposed correction cannot be recorded as learner work.
- Not included: Automatic source correction or competence promotion from model output alone.
- Exit condition: Failed, malformed, and false-pass review fixtures preserve state and render correct guidance.

<a id="kiko-048a"></a>
### KIKO-048A — Persist one passing review transaction

- Checkpoint kind: integration
- Observable outcome: A verified learner-authored review renders acceptance and atomically updates each approved owner once.
- Why it matters: Completion and competence need evidence without partial or duplicate durable updates.
- Prerequisites: KIKO-016C, KIKO-021, KIKO-022, KIKO-027D, and KIKO-048.
- Known concepts: Passing-review interaction, evidence/reference updates, atomic state, and user confirmation.
- New concepts and syntax: Multi-owner review transaction and idempotency key.
- Learner task: Connect one passing fake review through preview, approval, writes, and completion handoff.
- Verification: `.venv/bin/python -m unittest tests.integration.test_cli_review.PassingReviewTests -v`
- Expected behavior: Approved pass updates roadmap/evidence/reference once; decline changes nothing.
- Edge case: Interrupted or repeated approval cannot produce partial or duplicate evidence.
- Not included: Automatic source correction or competence promotion beyond evidence policy.
- Exit condition: Pass, decline, duplicate, interruption, and resume fixtures preserve transaction invariants.

<a id="kiko-049"></a>
### KIKO-049 — Complete CLI discovery and brief acceptance

- Checkpoint kind: integration
- Observable outcome: A broad idea moves through short discovery rounds to a separately accepted brief.
- Why it matters: Kiko's differentiating planning system must work before an editor UI exists.
- Prerequisites: KIKO-031A, KIKO-034C, and KIKO-046.
- Known concepts: Discovery state, question rounds, readiness, CLI prompts, and brief acceptance.
- New concepts and syntax: Resumable discovery session record.
- Learner task: Implement idea input, several question rounds, brief preview, accept, revise, and cancel.
- Verification: `.venv/bin/python -m unittest tests.integration.test_cli_planning.DiscoveryBriefTests -v`
- Expected behavior: Accepted brief becomes plan-ready; resume reuses answers; cancel writes no roadmap.
- Edge case: “I am not sure” preserves a visible default without repeating the same question.
- Not included: Automatic source generation, Marketplace setup, or speculative future features.
- Exit condition: Broad idea, detailed idea, resume, revise, unsure, and cancel discovery fixtures pass.

<a id="kiko-049a"></a>
### KIKO-049A — Generate and review a CLI plan candidate

- Checkpoint kind: integration
- Observable outcome: Accepted brief produces a validated/criticized plan summary and full-plan option through CLI.
- Why it matters: The learner must inspect scope, assumptions, risks, size, and first checkpoint before acceptance.
- Prerequisites: KIKO-038B, KIKO-044B, KIKO-049.
- Known concepts: Accepted brief, candidate/critique/repair, plan summary, and CLI interaction.
- New concepts and syntax: CLI plan-review state and expandable detail presentation.
- Learner task: Connect accepted brief to candidate pipeline and separate plan accept/revise/cancel prompt.
- Verification: `.venv/bin/python -m unittest tests.integration.test_cli_planning.PlanReviewTests -v`
- Expected behavior: Only a valid repaired candidate reaches review; no choice writes Tutor files yet.
- Edge case: Newly discovered product ambiguity returns to discovery with prior answers intact.
- Not included: Multi-file creation or application source generation.
- Exit condition: Accept-pending, revise, expand, ambiguity, invalid-provider, and cancel fixtures pass.

<a id="kiko-049b"></a>
### KIKO-049B — Stage and validate accepted Tutor files

- Checkpoint kind: integration
- Observable outcome: Explicitly accepted plan renders a complete Tutor document set in an isolated staging area and validates its manifest.
- Why it matters: Files must be complete and internally valid before the real workspace can be changed.
- Prerequisites: KIKO-016C and KIKO-049A.
- Known concepts: Accepted plan, templates, backups, atomic replacement, and state ownership.
- New concepts and syntax: Multi-file staging directory and document-manifest validation.
- Learner task: Render/stage the accepted Tutor files and validate every required path/link before commit.
- Verification: `.venv/bin/python -m unittest tests.integration.test_cli_planning.ProjectStagingTests -v`
- Expected behavior: Complete stage passes; missing/invalid file or link blocks before workspace mutation.
- Edge case: Existing project/profile remains untouched while staging is inspected.
- Not included: Learner application source, Git initialization, dependency installation, or publication.
- Exit condition: Complete, missing-file, invalid-link, existing-project, and no-workspace-write fixtures pass.

<a id="kiko-049c"></a>
### KIKO-049C — Commit or roll back Tutor-file creation

- Checkpoint kind: integration
- Observable outcome: A validated staged Tutor set commits completely or restores the prior workspace and later resumes correctly.
- Why it matters: Invalid/cancelled/interrupted creation must never leave a misleading partial learning project.
- Prerequisites: KIKO-049B.
- Known concepts: Validated stage, atomic replacement, backups, accepted plan, and state ownership.
- New concepts and syntax: Multi-file commit receipt and rollback/resume journal.
- Learner task: Commit one staged Tutor set and recover one simulated interruption.
- Verification: `.venv/bin/python -m unittest tests.integration.test_cli_planning.ProjectCommitTests -v`
- Expected behavior: Success installs every file; failure/cancel restores prior state; reopen finds first checkpoint.
- Edge case: Existing accepted plan/profile is backed up/preserved and never silently overwritten.
- Not included: Learner source, Git initialization, dependency installation, or publication.
- Exit condition: Commit, partial-failure, cancel, rollback, existing-project, and resume fixtures pass.

<a id="kiko-050"></a>
### KIKO-050 — Repair feedback and preview its CLI candidate

- Checkpoint kind: integration
- Observable outcome: Natural unclear-feedback repairs the current response and shows one sanitized candidate preview.
- Why it matters: Real Tutor defects need a safe improvement path separate from learner competence.
- Prerequisites: KIKO-028C and KIKO-046.
- Known concepts: Feedback classification, sanitization, user confirmation, and CLI subcommands.
- New concepts and syntax: CLI feedback preview presenter.
- Learner task: Connect one `feedback` input to Core repair and render its sanitized candidate preview.
- Verification: `.venv/bin/python -m unittest tests.integration.test_cli_feedback.PreviewTests -v`
- Expected behavior: Corrected interaction and candidate preview appear; learner/project progress is unchanged.
- Edge case: Duplicate signal previews the existing candidate identity rather than raw source/context.
- Not included: Remote telemetry or automatic installed-skill/code updates.
- Exit condition: Repair, preview, duplicate identity, privacy, and unchanged-state fixtures pass.

<a id="kiko-050a"></a>
### KIKO-050A — Keep, edit, or discard a CLI feedback candidate

- Checkpoint kind: integration
- Observable outcome: Explicit keep/edit/discard choice changes only the local sanitized feedback repository.
- Why it matters: Feedback retention belongs to the user and must remain separate from competence and project progress.
- Prerequisites: KIKO-050.
- Known concepts: Candidate preview, deduplication key, user confirmation, and feedback-state owner.
- New concepts and syntax: Local feedback repository and candidate decision transition.
- Learner task: Apply keep, safe edit, or discard to one previewed candidate.
- Verification: `.venv/bin/python -m unittest tests.integration.test_cli_feedback.CandidateDecisionTests -v`
- Expected behavior: Keep/edit persists one sanitized candidate; discard writes nothing; duplicates merge.
- Edge case: Edit cannot add forbidden raw conversation/source/secret fields.
- Not included: Export, remote telemetry, or automatic skill/code updates.
- Exit condition: Keep, edit, forbidden-edit, discard, duplicate, and competence-isolation fixtures pass.

<a id="kiko-050b"></a>
### KIKO-050B — Export a sanitized feedback candidate

- Checkpoint kind: integration
- Observable outcome: User exports selected sanitized feedback candidates without exporting learner/project/source data.
- Why it matters: Users need a portable improvement record while retaining privacy and owner separation.
- Prerequisites: KIKO-050A.
- Known concepts: Feedback repository, selected owners, sanitization, serialization, and file paths.
- New concepts and syntax: Versioned feedback export envelope.
- Learner task: Export one selected candidate set and validate its allowed fields.
- Verification: `.venv/bin/python -m unittest tests.integration.test_cli_feedback.ExportTests -v`
- Expected behavior: Export contains only selected sanitized candidates plus schema/version metadata.
- Edge case: Empty selection produces an explicit empty export, not unrelated state.
- Not included: Remote upload, telemetry, learner/project export, or self-modification.
- Exit condition: Selected, empty, forbidden-field, version, and owner-isolation fixtures pass.
