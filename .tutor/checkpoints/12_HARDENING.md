# Phase 12 — Security, Compatibility, and Lifecycle Hardening

<a id="kiko-067"></a>
### KIKO-067 — Enforce the read-only learning boundary

- Checkpoint kind: integration
- Observable outcome: Help/review/planning cannot authorize source edits, shell writes, or unsafe approval flows.
- Why it matters: Learner authorship is the central product guarantee.
- Prerequisites: KIKO-045, KIKO-056, and KIKO-062.
- Known concepts: Expert contracts, repository trust, approval errors, and end-to-end tests.
- New concepts and syntax: Capability denylist/allowlist and invariant tests over file hashes.
- Learner task: Add a security scenario that snapshots source and rejects every unexpected write/approval proposal.
- Verification: `.venv/bin/python -m unittest tests.security.test_read_only_invariant -v`
- Expected behavior: All supported interactions leave learner source unchanged; unsafe requests become blocked errors.
- Edge case: Tutor-owned project/learner state updates remain allowed only through documented transactions.
- Not included: Sandboxing arbitrary third-party tools or automatic source fixes.
- Exit condition: Source-hash, approval, path, and Tutor-owned-state invariants pass.

<a id="kiko-068"></a>
### KIKO-068 — Prevent concurrent state writers

- Checkpoint kind: implementation
- Observable outcome: Only one Kiko process writes a state owner at a time and stale locks recover safely.
- Why it matters: Concurrent CLI/extension instances must not interleave or lose learning history.
- Prerequisites: KIKO-016C and KIKO-059A.
- Known concepts: Atomic files, state owners, process IDs, and controlled recovery.
- New concepts and syntax: File lock, lock metadata, and stale-lock validation.
- Learner task: Protect one state transaction with a lock and simulate a competing/stale writer.
- Verification: `.venv/bin/python -m unittest tests.integration.test_process_lifecycle.StateLockTests -v`
- Expected behavior: First writer succeeds; competitor waits/fails clearly; verified stale lock is recoverable.
- Edge case: Stale lock after a crash is detected and recoverable without deleting valid state.
- Not included: Multi-user collaboration or distributed locking.
- Exit condition: First-writer, competing-writer, stale-lock, live-lock, and valid-state-preservation fixtures pass.

<a id="kiko-068a"></a>
### KIKO-068A — Cancel and shut down the full process tree

- Checkpoint kind: integration
- Observable outcome: Cancel, CLI exit, extension reload, and window close terminate pending requests and owned child processes once.
- Why it matters: Product lifecycle must not leak Codex/Core processes or hanging operations.
- Prerequisites: KIKO-042B, KIKO-052B, and KIKO-068.
- Known concepts: Cancellation, terminal guards, process disposal, locks, and recoverable errors.
- New concepts and syntax: Signal propagation and bounded process-tree shutdown sequence.
- Learner task: Add one shutdown coordinator and verify process/request/lock cleanup.
- Verification: `.venv/bin/python -m unittest tests.integration.test_process_lifecycle.ShutdownTests -v`
- Expected behavior: Each close path terminates within target and repeated close is idempotent.
- Edge case: Child ignores graceful stop and reaches bounded forced termination without corrupting state.
- Not included: Unowned system processes or distributed workers.
- Exit condition: Cancel, exit, reload, graceful timeout, forced stop, and repeated-close fixtures pass.

<a id="kiko-069"></a>
### KIKO-069 — Upgrade supported state-owner versions

- Checkpoint kind: implementation
- Observable outcome: Packaged Kiko applies supported migration chains to each touched state owner and validates the results.
- Why it matters: Product updates must preserve learning history and avoid incompatible silent corruption.
- Prerequisites: KIKO-016C, KIKO-017C, KIKO-066, and KIKO-068A.
- Known concepts: Versioned migrations, backups, artifacts, and compatibility errors.
- New concepts and syntax: Multi-owner migration order and post-migration contract validation.
- Learner task: Upgrade prior-version project/learner/session/feedback fixtures through their supported transitions.
- Verification: `.venv/bin/python -m unittest tests.e2e.test_upgrade_recovery.StateOwnerUpgradeTests -v`
- Expected behavior: Supported upgrade preserves each owner and reaches its current validated schema version.
- Edge case: Project, learner, reference, feedback, session, and protocol versions remain independently owned.
- Not included: Protocol negotiation, rollback, downgrade, cloud migrations, or indefinite historical support.
- Exit condition: Current, one-step, multi-step, and independently versioned state-owner fixtures pass.

<a id="kiko-069a"></a>
### KIKO-069A — Upgrade the supported local protocol

