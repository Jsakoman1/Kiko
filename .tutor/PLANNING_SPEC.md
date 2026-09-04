# Kiko Idea Discovery and Planning Specification

## Purpose and authority

This document defines how Kiko turns a learner's application idea into a
confirmed product brief and a complete, teachable implementation plan. It owns
the discovery questions, planning readiness gate, plan contract, completeness
audit, and user approval flow.

Codex may analyze requirements, propose technical choices, draft the plan, and
critique it. Codex does not invent unresolved product decisions on the user's
behalf. Kiko owns the workflow, validation, progressive disclosure, and durable
files.

## Required outcome

The planning flow must produce a plan that is:

- grounded in a product brief the user has confirmed
- complete from first source change through testing, packaging, delivery, and
  finished-product acceptance
- atomized into small, ordered, independently verifiable learning steps
- adapted to the learner's existing knowledge and requested explanation style
- explicit about assumptions, exclusions, risks, and deferred decisions
- traceable from every required product behavior to implementation and proof

The system cannot guarantee that a plan predicts every future discovery. It can
guarantee that known ambiguity is classified, product-defining ambiguity is
resolved, the draft passes explicit coverage checks, and later plan changes are
visible and justified.

## Planning state machine

```text
idea received
  -> facts extracted
  -> open decisions classified
  -> guided discovery rounds
  -> brief preview
  -> user confirms brief
  -> Codex drafts candidate plan
  -> deterministic structure validation
  -> Codex completeness critique
  -> repair and revalidate if needed
  -> user reviews plan summary
  -> user accepts plan
  -> project Tutor files are written
```

Cancellation before final acceptance must leave application source unchanged
and must not create a misleading active roadmap.

## Facts, decisions, assumptions, and ideas

Kiko keeps four categories separate during discovery:

- **Confirmed fact:** explicitly stated by the user or safely observed in an
  existing repository.
- **Open decision:** an answer is needed because different choices materially
  change the product, architecture, risk, cost, or learning path.
- **Technical assumption:** a reversible implementation choice Kiko can propose
  without asking a beginner to compare unfamiliar technologies.
- **Future idea:** useful but not required for the first finished release.

Kiko must not silently turn an open decision into a technical assumption. It
must not silently promote a future idea into required scope.

## What must be clarified with the user

Ask only when the answer is missing and materially changes the result.

### Product outcome

- What should the finished product enable someone to accomplish?
- What real problem does it solve, and what would make the project worth using?
- Is the goal a learning prototype, a personally usable tool, or a product
  intended for other users?

### Primary user and workflow

- Who is the first user?
- What is the main start-to-finish action the user must complete?
- Which secondary behaviors are required for the first release?

### Product surface and environment

- Is it a CLI, desktop, web, mobile, editor extension, service, library, or a
  combination?
- Which operating system, device, editor, or deployment environment matters?
- Must it work offline, locally, or across devices?

### Data, privacy, and lifecycle

- What information is created, read, stored, shared, or deleted?
- Is any data personal, secret, regulated, paid, or owned by another service?
- Must state survive restart, synchronize, export, migrate, or be removable?

### External systems and AI

- Which integrations are essential rather than optional?
- Who supplies credentials and what should happen when an integration fails?
- If AI is involved, what may it decide, what must be validated, and what action
  requires human control?

### Scope and completion

- What behavior is required for the smallest genuinely useful release?
- What is explicitly outside that release?
- What observable scenario proves the product is finished?

### Learning intent

- Which language or platform does the learner want to learn?
- What relevant concepts and languages have they used before?
- Do they prefer hints, guided teaching, or direct explanations?
- Are there time, dependency, cost, accessibility, or tooling constraints?

## Questions Kiko should usually not ask a beginner

Kiko normally proposes a conservative default for choices such as:

- folder and module names
- formatting, linting, and test-runner configuration
- minor library choices with no product-level consequence
- serialization details that remain local and reversible
- internal class/function decomposition
- exact protocol field names
- visual spacing, colors, and copy that do not affect accessibility or brand

The proposed default and its reason remain visible in the brief or architecture
as a technical assumption. The user can override it without needing to learn a
technology comparison first.

Kiko must ask when a technical-looking choice affects recurring cost, privacy,
vendor lock-in, deployment, accounts, platform support, data loss, legal terms,
or an irreversible architecture boundary.

## Beginner-friendly question policy

