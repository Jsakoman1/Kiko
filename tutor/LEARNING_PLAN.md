# Kiko v0.1 Learning Plan

## One-sentence definition

Kiko v0.1 is a command-line context notebook that stores one mission, its
rules, and useful notes in a local JSON file.

## Why this is the first version

Before an AI model can work well for us, it needs clear context. Kiko v0.1
creates that context without trying to solve planning, multi-agent work, model
selection, databases, or a user interface.

## Learning contract

You are the developer. You write every line of Kiko's source code.

I am the teacher. For each step, I will explain the purpose, relevant Python
syntax, Java comparison, program logic, architecture impact, and how to verify
your work. I will not write or edit your source code or give you the complete
solution. I will show a small implementation example for each new syntax idea,
then you will write your own version. Before you use a syntax feature for the
first time, I will add a compact reference entry to
`tutor/learning_journal.md`.

Every lesson follows this order:

1. Goal in plain English
2. Why the step matters to Kiko
3. New syntax and a small implementation example
4. Java comparison when useful
5. Your task
6. Verification command and expected result
7. Review after you finish

After you complete a step, you can share the code, terminal output, or an error.
I will review it and help you understand the next correction or improvement.

## Progress checkpoint

- [x] Step 1: Created and ran a basic Python script.
- [x] Step 2: Added `main()` and the direct-entry check.
- [x] Step 3: Added command-line argument handling and the `help` command.
- [x] Step 4: Added the in-memory `context` dictionary and the `show` command.
- [ ] Step 5: Save and load the context as JSON. **NEXT**
- [ ] Step 6: Implement `init` and `show` as real Kiko commands.
- [ ] Step 7: Implement `rule` and `note` with persistent updates.
- [ ] Step 8: Manually verify v0.1 and review the program line by line.

## Current handoff

- Last verified behavior: `help` and `show` display the expected in-memory data.
- Next step: Step 5 — save and load the context as JSON.
- Blockers: None.

Current behavior is intentionally temporary: the mission, rules, and notes are
created in memory every time the program starts, so they disappear when the
program exits. Step 5 will give Kiko its first durable state.

## Syntax journal

`tutor/learning_journal.md` is our short Python syntax journal, not the whole lesson.
Simple entries use one or two lines. The lesson itself includes a small,
concrete implementation example so you can see how the syntax is used.

## Final v0.1 behavior

```text
Human or AI model
        |
        v
python3 kiko.py COMMAND
        |
        v
kiko.py
        |
        v
.kiko/state.json
```

Kiko will support only these commands:

```text
init "mission"     Create or replace the single mission
rule "text"        Add a permanent rule
note "text"        Add useful context
show               Display the complete current context
help               Display the command list
```

Example use:

```bash
python3 kiko.py init "Build a useful AI assistant"
python3 kiko.py rule "Keep the code simple"
python3 kiko.py note "The project uses Python"
python3 kiko.py show
```

The saved JSON will look approximately like this:

```json
{
  "mission": "Build a useful AI assistant",
  "rules": ["Keep the code simple"],
  "notes": ["The project uses Python"]
}
```

## What v0.1 does not include

- Tasks, task states, priorities, or dependencies
- Multiple missions
- Agent identities or parallel agents
- Databases, web servers, or graphical interfaces
- OpenAI API calls, MCP, embeddings, or memory search
- Authentication or user accounts
- External Python packages

These are future options, not missing work.

## Learning steps

### Step 1: A Python script that runs — COMPLETE

You create `kiko.py` and make it display a short welcome message.

Learn:

- A Python file is a script.
- `python3 kiko.py` runs it.
- `print()` is similar to `System.out.println()`.

Done when:

```bash
python3 kiko.py
```

prints a welcome message.

### Step 2: Functions and the program entry point — COMPLETE

You move the welcome behavior into a `main()` function and call it through the
standard `if __name__ == "__main__":` pattern.

Learn:

- `def` creates a function.
- Indentation replaces Java braces.
- `main()` is the closest equivalent to Java's `public static void main`.

Done when the behavior stays the same and the structure is understood.

### Step 3: Command-line arguments — COMPLETE

You read a command such as `help` from `sys.argv`.

Learn:

- Imports
- Lists
- Indexing and slicing
- `if` statements

Done when:

```bash
python3 kiko.py help
```

prints a command list.

### Step 4: The context data structure — COMPLETE

You create one in-memory Python dictionary containing a mission, rules, and
notes.

Learn:

- Dictionaries as the simple equivalent of a Java `Map`
- Lists for ordered values
- Strings and `None`

Done when `show` prints the in-memory context.

### Step 5: Save and load JSON — NEXT

You save the dictionary to `.kiko/state.json`, then load it again on the next
run.

Learn:

- `Path` for file locations
- `json.dumps()` and `json.loads()`
- Reading and writing UTF-8 files

Done when the mission remains after closing and rerunning the program.

### Step 6: Implement `init` and `show`

You turn the data structure into the first useful Kiko feature.

Learn:

- Function parameters
- Validation with small error messages
- Returning values

Done when a user can save a mission and display it later.

### Step 7: Implement `rule` and `note`

You add permanent rules and useful context to the saved state.

Learn:

- List `.append()`
- Reusing functions
- Small command dispatching

Done when the final v0.1 command list works.

### Step 8: Manual verification and review

Run every command, inspect the generated JSON, and explain the final program
line by line.

Learn:

- Debugging by observing state
- How data moves through a small program
- How to decide whether a new feature is worth adding

Done when you can describe Kiko's data flow without help.

## How we will work together

For each step, I will first explain the goal, the relevant Python syntax, and
the Java comparison. I will then show a very small diagram or pseudocode when
useful. You will implement only that step, run it, inspect the result, and ask
for a review before continuing.

You can start the first lesson by saying: `Start Kiko step 1.`
