# Kiko Tutor Feedback

This file records short, structured Tutor-quality improvements discovered while
Kiko is built through its own teaching workflow. It is product feedback, not
learner competence evidence. It must not contain raw conversations, hidden
reasoning, secrets, full prompts, or source-code copies.

## Open candidates

- None.

## Accepted improvements

### DF-001 — Unannounced syntax in Step 4B

- Date: 2026-09-03
- Observation: The first Step 4B guidance used `lower()` and `get()` without
  first explaining them to the beginner.
- Contract/rule: New syntax must be declared and explained before use.
- Scope: shared skill, Kiko project, runtime product
- Immediate recovery: Step 4B was restarted with an explicit syntax explanation
  and a smaller learner task.
- Shared-skill change: Added mandatory Syntax preflight and no-unannounced-
  syntax rule.
- Project change: Added the same requirement to `LESSON_SPEC.md` and
  `PRODUCT_SPEC.md`.
- Runtime/roadmap change: KIKO-025 and KIKO-027–027C require structured Syntax
  preflight and Tutor interaction validation.
- Regression check: Reject a lesson fixture containing syntax absent from its
  known/new lists.
- User decision: accepted
- Skill status: implemented
- Project status: implemented
- Runtime status: planned

### DF-002 — Inconsistent lesson structure

- Date: 2026-09-04
- Observation: New-step guidance did not consistently show progress, problem,
  syntax, code flow, task, and verification in the same order.
- Contract/rule: Every interaction type needs a stable semantic format.
- Scope: shared skill, Kiko project, runtime product
- Immediate recovery: A canonical new-checkpoint format and smaller hint,
  review, debug, and handoff formats were defined.
- Shared-skill change: Added `references/lesson-contract.md` and a generated
  `LESSON_SPEC.md` template.
- Project change: Added `.tutor/LESSON_SPEC.md` as the single presentation
  authority and linked all other Kiko documents to it.
- Runtime/roadmap change: KIKO-027–027C create the interaction variants; CLI and
  VS Code become presenters over the same content.
- Regression check: Audit required fields/order for every interaction type and
  compare chat, CLI, and VS Code semantic parity.
- User decision: accepted
- Skill status: implemented
- Project status: implemented
- Runtime status: planned

### DF-003 — Planning could start before the product was clear

- Date: 2026-09-04
- Observation: The earlier workflow could create a plausible but incomplete
  roadmap before resolving product-defining ambiguity.
- Contract/rule: No plan generation before brief readiness and separate user
  acceptance.
- Scope: shared skill, Kiko project, runtime product
- Immediate recovery: Kiko's existing roadmap was expanded and audited without
  resetting verified work.
- Shared-skill change: Added `references/idea-to-plan.md`, readiness gates,
  candidate-plan critique, and richer project templates.
- Project change: Added `PLANNING_SPEC.md`, productization steps, and v1.0
  acceptance.
- Runtime/roadmap change: KIKO-029–034A, KIKO-038–038B, KIKO-044–044B, and
  KIKO-049–049B implement discovery, validation, critique, and approval.
- Regression check: Block planning with unresolved decisions; reject vague,
  untraceable, or incomplete product plans.
- User decision: accepted
- Skill status: implemented
- Project status: implemented
- Runtime status: planned

### DF-004 — No synchronized improvement hook

- Date: 2026-09-04
- Observation: Tutor problems could be fixed manually but had no standard path
  from learner feedback to shared skill, Kiko specification, runtime roadmap,
  and regression check.
- Contract/rule: Accepted reusable Tutor feedback must produce synchronized,
  traceable improvement without becoming learner-competence evidence.
- Scope: shared skill, Kiko project, runtime product
- Immediate recovery: Existing accepted improvements were reconstructed as
  short structured records.
- Shared-skill change: Added the controlled dogfood feedback loop and feedback
  template.
- Project change: Added this feedback record and linked the hook to Kiko's
  product, lesson, architecture, and agent rules.
- Runtime/roadmap change: KIKO-028–028A, KIKO-050, KIKO-054–054C,
  KIKO-060–060A, KIKO-062, and KIKO-074A implement classification, user control,
  UI, tests, and release proof.
