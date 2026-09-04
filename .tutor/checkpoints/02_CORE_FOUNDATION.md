# Phase 2 — Maintainable Core Foundation

<a id="kiko-012"></a>
### KIKO-012 — Create an isolated Python development environment

- Checkpoint kind: implementation
- Observable outcome: Kiko development commands run through a project-local `.venv`.
- Why it matters: Later dependencies and tests must not modify or depend on global Python packages.
- Prerequisites: KIKO-011.
- Known concepts: Python execution, paths, and terminal commands.
- New concepts and syntax: `python3 -m venv`, isolated interpreters, `.venv/bin/python`, and the `.gitignore` directory pattern `.venv/`.
- Learner task: Ignore `.venv/`, create the local environment, and verify its Python executable.
- Verification: Add `.venv/` to `.gitignore`, run `python3 -m venv .venv`, then run `.venv/bin/python --version` and `git status --short`.
- Expected behavior: The local interpreter runs, system Python receives no package install, and Git status does not list `.venv/`.
- Edge case: Recreating an existing `.venv` is not used as a destructive recovery action.
- Not included: Package metadata, source moves, dependencies, or CLI entry points.
- Exit condition: A project-local Python interpreter is available for later commands and its generated directory is ignored by Git.

<a id="kiko-012a"></a>
### KIKO-012A — Migrate existing CLI behavior into the package

- Checkpoint kind: implementation
- Observable outcome: Existing CLI behavior runs through `python -m kiko` from a real Python package.
- Why it matters: State, policy, providers, and protocol need separate testable modules before complexity grows.
- Prerequisites: KIKO-012.
- Known concepts: Modules, imports, functions, `.venv`, paths, and CLI execution.
- New concepts and syntax: Python packages, `__init__.py`, `__main__.py`, and relative import `from .cli import main`.
- Learner task: Move existing CLI code into a `kiko` package and route `python -m kiko` to the same `main()` function.
- Verification: Run `.venv/bin/python -m kiko`, `.venv/bin/python -m kiko help`, and `.venv/bin/python -m kiko show`.
- Expected behavior: Package execution preserves the previous welcome, help, and show output.
- Edge case: Importing `kiko.cli` does not execute `main()` automatically.
- Not included: `pyproject.toml`, editable installation, console scripts, policy refactoring, or App Server code.
- Exit condition: All previous CLI paths pass through package execution and import has no startup side effect.

<a id="kiko-012b"></a>
### KIKO-012B — Add editable install and the `kiko` console command

- Checkpoint kind: implementation
- Observable outcome: Package metadata installs Kiko editably and creates `.venv/bin/kiko` mapped to `kiko.cli:main`.
- Why it matters: Development and future UI processes need a stable command independent of source-file location.
- Prerequisites: KIKO-012A.
- Known concepts: `.venv`, `.gitignore`, Python package, modules, `main()`, and CLI behavior.
- New concepts and syntax: TOML table headers `[name]`, key/value assignment `key = value`, strings, lists, nested table `[project.scripts]`, `pyproject.toml`, build backend, editable install `pip install -e .`, script entry point, and generated-directory pattern `*.egg-info/`.
- Learner task: Add minimal package/build metadata, ignore generated package metadata, and install the current project editably inside `.venv`.
- Verification: Add `*.egg-info/` to `.gitignore`, run `.venv/bin/python -m pip install -e .`, then run `.venv/bin/kiko show`, `.venv/bin/python -m kiko show`, and `git status --short`.
- Expected behavior: Editable install succeeds, both entry points match, and Git does not list generated `.egg-info` content.
- Edge case: Import and module execution still work after installation; changing only Python source needs no reinstall.
- Not included: Runtime dependencies, release builds, publishing, signing, or version automation.
- Exit condition: Module and console entry points share one `main()` implementation and preserve all verified CLI behavior.

<a id="kiko-013"></a>
### KIKO-013 — Separate development progress from runtime project state

- Checkpoint kind: implementation
- Observable outcome: Documentation identifies Kiko-development progress separately from a future learner project's runtime checkpoint.
- Why it matters: The current plan says KIKO-011 while the prototype JSON previously displayed Step 2; two meanings cannot share one authority.
- Prerequisites: KIKO-012B.
- Known concepts: Nested state, project-local files, and ownership boundaries.
- New concepts and syntax: Separate domain models and derived display values.
- Learner task: Adjust the runtime state model and `show` labels so they cannot claim to be the development roadmap authority.
- Verification: `.venv/bin/kiko show`
- Expected behavior: Output clearly labels runtime/demo checkpoint data and the development handoff remains owned by `LEARNING_PLAN.md`.
- Edge case: Deleting runtime state recreates defaults without changing development progress.
- Not included: Parsing Markdown as a runtime API or automatically editing the development plan.
- Exit condition: No field or label ambiguously represents both progress domains.