- Checkpoint kind: implementation
- Observable outcome: Extension and Core negotiate one supported older protocol into the current request/event contract.
- Why it matters: Protocol compatibility is independent from persisted state migration.
- Prerequisites: KIKO-069.
- Known concepts: Versioned JSONL messages, compatibility errors, packaged Core/extension, and validation.
- New concepts and syntax: Protocol-version negotiation and supported-adapter selection.
- Learner task: Accept one supported older protocol fixture and map it to current internal messages.
- Verification: `.venv/bin/python -m unittest tests.e2e.test_upgrade_recovery.ProtocolUpgradeTests -v`
- Expected behavior: Current/one-supported-old protocol works; unsupported version blocks before a turn.
- Edge case: State-owner versions remain independent from protocol version.
- Not included: State migration, downgrade writes, or rollback.
- Exit condition: Current, supported-old, unsupported-old, future, and owner-independence fixtures pass.

<a id="kiko-069b"></a>
### KIKO-069B — Roll back a failed multi-owner migration

- Checkpoint kind: integration
- Observable outcome: A failed packaged upgrade restores validated backups for every touched state owner.
- Why it matters: Upgrade failure must not destroy history or encourage unsafe backward writes.
- Prerequisites: KIKO-069A.
- Known concepts: Migration chain, backups, atomic state, exports, and error recovery.
- New concepts and syntax: Multi-owner rollback receipt.
- Learner task: Simulate one invalid/partial migration and restore every touched owner from validated backups.
- Verification: `.venv/bin/python -m unittest tests.e2e.test_upgrade_recovery.RollbackTests -v`
- Expected behavior: Failure restores all touched owners or reports an unrecoverable block without continuing.
- Edge case: Partial multi-owner migration restores every owner or reports an unrecoverable block without continuing.
- Not included: Future-version/downgrade policy, indefinite historical support, or cloud recovery.
- Exit condition: Invalid migration, partial failure, complete rollback, invalid backup, and no-continue fixtures pass.

<a id="kiko-069c"></a>
### KIKO-069C — Protect future-version and downgrade paths

- Checkpoint kind: integration
- Observable outcome: Unsupported future state/protocol and downgrade attempts remain untouched and return safe export/upgrade guidance.
- Why it matters: Older Kiko must not silently rewrite data created by a newer incompatible release.
- Prerequisites: KIKO-069B.
- Known concepts: Version validation, backups, rollback, exports, compatibility errors, and packaged artifacts.
- New concepts and syntax: Downgrade write guard and compatibility receipt.
- Learner task: Reject future-version and downgrade fixtures without mutating any owner.
- Verification: `.venv/bin/python -m unittest tests.e2e.test_upgrade_recovery.DowngradeGuardTests -v`
- Expected behavior: Unsupported paths remain byte-for-byte unchanged and explain supported export/upgrade options.
- Edge case: Mixed current/future owners block the whole write transaction while remaining inspectable/exportable.
- Not included: Supporting every historical version or cloud recovery.
- Exit condition: Future state, future protocol, downgrade, mixed-owner, export-guidance, and no-write fixtures pass.

<a id="kiko-070"></a>
### KIKO-070 — Establish the supported compatibility matrix

- Checkpoint kind: integration
- Observable outcome: Release documents and doctor enforce tested macOS architecture, VS Code, and Codex CLI ranges.
- Why it matters: Unsupported combinations must fail before a tutoring turn, not unpredictably during it.
- Prerequisites: KIKO-057, KIKO-063, KIKO-065, and KIKO-069C.
- Known concepts: Version checks, artifacts, clean profiles, and diagnostics.
- New concepts and syntax: Compatibility matrix fixtures and minimum/maximum capability gates.
- Learner task: Define supported combinations and test one supported and one rejected combination per boundary.
- Verification: `make compatibility-check`
- Expected behavior: Supported matrix passes; unsupported versions produce exact update/downgrade guidance.
- Edge case: Newer unknown Codex protocol is blocked until adapter compatibility smoke passes.
- Not included: Windows/Linux or non-VS Code editor support.
- Exit condition: Matrix, doctor, package metadata, and release notes agree on supported versions.

<a id="kiko-071"></a>
### KIKO-071 — Bound context and token estimates

- Checkpoint kind: implementation
- Observable outcome: Kiko enforces context/message/token-estimate budgets before starting a provider turn.
- Why it matters: A local Tutor must stay responsive, affordable, private, and predictable on realistic repositories.
- Prerequisites: KIKO-026A, KIKO-045, and KIKO-056.
- Known concepts: Bounded context, message limits, safe file selection, and controlled errors.
- New concepts and syntax: Budget configuration and conservative token estimation.
- Learner task: Enforce one context/token estimate limit before starting a provider turn.
- Verification: `.venv/bin/python -m unittest tests.performance.test_product_budgets.ContextCostTests -v`
- Expected behavior: Within-budget fixture succeeds; oversize/high-token-estimate case stops with reduction guidance.
- Edge case: Structured fields are never silently cut in the middle to fit the budget.
- Not included: Price/cost reporting, analytics, latency/memory, or retries.
- Exit condition: Context, message, token-estimate, structured-boundary, and reduction-guidance fixtures pass.

<a id="kiko-071a"></a>
### KIKO-071A — Report estimated model cost conservatively