- Regression check: A reported Tutor-quality issue preserves the active
  checkpoint, creates no competence downgrade, and maps accepted changes to a
  regression test.
- User decision: accepted
- Skill status: implemented
- Project status: implemented
- Runtime status: planned

### DF-005 — Roadmap structure and dependency order were inconsistent

- Date: 2026-09-04
- Observation: The 853-line roadmap mixed progress and specifications, used
  several checkpoint shapes, placed package/contracts/tests after App Server
  and extension work, and disagreed with the prototype's displayed step.
- Contract/rule: Every checkpoint needs the same atomic contract, forward-only
  dependencies, one progress authority, and exact verification.
- Scope: shared skill, Kiko project, runtime product
- Immediate recovery: The roadmap was normalized before starting another source
  checkpoint; verified learning evidence was preserved.
- Shared-skill change: Added a large-roadmap sharding rule and reusable detailed
  checkpoint template.
- Project change: `LEARNING_PLAN.md` now owns only status/order/handoff and links
  to symmetric specifications under `.tutor/checkpoints/`.
- Runtime/roadmap change: Core package, progress ownership, contracts, tests, and
  repository trust now precede evidence writes, App Server, CLI, and extension.
- Regression check: Run the shared `scripts/validate_project_plan.py` to audit
  unique IDs, links/anchors, one `NEXT`, required fields, prerequisite direction,
  checkbox ownership, and runtime mirror.
- User decision: accepted
- Skill status: implemented
- Project status: implemented
- Runtime status: planned through KIKO-013, KIKO-014, KIKO-015, and KIKO-018

### DF-006 — Every lesson loaded unrelated stable documentation

- Date: 2026-09-04
- Observation: Project entry rules required roughly 2,000 lines of brief,
  architecture, product, planning, lesson, progress, and evidence documents for
  every teaching or review interaction.
- Contract/rule: Read every relevant authority completely, but route unrelated
  stable documents by interaction type.
- Scope: shared skill, Kiko project, runtime product
- Immediate recovery: Added progressive context routing while retaining the
  active plan/checkpoint and required learner evidence.
- Shared-skill change: Added `project-context-routing.md` and updated project
  templates.
- Project change: `AGENTS.md` and `AgentReadme.md` now define always-read and
  task-specific documents.
- Runtime/roadmap change: KIKO-026 enforces bounded Tutor context.
- Regression check: A normal lesson reads plan, active checkpoint, lesson/evidence,
  learner/reference, and relevant source without loading planning/product docs.
- User decision: accepted
- Skill status: implemented
- Project status: implemented
- Runtime status: planned in KIKO-026

### DF-007 — State contracts depended on tests introduced later

- Date: 2026-09-04
- Observation: KIKO-014 used `unittest`, but the test environment was introduced
  in the following checkpoint.
- Contract/rule: New syntax and infrastructure must precede every dependent
  checkpoint.
- Scope: Kiko project
- Immediate recovery: Reordered pending checkpoint contents before implementation.
- Shared-skill change: None; existing prerequisite audit already requires
  forward dependency order.
- Project change: KIKO-014 now establishes `.venv`/isolated tests and KIKO-015
  implements versioned state contracts.
- Runtime/roadmap change: Future Python verification commands consistently use
  `.venv/bin/python` or `.venv/bin/kiko`.
- Regression check: Shared plan validator requires every declared prerequisite
  to appear earlier; content review checks new infrastructure before use.
- User decision: accepted
- Skill status: not needed
- Project status: verified
- Runtime status: planned in KIKO-012 through KIKO-015

### DF-008 — Explanation-language state contradicted actual use

- Date: 2026-09-04
- Observation: Project/global profiles said English while learner-facing
  explanations consistently used Croatian.
- Contract/rule: Explanation language must match the learner's confirmed current
  preference; code and technical literals remain separately owned.
- Scope: learner-specific, Kiko project, runtime product
- Immediate recovery: Confirmed the proposed Croatian-explanation/English-code
  split through the user's instruction to apply the audit fixes.
- Shared-skill change: None; the skill already infers and stores explanation
  language separately from source-language policy.
