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
- Current product truth: Kiko reads global learner state separately and selects
  Python concept summaries; it does not yet read the personal reference.
- Next implementation: Step 4C — read the personal reference without copying
  it into project state.
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

### Learning substeps

1. [x] Read the global learner profile and display previous languages.
2. [x] Select relevant concept summaries for the current project.
3. [ ] Read the personal reference without copying it into project state.

Substeps 1 and 2 are complete. The next lesson covers only substep 3.

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

## Atomic implementation roadmap

Each unchecked item below is one future lesson or one tightly bounded review.
Completion requires its verification, not merely code that appears plausible.
The learner writes all application-source changes.

### Step 4C — Read the personal reference

- [ ] Add a function that locates the global `REFERENCE.md` beside
  `learner.json`.
- [ ] Return safe empty text when the reference file does not exist.
- [ ] Display a deliberately small reference preview through `show`; do not
  copy the reference into `.tutor/state.json`.
- [ ] Verify normal and missing-file behavior.

**Exit condition:** Kiko reads project state, learner state, and reference as
three separate sources, while `.tutor/state.json` remains project-only.

### Step 5 — Conservative learner evidence and reference updates

#### 5A — Describe one evidence record

- [ ] Define the minimum fields: project, checkpoint, learner action, help,
  and date.
- [ ] Add a pure function that creates one evidence dictionary; do not write a
  file yet.
- [ ] Verify that the result contains no source code, conversation history, or
  private unrelated data.

#### 5B — Update an encountered concept conservatively

- [ ] Find one concept by its lightweight ID.
- [ ] Append one evidence record without deleting existing evidence.
- [ ] Keep the stage at `assisted` when task-specific help was used.
- [ ] Verify that an absent concept is added as `introduced` or `assisted`, as
  supported by observable learner work.

#### 5C — Save global learner state safely

- [ ] Write the updated global learner JSON only after a completed review.
- [ ] Preserve profile fields, unrelated concepts, and valid existing evidence.
- [ ] Verify one update with a temporary, known concept and inspect the result.

#### 5D — Grow the personal reference separately

- [ ] Add one short syntax entry only after real learner use.
- [ ] Keep it separate from competence stage and evidence.
- [ ] Verify that a reference update never changes learner competence by itself.

**Exit condition:** learner evidence and syntax memory can be updated without
merging either into project state or overstating competence.

### Step 6 — Tutor policy and bounded context

#### 6A — Represent a learner request

- [ ] Add a small request shape containing the question and requested help.
- [ ] Keep it in memory for one CLI invocation; do not persist conversation
  transcripts.
- [ ] Verify that an empty or whitespace-only question is rejected clearly.

#### 6B — Select the assistance mode

- [ ] Recognize `teach`, `remind`, `hint`, `review`, `debug`, and `unblock`.
- [ ] Use the project help preference when the request does not specify one.
- [ ] Verify each mode with deterministic input examples.

#### 6C — Build a Syntax preflight

- [ ] Select relevant known syntax from the personal reference.
- [ ] Declare required new syntax before showing it.
- [ ] Declare related syntax that is intentionally not used yet when useful.
- [ ] Verify that a lesson example cannot contain unannounced syntax.

#### 6D — Compile minimal Tutor context

- [ ] Combine only the active checkpoint, selected concepts, relevant reference
  entries, project decisions, and current learner request.
- [ ] Keep raw global profile, full roadmap, full reference, and conversation
  history out unless a specific field is needed.
- [ ] Verify the exact context dictionary printed by a development-only command.

**Exit condition:** Kiko can turn one learner question into a small,
pedagogically bounded context without calling any model.

### Step 7 — Provider-neutral expert boundary with a fake expert

#### 7A — Define request and result shapes

- [ ] Define the minimum `expert_request` fields Kiko sends outside its core.
- [ ] Define the minimum `expert_result` fields Kiko accepts: explanation,
  hints, uncertainty, and proposed knowledge signals.
- [ ] Verify that neither shape lets an expert write application source.

#### 7B — Define one provider operation

- [ ] Introduce one `ask(expert_request)` operation.
- [ ] Keep Tutor policy and persistence outside this operation.
- [ ] Verify a caller can use the operation without knowing provider details.

#### 7C — Implement a deterministic fake expert

- [ ] Return a fixed, valid result for a known request.
- [ ] Return a clear controlled error for an unsupported request.
- [ ] Verify Tutor Core behavior without Codex installed or running.

**Exit condition:** Kiko's tutoring flow works against a fake expert, proving
the provider seam before live protocol complexity is introduced.

### Step 8 — Codex App Server adapter lifecycle

#### 8A — Start and stop the local process