<a id="kiko-014"></a>
### KIKO-014 — Establish the first unittest discovery test

- Checkpoint kind: implementation
- Observable outcome: One pure `create_context()` unit test is discovered and passes inside `.venv`.
- Why it matters: Every later behavior needs repeatable automated verification before filesystem isolation is added.
- Prerequisites: KIKO-012A and KIKO-013.
- Known concepts: Local `.venv`, functions, imports, dictionaries, and command verification.
- New concepts and syntax: `unittest`, Python `class` inheritance, explicit `self`, `test_` discovery naming, and `assertEqual`.
- Learner task: Add one pure unit test that verifies the default project name returned by `create_context()`.
- Verification: `.venv/bin/python -m unittest discover -s tests -v`
- Expected behavior: Exactly one discovered test passes and the command ends with `OK`.
- Edge case: Importing `kiko.cli` for the test produces no CLI output or state write.
- Not included: Filesystem access, `TemporaryDirectory`, mocking, setup/cleanup methods, state-schema validation, or live Codex.
- Exit condition: The first pure unit test is discoverable, repeatable, and fails when its expected project name is intentionally wrong.

<a id="kiko-014a"></a>
### KIKO-014A — Isolate filesystem tests from real learner data

- Checkpoint kind: implementation
- Observable outcome: A learner-state filesystem test uses a temporary home and never reads or writes the real global learner profile.
- Why it matters: Future evidence and migration tests must be repeatable without risking private state.
- Prerequisites: KIKO-014.
- Known concepts: `unittest`, test discovery, test classes, assertions, paths, and learner-state loading.
- New concepts and syntax: `TemporaryDirectory`, nested `with` context managers, `unittest.mock.patch.object`, and automatic cleanup.
- Learner task: Add one missing-learner-state test with a temporary home and patched `Path.home()`.
- Verification: `.venv/bin/python -m unittest discover -s tests -v`
- Expected behavior: Both tests pass; learner loader returns the safe empty profile/concepts from the temporary home and the real learner file remains untouched.
- Edge case: Temporary files are removed after both passing and failing test paths.
- Not included: State schema validation, production dependency injection, global-state writes, or migration.
- Exit condition: The missing-profile temporary-home fixture passes and the real Application Support learner file is not accessed or changed.

<a id="kiko-015"></a>
### KIKO-015 — Validate the project-state root and version

- Checkpoint kind: implementation
- Observable outcome: Project runtime state must be a dictionary with the supported version before Kiko accepts it.
- Why it matters: Non-state values and unsupported versions must fail safely before deeper fields are inspected.
- Prerequisites: KIKO-014A.
- Known concepts: Dictionaries, versions, functions, conditions, classes, context managers, and isolated tests.
- New concepts and syntax: `isinstance`, boolean `not`, a domain-specific exception class, `raise`, `pass`, and `assertRaises`.
- Learner task: Create a pure project-state validator that accepts a version-1 dictionary unchanged and raises one controlled error for a non-dictionary or missing/unsupported version; cover those paths with unit tests.
- Verification: `.venv/bin/python -m unittest tests.test_state_contracts.ProjectStateRootTests -v`
- Expected behavior: A version-1 dictionary is returned unchanged; non-dictionary, missing-version, and future-version inputs raise the project-state error.
- Edge case: A missing `version` is rejected through the same controlled error rather than causing an unrelated Python exception.
- Not included: Nested project fields, field types, unknown-field policy, persistence, migration, or UI error rendering.
- Exit condition: Valid-root, non-dictionary, missing-version, and future-version fixtures pass.

<a id="kiko-015a"></a>
### KIKO-015A — Validate project-state required fields and types