- Project change: Project instructions, lesson spec, planning record, and global
  learner profile now specify Croatian explanations and English technical text.
- Runtime/roadmap change: KIKO-061 verifies localization and fallback boundaries.
- Regression check: Project/global explanation preferences agree and localized
  headings do not translate code, identifiers, commands, or literal output.
- User decision: accepted
- Skill status: not needed
- Project status: verified
- Runtime status: planned in KIKO-061

### DF-009 — Roadmap validation existed only as an ad hoc command

- Date: 2026-09-04
- Observation: The normalized roadmap passed a one-off inline audit that future
  replanning could not reliably reuse.
- Contract/rule: Repeated deterministic validation belongs in a shared script.
- Scope: shared skill, Kiko project, runtime product
- Immediate recovery: Converted the audit into a dependency-free shared validator.
- Shared-skill change: Added `scripts/validate_project_plan.py` and mandatory use
  after creating or materially changing a sharded plan.
- Project change: The then-current 76-checkpoint roadmap passed the reusable
  validator; DF-010's normalized 121-checkpoint roadmap also passes it.
- Runtime/roadmap change: KIKO-032–032B later implement equivalent product-side
  structure, dependency, and atomicity validation.
- Regression check: Validator checks item format, IDs, status/NEXT, links,
  anchors, all 12 fields/order, kinds, prerequisites, size-audit coverage,
  orphan specs, checkbox ownership, and recognized runtime mirror.
- User decision: accepted
- Skill status: implemented
- Project status: verified
- Runtime status: planned in KIKO-032 through KIKO-032B

### DF-010 — Pending checkpoints had inconsistent learning size

- Date: 2026-09-04
- Observation: KIKO-032 combined several independently teachable validators and
  was roughly an order of magnitude larger than early KIKO-005.
- Contract/rule: One implementation checkpoint gets one primary behavior, one
  main new mental model, one learner-owned responsibility change, and one
  primary verification; integration/acceptance may combine only existing work.
- Scope: shared skill, Kiko project, runtime product
- Immediate recovery: Audited all 66 originally pending checkpoints before
  continuing KIKO-011.
- Shared-skill change: Added the checkpoint complexity budget and checkpoint-kind
  field to planning rules/templates; validator now enforces valid kinds and
  complete size-audit mapping.
- Project change: `CHECKPOINT_SIZE_AUDIT.md` records every keep/split decision;
  29 oversized originals were split into 45 smaller checkpoints.
- Runtime/roadmap change: KIKO-032, KIKO-032A, and KIKO-032B separately validate
  fields/IDs, prerequisites/order, and semantic atomicity.
- Regression check: The 121-checkpoint plan passes structural validation, every
  pending ID appears exactly once in the size audit, and future replanning must
  repeat the semantic keep/split/integration/acceptance audit.
- User decision: accepted
- Skill status: implemented
- Project status: verified
- Runtime status: planned in KIKO-032 through KIKO-032B

### DF-011 — Completing an audited checkpoint invalidated the plan validator

- Date: 2026-09-04
- Observation: After KIKO-011 passed, the shared validator rejected its retained
  historical size-audit entry because the checkpoint was no longer pending.
- Contract/rule: Every currently pending checkpoint must be size-audited, while
  completed checkpoints remain valid historical audit records.
- Scope: shared skill, Kiko project, runtime product
- Immediate recovery: Confirmed KIKO-011 independently, corrected validator
  semantics, and reran the full roadmap audit.
- Shared-skill change: Size-audit validation now allows known completed IDs and
  still rejects unknown IDs or uncovered pending checkpoints.
- Project change: KIKO-032B includes completed-audit-history regression behavior.
- Runtime/roadmap change: Product-side atomicity validation must preserve audit
  lineage as progress advances.
- Regression check: Completing KIKO-011 yields 11 complete/110 pending and a
  valid audit; removing any pending normalized ID still fails validation.
- User decision: accepted as an in-scope completion-validator correction
- Skill status: verified
- Project status: verified
- Runtime status: planned in KIKO-032B

### DF-012 — Package structure and editable installation were combined

