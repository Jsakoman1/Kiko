# Kiko Learning Log

## Preserved learner-authored evidence

- Legacy Step 1: Created and ran a Python script that printed terminal output.
  Help used: syntax example.
- Legacy Step 2: Moved behavior into `main()` and added the module entry-point
  guard. Help used: syntax example.
- Legacy Step 3: Read command-line arguments and implemented `help`. Help used:
  guided example.
- Legacy Step 4: Created lists and a dictionary for mission, rules, and notes,
  then implemented `show`. Help used: example and one debugging explanation.
- Project Step 1: Extracted dictionary creation into `create_context()` and
  returned it to `main()`. Help used: one focused example.
- Project Step 2: Added version, project, and Tutor sections with nested
  dictionaries and displayed their values. Help used: focused structure example.
- Project Step 3A: Serialized the context with `json.dumps()` and wrote
  `.tutor/state.json` with `Path.write_text()`. Help used: focused example.
- Project Step 3B: Loaded the saved JSON with `json.loads()` and used the saved
  value after it was changed. Help used: focused example.
- Project Step 4A: Loaded the private global learner profile separately and
  displayed the learner's previous language. Help used: focused example.
- Project Step 4B: Selected and displayed only Python concept summaries from
  the separate global learner state. Help used: guided explanation and example.
- KIKO-011: Loaded the separate global personal reference, displayed a bounded
  five-line preview, and handled a missing reference safely. Help used: guided
  lesson and one debugging explanation about text versus parsed JSON.
- KIKO-012: Added `.venv/` to `.gitignore`, created an isolated local Python
  environment, and verified that its interpreter differs from the base Python.
  Help used: guided command and environment explanation.
- KIKO-012A: Moved the existing CLI into a regular Python package, routed
  `python -m kiko` through `__main__.py`, and preserved welcome/help/show plus
  import-without-startup behavior. Help used: guided package example and one
  debugging explanation about module versus direct-file execution.
- KIKO-012B: Wrote TOML build/project/script metadata, installed Kiko editably,
  and verified that the generated `kiko` command and package module execution
  share the same CLI behavior. Help used: detailed configuration-format
  explanation and debugging of environment/module command mistakes.
- KIKO-013: Renamed ambiguous runtime checkpoint state and CLI output so the
  running learner-project state no longer claims ownership of Kiko-development
  roadmap progress. Help used: guided architecture explanation and concrete
  development/runtime/CLI comparison.
- KIKO-014: Added a root-discovered `unittest.TestCase` that verifies the default
  Kiko project name and confirmed that importing the CLI has no startup side
  effect. Help used: guided unittest example and one test-directory correction.
- KIKO-014A: Added a temporary-home learner-state test using a context manager
  and mock patch, then proved the real global learner profile's checksum,
  modification time, and size remained unchanged. Help used: guided isolation
  example.
- KIKO-015: Implemented a pure project-state root/version validator with a
  domain-specific error and four isolated tests for valid, non-dictionary,
  missing-version, and future-version inputs. Help used: guided lesson,
  progressive debugging, and one project-specific correction.
- KIKO-015A: Extended project-state validation across required top-level,
  project, and Tutor field types; added five tests covering valid state,
  missing nested data, wrong types, nested shape, and unknown-field
  preservation. Help used: guided lesson, progressive debugging, and targeted
  fixture corrections.
- KIKO-015B: Injected a project-state path through save/load, corrected the
  text-to-dictionary validation boundary, and returned the validated parsed
  object. Help used: pair-programmed lesson and progressive debugging. The five
  loading fixtures were agent-authored and are not learner competence evidence.

These prove completed project steps. The related Python concepts are recorded
as `assisted`, not independent or reliable.

## Learning signals

- One ordering error occurred when `context` was used before it was created.
  The learner corrected it after the execution-order explanation. This is a
  single useful lesson, not a recurring weakness.

## Product transition

- The original Kiko Python prototype is preserved as the starting point.
- The current prototype now has a separate state-creation function.
- The current prototype now writes and loads a JSON state file.
- The current prototype now reads global learner state without copying it into
  project state.
- The current prototype now selects language-relevant concept summaries without
  merging global learner state into project state.
- The current prototype now reads and previews the personal reference without
  copying it into project state.
- Kiko development now has an ignored project-local Python environment for
  isolated package and test work.
- Kiko now runs as a Python package through `python -m kiko` while preserving
  the prototype CLI behavior.
- Kiko now has validated package metadata and a project-local editable `kiko`
  console command.
- Kiko-development progress and runtime learner-project checkpoint state now
  have separate owners and domain-specific names.
- Kiko now has a discoverable automated unit-test foundation outside the
  application package.
- Kiko filesystem tests can now isolate private learner state from the real
  Application Support directory.
- Kiko now rejects invalid project-state roots and unsupported schema versions
  through one controlled domain error before deeper fields are inspected.
- Kiko now validates the complete current project-state field shape while
  preserving unknown non-conflicting fields for forward compatibility.
- Kiko now enforces that validator at the real project-state loading boundary
  and leaves invalid saved input unchanged; five pair-programmed loading tests
  cover the integration.
- The old syntax journal was migrated into the global personal reference.
- The new Project Tutor implementation roadmap starts at Step 1 without
  resetting prior learning.

## Recurring learning signals

- None.