- Checkpoint kind: implementation
- Observable outcome: A supported project-state dictionary is accepted only when its required nested fields have the expected types.
- Why it matters: A correct root and version are not enough if Kiko cannot safely read the project and Tutor values inside them.
- Prerequisites: KIKO-015.
- Known concepts: Project-state root validation, nested dictionaries, lists, strings, controlled errors, and isolated tests.
- New concepts and syntax: Required-field validation and nested type checks.
- Learner task: Extend the project-state validator to check the required top-level, `project`, and `tutor` fields while preserving unrelated unknown fields.
- Verification: `.venv/bin/python -m unittest tests.test_state_contracts.ProjectStateFieldTests -v`
- Expected behavior: The current project shape passes; missing required fields and wrong field types raise the project-state error.
- Edge case: Unknown non-conflicting fields remain unchanged for forward compatibility.
- Not included: Learner/session/feedback contracts, persistence, migration, or UI error rendering.
- Exit condition: Valid, missing-field, wrong-type, nested-shape, and unknown-field fixtures pass.

<a id="kiko-015b"></a>
### KIKO-015B — Enforce the project-state contract during loading

- Checkpoint kind: integration
- Observable outcome: Loading project state returns only data that passed the complete project-state validator.
- Why it matters: A tested validator protects users only after the real file-loading path consistently calls it.
- Prerequisites: KIKO-015A.
- Known concepts: JSON loading, paths, project-state validation, controlled errors, temporary directories, and mocking.
- New concepts and syntax: Injected state paths and validation at an I/O boundary.
- Learner task: Let project-state loading use an injected test path and pass every parsed/default state through the project-state validator before returning it.
- Verification: `.venv/bin/python -m unittest tests.test_state_loading.ProjectStateLoadingTests -v`
- Expected behavior: Valid saved/default state returns; parsed invalid or future state raises the project-state error without rewriting the fixture.
- Edge case: A failed validation leaves the invalid input file unchanged for later diagnosis or recovery.
- Not included: Atomic writes, backups, schema migration, or user-interface error rendering.
- Exit condition: Valid, default, invalid-shape, future-version, and no-rewrite loading fixtures pass.

<a id="kiko-015c"></a>
### KIKO-015C — Validate the learner-state contract

- Checkpoint kind: implementation
- Observable outcome: Global learner state validates through its own versioned profile/concepts contract.
- Why it matters: Cross-project knowledge must reject malformed data without borrowing project-state fields.
- Prerequisites: KIKO-015B.
- Known concepts: Versioned validators, nested fields, lists, controlled errors, and isolated fixtures.
- New concepts and syntax: Owner-specific contract composition with reusable field validators.
- Learner task: Validate learner schema version, profile, and concepts without accepting project-state shape.
- Verification: `.venv/bin/python -m unittest tests.test_state_contracts.LearnerStateTests -v`
- Expected behavior: Valid learner state passes; missing/wrong-type/profile/project-shape fixtures fail clearly.
- Edge case: Unknown non-conflicting learner fields remain preserved.
- Not included: Session/feedback contracts, persistence, migration, or UI errors.
- Exit condition: Valid, malformed, wrong-owner, unknown-field, and future-version learner fixtures pass.

<a id="kiko-015d"></a>
### KIKO-015D — Validate the session-state contract

- Checkpoint kind: implementation
- Observable outcome: Ephemeral expert-session state validates independently from project progress and learner evidence.
- Why it matters: Provider thread IDs must never become canonical project or competence state.
- Prerequisites: KIKO-015C.
- Known concepts: Owner-specific validators, versions, controlled errors, and isolated fixtures.
- New concepts and syntax: Optional session fields and ephemeral-state ownership.
- Learner task: Validate one session schema containing only its version and optional provider/thread identifiers.
- Verification: `.venv/bin/python -m unittest tests.test_state_contracts.SessionStateTests -v`
- Expected behavior: Valid empty/identified sessions pass; project/learner fields and unsupported versions fail.
- Edge case: A missing optional thread ID remains valid and means no resumable session.
- Not included: Starting/resuming provider threads, persistence, or migration.
- Exit condition: Empty, identified, wrong-owner, wrong-type, and future-version session fixtures pass.

<a id="kiko-015e"></a>
### KIKO-015E — Validate the Tutor-feedback-state contract

