# Kiko v1.0 Learning and Delivery Plan

## Authority and format

This file is the only source of checkpoint order, checkbox progress, active
work, and handoff. Stable checkpoint teaching contracts live under
`.tutor/checkpoints/` and contain no competing completion status.

Every checkpoint specification uses the same fields required by
`PLANNING_SPEC.md`: kind, outcome, product reason, prerequisites, known concepts,
new concepts/syntax, one learner task, exact verification, expected behavior,
edge case, exclusions, and exit condition.

## Current handoff

- Active checkpoint: `KIKO-011` — Read the personal reference (legacy Step 4C).
- Status: not started.
- Last verified: `KIKO-010` — selected Python concept summaries from global
  learner state.
- Current product truth: `kiko.py show` reads separate project and learner JSON,
  selects Python concepts, and does not yet read `REFERENCE.md`.
- Progress authority: this file. The prototype `state.json` field is a temporary
  runtime mirror, not a second development-roadmap authority.
- Planning system: idea discovery, readiness, candidate critique, lesson
  contract, and dogfood feedback systems are adopted.
- Blockers: none for `KIKO-011`.

## Release path

- Phases 0–3 preserve the prototype, establish Core/test boundaries, and
  complete state/evidence basics.
- Phases 4–9 produce the tested v0.1 vertical proof.
- Phases 10–13 turn that proof into an installable, supportable local v1.0.
- Package boundaries, contracts, isolated tests, and threat modeling precede
  App Server and VS Code implementation.
- Verification is introduced with each behavior; Phase 9 aggregates the full
  product-quality suite rather than postponing testing until the end.

## Phase 0 — Verified learning foundation

