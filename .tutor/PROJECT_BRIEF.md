# Project Tutor Product Brief

## Mission

Build a local Project Tutor that increases a learner's ability to create real
software themselves. It uses expert models for repository reasoning while
preserving learner ownership, progressive assistance, and durable learning.

## Product distinction

Normal coding agents optimize for completed code. Project Tutor optimizes for
the learner becoming more capable of completing code. Working software matters,
but AI-written software is not evidence of learner competence.

## Learner and initial platform

- Primary learner: one local user on macOS
- Initial learning languages: Python and Java
- Tutor Core language: Python
- Editor surface: thin TypeScript VS Code extension
- Expert today: Codex App Server
- Future expert possibility: local model behind the same narrow boundary

## Strongest value

The differentiator is not chat, code generation, or a dashboard. It is the
combination of:

- cross-project learner knowledge
- evidence-aware competence rather than binary completion
- progressive help that decreases as competence grows
- project-local roadmap and handoff
- repository-aware expert reasoning constrained by Tutor pedagogy
- a personal reference grown from real work

## Version 0.1 proof

Version 0.1 proves one local vertical loop:

```text
recognize a learning project
  -> combine global learner knowledge with project-local state
  -> receive a question in a VS Code sidebar
  -> ask Codex through App Server with bounded Tutor context
  -> return learner-appropriate guidance
  -> learner changes code
  -> review learner work
  -> update project and learner evidence
```

The same Python Tutor Core must also work through a small standalone CLI so the
product is not owned by the editor extension.

## Required v0.1 behavior

- Create or recognize one `.tutor/` learning project.
- Maintain one private global learner profile and personal reference.
- Maintain a project roadmap, current checkpoint, help preference, and handoff.
- Distinguish introduced, assisted, independent, and reliable knowledge.
- Ask Codex for read-only repository reasoning through a narrow local adapter.
- Return progressive hints, explanations, reviews, and debugging guidance.
- Keep the learner as the author of substantive source changes.
- Resume from durable state instead of relying on chat history.
- Provide a minimal VS Code sidebar over the same Python core.

## Deliberately excluded from v0.1

- PySide6 or another desktop GUI
- Local LLM inference
- Windows, Linux, JetBrains, Xcode, mobile, or web clients
- Accounts, authentication, cloud backend, subscriptions, or collaboration
- Embeddings, vector search, or a giant programming ontology
- A custom coding agent, generic workflow engine, or Codex replacement
- Automatic source implementation by Tutor
- Large analytics, telemetry, or evaluation infrastructure

## Critical assessment

The central product hypothesis is coherent only if assistance decreases and
learner-authored evidence changes future teaching. If every request simply
becomes a prompt sent to Codex, this is an AI wrapper with no durable advantage.

Weak assumptions and risks:

- Competence cannot be inferred reliably from one successful task.
- A model may over-explain, reveal full solutions, or mistake task completion
  for learning.
- Global knowledge can become noisy or invasive if raw activity is retained.
- App Server protocol changes can break the adapter.
- A Python backend plus TypeScript extension creates a packaging boundary.
- Two polished UIs would consume effort before proving pedagogical value.
- A personal reference may become a language manual unless additions require
  real project use.

Version 0.1 therefore uses conservative competence updates, a small state model,
read-only Codex behavior, one editor surface, and no second GUI.

## Acceptance

The vertical slice succeeds when a learner can return to a real project, receive
guidance adapted to prior demonstrated knowledge, implement a small change,
receive a repository-aware review, and produce durable project and learner
evidence without Tutor editing the application source.
