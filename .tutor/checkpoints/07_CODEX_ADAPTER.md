# Phase 7 — Codex App Server Adapter

<a id="kiko-039"></a>
### KIKO-039 — Start and stop the App Server process

- Checkpoint kind: implementation
- Observable outcome: The Codex App Server child process starts with piped stdio and closes cleanly.
- Why it matters: Kiko needs a local expert process without coupling Tutor Core to process management.
- Prerequisites: KIKO-036A and KIKO-018.
- Known concepts: Module boundaries, exceptions, paths, and read-only policy.
- New concepts and syntax: `subprocess.Popen`, pipes, process lifetime, and context-managed cleanup.
- Learner task: Start the configured command and expose a deterministic close operation.
- Verification: `.venv/bin/python -m unittest tests.integration.test_app_server_process -v`
- Expected behavior: Fake-process fixture starts/stops; missing command and non-zero exit become controlled errors.
- Edge case: Closing twice is safe and leaves no child process.
- Not included: JSON-RPC initialization or live model turns.
- Exit condition: Start, missing-command, crash, normal-close, and duplicate-close fixtures pass.

<a id="kiko-040"></a>
### KIKO-040 — Complete the initialize handshake

- Checkpoint kind: implementation
- Observable outcome: Adapter sends `initialize`, validates its response, then sends `initialized`.
- Why it matters: No thread or turn may start before protocol negotiation succeeds.
- Prerequisites: KIKO-039 and KIKO-035.
- Known concepts: JSON messages, request IDs, validation, and process pipes.
- New concepts and syntax: JSON-RPC request/response correlation and notification messages.
- Learner task: Implement the handshake against a scripted fake App Server.
- Verification: `.venv/bin/python -m unittest tests.integration.test_app_server_initialize -v`
- Expected behavior: Correct order succeeds; malformed, mismatched, timeout, and error responses fail clearly.
- Edge case: Unknown notifications during initialization do not break request correlation.
- Not included: Thread creation or live Codex authentication repair.
- Exit condition: All handshake protocol fixtures pass before enabling later lifecycle methods.

<a id="kiko-041"></a>
### KIKO-041 — Start one project thread

- Checkpoint kind: implementation
- Observable outcome: Adapter starts one new thread bound to the selected workspace path.
- Why it matters: Repository-aware help must begin in the correct project before resume behavior is introduced.
- Prerequisites: KIKO-040 and KIKO-018.
- Known concepts: Paths, IDs, state ownership, and validated messages.
- New concepts and syntax: Session-only thread identifier.
- Learner task: Start one thread against fake lifecycle messages and return its session-only ID.
- Verification: `.venv/bin/python -m unittest tests.integration.test_app_server_thread.StartThreadTests -v`
- Expected behavior: Correct resolved workspace is sent and a valid thread ID remains outside project/learner state.
- Edge case: Thread IDs never enter learner competence or project progress data.
- Not included: Resume/fallback, starting a turn, or retaining raw conversation as project truth.
- Exit condition: Start, malformed-response, wrong-workspace, and state-isolation fixtures pass.

<a id="kiko-041a"></a>
### KIKO-041A — Resume or replace one project thread

- Checkpoint kind: implementation
- Observable outcome: A valid session thread resumes; a stale/unsupported thread produces one controlled fresh-thread fallback.
- Why it matters: Kiko should resume useful provider context without treating it as canonical state or blocking on stale IDs.
- Prerequisites: KIKO-041.
- Known concepts: Thread start, session-only IDs, workspace binding, validation, and controlled errors.
- New concepts and syntax: Resume request and explicit stale-session fallback result.
- Learner task: Resume one fake thread and route stale/invalid IDs to the documented new-thread path.
- Verification: `.venv/bin/python -m unittest tests.integration.test_app_server_thread.ResumeThreadTests -v`
- Expected behavior: Valid session resumes in the same workspace; stale ID starts one fresh thread with a visible reason.
- Edge case: A thread from another workspace is rejected rather than resumed.
- Not included: Starting a turn or storing transcript as project truth.
- Exit condition: Resume, stale, malformed, wrong-workspace, and fresh-fallback fixtures pass.

<a id="kiko-042"></a>
### KIKO-042 — Read and correlate JSONL messages

