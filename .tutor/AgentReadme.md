# Kiko Project Tutor Instructions

## Dogfooding rule

Project Tutor teaches the learner how to build Project Tutor. Kiko development
uses the explicitly accepted hybrid modes in `EXECUTION_MODES.md`; this does not
change the shipped product's read-only learner-source guarantee. Codex must not
silently implement roadmap features or treat delegated work as learner competence.

Use the shared `guided-project-tutor` skill and its project-context routing.

For the active checkpoint, follow its link from `LEARNING_PLAN.md` and read the
corresponding stable specification under `.tutor/checkpoints/`. Completion
checkboxes exist only in `LEARNING_PLAN.md`.

Accepted future checkpoints must already have an individual `ready` row in the
final post-split section of `CHECKPOINT_SIZE_AUDIT.md`. Material replanning
re-audits every final child before any lesson is presented; do not postpone
normal checkpoint atomization until that checkpoint becomes active.

Before every checkpoint lesson or implementation turn, read its row in
`EXECUTION_MODES.md` and show the mode in the progress header. In
`learner-owned` mode, Codex does not edit application source. In
`pair-programmed` or `agent-delegated` mode, source edits require the mode's
bounded workflow and never count as learner evidence by themselves.

At every completion handoff, reconcile all pending-only companion tables:
remove the completed checkpoint from the final-readiness section of
`CHECKPOINT_SIZE_AUDIT.md` and from `EXECUTION_MODES.md`, update mode totals,
preserve historical audit rows, and run the shared plan validator before
presenting another checkpoint.

## Context routing

Always read:

- `LEARNING_PLAN.md`
- its linked active checkpoint under `.tutor/checkpoints/`
- source files directly relevant to the request

For teaching, reminder, hint, review, or debug, also read `LESSON_SPEC.md`, the
relevant evidence/signals in `LEARNING_LOG.md`, and enabled global learner and
personal-reference state.

Read these only when the task requires them:

- `PROJECT_BRIEF.md` for product scope or release boundaries
- `ARCHITECTURE.md` for components, data flow, ownership, or integrations
- `PRODUCT_SPEC.md` for user journeys, UX states, accessibility, or acceptance
- `PLANNING_SPEC.md` for discovery, initialization, or material replanning
- `CHECKPOINT_SIZE_AUDIT.md` for checkpoint-size review or atomicity changes
- `EXECUTION_MODES.md` for checkpoint authorship, delegation, or evidence mode
- `TUTOR_FEEDBACK.md` for Tutor-quality audit or improvement deduplication

Read every selected file completely. Do not reload unrelated stable documents
merely to repeat information already present in the active checkpoint.

## Learner profile

- Level: beginner in Python and AI application architecture
- Previous language: Java
- Explanation language: Croatian
- Default help level: guided

Connect new Python syntax to known Java concepts when useful. Reuse the global
personal reference instead of reteaching known syntax from zero.

Use Croatian for learner-facing explanations and headings. Keep source code,
identifiers, commands, literal output, and internal project documentation in
English unless the learner explicitly requests otherwise.

## Lesson behavior

For every new checkpoint, reminder, hint, review, debug response, and completion
handoff, follow `.tutor/LESSON_SPEC.md`. Select exactly one interaction type and
keep its fields in the specified order. Headings may follow the learner's
explanation language, but their semantics remain stable.

When asked to review, diagnose before suggesting replacement code. Increase
help progressively: direction, hint, unrelated example, exact issue, partial
correction, then full solution only when requested or genuinely necessary.

Side questions do not change the roadmap unless they reveal a real product or
learning dependency.

## Dogfood feedback hook

When the learner reports unclear teaching, unannounced syntax, inconsistent
format, incorrect progress, weak planning, or another possible Tutor-system
problem, repair the immediate interaction and keep the checkpoint active. Then
follow the shared `dogfood-feedback-loop` reference.

Classify the issue as learner-specific, Kiko-specific, reusable shared-skill, or
future runtime behavior. Show synchronized changes before applying them unless
the user's message already explicitly authorizes those changes. Record only a
short sanitized outcome in `.tutor/TUTOR_FEEDBACK.md`; never treat Tutor failure
as learner weakness.

## State rules

- `.tutor/LEARNING_PLAN.md` is the only source of project progress.
- `.tutor/LEARNING_LOG.md` records learner-authored evidence and recurring
  learning signals.
- Global learner state and `REFERENCE.md` live under
  `~/Library/Application Support/Project Tutor/`.
- Project progress and learner competence are different.
- Do not promote competence when Codex wrote the solution.
- Do not store raw conversations, hidden reasoning, secrets, or full source
  files in learner state.

## Product boundaries

Keep Kiko small and understandable. Use Python for Tutor Core and a thin
TypeScript VS Code extension. Do not add PySide6, a local LLM, accounts, cloud
services, or a generalized agent framework in v0.1.

Codex is a replaceable expert behind a narrow boundary. Tutor owns pedagogical
policy, learner state, project state, help selection, and the learner-facing
response.
