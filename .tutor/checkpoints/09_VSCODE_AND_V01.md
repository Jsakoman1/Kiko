# Phase 9 — Thin VS Code Extension and v0.1 Proof

<a id="kiko-051"></a>
### KIKO-051 — Create the TypeScript extension development environment

- Checkpoint kind: implementation
- Observable outcome: An isolated `extension/` TypeScript project type-checks and runs one empty test command.
- Why it matters: TypeScript is a new language/toolchain and must be learned before VS Code lifecycle code is added.
- Prerequisites: KIKO-025A and KIKO-046.
- Known concepts: Project-local environments, package metadata, configuration-format preflight, and test commands.
- New concepts and syntax: `package.json`, `tsconfig.json`, npm development dependencies/scripts, and TypeScript compiler check.
- Learner task: Create the minimal extension development configuration without registering or activating Kiko yet.
- Verification: Run `npm --prefix extension install`, then `npm --prefix extension run check` and `npm --prefix extension test`.
- Expected behavior: Dependencies install locally, TypeScript configuration is valid, and the empty test foundation passes.
- Edge case: Generated `node_modules/` and build output remain ignored by Git.
- Not included: VS Code activation, contribution points, sidebar provider, Core process, or Tutor rendering.
- Exit condition: A clean local TypeScript check/test cycle passes without editor behavior.

<a id="kiko-051a"></a>
### KIKO-051A — Activate a static Kiko sidebar

- Checkpoint kind: implementation
- Observable outcome: VS Code activates one static Kiko sidebar without containing Tutor policy.
- Why it matters: The first editor behavior should prove the extension lifecycle and thin UI boundary only.
- Prerequisites: KIKO-017C and KIKO-051.
- Known concepts: TypeScript project, CLI/process boundary, and UI responsibility from the architecture.
- New concepts and syntax: Extension activation, contribution points, command registration, and view provider lifecycle.
- Learner task: Register the Kiko view and show one static connection-status message.
- Verification: Run `npm --prefix extension run check`, then `npm --prefix extension test -- --runInBand activation`.
- Expected behavior: The extension-host fixture activates the Kiko view through documented entry points.
- Edge case: Activation without an open workspace shows a static setup message instead of crashing.
- Not included: Python process startup, interactive actions, chat rendering, or Tutor decisions in TypeScript.
- Exit condition: Static activation/view fixtures pass and TypeScript contains no pedagogical policy.

<a id="kiko-052"></a>
### KIKO-052 — Start and stop Core from the extension

- Checkpoint kind: implementation
- Observable outcome: Extension starts one configured Core child process and disposes it on extension shutdown.
- Why it matters: The UI must speak the stable contract defined before its implementation.
- Prerequisites: KIKO-017C, KIKO-039, KIKO-046, and KIKO-051A.
- Known concepts: Process ownership, configured commands, extension activation, and controlled errors.
- New concepts and syntax: Node child process spawn and VS Code disposable lifecycle.
- Learner task: Start/stop a scripted fake Core without sending protocol messages.
- Verification: `npm --prefix extension test -- --runInBand core-process`
- Expected behavior: Activation starts once; dispose/reload closes the exact child process.
- Edge case: Missing command and duplicate dispose show controlled behavior without orphan process.
- Not included: JSONL parsing, request correlation, or Tutor rendering.
- Exit condition: Start, missing-command, duplicate-start, dispose, and reload fixtures pass.

<a id="kiko-052a"></a>
### KIKO-052A — Correlate one extension/Core JSONL request

- Checkpoint kind: implementation
- Observable outcome: Extension sends one versioned JSONL request and resolves the matching result by request ID.
- Why it matters: UI actions need a transport that remains independent from Python internals.
- Prerequisites: KIKO-017C and KIKO-052.
- Known concepts: Core process, JSONL framing, request IDs, and TypeScript promises.
- New concepts and syntax: Stream line buffering and pending-promise map.
- Learner task: Implement one status request/result round trip against fake Core.
- Verification: `npm --prefix extension test -- --runInBand core-protocol`
- Expected behavior: Interleaved lines resolve only the matching request and valid status reaches the extension.
- Edge case: Malformed/unmatched/duplicate result cannot resolve a request incorrectly.
- Not included: Cancellation, timeout, UI state rendering, or live Codex.
- Exit condition: Valid, interleaved, malformed, unmatched, and duplicate-ID fixtures pass.

<a id="kiko-052b"></a>
### KIKO-052B — Handle extension/Core cancel and failure disposal

- Checkpoint kind: implementation
- Observable outcome: Pending extension requests terminate once on cancel, timeout, malformed protocol, or Core exit.
- Why it matters: VS Code must stay responsive and leave no hanging promises/processes.
- Prerequisites: KIKO-052A.
- Known concepts: Pending requests, terminal states, process disposal, and controlled errors.
- New concepts and syntax: Promise rejection mapping, cancellation token, and bounded timeout.
- Learner task: Route scripted terminal protocol/process events to one visible extension error result.
- Verification: `npm --prefix extension test -- --runInBand core-failures`
- Expected behavior: Each terminal path cleans pending requests and disposes/restarts only as documented.
- Edge case: Late result after cancel/exit is ignored and cannot mutate UI state.
- Not included: Final error copy or Tutor workflow retry policy.
- Exit condition: Cancel, timeout, malformed line, Core exit, and late-result fixtures pass.