- Date: 2026-09-04
- Observation: Starting KIKO-012A required Python package/module structure,
  relative imports, TOML metadata, a build backend, editable installation, and
  console entry points in one beginner checkpoint; the fresh `.venv` also had no
  build backend installed.
- Contract/rule: One implementation checkpoint gets one main new mental model
  and one learner-owned responsibility change.
- Scope: Kiko project
- Immediate recovery: Split the checkpoint before presenting source instructions.
- Shared-skill change: None; the existing complexity budget detected the issue.
- Project change: KIKO-012A now covers package/module execution only; KIKO-012B
  separately covers `pyproject.toml`, build backend, editable install, and the
  generated `kiko` command.
- Runtime/roadmap change: KIKO-013 now depends on the installed entry point from
  KIKO-012B.
- Regression check: Each checkpoint has one primary mental model and separate
  verification for `python -m kiko` versus `.venv/bin/kiko`.
- User decision: accepted through the standing dogfood/atomicity instruction
- Skill status: not needed
- Project status: verified
- Runtime status: not applicable

### DF-013 — TOML was presented without its language structure

- Date: 2026-09-04
- Observation: KIKO-012B explained which values to enter but did not first
  explain TOML hierarchy, table scope, assignment syntax, value types, field
  ownership, required/default status, or the mapping from metadata to Kiko.
- Contract/rule: An unfamiliar declarative format must receive a format-specific
  preflight before any project configuration is assigned.
- Scope: shared skill, Kiko project, runtime product
- Immediate recovery: Kept KIKO-012B active and replaced the opaque block with a
  bottom-up TOML explanation tied to pip, setuptools, and Kiko behavior.
- Shared-skill change: Extended the lesson contract and generated lesson template
  with a configuration/data-format preflight.
- Project change: `LESSON_SPEC.md` and `PRODUCT_SPEC.md` now require format
  hierarchy, punctuation, types, fields, effects, mappings, and errors.
- Runtime/roadmap change: KIKO-025 now builds/audits both code-syntax and
  configuration-format preflights; canonical TutorInteraction carries
  `format_preflight` separately.
- Regression check: Reject a TOML lesson that uses an unexplained section,
  field, value type, required/default decision, or Kiko mapping.
- User decision: explicitly accepted in the feedback request
- Skill status: implemented
- Project status: implemented
- Runtime status: planned in KIKO-025 and KIKO-027

### DF-014 — First unittest and filesystem isolation were combined

- Date: 2026-09-04
- Observation: Starting KIKO-014 would have introduced unittest discovery,
  Python class/inheritance syntax, assertions, temporary directories, nested
  context managers, and mocking in one beginner checkpoint.
- Contract/rule: One implementation checkpoint gets one main new mental model;
  later steps may build on it without hiding new syntax.
- Scope: Kiko project
- Immediate recovery: Split the checkpoint before presenting the test task.
- Shared-skill change: None; the existing complexity/Syntax-preflight rules
  detected the issue.
- Project change: KIKO-014 now introduces one pure discovered unit test;
  KIKO-014A separately isolates filesystem state with a temporary home/mock.
- Runtime/roadmap change: KIKO-015 state contracts now depend on the completed
  filesystem-isolation checkpoint.
- Regression check: KIKO-014 uses no filesystem/mocking syntax; KIKO-014A starts
  only after unittest class/assertion syntax is recorded.
- User decision: accepted through the standing dogfood/atomicity instruction
- Skill status: not needed
- Project status: verified
- Runtime status: not applicable

### DF-015 — Parent-only size audit missed final child readiness

- Date: 2026-09-04
- Observation: Starting KIKO-015 exposed that the earlier roadmap audit had
  classified original parent checkpoints but had not dry-run every final child;
  some children still combined independent outcomes and syntax families.
- Contract/rule: One implementation checkpoint gets one main new mental model
  and one primary observable behavior.
- Scope: Kiko project
- Immediate recovery: Paused KIKO-015 and performed a second semantic pass over
  every final pending checkpoint before resuming any lesson.
- Shared-skill change: `guided-project-tutor` now requires a full final-child
  lesson-readiness pass after splitting; its project templates retain the rows,
  and its validator rejects missing, duplicate, non-pending, reordered, stale-
  title, placeholder, or malformed readiness records.