- Checkpoint kind: implementation
- Observable outcome: Adapter reads one JSON object per line and correlates responses with pending request IDs.
- Why it matters: Reliable framing/correlation is required before event meanings or terminal behavior are added.
- Prerequisites: KIKO-040 and KIKO-041A.
- Known concepts: JSONL messages, loops, IDs, validation, and controlled errors.
- New concepts and syntax: Background line reader, pending-request map, and response correlation.
- Learner task: Parse scripted JSONL and deliver matching responses to two pending requests.
- Verification: `.venv/bin/python -m unittest tests.integration.test_app_server_events.CorrelationTests -v`
- Expected behavior: Interleaved valid responses reach the correct request; malformed/unmatched lines report controlled findings.
- Edge case: Duplicate response ID cannot complete a request twice.
- Not included: Notification dispatch, timeout, cancellation, or UI rendering.
- Exit condition: Framing, interleaving, malformed-line, unmatched-ID, and duplicate-ID fixtures pass.

<a id="kiko-042a"></a>
### KIKO-042A — Dispatch known and unknown App Server events

- Checkpoint kind: implementation
- Observable outcome: Known notifications reach typed handlers while unknown notifications are safely retained/ignored.
- Why it matters: App Server may add events without making Kiko crash.
- Prerequisites: KIKO-042.
- Known concepts: JSONL reader, tagged message types, validation, and controlled findings.
- New concepts and syntax: Event dispatch table and unknown-notification fallback.
- Learner task: Route scripted known completion/error/item events plus one unknown event.
- Verification: `.venv/bin/python -m unittest tests.integration.test_app_server_events.DispatchTests -v`
- Expected behavior: Known handlers receive validated data; unknown event does not terminate the reader.
- Edge case: A known event with invalid payload is an error, not an unknown event.
- Not included: Timeout, cancel, process exit, or learner-facing rendering.
- Exit condition: Known, unknown, and malformed-known event fixtures pass.

<a id="kiko-042b"></a>
### KIKO-042B — Terminate timeout, cancel, and process-exit paths

- Checkpoint kind: implementation
- Observable outcome: Every pending operation reaches one bounded terminal result on timeout, cancel, completion, error, or child exit.
- Why it matters: CLI and extension must never wait forever or complete a request twice.
- Prerequisites: KIKO-042A.
- Known concepts: Pending requests, event handlers, process lifetime, and controlled errors.
- New concepts and syntax: Deadline state, cancellation token, and terminal-state guard.
- Learner task: Add one terminal-state transition function and scripted terminal fixtures.
- Verification: `.venv/bin/python -m unittest tests.integration.test_app_server_events.TerminalTests -v`
- Expected behavior: Each path resolves once, cleans pending state, and ignores late events.
- Edge case: Process exit during cancellation reports one deterministic terminal cause.
- Not included: Automatic retry policy or UI presentation.
- Exit condition: Complete, error, timeout, cancel, process-exit, and late-event fixtures pass.

<a id="kiko-043"></a>
### KIKO-043 — Complete one validated read-only tutoring turn

- Checkpoint kind: integration
- Observable outcome: A bounded expert request produces one validated TutorInteraction through live/fake adapter parity.
- Why it matters: This is the first repository-aware teaching value delivered through Codex.
- Prerequisites: KIKO-026A, KIKO-027F, KIKO-035, and KIKO-042B.
- Known concepts: Bounded context, expert contracts, event collection, and result validation.
- New concepts and syntax: Structured output schema and turn completion aggregation.
- Learner task: Start one tutoring turn and validate the completed expert proposal before presentation.
- Verification: `.venv/bin/python -m unittest tests.integration.test_codex_tutoring_turn -v`
- Expected behavior: Valid result renders; missing fields, approval request, unsafe action, and incomplete turn are rejected.
- Edge case: Proposed evidence remains inert until a later learner-authored review passes.
- Not included: Planning turns, extension UI, or source edits.
- Exit condition: Fake protocol tests pass and one optional authenticated smoke check completes read-only.

<a id="kiko-044"></a>
### KIKO-044 — Generate one live candidate plan