- Checkpoint kind: implementation
- Observable outcome: Sanitized Tutor-feedback candidates validate under a separate versioned owner.
- Why it matters: Product-quality feedback must not be confused with learner competence or raw conversation history.
- Prerequisites: KIKO-015D.
- Known concepts: Owner-specific validators, versions, controlled errors, and isolated fixtures.
- New concepts and syntax: Feedback-candidate field allowlist at the state boundary.
- Learner task: Validate the minimal feedback-state container and reject learner/project/raw-content fields.
- Verification: `.venv/bin/python -m unittest tests.test_state_contracts.FeedbackStateTests -v`
- Expected behavior: Valid empty/candidate containers pass; forbidden-owner and unsupported-version data fail.
- Edge case: One invalid feedback file does not invalidate valid project or learner fixtures.
- Not included: Feedback classification, sanitization behavior, persistence, or UI controls.
- Exit condition: Empty, candidate, forbidden-field, wrong-owner, and future-version feedback fixtures pass.

<a id="kiko-016"></a>
### KIKO-016 — Write state through atomic replacement

- Checkpoint kind: implementation
- Observable outcome: One JSON update completes fully or leaves the previous file unchanged.
- Why it matters: Interrupted writes must not create partial state.
- Prerequisites: KIKO-014 and KIKO-015B.
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
- Expected behavior: Valid prior state is copied once; invalid current data is not promoted to backup.
- Edge case: Existing valid backup is not silently overwritten by corrupt state.
- Not included: Schema transformation or concurrent writer locks.
- Exit condition: Create, preserve-existing, reject-corrupt, and missing-current backup fixtures pass.

<a id="kiko-016b"></a>
### KIKO-016B — Restore a validated state backup

- Checkpoint kind: implementation
- Observable outcome: One invalid/current state file can be replaced by its validated backup through atomic replacement.
- Why it matters: Preserving a backup helps only when Kiko has a safe explicit restoration path.
- Prerequisites: KIKO-016A.
- Known concepts: Atomic replacement, backup paths, state validation, and isolated fixtures.
- New concepts and syntax: Backup restore decision and restore receipt.
- Learner task: Restore one owner from a validated backup without overwriting evidence when the backup is invalid.
- Verification: `.venv/bin/python -m unittest tests.test_state_persistence.RestoreBackupTests -v`
- Expected behavior: Valid backup restores atomically; missing/invalid backup leaves current data untouched and fails clearly.
- Edge case: Restoring current valid state is an explicit no-op rather than a duplicate rewrite.
- Not included: Schema migration, multi-owner rollback, locking, or UI recovery.
- Exit condition: Valid, missing, invalid, current-no-op, and interrupted-restore fixtures pass.

<a id="kiko-016c"></a>
### KIKO-016C — Migrate a supported state schema version

- Checkpoint kind: implementation
- Observable outcome: One supported old schema migrates to the current schema after backup and validation.
- Why it matters: Kiko upgrades must preserve learner/project history without accepting unknown future formats.
- Prerequisites: KIKO-016B.
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
### KIKO-017A — Define the protocol error result

- Checkpoint kind: implementation
- Observable outcome: A failed request returns one versioned error result tied to its request ID.
- Why it matters: CLI and extension need a deterministic non-success result before lifecycle events are added.
- Prerequisites: KIKO-017.
- Known concepts: Versioned JSONL envelope, request IDs, tagged messages, and state contracts.
- New concepts and syntax: Tagged error payload and stable error-code field.
- Learner task: Define and validate one error-result envelope without adding progress or cancellation.
- Verification: `.venv/bin/python -m unittest tests.test_local_protocol.ErrorResultTests -v`
- Expected behavior: Valid error correlates; missing code/message, wrong ID, and unknown version fail clearly.
- Edge case: Safe optional diagnostic metadata cannot replace the stable error code.
- Not included: Progress, cancellation, transport, retry policy, or UI rendering.
- Exit condition: Valid, malformed, mismatched-ID, unknown-version, and optional-metadata fixtures pass.

<a id="kiko-017b"></a>
### KIKO-017B — Define protocol progress events

- Checkpoint kind: implementation
- Observable outcome: A non-terminal progress event is tied to one active request without completing it.
- Why it matters: Long Core operations need visible progress that cannot masquerade as a final result.
- Prerequisites: KIKO-017A.
- Known concepts: Versioned envelopes, request IDs, tags, and terminal results.
- New concepts and syntax: Non-terminal notification semantics and bounded progress payload.
- Learner task: Define and validate one progress-event shape for an active request.
- Verification: `.venv/bin/python -m unittest tests.test_local_protocol.ProgressEventTests -v`
- Expected behavior: Valid progress correlates and remains non-terminal; malformed or post-terminal progress fails.
- Edge case: Progress after success/error cannot reopen the completed request.
- Not included: Cancellation, transport, percentage estimation, or UI rendering.
- Exit condition: Valid, malformed, unknown-request, and post-terminal progress fixtures pass.

