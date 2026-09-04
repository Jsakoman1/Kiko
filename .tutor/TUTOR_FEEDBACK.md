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