- [x] [KIKO-001 — Run a basic Python script](checkpoints/00_VERIFIED_FOUNDATION.md#kiko-001)
- [x] [KIKO-002 — Add the module entry point](checkpoints/00_VERIFIED_FOUNDATION.md#kiko-002)
- [x] [KIKO-003 — Read CLI arguments and show help](checkpoints/00_VERIFIED_FOUNDATION.md#kiko-003)
- [x] [KIKO-004 — Store and display in-memory context](checkpoints/00_VERIFIED_FOUNDATION.md#kiko-004)
- [x] [KIKO-005 — Separate context creation from CLI behavior](checkpoints/00_VERIFIED_FOUNDATION.md#kiko-005)
- [x] [KIKO-006 — Shape nested versioned project state](checkpoints/00_VERIFIED_FOUNDATION.md#kiko-006)
- [x] [KIKO-007 — Save project state as JSON](checkpoints/00_VERIFIED_FOUNDATION.md#kiko-007)
- [x] [KIKO-008 — Load project state with a safe default](checkpoints/00_VERIFIED_FOUNDATION.md#kiko-008)
- [x] [KIKO-009 — Read the global learner profile](checkpoints/00_VERIFIED_FOUNDATION.md#kiko-009)
- [x] [KIKO-010 — Select relevant concept summaries](checkpoints/00_VERIFIED_FOUNDATION.md#kiko-010)

## Phase 1 — Global personal reference

- [ ] [KIKO-011 — Read the personal reference](checkpoints/01_REFERENCE.md#kiko-011) **NEXT**

## Phase 2 — Maintainable Core foundation

- [ ] [KIKO-012 — Create an isolated Python development environment](checkpoints/02_CORE_FOUNDATION.md#kiko-012)
- [ ] [KIKO-012A — Migrate existing CLI behavior into the package](checkpoints/02_CORE_FOUNDATION.md#kiko-012a)
- [ ] [KIKO-013 — Separate development progress from runtime project state](checkpoints/02_CORE_FOUNDATION.md#kiko-013)
- [ ] [KIKO-014 — Establish an isolated development and test environment](checkpoints/02_CORE_FOUNDATION.md#kiko-014)
- [ ] [KIKO-015 — Define and validate the project-state contract](checkpoints/02_CORE_FOUNDATION.md#kiko-015)
- [ ] [KIKO-015A — Apply state contracts to every remaining owner](checkpoints/02_CORE_FOUNDATION.md#kiko-015a)
- [ ] [KIKO-016 — Write state through atomic replacement](checkpoints/02_CORE_FOUNDATION.md#kiko-016)
- [ ] [KIKO-016A — Preserve a recoverable state backup](checkpoints/02_CORE_FOUNDATION.md#kiko-016a)
- [ ] [KIKO-016B — Migrate supported state schema versions](checkpoints/02_CORE_FOUNDATION.md#kiko-016b)
- [ ] [KIKO-017 — Define the versioned JSONL request/result envelope](checkpoints/02_CORE_FOUNDATION.md#kiko-017)
- [ ] [KIKO-017A — Define protocol error, progress, and cancel events](checkpoints/02_CORE_FOUNDATION.md#kiko-017a)
- [ ] [KIKO-018 — Enforce workspace file containment](checkpoints/02_CORE_FOUNDATION.md#kiko-018)
- [ ] [KIKO-018A — Filter secret and oversized repository content](checkpoints/02_CORE_FOUNDATION.md#kiko-018a)
- [ ] [KIKO-018B — Label repository text as untrusted model data](checkpoints/02_CORE_FOUNDATION.md#kiko-018b)

## Phase 3 — Conservative learner evidence

- [ ] [KIKO-019 — Create one minimal evidence record](checkpoints/03_EVIDENCE.md#kiko-019)
- [ ] [KIKO-020 — Update one encountered concept conservatively](checkpoints/03_EVIDENCE.md#kiko-020)
- [ ] [KIKO-021 — Save learner state without losing unrelated data](checkpoints/03_EVIDENCE.md#kiko-021)
- [ ] [KIKO-022 — Add a used syntax entry to the personal reference](checkpoints/03_EVIDENCE.md#kiko-022)

## Phase 4 — Deterministic teaching Core

- [ ] [KIKO-023 — Represent and validate one learner request](checkpoints/04_TEACHING_CORE.md#kiko-023)
- [ ] [KIKO-024 — Select interaction intent and assistance level](checkpoints/04_TEACHING_CORE.md#kiko-024)
- [ ] [KIKO-025 — Build and audit Syntax preflight](checkpoints/04_TEACHING_CORE.md#kiko-025)
- [ ] [KIKO-026 — Compile bounded Tutor context](checkpoints/04_TEACHING_CORE.md#kiko-026)
- [ ] [KIKO-027 — Build the canonical new-checkpoint interaction](checkpoints/04_TEACHING_CORE.md#kiko-027)
- [ ] [KIKO-027A — Validate reminder and hint interactions](checkpoints/04_TEACHING_CORE.md#kiko-027a)
- [ ] [KIKO-027B — Validate failed and passing review interactions](checkpoints/04_TEACHING_CORE.md#kiko-027b)
- [ ] [KIKO-027C — Validate debug and completion handoff interactions](checkpoints/04_TEACHING_CORE.md#kiko-027c)
- [ ] [KIKO-028 — Classify feedback and repair the current interaction](checkpoints/04_TEACHING_CORE.md#kiko-028)
- [ ] [KIKO-028A — Sanitize and deduplicate feedback candidates](checkpoints/04_TEACHING_CORE.md#kiko-028a)

## Phase 5 — Idea discovery and planning Core

- [ ] [KIKO-029 — Classify facts, decisions, assumptions, and future ideas](checkpoints/05_PLANNING_CORE.md#kiko-029)
- [ ] [KIKO-030 — Run beginner-friendly discovery rounds](checkpoints/05_PLANNING_CORE.md#kiko-030)
- [ ] [KIKO-031 — Enforce brief readiness and separate acceptance](checkpoints/05_PLANNING_CORE.md#kiko-031)
- [ ] [KIKO-032 — Validate checkpoint fields and unique IDs](checkpoints/05_PLANNING_CORE.md#kiko-032)
- [ ] [KIKO-032A — Validate prerequisite references and ordering](checkpoints/05_PLANNING_CORE.md#kiko-032a)
- [ ] [KIKO-032B — Reject vague or multi-outcome checkpoints](checkpoints/05_PLANNING_CORE.md#kiko-032b)
- [ ] [KIKO-033 — Trace requirements to implementation and verification](checkpoints/05_PLANNING_CORE.md#kiko-033)
- [ ] [KIKO-033A — Audit product, data, and integration coverage](checkpoints/05_PLANNING_CORE.md#kiko-033a)
- [ ] [KIKO-033B — Audit engineering, release, and teaching coverage](checkpoints/05_PLANNING_CORE.md#kiko-033b)
- [ ] [KIKO-034 — Present a plan without overwhelming beginners](checkpoints/05_PLANNING_CORE.md#kiko-034)
- [ ] [KIKO-034A — Apply plan accept, revise, expand, and cancel decisions](checkpoints/05_PLANNING_CORE.md#kiko-034a)

## Phase 6 — Provider-neutral expert boundary

- [ ] [KIKO-035 — Define tutoring expert request and result contracts](checkpoints/06_EXPERT_BOUNDARY.md#kiko-035)
- [ ] [KIKO-035A — Define planning expert request and result contracts](checkpoints/06_EXPERT_BOUNDARY.md#kiko-035a)
- [ ] [KIKO-036 — Introduce the single ExpertProvider operation](checkpoints/06_EXPERT_BOUNDARY.md#kiko-036)
- [ ] [KIKO-037 — Prove tutoring with a deterministic fake expert](checkpoints/06_EXPERT_BOUNDARY.md#kiko-037)
- [ ] [KIKO-038 — Produce a fake candidate plan](checkpoints/06_EXPERT_BOUNDARY.md#kiko-038)
- [ ] [KIKO-038A — Critique a fake candidate plan](checkpoints/06_EXPERT_BOUNDARY.md#kiko-038a)
- [ ] [KIKO-038B — Repair or reopen a fake plan](checkpoints/06_EXPERT_BOUNDARY.md#kiko-038b)

## Phase 7 — Codex App Server adapter

- [ ] [KIKO-039 — Start and stop the App Server process](checkpoints/07_CODEX_ADAPTER.md#kiko-039)
- [ ] [KIKO-040 — Complete the initialize handshake](checkpoints/07_CODEX_ADAPTER.md#kiko-040)
- [ ] [KIKO-041 — Start and resume one project thread](checkpoints/07_CODEX_ADAPTER.md#kiko-041)
- [ ] [KIKO-042 — Read and correlate JSONL messages](checkpoints/07_CODEX_ADAPTER.md#kiko-042)
- [ ] [KIKO-042A — Dispatch known and unknown App Server events](checkpoints/07_CODEX_ADAPTER.md#kiko-042a)
- [ ] [KIKO-042B — Terminate timeout, cancel, and process-exit paths](checkpoints/07_CODEX_ADAPTER.md#kiko-042b)
- [ ] [KIKO-043 — Complete one validated read-only tutoring turn](checkpoints/07_CODEX_ADAPTER.md#kiko-043)
- [ ] [KIKO-044 — Generate one live candidate plan](checkpoints/07_CODEX_ADAPTER.md#kiko-044)
- [ ] [KIKO-044A — Run one live plan critique turn](checkpoints/07_CODEX_ADAPTER.md#kiko-044a)
- [ ] [KIKO-044B — Repair or reopen a live plan candidate](checkpoints/07_CODEX_ADAPTER.md#kiko-044b)
- [ ] [KIKO-045 — Defend the expert boundary from unsafe repository content](checkpoints/07_CODEX_ADAPTER.md#kiko-045)

## Phase 8 — Standalone CLI vertical slice

- [ ] [KIKO-046 — Add stable learner-facing CLI commands](checkpoints/08_CLI_VERTICAL_SLICE.md#kiko-046)
- [ ] [KIKO-047 — Connect the complete help interaction](checkpoints/08_CLI_VERTICAL_SLICE.md#kiko-047)
- [ ] [KIKO-048 — Render one failed CLI review](checkpoints/08_CLI_VERTICAL_SLICE.md#kiko-048)
- [ ] [KIKO-048A — Persist one passing review transaction](checkpoints/08_CLI_VERTICAL_SLICE.md#kiko-048a)
- [ ] [KIKO-049 — Complete CLI discovery and brief acceptance](checkpoints/08_CLI_VERTICAL_SLICE.md#kiko-049)
- [ ] [KIKO-049A — Generate and review a CLI plan candidate](checkpoints/08_CLI_VERTICAL_SLICE.md#kiko-049a)
- [ ] [KIKO-049B — Accept and create Tutor files transactionally](checkpoints/08_CLI_VERTICAL_SLICE.md#kiko-049b)
- [ ] [KIKO-050 — Complete controlled feedback through CLI](checkpoints/08_CLI_VERTICAL_SLICE.md#kiko-050)

## Phase 9 — Thin VS Code extension and v0.1 proof

- [ ] [KIKO-051 — Create the TypeScript extension shell](checkpoints/09_VSCODE_AND_V01.md#kiko-051)
- [ ] [KIKO-052 — Start and stop Core from the extension](checkpoints/09_VSCODE_AND_V01.md#kiko-052)
- [ ] [KIKO-052A — Correlate one extension/Core JSONL request](checkpoints/09_VSCODE_AND_V01.md#kiko-052a)
- [ ] [KIKO-052B — Handle extension/Core cancel and failure disposal](checkpoints/09_VSCODE_AND_V01.md#kiko-052b)
- [ ] [KIKO-053 — Render setup, ready, and working states](checkpoints/09_VSCODE_AND_V01.md#kiko-053)
- [ ] [KIKO-053A — Render response and review sidebar states](checkpoints/09_VSCODE_AND_V01.md#kiko-053a)
- [ ] [KIKO-053B — Render recoverable-error and blocked states](checkpoints/09_VSCODE_AND_V01.md#kiko-053b)
- [ ] [KIKO-054 — Connect sidebar help and hint actions](checkpoints/09_VSCODE_AND_V01.md#kiko-054)
- [ ] [KIKO-054A — Connect the sidebar review action](checkpoints/09_VSCODE_AND_V01.md#kiko-054a)
- [ ] [KIKO-054B — Connect the sidebar planning action](checkpoints/09_VSCODE_AND_V01.md#kiko-054b)
- [ ] [KIKO-054C — Connect cancel, retry, and unclear-feedback actions](checkpoints/09_VSCODE_AND_V01.md#kiko-054c)
- [ ] [KIKO-055 — Test the extension against a fake Core](checkpoints/09_VSCODE_AND_V01.md#kiko-055)
- [ ] [KIKO-056 — Pass the v0.1 end-to-end vertical proof](checkpoints/09_VSCODE_AND_V01.md#kiko-056)

## Phase 10 — Product quality and onboarding

- [ ] [KIKO-057 — Diagnose dependencies and authentication](checkpoints/10_PRODUCT_QUALITY.md#kiko-057)
- [ ] [KIKO-058 — Recognize workspace and show setup readiness](checkpoints/10_PRODUCT_QUALITY.md#kiko-058)
- [ ] [KIKO-058A — Complete onboarding discovery and approvals](checkpoints/10_PRODUCT_QUALITY.md#kiko-058a)
- [ ] [KIKO-058B — Create or resume the project transactionally](checkpoints/10_PRODUCT_QUALITY.md#kiko-058b)
- [ ] [KIKO-059 — Define stable product error codes and recovery mapping](checkpoints/10_PRODUCT_QUALITY.md#kiko-059)
- [ ] [KIKO-059A — Present recovery actions consistently across surfaces](checkpoints/10_PRODUCT_QUALITY.md#kiko-059a)
- [ ] [KIKO-060 — Inspect and export learner and feedback data](checkpoints/10_PRODUCT_QUALITY.md#kiko-060)
- [ ] [KIKO-060A — Reset or delete selected local data safely](checkpoints/10_PRODUCT_QUALITY.md#kiko-060a)
- [ ] [KIKO-061 — Localize headings without changing technical literals](checkpoints/10_PRODUCT_QUALITY.md#kiko-061)
- [ ] [KIKO-061A — Verify keyboard and visual accessibility](checkpoints/10_PRODUCT_QUALITY.md#kiko-061a)
- [ ] [KIKO-062 — Aggregate one full product verification command](checkpoints/10_PRODUCT_QUALITY.md#kiko-062)

## Phase 11 — Installable artifacts

- [ ] [KIKO-063 — Choose and prove the macOS Core distribution](checkpoints/11_PACKAGING.md#kiko-063)
- [ ] [KIKO-064 — Build the versioned Core and CLI artifact](checkpoints/11_PACKAGING.md#kiko-064)
- [ ] [KIKO-064A — Complete Core signing, notices, and isolated smoke](checkpoints/11_PACKAGING.md#kiko-064a)
- [ ] [KIKO-065 — Package an installable VS Code VSIX](checkpoints/11_PACKAGING.md#kiko-065)
- [ ] [KIKO-066 — Produce reproducible versioned release output](checkpoints/11_PACKAGING.md#kiko-066)

## Phase 12 — Security, compatibility, and lifecycle hardening

- [ ] [KIKO-067 — Enforce the read-only learning boundary](checkpoints/12_HARDENING.md#kiko-067)
- [ ] [KIKO-068 — Prevent concurrent state writers](checkpoints/12_HARDENING.md#kiko-068)
- [ ] [KIKO-068A — Cancel and shut down the full process tree](checkpoints/12_HARDENING.md#kiko-068a)
- [ ] [KIKO-069 — Upgrade supported state and protocol versions](checkpoints/12_HARDENING.md#kiko-069)
- [ ] [KIKO-069A — Roll back failed migration and protect downgrades](checkpoints/12_HARDENING.md#kiko-069a)
- [ ] [KIKO-070 — Establish the supported compatibility matrix](checkpoints/12_HARDENING.md#kiko-070)
- [ ] [KIKO-071 — Bound context size and estimated model cost](checkpoints/12_HARDENING.md#kiko-071)
- [ ] [KIKO-071A — Measure and bound latency and memory](checkpoints/12_HARDENING.md#kiko-071a)
- [ ] [KIKO-071B — Bound retries and retained logs](checkpoints/12_HARDENING.md#kiko-071b)

## Phase 13 — Finished-product release

- [ ] [KIKO-072 — Install on a clean supported macOS profile](checkpoints/13_RELEASE.md#kiko-072)
- [ ] [KIKO-073 — Complete and resume a real learning journey](checkpoints/13_RELEASE.md#kiko-073)
- [ ] [KIKO-074 — Prove cross-project knowledge and progress isolation](checkpoints/13_RELEASE.md#kiko-074)
- [ ] [KIKO-074A — Prove release failure and feedback recovery](checkpoints/13_RELEASE.md#kiko-074a)
- [ ] [KIKO-075 — Prove packaged upgrade without data loss](checkpoints/13_RELEASE.md#kiko-075)
- [ ] [KIKO-075A — Prove uninstall and data-retention choices](checkpoints/13_RELEASE.md#kiko-075a)
- [ ] [KIKO-076 — Create the v1.0 release record](checkpoints/13_RELEASE.md#kiko-076)

## Change policy

- Preserve stable checkpoint IDs after acceptance.
- Add new requirements only through confirmed scope or accepted dogfood feedback.
- A reordered pending checkpoint keeps its ID and updates dependency links.
- A changed product decision identifies affected checkpoints before replanning.
- Completed checkpoints remain complete unless observable evidence is invalidated.
- Detailed checkpoint files never contain completion checkboxes.
