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
- The old syntax journal was migrated into the global personal reference.
- The new Project Tutor implementation roadmap starts at Step 1 without
  resetting prior learning.

## Recurring learning signals

- None.