<a id="kiko-053"></a>
### KIKO-053 — Render setup, ready, and working states

- Checkpoint kind: implementation
- Observable outcome: Setup, Ready, and Working states render from Core status/progress data.
- Why it matters: Users need predictable orientation and recovery without duplicated pedagogy.
- Prerequisites: KIKO-027F, KIKO-051A, and KIKO-052B.
- Known concepts: Canonical TutorInteraction and explicit UI states.
- New concepts and syntax: Webview state rendering, safe text escaping, and initial focus management.
- Learner task: Render setup, ready, and working fixtures without adding teaching policy.
- Verification: `npm --prefix extension test -- --runInBand initial-views`
- Expected behavior: Each state shows its required status/progress/action and escapes untrusted text.
- Edge case: Activation without workspace remains in actionable setup state.
- Not included: Visual branding polish or teaching logic in TypeScript.
- Exit condition: Setup, ready, working, missing-workspace, and escaped-text fixtures pass.

<a id="kiko-053a"></a>
### KIKO-053A — Render response and review sidebar states

- Checkpoint kind: implementation
- Observable outcome: Response and Review states render canonical TutorInteraction fields without reordering or reinterpretation.
- Why it matters: Python Core, not TypeScript, owns pedagogy and review truth.
- Prerequisites: KIKO-053.
- Known concepts: Canonical interactions, webview rendering, safe escaping, and presenter boundaries.
- New concepts and syntax: Interaction-section rendering and review-verdict styling.
- Learner task: Render new lesson, hint, failed review, and passing review fixtures from Core payloads.
- Verification: `npm --prefix extension test -- --runInBand response-review-views`
- Expected behavior: Required fields/order match `LESSON_SPEC.md`; absent optional fields do not create empty UI.
- Edge case: Passing review names but does not render the next lesson body.
- Not included: Error/blocked states or action wiring.
- Exit condition: Lesson, hint, failed-review, passing-review, and optional-field fixtures pass.

<a id="kiko-053b"></a>
### KIKO-053B — Render recoverable-error and blocked states

- Checkpoint kind: implementation
- Observable outcome: Recoverable and blocked Core results show cause, safe detail, and allowed next actions.
- Why it matters: Product failures must not look like teaching feedback or leave a blank sidebar.
- Prerequisites: KIKO-052B and KIKO-053A.
- Known concepts: Controlled Core errors, safe rendering, and explicit view states.
- New concepts and syntax: Error-code-to-view mapping and conditional action availability.
- Learner task: Render one recoverable and one blocked fixture without exposing unsafe detail.
- Verification: `npm --prefix extension test -- --runInBand error-views`
- Expected behavior: Recoverable state offers valid retry/restart; blocked state explains external resolution.
- Edge case: Unknown error uses safe fallback and diagnostic ID, not raw secret-bearing stderr.
- Not included: Full error taxonomy/copy or recovery execution.
- Exit condition: Known recoverable, blocked, unknown, and sanitized-detail fixtures pass.

<a id="kiko-054"></a>
### KIKO-054 — Connect sidebar help and hint actions

- Checkpoint kind: implementation
- Observable outcome: Question and hint actions call Core and render canonical response states.
- Why it matters: The extension becomes a usable surface over already proven Core behavior.
- Prerequisites: KIKO-047 and KIKO-053A.
- Known concepts: Core commands, protocol requests, UI states, and user confirmation.
- New concepts and syntax: Action correlation and working-to-response transition.
- Learner task: Connect question submission and one hint request without adding help policy to TypeScript.
- Verification: `npm --prefix extension test -- --runInBand help-actions`
- Expected behavior: Each action reaches the correct Core handler and renders its returned interaction.
- Edge case: Double submit cannot create duplicate active requests.
- Not included: Marketplace publishing or multi-window collaboration.
- Exit condition: Ask, hint, empty input, and duplicate-submit fixtures pass.

<a id="kiko-054a"></a>
### KIKO-054A — Connect the sidebar review action

- Checkpoint kind: integration
- Observable outcome: Review action renders failed or passing review and performs only Core-approved confirmation flow.
- Why it matters: Extension must not decide verification truth or mutate evidence itself.
- Prerequisites: KIKO-048A, KIKO-053A, and KIKO-054.
- Known concepts: Review CLI/Core flow, review views, user confirmation, and protocol actions.
- New concepts and syntax: Review preview/confirm action correlation.
- Learner task: Connect review request and accepted-update confirmation against fake Core.
- Verification: `npm --prefix extension test -- --runInBand review-action`
- Expected behavior: Failed review offers retry task; pass shows proposal and only Core performs confirmed update.
- Edge case: Closing/declining confirmation preserves all durable state.
- Not included: Planning or feedback actions.
- Exit condition: Fail, pass, confirm, decline, and close-during-confirmation fixtures pass.

<a id="kiko-054b"></a>
### KIKO-054B — Connect the sidebar planning action

