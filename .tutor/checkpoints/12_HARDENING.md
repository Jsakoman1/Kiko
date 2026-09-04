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
- Prerequisites: KIKO-016B and KIKO-059A.
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
### KIKO-069 — Upgrade supported state and protocol versions

- Checkpoint kind: implementation
- Observable outcome: Packaged Kiko applies the supported migration chain and validates the resulting state/protocol version.
- Why it matters: Product updates must preserve learning history and avoid incompatible silent corruption.
- Prerequisites: KIKO-016B, KIKO-017A, KIKO-066, and KIKO-068A.
- Known concepts: Versioned migrations, backups, artifacts, and compatibility errors.
- New concepts and syntax: Ordered migration chain and post-migration contract validation.
- Learner task: Upgrade one prior-version project/learner/protocol fixture through supported transitions.
- Verification: `.venv/bin/python -m unittest tests.e2e.test_upgrade_recovery.SupportedUpgradeTests -v`
- Expected behavior: Supported upgrade preserves all owners and reaches current validated versions.
- Edge case: Project, learner, reference, feedback, session, and protocol versions remain independently owned.
- Not included: Cloud migrations or indefinite support for every historical version.
- Exit condition: Direct/current, one-step, multi-step, and independently versioned owner fixtures pass.

<a id="kiko-069a"></a>
### KIKO-069A — Roll back failed migration and protect downgrades

- Checkpoint kind: integration
- Observable outcome: Failed upgrade restores validated backups; unsupported future/downgrade paths require safe export guidance.
- Why it matters: Upgrade failure must not destroy history or encourage unsafe backward writes.
- Prerequisites: KIKO-069.
- Known concepts: Migration chain, backups, atomic state, exports, and error recovery.
- New concepts and syntax: Rollback receipt and downgrade compatibility guard.
- Learner task: Simulate invalid migration, future version, and downgrade attempt against isolated profiles.
- Verification: `.venv/bin/python -m unittest tests.e2e.test_upgrade_recovery.RollbackDowngradeTests -v`
- Expected behavior: Failure restores all touched owners; unsupported paths remain untouched and explain export/upgrade options.
- Edge case: Partial multi-owner migration restores every owner or reports an unrecoverable block without continuing.
- Not included: Indefinite support for every historical version or cloud recovery.
- Exit condition: Invalid migration, partial failure, rollback, future version, and downgrade/export fixtures pass.

<a id="kiko-070"></a>
### KIKO-070 — Establish the supported compatibility matrix

- Checkpoint kind: integration
- Observable outcome: Release documents and doctor enforce tested macOS architecture, VS Code, and Codex CLI ranges.
- Why it matters: Unsupported combinations must fail before a tutoring turn, not unpredictably during it.
- Prerequisites: KIKO-057, KIKO-063, KIKO-065, and KIKO-069A.
- Known concepts: Version checks, artifacts, clean profiles, and diagnostics.
- New concepts and syntax: Compatibility matrix fixtures and minimum/maximum capability gates.
- Learner task: Define supported combinations and test one supported and one rejected combination per boundary.
- Verification: `make compatibility-check`
- Expected behavior: Supported matrix passes; unsupported versions produce exact update/downgrade guidance.
- Edge case: Newer unknown Codex protocol is blocked until adapter compatibility smoke passes.
- Not included: Windows/Linux or non-VS Code editor support.
- Exit condition: Matrix, doctor, package metadata, and release notes agree on supported versions.

<a id="kiko-071"></a>
### KIKO-071 — Bound context size and estimated model cost

- Checkpoint kind: implementation
- Observable outcome: Kiko enforces context/message/token-estimate budgets and reports why a turn cannot safely proceed.
- Why it matters: A local Tutor must stay responsive, affordable, private, and predictable on realistic repositories.
- Prerequisites: KIKO-026, KIKO-045, and KIKO-056.
- Known concepts: Bounded context, message limits, safe file selection, and controlled errors.
- New concepts and syntax: Budget configuration and conservative token/cost estimation.
- Learner task: Enforce one context/token estimate limit before starting a provider turn.
- Verification: `.venv/bin/python -m unittest tests.performance.test_product_budgets.ContextCostTests -v`
- Expected behavior: Within-budget fixture succeeds; oversize/high-estimate case stops with actionable reduction guidance.
- Edge case: Unknown provider price is labeled unknown rather than guessed as exact cost.
- Not included: Guaranteed provider pricing, analytics telemetry, or unbounded automatic retries.
- Exit condition: Context, message, token-estimate, cost-known/unknown, and reduction-guidance fixtures pass.

<a id="kiko-071a"></a>
### KIKO-071A — Measure and bound latency and memory

- Checkpoint kind: integration
- Observable outcome: Startup, first response, active turn, and shutdown have measured latency/memory targets.
- Why it matters: A local sidebar must remain responsive on small and realistic repositories.
- Prerequisites: KIKO-042B, KIKO-056, KIKO-068A, and KIKO-071.
- Known concepts: Process lifecycle, realistic fixtures, timeouts, and performance targets.
- New concepts and syntax: Monotonic timing and child-process memory sampling.
- Learner task: Measure one fake/live-safe lifecycle scenario and enforce documented warning/failure thresholds.
- Verification: `.venv/bin/python -m unittest tests.performance.test_product_budgets.LatencyMemoryTests -v`
- Expected behavior: Baseline fixtures stay within target; simulated slow/high-memory fixture reports the breached metric.
- Edge case: Environment variance is separated from deterministic hard timeout behavior.
- Not included: Provider speed guarantees or broad benchmarking platform.
- Exit condition: Small/realistic repository, slow, high-memory, and shutdown-target fixtures produce reproducible reports.

<a id="kiko-071b"></a>
### KIKO-071B — Bound retries and retained logs

- Checkpoint kind: implementation
- Observable outcome: Retry count/backoff and sanitized local diagnostic-log retention have explicit finite limits.
- Why it matters: Recovery must not loop indefinitely or retain private learning/source data.
- Prerequisites: KIKO-059A, KIKO-068A, and KIKO-071A.
- Known concepts: Error taxonomy, recovery actions, sanitization, user data control, and local budgets.
- New concepts and syntax: Retry policy and retention/rotation rule.
- Learner task: Enforce one bounded retry policy and one sanitized age/size-based log cleanup.
- Verification: `.venv/bin/python -m unittest tests.performance.test_product_budgets.RetryLogTests -v`
- Expected behavior: Retry stops at limit; logs exclude forbidden content and remove only expired/oversized diagnostic entries.
- Edge case: Cleanup never deletes learner/profile/reference/project state.
- Not included: Remote telemetry, raw prompts/source logging, or unlimited automatic retry.
- Exit condition: Retry, backoff, sanitization, size/age retention, and owner-preservation fixtures pass.
