# Phase 10 — Product Quality and Onboarding

<a id="kiko-057"></a>
### KIKO-057 — Diagnose dependencies and authentication

- Checkpoint kind: implementation
- Observable outcome: `kiko doctor` reports supported platform/Core/Codex/VS Code/auth status with recovery guidance.
- Why it matters: First-time users need actionable setup help instead of raw process failures.
- Prerequisites: KIKO-046 and KIKO-056.
- Known concepts: CLI commands, controlled errors, process checks, and version contracts.
- New concepts and syntax: Version comparison, capability checks, and sanitized diagnostics.
- Learner task: Add one doctor report with pass/warn/fail entries and no credential exposure.
- Verification: `.venv/bin/python -m unittest tests.test_doctor -v`
- Expected behavior: Supported fixture passes; missing/old/unauthenticated fixtures name the failing boundary and next action.
- Edge case: Doctor works without loading or changing a learner project.
- Not included: Installing dependencies, logging in automatically, or remote telemetry.
- Exit condition: Platform, Core, CLI, auth, and VS Code fixtures produce correct safe reports.

<a id="kiko-058"></a>
### KIKO-058 — Recognize workspace and show setup readiness

- Checkpoint kind: implementation
- Observable outcome: Sidebar/CLI distinguish unrecognized, existing valid, incomplete, and conflicting Tutor workspaces.
- Why it matters: Product value begins only when setup reaches a clear learner action safely.
- Prerequisites: KIKO-053B, KIKO-054D, and KIKO-057.
- Known concepts: Workspace paths, state validation, setup/ready views, and doctor results.
- New concepts and syntax: Project-recognition result and onboarding entry-state mapping.
- Learner task: Classify one opened workspace and render the correct first setup/ready action.
- Verification: `.venv/bin/python -m unittest tests.e2e.test_onboarding.WorkspaceRecognitionTests -v`
- Expected behavior: Missing, valid, incomplete, and conflicting Tutor states produce distinct non-destructive entry states.
- Edge case: Existing project/global state is never silently replaced or merged.
- Not included: Source generation, account creation, or choosing reversible implementation trivia for the user.
- Exit condition: Every workspace-state fixture reaches one correct setup/ready/blocked result.

<a id="kiko-058a"></a>
### KIKO-058A — Complete onboarding discovery and approvals

- Checkpoint kind: integration
- Observable outcome: A beginner completes short discovery rounds and separately accepts brief and plan through the primary UI.
- Why it matters: Thorough planning must remain understandable without exposing a technical questionnaire.
- Prerequisites: KIKO-049A, KIKO-054B, and KIKO-058.
- Known concepts: Discovery/plan Core flow, planning sidebar action, and progressive disclosure.
- New concepts and syntax: Onboarding-stage presenter state and persisted draft-session pointer.
- Learner task: Connect unrecognized workspace through questions, brief preview, plan summary, revise, and approvals.
- Verification: `.venv/bin/python -m unittest tests.e2e.test_onboarding.DiscoveryApprovalTests -v`
- Expected behavior: Beginner sees at most three questions, confirmed summary, plan scope/size/first step, and separate approvals.
- Edge case: Cancel/provider failure preserves answers without creating Tutor files.
- Not included: Transactional file creation or application source generation.
- Exit condition: New, unsure, revise, cancel, resume, and separate-approval journeys pass.

<a id="kiko-058b"></a>
### KIKO-058B — Create or resume the project transactionally

- Checkpoint kind: integration
- Observable outcome: Accepted onboarding creates all Tutor files and returns Ready at the first checkpoint; reopening resumes correctly.
- Why it matters: Setup must not leave partial projects or reset accepted progress.
- Prerequisites: KIKO-049C and KIKO-058A.
- Known concepts: Transactional Tutor-file creation, workspace recognition, sidebar states, and handoff.
- New concepts and syntax: Onboarding completion receipt and reopen validation.
- Learner task: Connect final plan acceptance to Core creation and later workspace reopen.
- Verification: `.venv/bin/python -m unittest tests.e2e.test_onboarding.CreateResumeTests -v`
- Expected behavior: Accepted project becomes Ready at first checkpoint; reopen finds same handoff; failure restores prior workspace.
- Edge case: Existing valid project routes to resume without re-running initialization.
- Not included: Source generation or dependency installation.
- Exit condition: Create, partial-failure, cancel, existing-project, and reopen fixtures pass across CLI/sidebar.

<a id="kiko-059"></a>
### KIKO-059 — Define stable product error codes and recovery mapping