- Checkpoint kind: implementation
- Observable outcome: A provider turn reports an estimated cost range when pricing is known and `unknown` when it is not.
- Why it matters: Cost transparency must not present a guess as an exact current price.
- Prerequisites: KIKO-071.
- Known concepts: Token estimates, provider metadata, controlled unknown values, and budget errors.
- New concepts and syntax: Versioned pricing input and estimated-cost range.
- Learner task: Calculate/display a conservative estimate from injected pricing data without fetching live prices.
- Verification: `.venv/bin/python -m unittest tests.performance.test_product_budgets.CostEstimateTests -v`
- Expected behavior: Known injected price produces a labeled estimate range; missing/stale price reports unknown.
- Edge case: Estimate never blocks a turn solely because pricing metadata is unavailable.
- Not included: Live price lookup, guaranteed billing, telemetry, latency, or memory.
- Exit condition: Known, unknown, stale, range-label, and non-blocking fixtures pass.

<a id="kiko-071b"></a>
### KIKO-071B — Measure and bound lifecycle latency

- Checkpoint kind: integration
- Observable outcome: Startup, first response, active fake turn, and shutdown have measured latency targets.
- Why it matters: A local sidebar must remain responsive on small and realistic repositories.
- Prerequisites: KIKO-042B, KIKO-056, KIKO-068A, and KIKO-071A.
- Known concepts: Process lifecycle, realistic fixtures, timeouts, and performance targets.
- New concepts and syntax: Monotonic timing and latency threshold report.
- Learner task: Measure one deterministic fake lifecycle and enforce documented warning/failure thresholds.
- Verification: `.venv/bin/python -m unittest tests.performance.test_product_budgets.LatencyTests -v`
- Expected behavior: Baseline stays within target; simulated slow stage reports its exact breached metric.
- Edge case: Environment variance is separated from deterministic hard timeout behavior.
- Not included: Memory sampling, provider speed guarantees, or a broad benchmarking platform.
- Exit condition: Startup, first-response, active-turn, slow-stage, and shutdown fixtures produce reproducible reports.

<a id="kiko-071c"></a>
### KIKO-071C — Measure and bound process memory

- Checkpoint kind: integration
- Observable outcome: Core and owned Codex child-process memory are sampled against documented warning/failure targets.
- Why it matters: A local sidebar must not consume unbounded memory on realistic repositories.
- Prerequisites: KIKO-071B.
- Known concepts: Owned processes, realistic fixtures, performance thresholds, and reproducible reports.
- New concepts and syntax: Child-process memory sampling and aggregate-memory report.
- Learner task: Measure one deterministic process scenario and report the process that breaches its target.
- Verification: `.venv/bin/python -m unittest tests.performance.test_product_budgets.MemoryTests -v`
- Expected behavior: Baseline stays within target; simulated high-memory process reports the exact breach.
- Edge case: Unsupported sampling environment reports `not measured` rather than fabricated success.
- Not included: Latency, provider guarantees, or broad benchmarking.
- Exit condition: Core, child, aggregate, high-memory, and unsupported-sampler fixtures pass.

<a id="kiko-071d"></a>
### KIKO-071D — Bound automatic retries

- Checkpoint kind: implementation
- Observable outcome: Automatic retry count and backoff have explicit finite limits per recoverable operation.
- Why it matters: Recovery must not loop indefinitely or duplicate requests/processes.
- Prerequisites: KIKO-059A, KIKO-068A, and KIKO-071C.
- Known concepts: Error taxonomy, recovery actions, sanitization, user data control, and local budgets.
- New concepts and syntax: Retry-attempt budget and bounded backoff schedule.
- Learner task: Enforce one retry policy for controlled recoverable errors.
- Verification: `.venv/bin/python -m unittest tests.performance.test_product_budgets.RetryTests -v`
- Expected behavior: Eligible failures retry within limit; non-retryable/limit cases stop with one terminal result.
- Edge case: Retry cannot duplicate an already terminal request or state write.
- Not included: Diagnostic logs, telemetry, or unlimited automatic retry.
- Exit condition: Retryable, non-retryable, limit, backoff, and no-duplicate fixtures pass.

<a id="kiko-071e"></a>
### KIKO-071E — Sanitize and bound retained diagnostic logs

- Checkpoint kind: implementation
- Observable outcome: Local diagnostic logs use an allowlist and finite age/size retention without touching user state.
- Why it matters: Diagnostics must not retain private prompts/source indefinitely or delete canonical learning data.
- Prerequisites: KIKO-071D.
- Known concepts: Sanitization, owner boundaries, size/age budgets, paths, and atomic cleanup.
- New concepts and syntax: Diagnostic-log retention/rotation rule.
- Learner task: Sanitize log entries and remove only expired/oversized diagnostic log files.
- Verification: `.venv/bin/python -m unittest tests.performance.test_product_budgets.DiagnosticLogTests -v`
- Expected behavior: Allowed metadata remains; forbidden content is absent; cleanup respects age/size limits.
- Edge case: Cleanup never deletes learner, reference, project, feedback, or session state.
- Not included: Remote telemetry or raw prompt/source logging.
- Exit condition: Sanitization, age, size, rotation, and owner-preservation fixtures pass.
