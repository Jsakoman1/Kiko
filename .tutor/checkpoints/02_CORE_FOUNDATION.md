# Phase 2 — Maintainable Core Foundation

<a id="kiko-012"></a>
### KIKO-012 — Create an isolated Python development environment

- Checkpoint kind: implementation
- Observable outcome: Kiko development commands run through a project-local `.venv`.
- Why it matters: Later dependencies and tests must not modify or depend on global Python packages.
- Prerequisites: KIKO-011.
- Known concepts: Python execution, paths, and terminal commands.
- New concepts and syntax: `python3 -m venv`, isolated interpreters, and `.venv/bin/python`.
- Learner task: Create `.venv` and verify that its Python executable is used.
- Verification: Run `python3 -m venv .venv`, then `.venv/bin/python --version`.
- Expected behavior: The local interpreter runs and no package is installed into system Python.
- Edge case: Recreating an existing `.venv` is not used as a destructive recovery action.
- Not included: Package metadata, source moves, dependencies, or CLI entry points.
- Exit condition: A local isolated Python interpreter is available for all later development commands.

<a id="kiko-012a"></a>
### KIKO-012A — Migrate existing CLI behavior into the package

- Checkpoint kind: implementation
- Observable outcome: Existing CLI behavior runs from an editable `kiko` package.
- Why it matters: State, policy, providers, and protocol need separate testable modules before complexity grows.
- Prerequisites: KIKO-012.
- Known concepts: Modules, imports, functions, `.venv`, paths, and CLI execution.
- New concepts and syntax: `pyproject.toml`, packages, `__main__.py`, and console entry points.
- Learner task: Create the package skeleton and move existing behavior without changing output.
- Verification: Run `.venv/bin/python -m pip install -e .`, then `.venv/bin/kiko show`.
- Expected behavior: Editable install succeeds and packaged `show` matches the previous script behavior.
- Edge case: `.venv/bin/python -m kiko show` and `.venv/bin/kiko show` use the same entry function.
- Not included: Policy refactoring, App Server code, extension code, or release packaging.
- Exit condition: All previously verified CLI behavior passes through the package entry point.

<a id="kiko-013"></a>
### KIKO-013 — Separate development progress from runtime project state

- Checkpoint kind: implementation
- Observable outcome: Documentation identifies Kiko-development progress separately from a future learner project's runtime checkpoint.
- Why it matters: The current plan says KIKO-011 while the prototype JSON previously displayed Step 2; two meanings cannot share one authority.
- Prerequisites: KIKO-012A.
- Known concepts: Nested state, project-local files, and ownership boundaries.
- New concepts and syntax: Separate domain models and derived display values.
- Learner task: Adjust the runtime state model and `show` labels so they cannot claim to be the development roadmap authority.
- Verification: `.venv/bin/kiko show`
- Expected behavior: Output clearly labels runtime/demo checkpoint data and the development handoff remains owned by `LEARNING_PLAN.md`.
- Edge case: Deleting runtime state recreates defaults without changing development progress.
- Not included: Parsing Markdown as a runtime API or automatically editing the development plan.
- Exit condition: No field or label ambiguously represents both progress domains.

<a id="kiko-014"></a>
### KIKO-014 — Establish an isolated development and test environment

- Checkpoint kind: implementation
- Observable outcome: Built-in tests run inside `.venv` with temporary project/global directories and never touch the real learner profile.
- Why it matters: Every later behavior needs repeatable verification without risking private state or global Python packages.
- Prerequisites: KIKO-012A and KIKO-013.
- Known concepts: Local `.venv`, functions, paths, JSON fixtures, and command verification.
- New concepts and syntax: `unittest`, `TemporaryDirectory`, setup/cleanup, and test assertions.
- Learner task: Add the first isolated state test with a temporary learner directory.
- Verification: `.venv/bin/python -m unittest discover -s tests -v`
- Expected behavior: The test passes using `.venv` and reports a temporary path rather than the real Application Support path.
- Edge case: Test failure still cleans up temporary files and does not alter global learner data.
- Not included: State-schema validation, live Codex, or VS Code integration tests.
- Exit condition: One repeatable test command proves environment and user-data isolation.

<a id="kiko-015"></a>
### KIKO-015 — Define and validate the project-state contract

- Checkpoint kind: implementation
- Observable outcome: Project runtime state is validated against one explicit versioned contract.
- Why it matters: Invalid or future data must fail safely before Kiko writes or acts on it.
- Prerequisites: KIKO-014.
- Known concepts: Dictionaries, JSON, versions, explicit conditions, and isolated tests.
- New concepts and syntax: Typed data boundaries, validation functions, and domain-specific exceptions.
- Learner task: Validate project-state required fields/types/version and return a controlled error.
- Verification: `.venv/bin/python -m unittest tests.test_state_contracts.ProjectStateTests -v`
- Expected behavior: Valid project state loads; malformed and unsupported-version fixtures fail clearly.
- Edge case: Unknown non-conflicting fields remain preserved for forward compatibility.
- Not included: Automatic migration or UI error rendering.
- Exit condition: Project-state valid, missing-field, wrong-type, unknown-field, and future-version fixtures pass.