- [ ] Launch `codex app-server --listen stdio://` as a child process.
- [ ] Capture standard input, output, and error without blocking the CLI.
- [ ] Close the child process cleanly when Kiko exits.

#### 8B — Exchange initialization messages

- [ ] Send the JSON-RPC `initialize` request.
- [ ] Validate the response before sending the `initialized` notification.
- [ ] Surface version, startup, or protocol failures as explicit Tutor errors.

#### 8C — Create or resume one thread

- [ ] Start one App Server thread using the selected project working directory.
- [ ] Keep the thread identifier as session data, not learner competence data.
- [ ] Verify a resumed invocation uses the same thread when appropriate.

#### 8D — Handle lifecycle events defensively

- [ ] Read JSONL messages one at a time.
- [ ] Handle expected completion and error events.
- [ ] Ignore or report unknown notifications without crashing.

**Exit condition:** the adapter completes the App Server lifecycle reliably but
does not yet expose a live tutoring answer through the CLI.

### Step 9 — One structured, read-only Codex tutoring turn

#### 9A — Compose the bounded expert request

- [ ] Convert Step 6's minimal Tutor context into an expert request.
- [ ] State the active objective, allowed help level, no-source-edit boundary,
  and expected result shape.
- [ ] Include only exact relevant source files, not the whole repository.

#### 9B — Start and collect one turn

- [ ] Start one turn on the App Server thread.
- [ ] Collect assistant messages and completion status.
- [ ] Handle approval requests as errors in v0.1's read-only mode.

#### 9C — Validate the returned result

- [ ] Reject missing explanation, invalid fields, and unsupported actions.
- [ ] Treat proposed knowledge signals as suggestions, not durable state.
- [ ] Verify a valid result is converted to a learner-facing response.

**Exit condition:** one real Codex response can help with a bounded question,
while Kiko retains policy, validation, and source-edit authority.

### Step 10 — Standalone Tutor CLI vertical slice

#### 10A — Add learner-facing commands

- [ ] Add one command to ask for help and one to request review.
- [ ] Keep `help` and `show` working as inspection commands.
- [ ] Verify usage messages for missing or malformed arguments.

#### 10B — Connect the full in-memory flow

- [ ] Load state and reference.
- [ ] Classify the request and compile bounded context.
- [ ] Call fake or Codex expert, validate the result, and print the response.
- [ ] Verify fake-expert mode separately from live-Codex mode.

#### 10C — Review learner-authored work

- [ ] Ask the expert for read-only observations about selected files.
- [ ] Present the first actionable issue before offering a correction.
- [ ] Verify Kiko itself never edits learner application source.

#### 10D — Persist only verified learning outcomes

- [ ] Update roadmap handoff and evidence after accepted learner work.
- [ ] Update personal reference only for syntax actually used.
- [ ] Verify a later CLI run resumes from durable state rather than chat memory.

**Exit condition:** the Python CLI demonstrates the complete learning loop for
one local project.

### Step 11 — Thin TypeScript VS Code extension

#### 11A — Create the extension shell

- [ ] Create a minimal TypeScript extension with one sidebar view.
- [ ] Add activation only for the Tutor view or explicit Tutor command.
- [ ] Verify the extension can be launched in the VS Code extension host.

#### 11B — Render a minimal learner interface

- [ ] Show the active checkpoint, a question input, and a response area.
- [ ] Show loading, error, and approval-required states.
- [ ] Keep teaching policy and learner-state logic out of TypeScript.

#### 11C — Connect to the Python process

- [ ] Start the Python Tutor process locally.
- [ ] Send one JSONL request and receive one JSONL response.
- [ ] Verify malformed messages produce a visible, non-crashing error.

#### 11D — Support the two v0.1 actions

- [ ] Send a help request from the sidebar.
- [ ] Send a read-only review request from the sidebar.
- [ ] Render validated Python Tutor responses without reshaping pedagogy.

**Exit condition:** VS Code is a thin input/output surface over the proven
Python core, not a second Tutor implementation.

### Step 12 — End-to-end v0.1 acceptance

- [ ] Open one real learning project from VS Code.
- [ ] Demonstrate global knowledge and project state remain separate.
- [ ] Ask a bounded question and receive assistance matched to learner history.
- [ ] Change source as the learner, then request and receive read-only review.
- [ ] Record only verified learner evidence and one justified reference entry.
- [ ] Restart the CLI and prove durable state resumes correctly.
- [ ] Simulate a missing global file and an App Server failure; verify clear,
  safe errors.
- [ ] Document the smallest local installation and launch path.

**Exit condition:** one learner completes a real, durable, repository-aware
tutoring loop without Kiko becoming an automatic code-writing agent.
