# Phase 0 — Verified Learning Foundation

These historical checkpoints are normalized for traceability. Completion status
remains only in `LEARNING_PLAN.md`; evidence remains in `LEARNING_LOG.md`.

<a id="kiko-001"></a>
### KIKO-001 — Run a basic Python script

- Checkpoint kind: implementation
- Observable outcome: A Python file prints a welcome message in the terminal.
- Why it matters: It proves the learner can create and execute the smallest Kiko program.
- Prerequisites: Python 3 available in the shell.
- Known concepts: Basic programming experience from Java.
- New concepts and syntax: `print(...)` and running `python3 file.py`.
- Learner task: Create and run the first Kiko script.
- Verification: `python3 kiko.py`
- Expected behavior: The terminal prints the Kiko welcome text without an exception.
- Edge case: Running from the project directory finds the intended file.
- Not included: Functions, arguments, state, persistence, or models.
- Exit condition: The learner-authored script runs and its output is observed.

<a id="kiko-002"></a>
### KIKO-002 — Add the module entry point

- Checkpoint kind: implementation
- Observable outcome: Direct execution calls `main()` through the module guard.
- Why it matters: Program startup becomes explicit before CLI behavior grows.
- Prerequisites: KIKO-001.
- Known concepts: Java methods and program entry points.
- New concepts and syntax: `def`, indentation, `main()`, and `if __name__ == "__main__":`.
- Learner task: Move startup behavior into `main()` and call it only on direct execution.
- Verification: `python3 kiko.py`
- Expected behavior: The same welcome output appears once.
- Edge case: Importing the module must not run `main()` automatically.
- Not included: Commands, files, or structured state.
- Exit condition: Direct execution works and import has no startup side effect.

<a id="kiko-003"></a>
### KIKO-003 — Read CLI arguments and show help

- Checkpoint kind: implementation
- Observable outcome: Kiko distinguishes no command from the `help` command.
- Why it matters: A stable CLI entry surface is needed for all later Core behavior.
- Prerequisites: KIKO-002.
- Known concepts: Functions, lists, conditions, and Java command-line arguments.
- New concepts and syntax: `import sys`, `sys.argv[1:]`, `len`, indexing, `if`/`else`.
- Learner task: Read arguments and print a small command list for `help`.
- Verification: `python3 kiko.py help`
- Expected behavior: The supported Kiko commands are printed.
- Edge case: `python3 kiko.py` still prints the welcome message.
- Not included: Command parser libraries or persistence.
- Exit condition: Both no-command and `help` paths behave as specified.

<a id="kiko-004"></a>
### KIKO-004 — Store and display in-memory context

- Checkpoint kind: implementation
- Observable outcome: `show` prints mission, rules, and notes from one dictionary.
- Why it matters: Kiko needs structured context before it can persist or select it.
- Prerequisites: KIKO-003.
- Known concepts: Java collections and CLI conditions.
- New concepts and syntax: Python list/dictionary literals and bracket key access.
- Learner task: Create the context values and display them through `show`.
- Verification: `python3 kiko.py show`
- Expected behavior: Mission, rules, and notes are printed from the dictionary.
- Edge case: Existing no-command and `help` behavior remains unchanged.
- Not included: Nested state or file persistence.
- Exit condition: All three context fields are read from one learner-authored dictionary.

<a id="kiko-005"></a>
### KIKO-005 — Separate context creation from CLI behavior

- Checkpoint kind: implementation
- Observable outcome: `main()` obtains context from a dedicated function.
- Why it matters: State acquisition must be replaceable by disk loading later.
- Prerequisites: KIKO-004.
- Known concepts: Functions, dictionaries, and variable assignment.
- New concepts and syntax: Returning a dictionary and assigning a function result.
- Learner task: Extract context creation without changing CLI behavior.
- Verification: `python3 kiko.py && python3 kiko.py help && python3 kiko.py show`
- Expected behavior: All three existing CLI paths behave exactly as before.
- Edge case: `main()` must not use context before the function returns it.
- Not included: Persistence, classes, or models.
- Exit condition: Context creation and command handling have separate functions.

