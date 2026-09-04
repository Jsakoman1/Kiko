# Project Tutor v0.1 Architecture

## Current truth — 2026-09-03

- The shared `guided-project-tutor` skill is a working documentation-driven
  teaching workflow, not an application runtime.
- Kiko is a small Python learning prototype with `help`, `show`, and separate
  state-loading functions. It writes/loads project JSON, reads global learner
  profile concepts, and has no model connection.
- KIKO-001 through KIKO-010 are verified and preserved in the learning log and
  global learner state; KIKO-011 is next.
- Local Codex CLI version is `0.152.1` on macOS.
- A live no-model App Server `initialize` handshake succeeded over `stdio`.
- JSON Schema and TypeScript bindings can be generated from the installed Codex
  version.
- PySide6 is not installed. It is intentionally deferred rather than added.
- The `code` CLI was not available in the inspected shell; VS Code extension
  packaging and host discovery remain implementation-time checks.

## Chosen architecture

```text
VS Code sidebar (TypeScript)
  rendering + user input only
              |
              | local JSONL
              v
Tutor application process (Python)
  Tutor Core
  idea discovery + plan compiler
  Tutor-quality feedback classifier
  learner/project state
  pedagogical request composer
  response validator/presenter
              |
              | ExpertProvider boundary
              v
Codex App Server adapter (Python)
  local child process + stdio JSON-RPC
              |
              v
Codex
  repository-aware technical reasoning
```

The Python process is the standalone Tutor application in v0.1. Its CLI proves
the core before the VS Code sidebar is added. The extension stays thin and does
not own pedagogy or duplicate state.

## Component responsibilities

### Tutor Core

Owns learner intent, active project step, help level, competence-sensitive
teaching policy, context selection, response shape, and state updates. It never
treats model output as verified learner knowledge.

Tutor Core produces one canonical structured interaction matching
`.tutor/LESSON_SPEC.md`. The CLI and VS Code extension are presenters: they may
adapt layout to the surface but must not reorder fields, choose help level,
introduce syntax, advance progress, or reinterpret review evidence.

### Tutor-quality feedback classifier

Receives an explicit unclear/format/help report or a detected contract
violation, repairs the active interaction, and classifies the issue without
changing progress or competence. It creates only a sanitized candidate containing
category, violated contract, short observation, proposed improvement, and
regression target.

The installed product may keep that candidate in optional local feedback state
that the user can inspect, export, or delete. It never rewrites installed code,
the shared skill, or an accepted roadmap. Applying reusable changes remains a
development and release activity tracked in `.tutor/TUTOR_FEEDBACK.md`.

### Idea discovery and plan compiler

Owns the state machine from natural-language idea through confirmed brief and
accepted roadmap. It classifies uncertainty, asks only product-defining
questions, tracks visible assumptions, and enforces a readiness gate before
Codex may draft a plan.

Planning uses Codex in bounded stages: requirement analysis, candidate plan,
and completeness critique. Kiko validates structure and traceability between
stages. A Codex plan is never canonical by itself; blocking ambiguity returns
to the user, and project Tutor files are written only after separate user
confirmation of the brief and final plan. The exact contract lives in
`.tutor/PLANNING_SPEC.md`.

### VS Code extension

Shows the conversation, roadmap position, and approval/error states. It sends
user actions to the Python process and renders Tutor results. It does not call
Codex directly or contain a second learning model.

### Expert boundary

Use one small conceptual operation:

```text
ask(expert_request) -> expert_result
```

`expert_request` contains the bounded technical question, relevant repository
context, current learning objective, known concepts, allowed help level, and a
required result shape. `expert_result` contains explanation, hints, review or
debug findings, uncertainty, and proposed knowledge signals. Tutor validates
and chooses what becomes learner-facing or durable.

The first implementation should use a fake expert so Tutor Core can be tested
without Codex. `CodexAppServerExpert` becomes the second implementation. A
future local model may implement the same operation without changing Tutor
state, roadmap, or UI.

## Codex App Server direction

Use App Server because the product needs a rich local client, persistent
threads, streamed events, approvals, and repository context. Use the default
local `stdio` JSONL transport and the non-experimental API surface; do not use
experimental WebSockets in v0.1. The installed CLI still labels the App Server
command itself experimental, so the adapter remains a versioned risk boundary.

