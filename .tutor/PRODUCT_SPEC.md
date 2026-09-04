# Kiko Product Experience Specification

## Status and authority

This document defines how Kiko should behave for a learner. The product brief
owns product scope, the architecture owns technical boundaries, the learning
plan owns implementation progress, and this specification owns user-visible
flows and pedagogical acceptance.

Kiko v0.1 proves the central flow. Kiko v1.0 turns the same flow into a tested,
installable local product with a CLI and VS Code surface.

## Product promise

Kiko helps a learner finish real software while becoming more capable of doing
the work independently. It remembers relevant learning across projects,
explains unfamiliar syntax before using it, provides progressively stronger
help, reviews learner-authored work, and resumes from durable local state.

Kiko is not an automatic application builder. The learner owns substantive
application-source changes. Codex is a replaceable read-only reasoning provider;
Kiko owns teaching policy, context selection, validation, and durable learning
state.

## Primary user and job

The primary v1.0 user is one learner on macOS who is learning Python or Java by
building a real local project in VS Code.

The user's main job is:

> Help me understand and complete the next useful part of my project without
> taking authorship of the code away from me, and remember enough that I do not
> restart from zero next time.

## Supported product surfaces

### VS Code extension

The primary everyday surface. It shows project recognition, the active
checkpoint, help level, provider status, Tutor responses, and actions for asking,
requesting a hint, requesting review, cancelling, retrying, and diagnostics.

### Kiko CLI

The supported diagnostic and non-editor surface. It exercises the same Python
Tutor Core and provides project initialization, status, help, review, provider
diagnostics, and version information. It must not implement a second teaching
policy.

## Non-negotiable behavior

1. **Learner authorship:** Kiko and its expert do not edit substantive learner
   source in v1.0.
2. **Syntax before use:** unfamiliar syntax is explained before it appears in a
   lesson example or task.
3. **Progressive assistance:** Kiko begins at the requested or appropriate help
   level and increases help only when asked or when genuine difficulty is
   evident.
4. **One bounded task:** a teaching response ends with one focused task, one
   verification method, and expected behavior.
5. **Evidence after observation:** completion and competence change only after
   learner-authored work is reviewed; model output is never competence evidence.
6. **Separate state ownership:** project progress stays with the project;
   cross-project competence and the personal reference stay in private global
   learner state.
7. **Minimal context:** one expert request contains only the active objective,
   current request, relevant concepts/reference entries, exact relevant files,
   help boundary, and required result shape.
8. **Safe failure:** missing auth, corrupt state, provider failure, cancellation,
   or unsupported versions produce clear recovery choices and never masquerade
   as teaching feedback.
9. **Side questions preserve progress:** answering a related question does not
   silently complete or replace the active checkpoint.
10. **Local learner control:** the user can inspect, export, retain, reset, or
    delete durable learner data through explicit actions.
11. **Controlled Tutor improvement:** explicit reports of unclear or broken
    teaching repair the current interaction and produce optional sanitized
    product feedback without changing competence or self-modifying Kiko.

## Canonical teaching response

Every interaction follows exactly one format from `LESSON_SPEC.md`. That file is
the single source for field order, progress orientation, Syntax preflight,
explanation, task, verification, review, debug, and completion handoff.

Chat, CLI, and VS Code may style those fields differently, but may not invent,
remove, or reorder pedagogical content. Headings are localized to the learner's
explanation language while their semantic meaning stays stable.

## Progressive help ladder

Kiko follows the hint ladder and interaction-specific formats in
`LESSON_SPEC.md`. It records the actual help used. Receiving stronger help can
complete a project task, but it does not prove independent competence.

## Durable state changes

| User action | Project state | Global learner state | Personal reference |
| --- | --- | --- | --- |
| Ask a question | no change | no change | no change |
| Request a hint | no change | no competence promotion | no change |
| Receive an expert answer | no change | no change | no change |
| Failed review | checkpoint stays active | no promotion; repeated meaningful difficulty may later become a signal | no automatic addition |
| Accepted learner work | advance verified checkpoint and handoff | append minimal evidence and conservatively update stage | add only genuinely new syntax actually used |
| Initialize a project | create confirmed project-local Tutor files | preserve existing profile | preserve existing reference |
| Change help preference | update the owning preference field | no competence change | no change |
| Report unclear/broken Tutor guidance | checkpoint stays active | no competence change | no change; optional sanitized feedback is separate |

Raw conversations, hidden reasoning, secrets, full source files, and unverified
model proposals are never stored as learner evidence.

## Tutor-quality feedback flow

When the learner says that an explanation is unclear, syntax was skipped, the
format changed, progress is wrong, or help is inappropriate:

1. Kiko repairs the current interaction and preserves the active checkpoint.
2. It classifies the signal as learner-specific, project-specific, reusable
   Tutor behavior, or product/runtime behavior.