- Ask no more than three short questions in one round.
- Use product language before technical language.
- Explain in one sentence why a question matters.
- Offer a recommended default when one is safe.
- Always allow "I am not sure"; convert it into an explicit proposed assumption.
- Reuse prior answers and observed repository facts; never ask the same question
  again unless the answer conflicts with new information.
- After each round, summarize newly confirmed decisions and show only the next
  unresolved blockers.
- Do not show an exhaustive technical questionnaire to the learner.

Example:

> Should your notes stay only on this Mac, or should they synchronize between
> devices? This changes whether the first version needs accounts and a backend.
> For a first learning project, local-only is the recommended default.

## Open-decision classification

For every uncertainty, Kiko records:

- a short ID
- the question in beginner-friendly language
- why the answer matters
- classification: `blocking`, `deferrable`, or `future`
- current answer or proposed default
- source: user, repository observation, or Kiko assumption
- status: open or confirmed

An uncertainty is **blocking** when different answers change required behavior,
the primary surface, state ownership, privacy, external dependencies, release
definition, or learning path. All blocking decisions must be confirmed before
Codex receives the plan-generation request.

A **deferrable** decision may remain open only when the plan names the latest
step before which it must be resolved and earlier work is valid either way.

## Brief readiness gate

Kiko may request a plan draft only when all of these are true:

- product outcome and first user are confirmed
- primary workflow and required first-release behaviors are confirmed
- target surface and supported environment are confirmed
- required data and external-system boundaries are known
- material privacy, cost, deployment, and AI authority questions are resolved
- smallest useful release and explicit exclusions are confirmed
- finished-product acceptance scenario is stated in observable language
- learner language, experience, help preference, and constraints are known
- no blocking decision remains open
- every remaining assumption is visible and reversible

Readiness is a deterministic Kiko decision. Codex cannot declare its own input
complete merely because it can generate a plausible plan.

## Brief preview and confirmation

Before plan generation, Kiko shows a concise preview containing:

- one-sentence product promise
- primary user and primary workflow
- required first-release behaviors
- target surfaces and environments
- stored data and external integrations
- AI authority and validation boundary, when relevant
- explicit exclusions and future ideas
- proposed technical assumptions
- finished-product acceptance scenario
- learner goal and teaching preference

The user may confirm, correct, or reopen any decision. Kiko stores a confirmed
brief only after explicit acceptance.

## Codex planning request

Kiko sends Codex a bounded structured request containing:

- the confirmed brief
- learner profile summary and relevant prior concepts
- chosen product and architecture constraints
- known repository facts when extending an existing project
- required plan schema and atomicity rules
- mandatory coverage checklist
- no-source-edit and learner-authorship boundaries

It must not send unrelated learner history, secrets, an entire repository by
default, or unresolved product decisions disguised as facts.

## Candidate plan contract

### Release structure

The plan separates at least these outcomes when applicable:

1. foundation and smallest executable behavior
2. core domain behavior
3. state, data lifecycle, and migrations
4. external integrations behind replaceable boundaries
5. primary user workflow and all visible states
6. validation, errors, security, privacy, and accessibility
7. unit, integration, protocol, and end-to-end verification
8. packaging, deployment, onboarding, upgrades, and uninstall
9. clean-environment finished-product acceptance

Not every small project needs nine named phases, but no applicable concern may
disappear merely because the user is a beginner.

### Atomic checkpoint structure

Every implementation checkpoint contains:

- checkpoint kind: implementation, integration, acceptance, or decision
- stable ID and short title
- one observable outcome
- reason it matters to the product
- prerequisites and earlier checkpoints it depends on
- relevant knowledge the learner already has
- genuinely new concepts and syntax
- one bounded learner task
- exact verification command or observable action
- expected successful behavior
- failure or edge case introduced by this checkpoint
- explicit exclusions that prevent scope creep
- exit condition

The checkpoint's learner-facing presentation must be renderable through the
`new_checkpoint` contract in `LESSON_SPEC.md` without inventing missing progress,
problem, syntax, task, or verification information.

A checkpoint is too broad when it contains multiple independently testable
behaviors, requires several unrelated concepts, uses phrases such as "build the
backend" or "finish the UI", or cannot be reviewed with one focused verification.
Kiko asks Codex to split such checkpoints before presenting the plan.

### Checkpoint complexity budget

