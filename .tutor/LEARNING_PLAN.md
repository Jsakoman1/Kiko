# Project Tutor v0.1 Learning Plan

## Preserved foundation

- [x] Ran a basic Python script and used terminal output.
- [x] Added `main()` and the module entry-point guard.
- [x] Added command-line arguments and `help`.
- [x] Added an in-memory context dictionary and `show`.
- [x] Prepared the Project Tutor product brief, architecture, state ownership,
  Codex integration direction, and learner knowledge migration.

These are completed project facts. They do not imply independent mastery of all
related concepts.

## Product implementation roadmap

- [x] Step 1: Separate project-state creation from CLI behavior.
- [x] Step 2: Expand the versioned project-state shape for roadmap and help
  preference.
- [x] Step 3: Save and load project state from `.tutor/state.json`.
- [ ] Step 4: Read the private global learner profile and personal reference.
  **NEXT**
- [ ] Step 5: Update competence evidence and reference entries conservatively.
- [ ] Step 6: Select assistance level and compile bounded Tutor context.
- [ ] Step 7: Introduce the small ExpertProvider boundary with a fake expert.
- [ ] Step 8: Implement the Codex App Server `stdio` handshake and lifecycle.
- [ ] Step 9: Complete one structured, read-only Codex tutoring turn.
- [ ] Step 10: Prove the full standalone Tutor CLI loop.
- [ ] Step 11: Build the thin TypeScript VS Code sidebar and local process link.
- [ ] Step 12: Prove the end-to-end v0.1 learning loop and acceptance criteria.

This roadmap is complete enough to guide v0.1. A checkpoint may be split after
review if it proves too large for one learning step; splitting must preserve the
same product outcome rather than expanding scope.

## Current handoff

- Last verified behavior: `show` loads the versioned nested context from
  `.tutor/state.json`, including a manually changed saved value.
- Current product truth: Kiko has durable project state but no global learner
  integration or model connection.
- Next implementation: Step 4 — read global learner knowledge and reference.
- Blockers: None.

## Step 1 — Separate project state from CLI behavior — COMPLETE

### Objective

Move creation of the current mission/rules/notes dictionary into a small
function. `main()` should ask that function for the state and keep handling CLI
behavior.

### Why it matters

Tutor state will soon be loaded from disk. Separating "obtain state" from
"respond to a command" gives us the first clean architecture boundary without
adding classes or frameworks.

### What the learner already knows

- defining and calling a function
- dictionaries and lists
- assigning values to variables
- reading dictionary values
- running and checking CLI commands

### New concept

- returning a value from a function and assigning that result

### Success condition

- `main()` no longer creates the dictionary directly
- the three existing commands behave exactly as before
- no persistence, new commands, classes, or model integration are added

### Initial guidance

Create a clearly named function above `main()`. Let it create the existing
dictionary and return it. In `main()`, replace the dictionary literal with a
call to that function. Think of it as a tiny factory method from Java, but use a
plain Python function.

### Verification

```bash
python3 kiko.py
python3 kiko.py help
python3 kiko.py show
```

Expected behavior remains the current welcome message, command list, and
mission/rules/notes output.

## Step 2 — Shape the project state — COMPLETE

### Objective

Add a small versioned project-state structure inside `create_context()`. Include
the project identity, the Tutor help preference, and the current learning step.

### Why it matters

Tutor needs to distinguish project information from Tutor information before it
can save or combine that state with global learner knowledge. A version number
also gives us a safe place to evolve the structure later.

### What the learner already knows

- functions and `return`
- dictionaries and lists
- reading dictionary values
- command-line conditions

### New concept

- nested dictionaries as a small structured state model

### Success condition

- `create_context()` returns one dictionary with `version`, `project`, and
  `tutor` sections
- `project` contains a name and language
- `tutor` contains a help preference and current step
- `show` displays the new values
- existing `help` and no-command behavior still work
- no file persistence, model calls, or new modules are added

### Initial guidance