- Checkpoint kind: implementation
- Observable outcome: A confirmed brief produces one structured, non-canonical candidate plan through Codex.
- Why it matters: Product planning must use model reasoning without surrendering readiness, coverage, or acceptance control.
- Prerequisites: KIKO-034C, KIKO-038B, and KIKO-042B.
- Known concepts: Multi-stage fake planning, structured outputs, validation, and acceptance states.
- New concepts and syntax: Planning-purpose turn and candidate-version correlation.
- Learner task: Send the confirmed brief and validate one returned candidate plan.
- Verification: `.venv/bin/python -m unittest tests.integration.test_codex_planning_flow.CandidateTurnTests -v`
- Expected behavior: Valid candidate remains pending; invalid/provider-failure output leaves accepted plan unchanged.
- Edge case: Candidate cannot mark its own brief or plan as user-accepted.
- Not included: Writing Tutor project files before acceptance.
- Exit condition: Valid, invalid, provider-failure, and acceptance-boundary candidate fixtures pass.

<a id="kiko-044a"></a>
### KIKO-044A — Run one live plan critique turn

- Checkpoint kind: integration
- Observable outcome: A separate Codex turn returns structured findings against the confirmed brief and coverage budget.
- Why it matters: Live plan quality needs an independent purpose and validated finding schema.
- Prerequisites: KIKO-044.
- Known concepts: Candidate plan, fake critique, expert turns, and coverage validators.
- New concepts and syntax: Critique-specific structured output schema.
- Learner task: Send one candidate for critique and validate the returned findings without changing it.
- Verification: `.venv/bin/python -m unittest tests.integration.test_codex_planning_flow.CritiqueTurnTests -v`
- Expected behavior: Findings map to checkpoint/requirement IDs; scope-expansion proposals remain flagged.
- Edge case: Malformed critique blocks repair and preserves both confirmed brief and accepted plan.
- Not included: Applying repairs or asking the user new questions.
- Exit condition: Valid, malformed, missing-ID, and scope-expansion critique fixtures pass.

<a id="kiko-044b"></a>
### KIKO-044B — Repair or reopen a live plan candidate

- Checkpoint kind: integration
- Observable outcome: Critique produces a revalidated candidate or reopens one blocking decision before plan review.
- Why it matters: Codex may improve implementation detail but cannot invent unresolved product facts.
- Prerequisites: KIKO-044A.
- Known concepts: Critique findings, fake repair, discovery blockers, validation, and candidate lineage.
- New concepts and syntax: Repair-purpose turn and affected-section mapping.
- Learner task: Process one repair response and one ambiguity response through the correct branch.
- Verification: `.venv/bin/python -m unittest tests.integration.test_codex_planning_flow.RepairTurnTests -v`
- Expected behavior: Repaired valid plan reaches user review; ambiguity returns to discovery with confirmed answers intact.
- Edge case: Cancel/provider failure preserves the last accepted plan and discards only the pending repair.
- Not included: Writing project files before final plan acceptance.
- Exit condition: Repair, revalidation, ambiguity, cancel, and provider-failure fixtures pass.

<a id="kiko-045"></a>
### KIKO-045 — Defend the expert boundary from unsafe repository content

- Checkpoint kind: integration
- Observable outcome: Only safe selected files reach Codex as quoted data under immutable Tutor policy.
- Why it matters: Repository content can contain prompt injection, secrets, symlink escapes, and misleading instructions.
- Prerequisites: KIKO-018C, KIKO-026A, KIKO-035, and KIKO-043.
- Known concepts: Repository safety policy, bounded context, redaction, and read-only expert contracts.
- New concepts and syntax: Trust labels, content delimiters, secret-pattern filtering, and provenance metadata.
- Learner task: Compose one expert request that preserves policy priority and rejects unsafe fixture content.
- Verification: `.venv/bin/python -m unittest tests.security.test_expert_boundary -v`
- Expected behavior: Safe file data is labeled; injected instructions cannot alter policy; secrets/outside paths are excluded.
- Edge case: A necessary file containing suspected secret material blocks with an explanation instead of silent partial disclosure.
- Not included: Executing repository commands or claiming perfect secret detection.
- Exit condition: Prompt-injection, secret, symlink, oversized-file, and policy-override fixtures pass.