For an implementation checkpoint, allow one primary product behavior, one main
new mental model, one learner-owned responsibility change, and one primary
verification. Supporting syntax and edge-case assertions may remain together
only when they test the same behavior.

Later checkpoints may be moderately larger than KIKO-005 as the learner grows,
but not an order of magnitude larger. A practical target is no more than roughly
two to four KIKO-005-sized learning changes in one checkpoint; prefer the smaller
split whenever two parts can be implemented and reviewed independently.

Integration and acceptance checkpoints may run several already implemented
behaviors together if they introduce no unrelated implementation and answer one
clear integration or release question.

Before plan acceptance or material replanning, classify every pending checkpoint
as `keep`, `split`, or `integration/acceptance` and retain the audit mapping in
`CHECKPOINT_SIZE_AUDIT.md`.

### Product increments

The ordering should create small working vertical increments. Infrastructure is
introduced when the next product behavior requires it, not as a long detached
setup phase. Dependencies flow forward without circular prerequisites.

## Mandatory plan coverage audit

Kiko validates structure deterministically and asks Codex for a separate
content critique. The audit checks:

### Requirement traceability

- every required behavior maps to one or more checkpoints
- every checkpoint maps back to a confirmed requirement, learning need, risk,
  or release obligation
- every finished-product acceptance scenario maps to an end-to-end test

### User experience completeness

- first run and onboarding
- primary happy path
- empty, loading, success, validation, recoverable-error, blocked, cancel, retry,
  restart, and resume states where applicable
- keyboard/accessibility expectations for interactive interfaces

### Data and integration completeness

- ownership, schema, validation, persistence, migration, export, retention, and
  deletion where applicable
- authentication, timeout, cancellation, malformed response, unavailable
  service, compatibility, and cleanup for each external boundary
- explicit AI authority, output validation, and human-control points

### Engineering and release completeness

- unit, integration, contract/protocol, and end-to-end tests
- diagnostics that avoid secrets and unnecessary personal data
- packaging or deployment from a clean checkout
- configuration, dependency checks, upgrade/rollback, and uninstall
- documentation, supported versions, known limitations, and release evidence

### Teaching completeness

- prerequisites appear before dependent concepts
- new syntax is introduced before use
- checkpoint size matches one focused learner change
- verification is accessible to the learner
- the plan does not assume competence merely because a concept was explained
- difficult infrastructure is connected to a real product need

## Draft, critique, and repair

The first Codex output is always a candidate, never the canonical roadmap.

1. Kiko validates required fields, IDs, dependencies, and traceability.
2. A separate Codex critique receives the confirmed brief, candidate plan, and
   coverage checklist and returns gaps, vague checkpoints, unsafe assumptions,
   and missing finished-product work.
3. Kiko requests a repaired candidate containing explicit changes.
4. Validation repeats until the candidate passes or Kiko reports the unresolved
   blocker to the user.

The critique must not expand scope with speculative features. A newly discovered
product decision returns to discovery instead of being silently answered during
repair.

## User plan review

Kiko does not initially overwhelm a beginner with the full roadmap. It first
shows:

- product promise and confirmed release boundary
- major product increments
- number and shape of atomic checkpoints
- assumptions, exclusions, risks, and deferrable decisions
- the first checkpoint in full
- confirmation that tests, packaging, delivery, and finished-product acceptance
  are included

The user can expand the complete plan, request a simpler explanation, change a
decision, or accept it. Changing a product decision invalidates affected plan
sections and returns them through validation.

## Durable output

Only after user acceptance does Kiko write or update:

- `PROJECT_BRIEF.md` for confirmed product scope
- `PRODUCT_SPEC.md` for user-visible behavior and acceptance journeys
- `ARCHITECTURE.md` for chosen boundaries and explicit technical assumptions
- `LEARNING_PLAN.md` for ordered progress and current handoff
- `LEARNING_LOG.md` for later learner-authored evidence, initially empty
- `AgentReadme.md` and `AGENTS.md` for stable teaching and agent entry rules

The accepted plan receives a version and decision summary. Later changes state
what changed, why, which checkpoints are affected, and whether completed work
remains valid. Plan evolution is expected; silent roadmap replacement is not.

## Planning failure and recovery

- Provider failure preserves confirmed answers and the brief candidate so the
  user does not repeat discovery.
- Invalid Codex output is never written as the active plan.
- Repeated validation failure reports the exact uncovered requirements or
  unresolved decision.