- Checkpoint kind: implementation
- Observable outcome: State, protocol, auth, process, provider, and compatibility failures map to stable codes and allowed recovery actions.
- Why it matters: Users must know whether to retry, restart, reauthenticate, restore, or stop.
- Prerequisites: KIKO-042B, KIKO-052B, and KIKO-057.
- Known concepts: Controlled errors, diagnostics, backups, and process lifecycle.
- New concepts and syntax: Error taxonomy and code-to-recovery-action table.
- Learner task: Map representative boundary errors to code, safe detail policy, and allowed action set.
- Verification: `.venv/bin/python -m unittest tests.test_error_taxonomy -v`
- Expected behavior: Every known failure has one boundary/code and only valid retry/restart/reauth/restore/stop actions.
- Edge case: Unknown failure maps to a safe generic code without raw secret-bearing detail.
- Not included: Hiding failures as teaching feedback or automatic destructive repair.
- Exit condition: Known, unknown, recoverable, and blocked taxonomy fixtures pass.

<a id="kiko-059a"></a>
### KIKO-059A — Present recovery actions consistently across surfaces

- Checkpoint kind: integration
- Observable outcome: CLI and sidebar render the same error meaning and execute only the Core-approved recovery action.
- Why it matters: Users need consistent recovery regardless of surface.
- Prerequisites: KIKO-053B, KIKO-054D, and KIKO-059.
- Known concepts: Stable error codes, recoverable/blocked views, CLI presenter, and Core actions.
- New concepts and syntax: Cross-surface error fixture and recovery receipt.
- Learner task: Route one error/recovery pair through CLI and sidebar without duplicating policy.
- Verification: `.venv/bin/python -m unittest tests.e2e.test_error_recovery -v`
- Expected behavior: Both surfaces name the same cause/action and Core records one bounded retry/restart.
- Edge case: Repeated recovery action cannot duplicate process, request, write, or evidence.
- Not included: Automatic destructive repair or hiding errors as teaching feedback.
- Exit condition: Every documented error class has CLI/sidebar semantic parity and safe action evidence.

<a id="kiko-060"></a>
### KIKO-060 — Inspect learner and feedback data

- Checkpoint kind: implementation
- Observable outcome: User can inspect learner, reference, and feedback data as separate read-only owners.
- Why it matters: Private local learning history belongs to the user, not the model or project.
- Prerequisites: KIKO-021, KIKO-022, KIKO-028C, KIKO-050B, and KIKO-053A.
- Known concepts: Separate data owners, confirmations, atomic writes, and sanitized feedback.
- New concepts and syntax: Owner-specific read-only inspection view.
- Learner task: Implement inspection for each selected owner against temporary data without writing anything.
- Verification: `.venv/bin/python -m unittest tests.e2e.test_data_control.InspectTests -v`
- Expected behavior: Display is complete, sanitized, owner-labeled, and changes no source or durable state.
- Edge case: Missing owner data displays an explicit empty result rather than another owner's content.
- Not included: Export, reset/delete, cloud synchronization, telemetry, or expiration.
- Exit condition: Inspect, missing-data, sanitization, owner-isolation, and no-write fixtures pass.

<a id="kiko-060a"></a>
### KIKO-060A — Export learner and feedback data

- Checkpoint kind: implementation
- Observable outcome: User can export selected learner, reference, and feedback owners into one labeled portable bundle.
- Why it matters: Private local learning history belongs to the user and must be portable before destructive controls exist.
- Prerequisites: KIKO-060.
- Known concepts: Owner-specific inspection, serialization, sanitization, confirmations, and atomic writes.
- New concepts and syntax: Export manifest and owner-specific export entries.
- Learner task: Export selected temporary owners without modifying their source data.
- Verification: `.venv/bin/python -m unittest tests.e2e.test_data_control.ExportTests -v`
- Expected behavior: Bundle contains only selected labeled owners, versions, and sanitized content.
- Edge case: Missing selected owner produces an explicit empty entry, never another owner's data.
- Not included: Reset/delete, cloud upload, telemetry, or automatic expiration.
- Exit condition: Selected, missing, sanitized, owner-isolated, and no-source-write export fixtures pass.

<a id="kiko-060b"></a>
### KIKO-060B — Reset one selected local data owner

- Checkpoint kind: implementation
- Observable outcome: Explicit target-specific confirmation resets one selected owner to its valid empty/default state.
- Why it matters: Reset must preserve unrelated user-owned history and remain different from deletion.
- Prerequisites: KIKO-060A.
- Known concepts: Separate owners, export, confirmations, defaults, backups, and atomic state operations.
- New concepts and syntax: Destructive-action target receipt and typed confirmation phrase/action.
- Learner task: Implement one target-specific reset transaction with cancel and export-first option.
- Verification: `.venv/bin/python -m unittest tests.e2e.test_data_control.ResetTests -v`
- Expected behavior: Cancel changes nothing; confirmed reset writes only the target's valid default and preserves all others.
- Edge case: Ambiguous “reset all” is rejected unless each owner is explicitly listed and confirmed.
- Not included: Deleting files, cloud data, or unrelated Codex/VS Code state.
- Exit condition: Cancel, wrong-target, selective reset, export-first, and owner-preservation fixtures pass.

<a id="kiko-060c"></a>
### KIKO-060C — Delete one selected local data owner