<a id="kiko-015a"></a>
### KIKO-015A — Apply state contracts to every remaining owner

- Checkpoint kind: integration
- Observable outcome: Learner, session, and Tutor-feedback state each validate through their own versioned contract.
- Why it matters: Separate owners need explicit schemas without one giant mixed state model.
- Prerequisites: KIKO-015.
- Known concepts: Project-state validator, versions, controlled errors, and isolated fixtures.
- New concepts and syntax: Reusable field validators and owner-specific contract composition.
- Learner task: Apply the established validation pattern to learner, session, and feedback fixtures.
- Verification: `.venv/bin/python -m unittest tests.test_state_contracts.RemainingOwnerTests -v`
- Expected behavior: Each owner accepts its valid shape and rejects another owner's fields or unsupported version.
- Edge case: One invalid owner does not rewrite or invalidate unrelated valid files.
- Not included: Migration, persistence, or UI error rendering.
- Exit condition: Learner, session, feedback, cross-owner, and independent-version fixtures pass.

<a id="kiko-016"></a>
### KIKO-016 — Write state through atomic replacement

- Checkpoint kind: implementation
- Observable outcome: One JSON update completes fully or leaves the previous file unchanged.
- Why it matters: Interrupted writes must not create partial state.
- Prerequisites: KIKO-014 and KIKO-015A.
- Known concepts: JSON serialization, paths, versions, and isolated tests.
- New concepts and syntax: Temporary files, flush/close ordering, and atomic `Path.replace`.
- Learner task: Implement atomic replacement for one injected project-state path.
- Verification: `.venv/bin/python -m unittest tests.test_state_persistence.AtomicWriteTests -v`
- Expected behavior: Normal write replaces the file; serialization/interruption fixture preserves old valid state.
- Edge case: Temporary output is cleaned after a failed pre-replacement write.
- Not included: Cross-process locking, which belongs to KIKO-068.
- Exit condition: Successful and interrupted atomic-write fixtures pass.

<a id="kiko-016a"></a>
### KIKO-016A — Preserve a recoverable state backup

- Checkpoint kind: implementation
- Observable outcome: A valid previous state remains recoverable before replacement or migration.
- Why it matters: Users need a safe restoration point when a later write or migration is invalid.
- Prerequisites: KIKO-016.
- Known concepts: Atomic writes, paths, validation, and isolated fixtures.
- New concepts and syntax: Backup naming, copy semantics, and backup validation.
- Learner task: Preserve and validate one previous-state backup before replacing it.
- Verification: `.venv/bin/python -m unittest tests.test_state_persistence.BackupTests -v`
- Expected behavior: Valid prior state is copied once and can be restored; invalid current data is not promoted to backup.
- Edge case: Existing valid backup is not silently overwritten by corrupt state.
- Not included: Schema transformation or concurrent writer locks.
- Exit condition: Create, preserve, reject-corrupt, and restore backup fixtures pass.

<a id="kiko-016b"></a>
### KIKO-016B — Migrate supported state schema versions

- Checkpoint kind: implementation
- Observable outcome: One supported old schema migrates to the current schema after backup and validation.
- Why it matters: Kiko upgrades must preserve learner/project history without accepting unknown future formats.
- Prerequisites: KIKO-016A.
- Known concepts: Version validation, atomic writes, backups, and pure functions.
- New concepts and syntax: Migration functions and ordered schema-version transitions.
- Learner task: Implement one old-to-current migration and validate before atomic replacement.
- Verification: `.venv/bin/python -m unittest tests.test_state_persistence.MigrationTests -v`
- Expected behavior: Supported old state migrates; invalid result restores old data; future version is untouched and rejected.
- Edge case: Running migration on current state makes no duplicate change.
- Not included: Downgrade support or multi-process locking.
- Exit condition: Current, supported-old, invalid-migration, and future-version fixtures pass.

<a id="kiko-017"></a>
### KIKO-017 — Define the versioned JSONL request/result envelope