3. It shows a short sanitized feedback candidate and lets the user keep, edit,
   export, or discard it.
4. The feedback remains separate from learner competence and reference state.
5. Installed Kiko does not rewrite its own code, skill, or accepted roadmap.

During Kiko development, accepted candidates follow the shared dogfood loop and
map to a skill/project change plus an observable regression check. Outcomes are
recorded in `.tutor/TUTOR_FEEDBACK.md` without raw conversation text.

## Golden journey 1 — First installation and first project

### Preconditions

- Kiko Core/CLI and the VS Code extension were installed from release artifacts.
- The user opens a supported local project with no `.tutor/` directory.

### Visible flow

1. The sidebar says that this is not yet a Kiko learning project.
2. Kiko checks its own version, Core connection, Codex CLI availability, and
   authentication without exposing credentials.
3. Kiko extracts confirmed facts, open decisions, safe technical assumptions,
   and future ideas from the user's natural-language description.
4. Kiko resolves every product-defining open decision through short beginner-
   friendly question rounds defined in `PLANNING_SPEC.md`.
5. The user confirms a plain-language brief before Codex drafts any roadmap.
6. Kiko validates and critiques the candidate plan for coverage, atomicity,
   ordering, teaching quality, and finished-product work.
7. The user reviews the plan summary and first checkpoint before accepting it.
8. Only after acceptance does Kiko create the project Tutor files and display
   the first small checkpoint.

### State changes

- Project Tutor files are created only after confirmation.
- Existing global learner data is never replaced.
- No application source is generated.

### Acceptance

- A beginner reaches the first task without terminal setup or editing paths.
- No plan is generated while a product-defining decision remains unresolved.
- The accepted roadmap traces all required behavior through implementation,
  testing, packaging, and finished-product acceptance.
- Cancelling initialization leaves the workspace unchanged.
- Reopening the workspace recognizes the same project.

## Golden journey 2 — Continue an existing project

### Preconditions

- The project contains valid Tutor state and at least one completed checkpoint.

### Visible flow

1. Kiko recognizes the workspace and shows the current checkpoint and handoff.
2. It loads only relevant cross-project concepts and reference entries.
3. It offers to continue, ask a side question, or request review.
4. Continuing presents the next lesson using the canonical teaching response.

### State changes

- Merely opening or reading a project changes no progress or competence.
- A side question does not replace the active checkpoint.

### Acceptance

- The displayed checkpoint matches durable project state, not chat history.
- The lesson reuses relevant known syntax and does not reteach everything.

## Golden journey 3 — Learn one new concept

### Preconditions

- One active checkpoint has a defined success condition.

### Visible flow

1. Kiko explains one objective and why it matters.
2. Syntax preflight separates known, new, and deliberately excluded syntax.
3. Every new construct has a small isolated example.
4. The project example does not contain any unannounced construct.
5. Kiko gives one focused learner task and exact verification.
6. Kiko stops and waits for the learner to implement it.

### State changes

- Explanation alone does not complete the checkpoint.
- A newly explained concept may be `introduced`; stronger stages require
  learner-authored evidence.

### Acceptance

- A syntax audit finds no unannounced method, shorthand, import, or library call.
- The task can be attempted without copying a complete project solution.

## Golden journey 4 — Ask for a hint or debug help

### Preconditions

- The learner is working on an active task and reports uncertainty or failure.

### Visible flow

1. Kiko identifies whether the request is a hint, explanation, debugging, or
   explicit request for a solution.
2. It begins at the smallest useful help level.
3. For debugging, it distinguishes observed output from assumptions and points
   to the first actionable issue.
4. If the learner remains blocked, Kiko moves one level down the help ladder.
5. Kiko keeps the original task and verification visible.

### State changes

- Hint requests do not advance the roadmap.
- One typo or one difficulty does not set `needs_reinforcement`.
- The actual assistance level is retained only when later recording accepted
  learner work.

### Acceptance

- The first response does not reveal a full solution unless explicitly asked.
- A failed command is never presented as successful learning evidence.

## Golden journey 5 — Review learner-authored work

### Preconditions

- The learner states that the task is ready for review.

### Visible flow

1. Kiko reads only relevant project files and runs proportionate read-only
   verification.
2. If acceptance fails, Kiko explains the first actionable issue and preserves
   the active checkpoint.
3. If acceptance passes, Kiko explains what behavior was verified.
4. Kiko shows the proposed project-progress, evidence, and reference changes.
5. Kiko advances to the next checkpoint only after the review is accepted.

### State changes

- Project plan and handoff are updated only after successful verification.
- Global evidence records project, checkpoint, learner action, help, and date.
- Personal reference receives only newly used useful syntax.
- Codex-written code is never recorded as learner competence.

### Acceptance