- Checkpoint kind: implementation
- Observable outcome: Explicit target-specific confirmation removes only one selected local owner.
- Why it matters: Deletion is less reversible than reset and needs its own exact safety contract.
- Prerequisites: KIKO-060B.
- Known concepts: Owner targets, export-first option, confirmation receipt, backups, and atomic operations.
- New concepts and syntax: Delete-specific confirmation and absent-after-delete receipt.
- Learner task: Implement one target-specific delete transaction with cancel and prior-export option.
- Verification: `.venv/bin/python -m unittest tests.e2e.test_data_control.DeleteTests -v`
- Expected behavior: Cancel changes nothing; confirmed delete removes only its target and preserves all others.
- Edge case: Ambiguous “delete all” is rejected unless every owner is listed and confirmed separately.
- Not included: Cloud deletion or unrelated Codex/VS Code data.
- Exit condition: Cancel, wrong-target, selective delete, export-first, repeated-delete, and owner-preservation fixtures pass.

<a id="kiko-061"></a>
### KIKO-061 — Localize headings without changing technical literals

- Checkpoint kind: implementation
- Observable outcome: Interaction headings localize while semantic field order and technical literals remain unchanged.
- Why it matters: Consistent pedagogy must remain understandable and operable across supported explanation languages.
- Prerequisites: KIKO-027F and KIKO-053A.
- Known concepts: Canonical fields, presenters, and configured explanation language.
- New concepts and syntax: Localization keys and fallback locale.
- Learner task: Render one interaction in Croatian and fallback English without translating code/commands/output.
- Verification: `npm --prefix extension test -- --runInBand localization`
- Expected behavior: Labels localize and preserve order; technical literals remain byte-for-byte unchanged.
- Edge case: Missing translation falls back visibly without empty labels or semantic reordering.
- Not included: Full multilingual content authoring or formal external accessibility certification.
- Exit condition: Croatian, fallback, missing-key, semantic-order, and technical-literal fixtures pass.

<a id="kiko-061a"></a>
### KIKO-061A — Verify keyboard, labels, and focus

- Checkpoint kind: integration
- Observable outcome: Primary sidebar actions are keyboard operable with semantic labels and predictable focus.
- Why it matters: Product actions must be usable without a mouse or ambiguous unlabeled controls.
- Prerequisites: KIKO-053B, KIKO-054D, and KIKO-061.
- Known concepts: Sidebar states, localized labels, focus management, and primary actions.
- New concepts and syntax: ARIA labels, keyboard focus order, and focus assertions.
- Learner task: Add keyboard/label/focus checks to primary state/action fixtures.
- Verification: `npm --prefix extension test -- --runInBand keyboard-accessibility`
- Expected behavior: Keyboard-only user reaches each primary action and focus moves predictably after state changes.
- Edge case: Updating a working response does not repeatedly steal focus.
- Not included: Contrast, selectable text, formal certification, or unconfirmed assistive technologies.
- Exit condition: Keyboard, label, focus-order, state-change, and no-focus-steal fixtures pass.

<a id="kiko-061b"></a>
### KIKO-061B — Verify visual and text accessibility

- Checkpoint kind: integration
- Observable outcome: Sidebar states use readable contrast and status text while response/code text remains selectable.
- Why it matters: Meaning cannot depend on color alone and learning content must be copy/selectable.
- Prerequisites: KIKO-061A.
- Known concepts: Sidebar states, localized labels, safe rendering, and automated accessibility assertions.
- New concepts and syntax: Contrast assertions, non-color status cues, and selectable-text checks.
- Learner task: Add contrast/status/selectable-text checks to primary response and error fixtures.
- Verification: `npm --prefix extension test -- --runInBand visual-text-accessibility`
- Expected behavior: Every state has readable contrast/text meaning and long/streaming content remains selectable.
- Edge case: Streaming updates preserve selection and do not encode status through color alone.
- Not included: Formal external certification or unconfirmed assistive technology combinations.
- Exit condition: Contrast, text-cue, selectable, streaming-selection, and long-response fixtures pass.

<a id="kiko-062"></a>
### KIKO-062 — Aggregate one full product verification command

- Checkpoint kind: integration
- Observable outcome: One documented command runs deterministic Python, protocol, security, TypeScript, extension, and fake-e2e checks.
- Why it matters: Release confidence needs one reproducible gate rather than scattered manual memory.
- Prerequisites: KIKO-056, KIKO-057, KIKO-058B, KIKO-059A, KIKO-060C, and KIKO-061B.
- Known concepts: Existing test commands, clean fixtures, and failure exit codes.
- New concepts and syntax: Build orchestration target and test-stage reporting.
- Learner task: Add a root verification target that stops on failure and summarizes passed stages.
- Verification: `make verify`
- Expected behavior: A clean checkout's deterministic suite passes; any broken stage makes the command non-zero.
- Edge case: Live Codex smoke is clearly separate/skippable and cannot make deterministic CI flaky.
- Not included: Publishing artifacts or claiming live model determinism.
- Exit condition: The command covers every required deterministic quality gate and documents optional live checks.