Minimal lifecycle:

1. Spawn `codex app-server --listen stdio://`.
2. Send `initialize`, then the `initialized` notification.
3. Start or resume one thread with the project `cwd`.
4. Start a turn with Tutor-composed input and a structured output schema.
5. Consume agent-message, item, approval, error, and turn-completed events.
6. Return only the validated expert result to Tutor Core.
7. Close the child process cleanly when the Tutor session ends.

Keep Codex read-only for the first vertical slice. Tutor may review source, but
the learner edits it. Surface protocol/auth/version failures as Tutor errors;
do not disguise them as educational feedback.

Generate schemas from the installed Codex version during development and keep
the adapter limited to the methods and events it actually uses. Unknown
notifications should not crash the client. App Server and its WebSocket mode
carry experimental warnings, so compatibility tests are required at each Codex
upgrade.

Official reference: `https://learn.chatgpt.com/docs/app-server`

## State ownership

```text
~/Library/Application Support/Project Tutor/
  learner.json       private cross-project competence evidence
  REFERENCE.md        personal syntax and pattern reference
  feedback.json       optional sanitized local Tutor-quality candidates

<project>/.tutor/
  PROJECT_BRIEF.md    stable product goal and scope
  ARCHITECTURE.md     current chosen architecture and boundaries
  PRODUCT_SPEC.md     user-visible behavior and acceptance journeys
  PLANNING_SPEC.md    idea discovery and plan-quality contract
  LESSON_SPEC.md      standard learner-facing interaction contract
  TUTOR_FEEDBACK.md   development dogfood improvements, not learner evidence
  LEARNING_PLAN.md    only source of roadmap progress and handoff
  checkpoints/        stable checkpoint contracts without progress checkboxes
  LEARNING_LOG.md     project evidence and recurring learning signals
  AgentReadme.md      project-specific teaching settings

<project>/
  normal application source, tests, and documentation
```

The future runtime may add one versioned `.tutor/state.json` when machine
updates require it. Do not parse Markdown as the long-term application API, and
do not duplicate the same mutable progress in JSON and Markdown. Choose one
canonical runtime record and derive views only after the need is proven.

Conversation and App Server threads are useful interaction history, not
canonical learner or project state.

## Knowledge model

An absent concept is unseen. Encountered concepts use four stages:

- `introduced`: explained, not yet used
- `assisted`: used with task-specific help
- `independent`: used correctly without task-specific help
- `reliable`: independently demonstrated more than once or across projects

`needs_reinforcement` is a separate flag for repeated meaningful difficulty,
not a fifth stage and not a response to one typo.

Use lightweight identifiers such as `general:functions`,
`python:function-definition`, and `java:method-declaration`, with explicit
`related` links only when they improve a real lesson. This supports conceptual
transfer without creating a programming ontology.

The personal reference is a memory aid, not competence evidence. It grows only
after real use.

## Context selection

For one learner request, compile only:

- the active checkpoint and success condition
- the user's current question and requested help
- relevant learner concepts and reference entries
- relevant project decisions and exact source files
- the no-source-edit boundary
- the required expert result shape

Do not send the entire learner profile, roadmap, reference, repository, or prior
conversation by default.

## Lessons retained from AIS and Dora

Carry forward:

- models are replaceable reasoning providers, not authorities or truth stores
- durable state outranks conversation memory
- project truth stays with the project; global personal state has a separate
  owner and privacy boundary
- compile the smallest sufficiently complete context for one bounded task
- model output is a proposal until deterministic checks or learner evidence
  support it
- executor success, observed behavior, and verified learning are different
- use an existing maintained harness for model/session/tool plumbing
- keep live execution events separate from canonical product state

Do not carry forward their mission governance, event sourcing, hash chains,
capability registries, evidence ledgers, routers, or multi-agent machinery.
Project Tutor does not currently need them.

## Deliberate decisions

- No PySide6 in v0.1; the CLI plus VS Code sidebar proves the product with one
  core and one primary UI.
- No local LLM in v0.1; retain only the small ExpertProvider seam.
- No embeddings; state is small and directly selected.
- No database; versioned JSON and Markdown are sufficient for the proof.
- No automatic code edits from Codex; read-only review protects the learning
  objective.
- No large telemetry system; retain only minimal local evidence needed to adapt
  teaching.