<a id="kiko-017c"></a>
### KIKO-017C — Define protocol cancellation messages

- Checkpoint kind: implementation
- Observable outcome: Cancel request and cancelled result use explicit tags and the same request ID.
- Why it matters: A caller must be able to request cancellation and receive one unambiguous terminal result.
- Prerequisites: KIKO-017B.
- Known concepts: Versioned envelopes, request IDs, progress, and terminal results.
- New concepts and syntax: Cancel command and cancelled terminal-result semantics.
- Learner task: Define and validate the cancel/cancelled message pair independent of process behavior.
- Verification: `.venv/bin/python -m unittest tests.test_local_protocol.CancellationMessageTests -v`
- Expected behavior: Matching cancel/cancelled pair passes; wrong ID, duplicate terminal, and unknown tag fail.
- Edge case: Cancellation after an already terminal result cannot create a second terminal outcome.
- Not included: Killing processes, timeouts, retries, or UI actions.
- Exit condition: Valid, mismatched, duplicate-terminal, already-complete, and unknown-tag fixtures pass.

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
### KIKO-018A — Accept only bounded repository text

- Checkpoint kind: implementation
- Observable outcome: Selected safe paths produce text only when the file is decodable and within a fixed size limit.
- Why it matters: Valid workspace paths may still contain binary or impractically large content.
- Prerequisites: KIKO-018.
- Known concepts: Safe paths, file reading, allow/deny rules, and controlled errors.
- New concepts and syntax: Byte-size limit and explicit text-decoding failure.
- Learner task: Read one already-contained file only when it is bounded decodable text.
- Verification: `.venv/bin/python -m unittest tests.test_repository_safety.BoundedTextTests -v`
- Expected behavior: Normal text passes; oversized and binary/undecodable fixtures block with safe reasons.
- Edge case: Oversized text is blocked visibly rather than silently truncated.
- Not included: Secret detection, prompt-injection labeling, or context compilation.
- Exit condition: Normal, exact-limit, oversized, undecodable, and blocked-reason fixtures pass.

<a id="kiko-018b"></a>
### KIKO-018B — Filter likely repository secrets

- Checkpoint kind: implementation
- Observable outcome: Bounded text with a denied filename or credential-like content is blocked before context compilation.
- Why it matters: Valid text inside the workspace may still expose credentials or private configuration.
- Prerequisites: KIKO-018A.
- Known concepts: Bounded text, filename/content rules, controlled errors, and safe findings.
- New concepts and syntax: Conservative secret-name and credential-pattern heuristics.
- Learner task: Apply an explicit small denylist/pattern set to one bounded text item.
- Verification: `.venv/bin/python -m unittest tests.test_repository_safety.SecretFilterTests -v`
- Expected behavior: Normal text passes; denied-name and credential-like fixtures block without exposing the match.
- Edge case: A suspected necessary file blocks with an explanation instead of partial disclosure.
- Not included: Claiming perfect secret detection, untrusted labeling, or sending content to Codex.
- Exit condition: Benign, denied-name, credential-like, safe-reason, and false-positive-control fixtures pass.

<a id="kiko-018c"></a>
### KIKO-018C — Label repository text as untrusted model data

- Checkpoint kind: implementation
- Observable outcome: Filtered repository text is wrapped with provenance/trust labels and cannot override Tutor policy.
- Why it matters: Source or documentation may contain prompt-like instructions intended to redirect the expert.
- Prerequisites: KIKO-018B.
- Known concepts: Filtered text, policy priority, explicit boundaries, and structured metadata.
- New concepts and syntax: Trust labels, immutable instruction/data separation, and provenance fields.
- Learner task: Convert one filtered file into a clearly delimited untrusted context item.
- Verification: `.venv/bin/python -m unittest tests.test_repository_safety.UntrustedContentTests -v`
- Expected behavior: File instructions remain quoted data; Tutor constraints retain priority and provenance is preserved.
- Edge case: Nested Markdown/code blocks cannot escape the untrusted-content boundary.
- Not included: Sending the item to Codex or executing repository content.
- Exit condition: Benign, instruction-like, nested-delimiter, and provenance fixtures pass.