- Checkpoint kind: implementation
- Observable outcome: One request and its success result use an explicit versioned JSONL envelope with matching ID.
- Why it matters: The extension must depend on a stable process contract rather than Python internals.
- Prerequisites: KIKO-015A.
- Known concepts: JSON dictionaries, request/result boundaries, and versioning.
- New concepts and syntax: JSON Lines framing, request IDs, and tagged request/result messages.
- Learner task: Define and validate one request/result round trip independent of transport.
- Verification: `.venv/bin/python -m unittest tests.test_local_protocol -v`
- Expected behavior: Valid request/result round-trip; malformed, mismatched-ID, and unknown-version envelopes fail clearly.
- Edge case: Extra optional result metadata is preserved/ignored according to the contract.
- Not included: Starting a subprocess or implementing VS Code transport.
- Exit condition: Request, result, malformed, mismatched-ID, and version fixtures pass.

<a id="kiko-017a"></a>
### KIKO-017A — Define protocol error, progress, and cancel events

- Checkpoint kind: implementation
- Observable outcome: Error, progress, cancel request, and cancelled result use tagged shapes tied to one request ID.
- Why it matters: Long-running Core work needs explicit non-success lifecycle messages before extension transport.
- Prerequisites: KIKO-017.
- Known concepts: Versioned JSONL envelope, request IDs, tagged messages, and state contracts.
- New concepts and syntax: Progress notification and terminal cancellation message semantics.
- Learner task: Define/validate one error, progress, cancel, and cancelled message family.
- Verification: `.venv/bin/python -m unittest tests.test_local_protocol.LifecycleMessageTests -v`
- Expected behavior: Valid lifecycle messages correlate; invalid terminal/progress combinations fail precisely.
- Edge case: Progress after terminal result is rejected/ignored and cannot reopen a request.
- Not included: Process transport, timeout policy, or UI rendering.
- Exit condition: Error, progress, cancel, cancelled, invalid-order, and unknown-tag fixtures pass.

<a id="kiko-018"></a>
### KIKO-018 — Enforce workspace file containment

- Checkpoint kind: implementation
- Observable outcome: Kiko accepts only readable regular files whose resolved paths remain inside the selected workspace.
- Why it matters: A repository request must not escape into unrelated local files.
- Prerequisites: KIKO-014 and KIKO-015A.
- Known concepts: `Path`, project boundaries, validation, and read-only policy.
- New concepts and syntax: `Path.resolve`, containment checks, regular-file checks, and symlink escape reasoning.
- Learner task: Validate one requested path against the resolved workspace root.
- Verification: `.venv/bin/python -m unittest tests.test_repository_safety.PathContainmentTests -v`
- Expected behavior: Normal in-workspace files pass; outside, directory, missing, and escaping-symlink paths fail.
- Edge case: A symlink located inside the workspace but targeting outside remains rejected.
- Not included: Operating-system sandboxing or automatic source execution.
- Exit condition: All containment fixtures pass before file contents can be read.

<a id="kiko-018a"></a>
### KIKO-018A — Filter secret and oversized repository content

- Checkpoint kind: implementation
- Observable outcome: Selected files are blocked/redacted by explicit secret and size policies before context compilation.
- Why it matters: Valid workspace paths may still contain credentials or impractically large content.
- Prerequisites: KIKO-018.
- Known concepts: Safe paths, file reading, allow/deny rules, and controlled errors.
- New concepts and syntax: Size limits, filename/content secret heuristics, and redaction findings.
- Learner task: Apply one bounded content filter to already safe file paths.
- Verification: `.venv/bin/python -m unittest tests.test_repository_safety.ContentFilterTests -v`
- Expected behavior: Normal text passes; secret-name/content and oversized fixtures block with safe reasons.
- Edge case: Suspected necessary content blocks visibly instead of being silently truncated or sent.
- Not included: Claiming perfect secret detection or interpreting repository instructions.
- Exit condition: Normal, secret, oversized, binary, and blocked-reason fixtures pass.

<a id="kiko-018b"></a>
### KIKO-018B — Label repository text as untrusted model data

- Checkpoint kind: implementation
- Observable outcome: Repository content is wrapped with provenance/trust labels and cannot override Tutor policy.
- Why it matters: Source or documentation may contain prompt-like instructions intended to redirect the expert.
- Prerequisites: KIKO-018A.
- Known concepts: Bounded context, selected files, policy priority, and structured metadata.
- New concepts and syntax: Trust labels, immutable instruction/data separation, and provenance fields.
- Learner task: Convert one filtered file into a clearly delimited untrusted context item.
- Verification: `.venv/bin/python -m unittest tests.test_repository_safety.UntrustedContentTests -v`
- Expected behavior: File instructions remain quoted data; Tutor constraints retain priority and provenance is preserved.
- Edge case: Nested Markdown/code blocks cannot escape the untrusted-content boundary.
- Not included: Sending the item to Codex or executing repository content.
- Exit condition: Benign, instruction-like, nested-delimiter, and provenance fixtures pass.