- Project change: `PLANNING_SPEC.md` now owns the post-split lesson dry-run gate;
  `CHECKPOINT_SIZE_AUDIT.md` contains one readiness row for every final pending
  ID. Oversized child checkpoints were split across state, pedagogy, planning,
  provider, TypeScript, data-control, packaging, migration, and performance
  boundaries.
- Runtime/roadmap change: KIKO-032D implements the final-child readiness gate in
  Kiko; the normalized roadmap now has 168 checkpoints, 17 verified and 151
  individually audited pending checkpoints.
- Regression check: A plan fails acceptance when any final child lacks a
  readiness row or cannot render one complete lesson without invented syntax,
  task, verification, or scope.
- User decision: explicitly requested and accepted
- Skill status: verified
- Project status: verified
- Runtime status: planned in KIKO-032D

### DF-016 — Strict learner-only authorship made delivery impractically slow

- Date: 2026-09-04
- Observation: The complete 168-checkpoint plan protects learning quality, but
  requiring a separate learner-authored implementation cycle for all 151
  pending checkpoints would delay the product and over-teach repetitive glue.
- Contract/rule: Learning evidence must reflect learner action, while verified
  product progress and code authorship may remain separate when the learner
  explicitly accepts a bounded hybrid workflow.
- Scope: learner-specific, Kiko project, reusable shared skill
- Immediate recovery: Kept KIKO-015 paused and classified every pending
  checkpoint before resuming implementation.
- Shared-skill change: Added optional hybrid execution modes with strict
  learner-owned default, bounded delegation, conservative evidence rules,
  reusable project templates, context routing, and deterministic table
  validation.
- Project change: Added `EXECUTION_MODES.md`; Kiko lessons now show the mode and
  project instructions enforce its source/evidence boundary.
- Runtime/roadmap change: None; this controls how Kiko itself is developed and
  does not weaken the shipped product's read-only learner-source promise.
- Regression check: Validator requires every pending ID exactly once and in
  roadmap order; delegated code cannot create learner competence evidence.
- User decision: explicitly accepted
- Skill status: verified
- Project status: verified
- Runtime status: not applicable

### DF-017 — Repeated implementation patterns were not surfaced for refactoring

- Date: 2026-09-04
- Observation: The second state-validator implementation introduced a reusable
  typed-field helper, but the Tutor did not proactively identify the equivalent
  repetition in the first project-state validator or offer a shared refactor.
- Contract/rule: When repetition makes an abstraction materially useful, the
  Tutor must surface the opportunity and its scope rather than silently leaving
  parallel implementations.
- Scope: learner-specific, Kiko project, reusable shared skill
- Immediate recovery: Explained that the first explicit validator is complete
  for its checkpoint, distinguished behavior from maintainability, and agreed
  to offer reusable refactors when later checkpoints reveal repetition.
- Shared-skill change: Added a reuse-opportunity gate to the lesson interaction
  contract and generated lesson-spec template.
- Project change: Added the same gate to Kiko's authoritative `LESSON_SPEC.md`.
- Runtime/roadmap change: None; this request governs development tutoring and
  does not add a shipped Kiko runtime feature.
- Regression check: A checkpoint dry run with a second meaningful occurrence
  must name the repetition and offer or explicitly defer a bounded refactor;
  learner-owned source is never silently rewritten.
- User decision: explicitly accepted in the feedback request
- Skill status: implemented
- Project status: implemented
- Runtime status: not applicable

### DF-018 — Completion handoffs left pending-only tables stale

- Date: 2026-09-04
- Observation: KIKO-015 through KIKO-015C were completed in the roadmap, but
  their final-readiness and execution-mode rows remained in tables defined as
  pending-only, causing the project-plan validator to fail.
- Contract/rule: A durable completion handoff must reconcile every pending-only
  companion table while preserving historical audit records.
- Scope: Kiko project, reusable shared skill
- Immediate recovery: Removed only the four completed pending-only rows,
  recalculated execution-mode totals, and preserved the historical original-
  checkpoint audit.
- Shared-skill change: Added a completion bookkeeping invariant to the shared
  skill and generated project AgentReadme template.