- An existing project plan is backed up before an accepted replacement.
- Cancelling a revision preserves the last accepted plan.
- No planning action edits application source.

## Planning acceptance scenarios

### Beginner with a broad idea

Given "I want to learn Python by making a budgeting app", Kiko asks short
product-level questions in rounds, recommends safe technical defaults, confirms
the intended user and local/web/data boundaries, then produces an atomized plan
that includes a useful product, errors, tests, packaging, and acceptance without
asking the learner to select unfamiliar libraries.

### Experienced learner with detailed constraints

Given a detailed brief and repository, Kiko reuses stated facts, asks only about
material conflicts or omissions, exposes architecture choices, and produces a
more compact but equally traceable plan.

### Material ambiguity discovered during critique

If the plan critique discovers that account synchronization is implied but not
confirmed, Kiko does not choose a backend. It reopens discovery, explains why
the decision matters, and regenerates only affected plan sections after user
confirmation.

### User changes scope after acceptance

Kiko shows affected requirements and checkpoints, preserves valid completed
work, obtains confirmation for the revised brief, and versions the regenerated
plan instead of resetting progress silently.

## Release quality gates for planning

The planning feature is not complete until tests prove that:

- no plan request is sent while a blocking decision remains open
- beginner question rounds contain no more than three questions
- repeated answers are reused
- technical defaults remain visible assumptions rather than facts
- every required behavior and acceptance journey has traceability
- vague or multi-outcome checkpoints are rejected or split
- applicable error, data, test, packaging, upgrade, and delivery work is present
- plan critique cannot silently expand confirmed scope
- application source and the last accepted plan remain unchanged on cancel or
  invalid provider output
- the user must accept the brief and final plan in separate steps

## Kiko adoption record — 2026-09-04

Kiko adopted the shared Guided Project Tutor idea-to-plan system retroactively.
Existing verified checkpoints and learner evidence remain valid, and the active
implementation handoff is KIKO-011 (legacy Step 4C).

### Confirmed facts and product decisions

- Kiko is a local Project Tutor for one macOS learner.
- Learner-facing explanations use Croatian; source code, identifiers, commands,
  literal output, and internal technical documentation use English.
- Python owns Tutor Core and the supported CLI.
- A thin TypeScript VS Code extension is the primary everyday surface.
- Codex App Server is the first replaceable expert provider.
- The learner owns substantive application-source changes; help and review are
  read-only in v1.0.
- Private global learner knowledge and project-local progress have separate
  owners.
- v0.1 proves the central learning loop; v1.0 must be tested, installable,
  recoverable, upgradeable, and removable.

### Reversible technical assumptions

- JSON and Markdown remain sufficient for early local state while schemas and
  runtime ownership are clarified incrementally.
- The CLI proves Python Core behavior before the extension becomes the primary
  surface.
- The fake expert precedes live Codex integration.

### Deferred decisions and deadlines

- Choose managed Python versus a signed standalone Core artifact in KIKO-063.
- Set the supported macOS, VS Code, and Codex version matrix by KIKO-070.
- Finalize extension publisher metadata and branding before KIKO-065 packaging.
- Marketplace publication is optional and requires separate explicit approval;
  an installable `.vsix` is the v1.0 requirement.

None of these decisions blocks current KIKO-011 or invalidates earlier work.

### Explicitly excluded from v1.0

- automatic learner-source implementation
- cloud accounts or synchronization
- local model inference
- non-VS Code editor, mobile, or web clients
- a generalized autonomous-agent framework

### Traceability and validation result

- Product scope is retained in `PROJECT_BRIEF.md`.
- User-visible flows and quality gates are retained in `PRODUCT_SPEC.md`.
- Learner-facing interaction formats are retained in `LESSON_SPEC.md`.
- Accepted Tutor-quality improvements and their runtime/regression links are
  retained in `TUTOR_FEEDBACK.md`, separately from learner evidence.
- Technical boundaries are retained in `ARCHITECTURE.md`.
- Atomic implementation, productization, and release work are retained only in
  `LEARNING_PLAN.md`.
- The migrated plan covers Core, learner/project state, pedagogy, planning,
  expert boundary, App Server, CLI, extension, automated verification,
  onboarding, packaging, recovery, upgrades, uninstall, and clean-machine
  acceptance.
- No blocking product decision is currently open.
- Adoption was requested by the user; no application source or completed
  progress was changed during migration.
