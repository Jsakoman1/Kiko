# Kiko Lesson Interaction Specification

## Authority

This document is the single project source for learner-facing lesson, reminder,
hint, review, debug, and completion-handoff structure. Product behavior lives in
`PRODUCT_SPEC.md`; progress lives in `LEARNING_PLAN.md`; evidence lives in
`LEARNING_LOG.md`.

Chat, CLI, and the VS Code sidebar may render information differently, but they
must preserve the same fields, meaning, and order. Visible headings follow the
learner's current explanation language. Source code, identifiers, commands, and
literal output remain in the project's technical language.

For Kiko, learner-facing explanations and headings use Croatian. Source code,
identifiers, commands, literal output, and internal technical documentation use
English.

## Interaction types

Every Tutor response selects exactly one type:

- `new_checkpoint`
- `reminder`
- `hint`
- `review_failed`
- `review_passed`
- `debug`
- `completion_handoff`

Do not combine types merely to save a turn. In particular, a passing review may
name the next checkpoint but must not start teaching it.

## Shared progress header

Every interaction begins with:

```text
Step: <checkpoint ID and title>
Status: <not started | in progress | needs revision | verified>
Last verified: <checkpoint or observable behavior>
Today: <purpose of this interaction>
```

For the current Kiko handoff, a new lesson would begin conceptually as:

```text
Step: KIKO-011 — Read the personal reference (legacy 4C)
Status: in progress
Last verified: KIKO-010 — Selected Python concept summaries
Today: read REFERENCE.md safely without copying it into project state
```

The progress header reports project state. If competence is relevant, show it
separately with its evidence level; never present `assisted` or `independent` as
checkpoint status.

## New checkpoint format

### 1. Where we are

Show the shared progress header.

### 2. Problem to solve

Explain the missing product behavior first. State why it matters to the user and
where it fits in Kiko's architecture. Do not begin with syntax or replacement
code.

### 3. Done when

State the observable success conditions and the important boundary or failure
case for this checkpoint.

### 4. Syntax preflight

Always show:

- **Known syntax:** only the relevant syntax already encountered.
- **New syntax:** every unfamiliar construct needed now.
- **Not used yet:** related shortcuts excluded from this lesson when naming them
  prevents surprise.

Each new syntax card contains:

- exact syntax or method name
- plain-language meaning
- input and returned value, or observable effect
- one tiny isolated example unrelated to Kiko's solution
- one likely mistake only when useful

No example or task may contain an unannounced method, shorthand, import, or
library call. If another construct becomes necessary, update the preflight
before using it.

### 5. Mental model and code flow

Explain which values move between which functions, who owns each responsibility,
and which states remain separate. Explain the relevant code shape without giving
the complete Kiko solution. Compare with Java only when it shortens the learner's
path to understanding.

### 6. Small example

Show a minimal unrelated example. Explain the lines containing new syntax. This
section may be omitted only when no new concept is introduced and the personal
reference already provides a sufficient example.

### 7. Your task

Give exactly one bounded application-source change for the learner. Name the
file or location and behavior without supplying the complete solution.

### 8. Verification

Give the exact command or visible action, expected successful behavior, and one
safe edge-case check when relevant.

### 9. Stop point

State what the learner should send back: code, output, or a review request. Stop
before introducing another task.

## Reminder format

1. Progress header
2. Direct plain-language answer
3. One tiny example or personal-reference entry
4. Connection to the active task
5. Unchanged learner action and verification

A reminder does not change roadmap progress or competence.

## Hint format

1. Progress header
2. Current help level
3. One hint at that level
4. One next learner attempt
5. Unchanged verification

The help ladder is:

1. restate goal and relevant concept
2. directional hint
3. small unrelated example
4. faulty assumption or exact location
5. partial Kiko-specific correction
6. full solution only after explicit request or genuine repeated blockage

Advance one level per genuine retry unless the learner explicitly requests
stronger help. Do not repeat the whole lesson for a hint.

## Failed review format

1. Progress header with `needs revision`
2. Checks performed and observed results
3. Verdict: not yet verified
4. First actionable issue and why it matters
5. One proportional hint or correction
6. Next learner change
7. Exact re-verification

Do not advance progress or promote competence.

## Passing review format

1. Progress header with `verified`
2. Checks performed and observed results
3. Verdict: checkpoint verified
4. Accepted learner-authored behavior
5. Actual help level used
6. Project, evidence, and personal-reference updates
7. Next checkpoint title only
8. Stop and wait

## Debug format

1. Progress header
2. Expected behavior
3. Observed behavior and evidence
4. Confirmed cause or one explicitly labeled hypothesis
5. One next diagnostic or correction attempt
6. Exact action and expected diagnostic result

Do not claim a cause without evidence. Debugging does not complete a checkpoint
by itself.

## Completion handoff format

1. Verified checkpoint
2. Evidence that passed
3. State/files updated
4. State/files deliberately unchanged
5. Personal-reference additions, if any
6. Next checkpoint and why it follows
7. Stop point

## Canonical Tutor interaction data

Tutor Core should eventually produce this semantic structure before any surface
renders it:

```text
interaction_type
checkpoint: id, title, status, last_verified
purpose
problem
why_it_matters
success_conditions[]
syntax_preflight:
  known[]
  new[]: syntax, meaning, input_output_or_effect, example, common_mistake
  not_used_yet[]
mental_model
small_example
task
verification: command_or_action, expected_behavior, edge_case
review: checks, observations, verdict, accepted_behavior, help_used
debug: expected, observed, cause_or_hypothesis, next_experiment
state_updates: project, learner, reference
next_action
```

Only fields required by the chosen interaction type are populated. Python Tutor
Core owns the content and order. Chat, CLI, and VS Code presenters do not add,
remove, or reinterpret pedagogical decisions.

## Pre-send quality gate

- Exactly one interaction type is selected.
- Progress matches durable project state.
- Required fields are present and ordered.
- A new checkpoint explains the problem and product reason before syntax.
- Every construct used in examples and tasks is known or explained first.
- Only relevant known syntax is listed.
- The learner receives one owned action and exact verification.
- No unverified progress or competence update is claimed.
- The response stops at the correct boundary.

## Tutor-quality feedback hook

If the learner reports unclear teaching or a violation of this specification:

1. acknowledge the concrete gap
2. preserve the active checkpoint and learner competence
3. repair the current interaction using the correct format
4. classify the issue through the shared dogfood feedback loop
5. propose synchronized skill, project, runtime, and regression changes when
   the issue is reusable
6. record only the accepted sanitized outcome in `TUTOR_FEEDBACK.md`

The learner does not need to remember a command or feedback format. Natural
language such as “this is unclear” is sufficient to trigger the audit.