- Project change: Added the invariant to `AgentReadme.md` and clarified the
  pending-only final-readiness table.
- Runtime/roadmap change: None; roadmap scope and checkpoint order are unchanged.
- Regression check: After each completion, pending roadmap IDs must exactly
  match final-readiness and execution-mode rows in order, and the shared plan
  validator must pass before the next checkpoint lesson.
- User decision: explicitly accepted in the bookkeeping-fix request
- Skill status: implemented
- Project status: implemented
- Runtime status: not applicable

### DF-019 — Agent delegation skipped the learner's pre-implementation review

- Date: 2026-09-04
- Observation: KIKO-015D was implemented immediately after a generic continue
  signal without first presenting its problem, idea, design, proposal, reuse
  decision, and verification for learner review.
- Contract/rule: Execution mode changes authorship, not the mandatory
  new-checkpoint explanation or the learner's checkpoint-specific approval.
- Scope: learner-specific, Kiko project, reusable shared skill
- Immediate recovery: Kept KIKO-015E active, acknowledged the skipped gate, and
  provided the missing KIKO-015D explanation without treating agent code as
  learner competence.
- Shared-skill change: Changed agent-delegated continuation into a mandatory
  preview followed by a separate explicit approval before source edits; updated
  the hybrid/lesson rules and generated templates.
- Project change: Added the same gate to Kiko's AgentReadme, execution modes,
  and lesson specification.
- Runtime/roadmap change: None; this governs Kiko development workflow and does
  not change shipped product scope.
- Regression check: A generic continue signal may render an agent-delegated
  preview but cannot mutate source; a later explicit approval must proceed to
  implementation without repeating the preview.
- User decision: explicitly accepted in the feedback request
- Skill status: implemented
- Project status: implemented
- Runtime status: not applicable

### DF-020 — Checkpoint previews assumed the feature's value was obvious

- Date: 2026-09-04
- Observation: The KIKO-015E preview described feedback-state mechanics without
  first giving a human explanation of why users would want to give, retain, and
  later use Tutor-quality feedback.
- Contract/rule: Every new checkpoint needs a short user-value Intro before the
  technical problem; a feature name is not an explanation of purpose.
- Scope: learner-specific, Kiko project, reusable shared skill, runtime product
- Immediate recovery: Kept KIKO-015E in unapproved preview state and added a
  plain-language Intro requirement before revisiting its proposal.
- Shared-skill change: Added a mandatory two-to-four-sentence Intro to the new-
  checkpoint contract and generated lesson-spec template.
- Project change: Added the same field and ordering rule to Kiko's authoritative
  `LESSON_SPEC.md`.
- Runtime/roadmap change: KIKO-027 inherits the new canonical `intro` field from
  `LESSON_SPEC.md`; no new checkpoint or roadmap reorder is required.
- Regression check: Reject a new-checkpoint interaction whose Intro does not
  identify user benefit, real product use, and why the capability is valuable
  before technical details.
- User decision: explicitly accepted in the Intro request
- Skill status: implemented
- Project status: implemented
- Runtime status: planned in KIKO-027

## Record template

### <FEEDBACK_ID> — <SHORT_TITLE>

- Date: <DATE>
- Observation: <SHORT_OBSERVATION>
- Contract/rule: <VIOLATED_OR_MISSING_RULE>
- Scope: <LEARNER | PROJECT | SHARED_SKILL | RUNTIME_PRODUCT>
- Immediate recovery: <RECOVERY>
- Shared-skill change: <SKILL_CHANGE_OR_NONE>
- Project change: <PROJECT_CHANGE_OR_NONE>
- Runtime/roadmap change: <RUNTIME_CHANGE_OR_NONE>
- Regression check: <OBSERVABLE_PREVENTION>
- User decision: <PENDING | ACCEPTED | DECLINED>
- Skill status: <NOT_NEEDED | PLANNED | IMPLEMENTED | VERIFIED>
- Project status: <NOT_NEEDED | PLANNED | IMPLEMENTED | VERIFIED>
- Runtime status: <NOT_NEEDED | PLANNED | IMPLEMENTED | VERIFIED>