- Checkpoint kind: integration
- Observable outcome: Sidebar moves through discovery, brief approval, plan review, and accepted project creation via Core.
- Why it matters: New users need the validated plan workflow without duplicating it in TypeScript.
- Prerequisites: KIKO-049C, KIKO-053A, and KIKO-054A.
- Known concepts: CLI planning flow, setup/response views, protocol actions, and separate acceptance.
- New concepts and syntax: Multi-turn planning view state correlation.
- Learner task: Render and submit the next Core-provided discovery/approval action one stage at a time.
- Verification: `npm --prefix extension test -- --runInBand planning-action`
- Expected behavior: Answers/approvals reach Core; only accepted plan creation reaches Ready state.
- Edge case: Cancel/provider failure preserves confirmed answers and last accepted project state.
- Not included: Plan generation or validation logic in TypeScript.
- Exit condition: Discovery, brief, plan, accept, revise, cancel, and resume fixtures pass.

<a id="kiko-054c"></a>
### KIKO-054C — Connect cancel and retry actions

- Checkpoint kind: integration
- Observable outcome: Cancel/retry actions terminate or restart one request through Core-owned lifecycle policy.
- Why it matters: Users need request recovery without duplicate turns or processes.
- Prerequisites: KIKO-052B, KIKO-053B, and KIKO-054B.
- Known concepts: Terminal requests, recoverable views, feedback flow, and Core ownership.
- New concepts and syntax: Cancel/retry action correlation.
- Learner task: Connect cancel and one Core-approved retry to their protocol messages.
- Verification: `npm --prefix extension test -- --runInBand cancel-retry-actions`
- Expected behavior: Cancel/retry resolve once and return the documented view state.
- Edge case: Repeated click cannot duplicate a turn, process, or terminal result.
- Not included: Feedback actions, automatic repair, or telemetry.
- Exit condition: Cancel, retry, duplicate-click, late-result, and process-count fixtures pass.

<a id="kiko-054d"></a>
### KIKO-054D — Connect the unclear-feedback action

- Checkpoint kind: integration
- Observable outcome: “This was unclear” sends one feedback request to Core and renders its repaired interaction plus candidate controls.
- Why it matters: Tutor-quality feedback must remain separate from request cancellation and learner competence.
- Prerequisites: KIKO-050B, KIKO-053B, and KIKO-054C.
- Known concepts: Feedback repair/candidates, protocol actions, response views, and Core ownership.
- New concepts and syntax: Feedback-action correlation and candidate-control rendering.
- Learner task: Connect one unclear-feedback action without implementing classification or repair in TypeScript.
- Verification: `npm --prefix extension test -- --runInBand feedback-action`
- Expected behavior: Core repair renders and keep/edit/export/discard controls map back to Core messages.
- Edge case: Repeated click cannot duplicate feedback candidates or change competence/progress.
- Not included: Automatic skill/code mutation or remote telemetry.
- Exit condition: Repair, controls, duplicate-click, and unchanged-state fixtures pass.

<a id="kiko-055"></a>
### KIKO-055 — Test the extension against a fake Core

- Checkpoint kind: integration
- Observable outcome: Extension-host tests prove protocol, rendering, accessibility basics, and failure states without Codex.
- Why it matters: Editor behavior must be deterministic in CI and independent of live model variability.
- Prerequisites: KIKO-052B, KIKO-053B, and KIKO-054D.
- Known concepts: Test doubles, fixtures, protocol messages, and UI state assertions.
- New concepts and syntax: VS Code extension-host integration harness and fixture process control.
- Learner task: Add one end-to-end fake-Core scenario from activation through response and shutdown.
- Verification: `npm --prefix extension test`
- Expected behavior: All TypeScript/unit/extension-host tests pass from a clean dependency install.
- Edge case: Fake Core crash leaves the extension responsive with restart guidance.
- Not included: Authenticated Codex or packaging the VSIX.
- Exit condition: Help, review, planning, feedback, error, cancel, restart, and disposal paths pass.

<a id="kiko-056"></a>
### KIKO-056 — Pass the v0.1 end-to-end vertical proof

- Checkpoint kind: acceptance
- Observable outcome: One real project completes discovery/help/edit/review/evidence/resume through CLI and sidebar.
- Why it matters: It validates the central product hypothesis before release polish and distribution work.
- Prerequisites: KIKO-043, KIKO-044B, KIKO-048A, KIKO-049C, and KIKO-055.
- Known concepts: Full Core, provider, protocol, CLI, extension, and state flows.
- New concepts and syntax: End-to-end scenario orchestration and evidence capture.
- Learner task: Run and document golden journeys 2–5 with one authenticated read-only Codex turn.
- Verification: `.venv/bin/python -m unittest tests.e2e.test_v01_vertical_slice -v`
- Expected behavior: User resumes correct checkpoint; only accepted learner work updates evidence/reference; no source is AI-edited.
- Edge case: Missing global state and App Server failure show controlled recovery without partial progress.
- Not included: Clean-machine install, polished onboarding, upgrade, or release artifacts.
- Exit condition: Automated fake path and documented live smoke path satisfy v0.1 acceptance.