<a id="kiko-006"></a>
### KIKO-006 — Shape nested versioned project state

- Checkpoint kind: implementation
- Observable outcome: Context includes version, project, and Tutor sections.
- Why it matters: Related values need explicit ownership before saving or combining state.
- Prerequisites: KIKO-005.
- Known concepts: Dictionaries and returned values.
- New concepts and syntax: Nested dictionaries and multi-level bracket access.
- Learner task: Add nested project/Tutor data and display it through `show`.
- Verification: `python3 kiko.py show`
- Expected behavior: Project, language, help preference, and prototype step are visible.
- Edge case: Earlier mission, rules, and notes remain available.
- Not included: Schema validation or migration.
- Exit condition: The nested state shape is observable through the CLI.

<a id="kiko-007"></a>
### KIKO-007 — Save project state as JSON

- Checkpoint kind: implementation
- Observable outcome: Kiko writes readable state to `.tutor/state.json`.
- Why it matters: Project context must survive process exit.
- Prerequisites: KIKO-006.
- Known concepts: Functions, strings, and nested dictionaries.
- New concepts and syntax: `json.dumps`, `Path`, and `write_text`.
- Learner task: Serialize and save the context through a dedicated function.
- Verification: `python3 kiko.py show && python3 -m json.tool .tutor/state.json`
- Expected behavior: `show` works and the saved file is valid formatted JSON.
- Edge case: The target `.tutor` directory already exists.
- Not included: Atomic writes, backups, or migration.
- Exit condition: Valid project JSON is present after execution.

<a id="kiko-008"></a>
### KIKO-008 — Load project state with a safe default

- Checkpoint kind: implementation
- Observable outcome: Existing JSON is loaded; missing JSON recreates defaults safely.
- Why it matters: Kiko must resume rather than rebuild state on every run.
- Prerequisites: KIKO-007.
- Known concepts: Conditions, file existence, JSON serialization.
- New concepts and syntax: `read_text`, `json.loads`, and missing-file fallback flow.
- Learner task: Load saved context before command handling.
- Verification: `python3 kiko.py show`
- Expected behavior: A manually changed saved value appears in the next output.
- Edge case: A missing state file is recreated instead of crashing.
- Not included: Corrupt JSON recovery or version migration.
- Exit condition: Both existing-file and missing-file paths are observed working.

<a id="kiko-009"></a>
### KIKO-009 — Read the global learner profile

- Checkpoint kind: implementation
- Observable outcome: Kiko displays previous languages from a separate global JSON file.
- Why it matters: Cross-project knowledge must have a private owner separate from project state.
- Prerequisites: KIKO-008.
- Known concepts: `Path`, JSON loading, functions, and existence checks.
- New concepts and syntax: `Path.home()` and path joining with `/`.
- Learner task: Load the global learner file without copying it into project state.
- Verification: `python3 kiko.py show`
- Expected behavior: The configured previous language is displayed.
- Edge case: Missing global state returns a safe profile and concept list.
- Not included: Writing global evidence or reading the personal reference.
- Exit condition: Global and project state are loaded from distinct paths.

<a id="kiko-010"></a>
### KIKO-010 — Select relevant concept summaries

- Checkpoint kind: implementation
- Observable outcome: `show` displays only concepts whose IDs match the project language.
- Why it matters: Tutor context must be relevant and must not copy the full learner profile.
- Prerequisites: KIKO-009.
- Known concepts: Loops, lists, dictionaries, `startswith`, and `append`.
- New concepts and syntax: `lower`, f-strings, `dict.get`, and string concatenation.
- Learner task: Select Python concept ID/stage summaries from global learner state.
- Verification: `python3 kiko.py show`
- Expected behavior: Python summaries appear and unrelated language concepts do not.
- Edge case: An empty `concepts` list returns an empty relevant summary without error.
- Not included: Personal-reference reading or learner-state mutation.
- Exit condition: Normal and empty selection behavior pass read-only checks.