Keep the outer dictionary small. Put related values inside inner dictionaries,
then read them with two keys, such as the project name inside the `project`
section. This is similar to a Java `Map` containing another `Map`, but Python
lets us write it directly.

### Verification

```bash
python3 kiko.py
python3 kiko.py help
python3 kiko.py show
```

The `show` output should include the project name, language, help preference,
and current step.

## Step 3 — Save and load project state — COMPLETE

### Objective

Persist the context returned by `create_context()` in `.tutor/state.json` and
load it on a later run instead of rebuilding it every time.

### Why it matters

Durable project state is what lets Tutor resume. The roadmap, help preference,
and project decisions must survive closing the program and starting it again.

### What the learner already knows

- functions and returned dictionaries
- nested dictionaries and lists
- command-line conditions
- reading and displaying dictionary values

### New concepts

- importing `json` and `Path`
- converting Python data to JSON and back
- reading and writing a text file
- handling a missing state file

### Learning substeps

1. Save the current context to `.tutor/state.json`.
2. Run the program and inspect the file.
3. Load the file on the next run.
4. Keep a safe default when the file does not exist.

All four persistence substeps are complete, including loading the saved value
and using a safe default when the state file is missing.

### Success condition

- `show` reads the project context from the saved file
- changing a value in the saved file changes the next `show` result
- a missing state file does not crash the program
- no global learner state or model integration is added yet

### Verification

```bash
python3 kiko.py show
cat .tutor/state.json
```

Then change one saved value, run `show` again, and confirm that Kiko displays
the changed value.

## Step 4 — Read global learner knowledge and reference

### Objective

Load the private global learner profile and personal programming reference so
Kiko can recognize concepts already encountered in another project.

### Why it matters

The learner is the owner of knowledge across projects. A new project should not
restart every lesson from zero, while project-specific progress stays local.

### What the learner already knows

- functions, dictionaries, JSON, and file paths
- checking whether a file exists
- separating state creation, loading, and command handling

### New concept

- reading a second global state source and selecting only relevant values

### Success condition

- Kiko can read the global learner JSON without copying it into project state
- `show` displays only a small relevant learning summary
- missing global state is handled safely
- project state and learner state remain separate files
- no model calls or VS Code code are added

### Initial guidance

Treat the global profile as a separate owner and source. Read it, select the
learner concepts relevant to the current project language, and keep the rest
out of the project context. Do not merge the two dictionaries into one file.

## Later checkpoint intent

### Step 2 — Versioned project state

Add only the project identity, schema version, roadmap position, and help
preference needed by Tutor Core. Learn nested data and schema evolution basics.

### Step 3 — Project-local persistence

Persist the state under `.tutor/` and recover safely when it is missing or
invalid. Learn JSON, paths, file boundaries, and validation.

### Step 4 — Global learner state

Read the private cross-project learner profile without copying it into the
project. Learn ownership boundaries and merging relevant context.

### Step 5 — Evidence-based knowledge

Record introduced, assisted, independent, and reliable usage from learner work.
Keep reference entries separate from competence evidence.

### Step 6 — Pedagogical context

Classify the current request, choose progressive help, and compile only relevant
learner/project context. Side questions must not silently change the roadmap.

### Step 7 — Expert boundary

Define one small provider-neutral request/result seam and prove Tutor behavior
with a fake expert before adding Codex.

### Step 8 — App Server lifecycle

Start the local Codex App Server over `stdio`, initialize it, manage one thread,
consume events, and close it cleanly.

### Step 9 — Structured Codex turn

Send a bounded read-only repository question with the project working directory
and validate a structured expert result before Tutor displays it.

### Step 10 — Standalone vertical slice

Connect local state, Tutor policy, fake/Codex expert selection, learner input,
and learner-facing output through the Python CLI.

### Step 11 — VS Code sidebar

Create a minimal TypeScript extension that renders Tutor messages and talks to
the Python process. Do not duplicate pedagogy in TypeScript.

### Step 12 — v0.1 acceptance

Return to a real project, adapt guidance to prior knowledge, review a
learner-authored change, update durable evidence, verify privacy boundaries, and
document the minimum installation path.