- Review can be reproduced with an exact command or observable check.
- Stored evidence contains no raw conversation or source-code copy.
- Reopening the project resumes from the newly verified checkpoint.

## Golden journey 6 — Transfer learning across projects

### Preconditions

- The global learner profile contains evidence from another project.
- The user opens a different Python or Java learning project.

### Visible flow

1. Kiko reads the second project's local roadmap independently.
2. It selects only concepts and reference entries relevant to the current
   language and task.
3. It briefly connects a known general concept to unfamiliar language syntax
   when useful.
4. It does not imply mastery from unrelated project completion.

### State changes

- Project progress never moves between projects.
- New evidence identifies the project where the action occurred.

### Acceptance

- Python-specific syntax is not shown as known in an unrelated Java task.
- Relevant general knowledge reduces repetition without skipping new syntax.

## Golden journey 7 — Recover from a product failure

### Preconditions

- Codex is unavailable, authentication expired, a process stopped, state is
  corrupt, or a version is unsupported.

### Visible flow

1. Kiko names the failing boundary: project state, learner state, Core process,
   Codex process, authentication, protocol, or compatibility.
2. It shows a safe action: retry, restart, reauthenticate, restore backup,
   export data, or use fake-expert/demo mode where appropriate.
3. Diagnostics contain versions and sanitized technical details.
4. Teaching feedback is not fabricated while the expert boundary is broken.

### State changes

- Failed operations do not partially advance progress or competence.
- Corrupt data is preserved for recovery before replacement or migration.

### Acceptance

- The sidebar and CLI remain responsive and provide the same root cause.
- Retry or restart does not leave duplicate child processes.
- Recovery never silently deletes learner data.

## VS Code view states

The sidebar has a small explicit state model:

- **Setup:** no recognized project or a missing dependency needs action.
- **Ready:** project, checkpoint, help level, and provider status are visible.
- **Working:** one request is running; cancel remains available.
- **Response:** the Tutor result and next learner action are visible.
- **Review:** verification result and proposed durable updates are visible.
- **Recoverable error:** cause, safe detail, and retry/recovery action are shown.
- **Blocked:** an unsupported version or unsafe requested action must be resolved
  outside the current turn.

The view preserves keyboard focus, supports selectable text, uses readable
contrast, and does not require the mouse for primary actions.

## CLI and extension parity

Both surfaces must support project recognition, status, asking for help,
requesting review, cancellation, diagnostics, and version reporting. Their
formatting may differ, but Tutor decisions and durable state changes must be
identical because Python Tutor Core owns them.

## Pedagogical quality gates

The release fails even when the software runs if any of these are false:

- every new-lesson fixture passes the no-unannounced-syntax audit
- every interaction fixture matches the required field order in
  `LESSON_SPEC.md`
- Tutor-quality feedback preserves the checkpoint and cannot lower competence
- every accepted reusable feedback record names a regression check
- stronger help is recorded and does not produce false independent competence
- an expert response cannot directly advance a checkpoint
- a side question cannot replace the active task
- irrelevant cross-project knowledge is excluded
- learner-source files remain unchanged during help and review flows
- a beginner usability run can explain the next action without reading internal
  documentation

## Product success evidence

v1.0 requires local, privacy-preserving evidence rather than analytics:

- automated tests for deterministic policies and boundaries
- recorded golden-journey acceptance runs using fixtures
- one clean-profile installation and uninstall run
- one real Python learning-project dogfood run
- one cross-project transfer run involving Python and Java concepts
- one beginner usability session focused on comprehension, not task speed

## Out of scope for v1.0

- automatic application-source implementation
- cloud accounts, synchronization, subscriptions, or collaboration
- local model inference
- non-VS Code editor extensions
- mobile or web clients
- a general-purpose autonomous agent framework
- a large programming-concept ontology or behavioral analytics platform

These can enter a later backlog only after observed use demonstrates a need and
the product brief is deliberately revised.

## Roadmap traceability

- KIKO-001–022 preserve the learning foundation and implement safe state,
  reference, evidence, package, test, and ownership boundaries.
- KIKO-023–028 implement teaching policy, Syntax preflight, canonical
  interactions, bounded context, and Tutor-quality feedback.
- KIKO-029–034 implement idea discovery, readiness, plan validation, and user
  acceptance.
- KIKO-035–045 implement and secure the replaceable expert boundary.
- KIKO-046–056 prove the CLI and initial VS Code vertical slice.
- KIKO-057–062 complete onboarding, recovery, privacy, accessibility, and the
  deterministic product-quality gate.
- `PLANNING_SPEC.md` provides the mandatory discovery and plan-quality gates for
  journeys 1 and 2.
- KIKO-063–071 package and harden the supported product surfaces.
- KIKO-072–076 execute all golden journeys as finished-product acceptance.
