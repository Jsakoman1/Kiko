# Kiko v1.0 Learning and Delivery Plan

## Authority and format

This file is the only source of checkpoint order, checkbox progress, active
work, and handoff. Stable checkpoint teaching contracts live under
`.tutor/checkpoints/` and contain no competing completion status.

Every checkpoint specification uses the same fields required by
`PLANNING_SPEC.md`: kind, outcome, product reason, prerequisites, known concepts,
new concepts/syntax, one learner task, exact verification, expected behavior,
edge case, exclusions, and exit condition.

Development authorship and delegation modes live separately in
`EXECUTION_MODES.md`; they do not duplicate progress or checkpoint contracts.

## Current handoff

- Active checkpoint: `KIKO-015D` — Validate the session-state contract.
- Status: in progress.
- Last verified: `KIKO-015C` — added a separate versioned learner-state
  profile/concepts validator that rejects malformed and project-state shapes
  while preserving unknown non-conflicting fields.
- Current product truth: Kiko is an editable local Python package with a stable
  `.venv/bin/kiko` command. Its `show` behavior reads separate project, learner,
  and reference sources and displays `runtime_checkpoint: not-initialized` as
  runtime learner-project state. A pure project-state validator now checks the
  root, supported version, required nested fields, and their types while
  preserving unknown fields. The real loading boundary now validates parsed and
  default state through an injected path; isolated loading tests also prove that
  invalid saved input remains unchanged. Learner state now has its own pure
  owner-specific validator and reusable typed-field checks, without coupling it
  to project-state fields.
- Development progress authority: this file. Runtime project state separately
  owns `runtime_checkpoint` in `.tutor/state.json`.
- Planning system: idea discovery, readiness, candidate critique, lesson
  contract, and dogfood feedback systems are adopted.
- Future-checkpoint readiness: all remaining accepted checkpoints retain their
  individual post-split lesson dry-run result; KIKO-015D is now active.
- Hybrid execution: accepted for all pending work; active KIKO-015D is
  `agent-delegated`. Agent-written work may advance verified product progress but
  never counts as learner competence by itself.
- Blockers: none for `KIKO-015D`.

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

- [x] [KIKO-011 — Read the personal reference](checkpoints/01_REFERENCE.md#kiko-011)

## Phase 2 — Maintainable Core foundation

- [x] [KIKO-012 — Create an isolated Python development environment](checkpoints/02_CORE_FOUNDATION.md#kiko-012)
- [x] [KIKO-012A — Migrate existing CLI behavior into the package](checkpoints/02_CORE_FOUNDATION.md#kiko-012a)
- [x] [KIKO-012B — Add editable install and the `kiko` console command](checkpoints/02_CORE_FOUNDATION.md#kiko-012b)
- [x] [KIKO-013 — Separate development progress from runtime project state](checkpoints/02_CORE_FOUNDATION.md#kiko-013)
- [x] [KIKO-014 — Establish the first unittest discovery test](checkpoints/02_CORE_FOUNDATION.md#kiko-014)
- [x] [KIKO-014A — Isolate filesystem tests from real learner data](checkpoints/02_CORE_FOUNDATION.md#kiko-014a)
- [x] [KIKO-015 — Validate the project-state root and version](checkpoints/02_CORE_FOUNDATION.md#kiko-015)
- [x] [KIKO-015A — Validate project-state required fields and types](checkpoints/02_CORE_FOUNDATION.md#kiko-015a)
- [x] [KIKO-015B — Enforce the project-state contract during loading](checkpoints/02_CORE_FOUNDATION.md#kiko-015b)
- [x] [KIKO-015C — Validate the learner-state contract](checkpoints/02_CORE_FOUNDATION.md#kiko-015c)
- [ ] [KIKO-015D — Validate the session-state contract](checkpoints/02_CORE_FOUNDATION.md#kiko-015d) **NEXT**
- [ ] [KIKO-015E — Validate the Tutor-feedback-state contract](checkpoints/02_CORE_FOUNDATION.md#kiko-015e)
- [ ] [KIKO-016 — Write state through atomic replacement](checkpoints/02_CORE_FOUNDATION.md#kiko-016)
- [ ] [KIKO-016A — Preserve a recoverable state backup](checkpoints/02_CORE_FOUNDATION.md#kiko-016a)
- [ ] [KIKO-016B — Restore a validated state backup](checkpoints/02_CORE_FOUNDATION.md#kiko-016b)
- [ ] [KIKO-016C — Migrate a supported state schema version](checkpoints/02_CORE_FOUNDATION.md#kiko-016c)
- [ ] [KIKO-017 — Define the versioned JSONL request/result envelope](checkpoints/02_CORE_FOUNDATION.md#kiko-017)
- [ ] [KIKO-017A — Define the protocol error result](checkpoints/02_CORE_FOUNDATION.md#kiko-017a)
- [ ] [KIKO-017B — Define protocol progress events](checkpoints/02_CORE_FOUNDATION.md#kiko-017b)
- [ ] [KIKO-017C — Define protocol cancellation messages](checkpoints/02_CORE_FOUNDATION.md#kiko-017c)
- [ ] [KIKO-018 — Enforce workspace file containment](checkpoints/02_CORE_FOUNDATION.md#kiko-018)
- [ ] [KIKO-018A — Accept only bounded repository text](checkpoints/02_CORE_FOUNDATION.md#kiko-018a)
- [ ] [KIKO-018B — Filter likely repository secrets](checkpoints/02_CORE_FOUNDATION.md#kiko-018b)
- [ ] [KIKO-018C — Label repository text as untrusted model data](checkpoints/02_CORE_FOUNDATION.md#kiko-018c)

## Phase 3 — Conservative learner evidence

- [ ] [KIKO-019 — Create one minimal evidence record](checkpoints/03_EVIDENCE.md#kiko-019)
- [ ] [KIKO-020 — Update one encountered concept conservatively](checkpoints/03_EVIDENCE.md#kiko-020)
- [ ] [KIKO-021 — Save learner state without losing unrelated data](checkpoints/03_EVIDENCE.md#kiko-021)
- [ ] [KIKO-022 — Add a used syntax entry to the personal reference](checkpoints/03_EVIDENCE.md#kiko-022)

## Phase 4 — Deterministic teaching Core

- [ ] [KIKO-023 — Represent and validate one learner request](checkpoints/04_TEACHING_CORE.md#kiko-023)
- [ ] [KIKO-024 — Select the interaction intent](checkpoints/04_TEACHING_CORE.md#kiko-024)
- [ ] [KIKO-024A — Select the assistance level](checkpoints/04_TEACHING_CORE.md#kiko-024a)
- [ ] [KIKO-025 — Build and audit a code-syntax preflight](checkpoints/04_TEACHING_CORE.md#kiko-025)
- [ ] [KIKO-025A — Build and audit a configuration-format preflight](checkpoints/04_TEACHING_CORE.md#kiko-025a)
- [ ] [KIKO-026 — Compile allowed Tutor context](checkpoints/04_TEACHING_CORE.md#kiko-026)
- [ ] [KIKO-026A — Enforce the Tutor-context size boundary](checkpoints/04_TEACHING_CORE.md#kiko-026a)
- [ ] [KIKO-027 — Build the canonical new-checkpoint interaction](checkpoints/04_TEACHING_CORE.md#kiko-027)
- [ ] [KIKO-027A — Validate reminder interactions](checkpoints/04_TEACHING_CORE.md#kiko-027a)
- [ ] [KIKO-027B — Validate hint interactions](checkpoints/04_TEACHING_CORE.md#kiko-027b)
- [ ] [KIKO-027C — Validate failed-review interactions](checkpoints/04_TEACHING_CORE.md#kiko-027c)
- [ ] [KIKO-027D — Validate passing-review interactions](checkpoints/04_TEACHING_CORE.md#kiko-027d)
- [ ] [KIKO-027E — Validate debug interactions](checkpoints/04_TEACHING_CORE.md#kiko-027e)
- [ ] [KIKO-027F — Validate completion-handoff interactions](checkpoints/04_TEACHING_CORE.md#kiko-027f)
- [ ] [KIKO-028 — Classify Tutor-quality feedback](checkpoints/04_TEACHING_CORE.md#kiko-028)
- [ ] [KIKO-028A — Repair the current interaction](checkpoints/04_TEACHING_CORE.md#kiko-028a)
- [ ] [KIKO-028B — Sanitize a feedback candidate](checkpoints/04_TEACHING_CORE.md#kiko-028b)
- [ ] [KIKO-028C — Deduplicate feedback candidates](checkpoints/04_TEACHING_CORE.md#kiko-028c)

## Phase 5 — Idea discovery and planning Core

- [ ] [KIKO-029 — Classify facts, decisions, assumptions, and future ideas](checkpoints/05_PLANNING_CORE.md#kiko-029)
- [ ] [KIKO-030 — Run beginner-friendly discovery rounds](checkpoints/05_PLANNING_CORE.md#kiko-030)
- [ ] [KIKO-030A — Apply one discovery answer safely](checkpoints/05_PLANNING_CORE.md#kiko-030a)
- [ ] [KIKO-031 — Enforce brief readiness](checkpoints/05_PLANNING_CORE.md#kiko-031)
- [ ] [KIKO-031A — Record separate brief acceptance](checkpoints/05_PLANNING_CORE.md#kiko-031a)
- [ ] [KIKO-032 — Validate required checkpoint fields](checkpoints/05_PLANNING_CORE.md#kiko-032)
- [ ] [KIKO-032A — Validate unique stable checkpoint IDs](checkpoints/05_PLANNING_CORE.md#kiko-032a)
- [ ] [KIKO-032B — Validate prerequisite references and ordering](checkpoints/05_PLANNING_CORE.md#kiko-032b)
- [ ] [KIKO-032C — Reject vague or multi-outcome checkpoints](checkpoints/05_PLANNING_CORE.md#kiko-032c)
- [ ] [KIKO-032D — Require lesson readiness for every final checkpoint](checkpoints/05_PLANNING_CORE.md#kiko-032d)
- [ ] [KIKO-033 — Trace requirements to implementation and verification](checkpoints/05_PLANNING_CORE.md#kiko-033)
- [ ] [KIKO-033A — Audit user-experience coverage](checkpoints/05_PLANNING_CORE.md#kiko-033a)
- [ ] [KIKO-033B — Audit data-lifecycle coverage](checkpoints/05_PLANNING_CORE.md#kiko-033b)
- [ ] [KIKO-033C — Audit external-integration coverage](checkpoints/05_PLANNING_CORE.md#kiko-033c)
- [ ] [KIKO-033D — Audit engineering-quality coverage](checkpoints/05_PLANNING_CORE.md#kiko-033d)
- [ ] [KIKO-033E — Audit delivery and lifecycle coverage](checkpoints/05_PLANNING_CORE.md#kiko-033e)
- [ ] [KIKO-033F — Audit teaching-order coverage](checkpoints/05_PLANNING_CORE.md#kiko-033f)
- [ ] [KIKO-034 — Present a plan without overwhelming beginners](checkpoints/05_PLANNING_CORE.md#kiko-034)
- [ ] [KIKO-034A — Accept one validated plan candidate](checkpoints/05_PLANNING_CORE.md#kiko-034a)
- [ ] [KIKO-034B — Revise or reopen a plan candidate](checkpoints/05_PLANNING_CORE.md#kiko-034b)
- [ ] [KIKO-034C — Cancel a plan candidate safely](checkpoints/05_PLANNING_CORE.md#kiko-034c)

## Phase 6 — Provider-neutral expert boundary

- [ ] [KIKO-035 — Define tutoring expert request and result contracts](checkpoints/06_EXPERT_BOUNDARY.md#kiko-035)
- [ ] [KIKO-035A — Define candidate-plan expert contracts](checkpoints/06_EXPERT_BOUNDARY.md#kiko-035a)
- [ ] [KIKO-035B — Define plan-critique expert contracts](checkpoints/06_EXPERT_BOUNDARY.md#kiko-035b)
- [ ] [KIKO-035C — Define plan-repair expert contracts](checkpoints/06_EXPERT_BOUNDARY.md#kiko-035c)
- [ ] [KIKO-036 — Define the single ExpertProvider operation](checkpoints/06_EXPERT_BOUNDARY.md#kiko-036)
- [ ] [KIKO-036A — Inject and call an ExpertProvider](checkpoints/06_EXPERT_BOUNDARY.md#kiko-036a)
- [ ] [KIKO-037 — Prove tutoring with a deterministic fake expert](checkpoints/06_EXPERT_BOUNDARY.md#kiko-037)
- [ ] [KIKO-038 — Produce a fake candidate plan](checkpoints/06_EXPERT_BOUNDARY.md#kiko-038)
- [ ] [KIKO-038A — Critique a fake candidate plan](checkpoints/06_EXPERT_BOUNDARY.md#kiko-038a)
- [ ] [KIKO-038B — Repair or reopen a fake plan](checkpoints/06_EXPERT_BOUNDARY.md#kiko-038b)

## Phase 7 — Codex App Server adapter

- [ ] [KIKO-039 — Start and stop the App Server process](checkpoints/07_CODEX_ADAPTER.md#kiko-039)
- [ ] [KIKO-040 — Complete the initialize handshake](checkpoints/07_CODEX_ADAPTER.md#kiko-040)
- [ ] [KIKO-041 — Start one project thread](checkpoints/07_CODEX_ADAPTER.md#kiko-041)
- [ ] [KIKO-041A — Resume or replace one project thread](checkpoints/07_CODEX_ADAPTER.md#kiko-041a)
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
- [ ] [KIKO-049B — Stage and validate accepted Tutor files](checkpoints/08_CLI_VERTICAL_SLICE.md#kiko-049b)
- [ ] [KIKO-049C — Commit or roll back Tutor-file creation](checkpoints/08_CLI_VERTICAL_SLICE.md#kiko-049c)
- [ ] [KIKO-050 — Repair feedback and preview its CLI candidate](checkpoints/08_CLI_VERTICAL_SLICE.md#kiko-050)
- [ ] [KIKO-050A — Keep, edit, or discard a CLI feedback candidate](checkpoints/08_CLI_VERTICAL_SLICE.md#kiko-050a)
- [ ] [KIKO-050B — Export a sanitized feedback candidate](checkpoints/08_CLI_VERTICAL_SLICE.md#kiko-050b)

## Phase 9 — Thin VS Code extension and v0.1 proof

- [ ] [KIKO-051 — Create the TypeScript extension development environment](checkpoints/09_VSCODE_AND_V01.md#kiko-051)
- [ ] [KIKO-051A — Activate a static Kiko sidebar](checkpoints/09_VSCODE_AND_V01.md#kiko-051a)
- [ ] [KIKO-052 — Start and stop Core from the extension](checkpoints/09_VSCODE_AND_V01.md#kiko-052)
- [ ] [KIKO-052A — Correlate one extension/Core JSONL request](checkpoints/09_VSCODE_AND_V01.md#kiko-052a)
- [ ] [KIKO-052B — Handle extension/Core cancel and failure disposal](checkpoints/09_VSCODE_AND_V01.md#kiko-052b)
- [ ] [KIKO-053 — Render setup, ready, and working states](checkpoints/09_VSCODE_AND_V01.md#kiko-053)
- [ ] [KIKO-053A — Render response and review sidebar states](checkpoints/09_VSCODE_AND_V01.md#kiko-053a)
- [ ] [KIKO-053B — Render recoverable-error and blocked states](checkpoints/09_VSCODE_AND_V01.md#kiko-053b)
- [ ] [KIKO-054 — Connect sidebar help and hint actions](checkpoints/09_VSCODE_AND_V01.md#kiko-054)
- [ ] [KIKO-054A — Connect the sidebar review action](checkpoints/09_VSCODE_AND_V01.md#kiko-054a)
- [ ] [KIKO-054B — Connect the sidebar planning action](checkpoints/09_VSCODE_AND_V01.md#kiko-054b)
- [ ] [KIKO-054C — Connect cancel and retry actions](checkpoints/09_VSCODE_AND_V01.md#kiko-054c)
- [ ] [KIKO-054D — Connect the unclear-feedback action](checkpoints/09_VSCODE_AND_V01.md#kiko-054d)
- [ ] [KIKO-055 — Test the extension against a fake Core](checkpoints/09_VSCODE_AND_V01.md#kiko-055)
- [ ] [KIKO-056 — Pass the v0.1 end-to-end vertical proof](checkpoints/09_VSCODE_AND_V01.md#kiko-056)

## Phase 10 — Product quality and onboarding

- [ ] [KIKO-057 — Diagnose dependencies and authentication](checkpoints/10_PRODUCT_QUALITY.md#kiko-057)
- [ ] [KIKO-058 — Recognize workspace and show setup readiness](checkpoints/10_PRODUCT_QUALITY.md#kiko-058)
- [ ] [KIKO-058A — Complete onboarding discovery and approvals](checkpoints/10_PRODUCT_QUALITY.md#kiko-058a)
- [ ] [KIKO-058B — Create or resume the project transactionally](checkpoints/10_PRODUCT_QUALITY.md#kiko-058b)
- [ ] [KIKO-059 — Define stable product error codes and recovery mapping](checkpoints/10_PRODUCT_QUALITY.md#kiko-059)
- [ ] [KIKO-059A — Present recovery actions consistently across surfaces](checkpoints/10_PRODUCT_QUALITY.md#kiko-059a)
- [ ] [KIKO-060 — Inspect learner and feedback data](checkpoints/10_PRODUCT_QUALITY.md#kiko-060)
- [ ] [KIKO-060A — Export learner and feedback data](checkpoints/10_PRODUCT_QUALITY.md#kiko-060a)
- [ ] [KIKO-060B — Reset one selected local data owner](checkpoints/10_PRODUCT_QUALITY.md#kiko-060b)
- [ ] [KIKO-060C — Delete one selected local data owner](checkpoints/10_PRODUCT_QUALITY.md#kiko-060c)
- [ ] [KIKO-061 — Localize headings without changing technical literals](checkpoints/10_PRODUCT_QUALITY.md#kiko-061)
- [ ] [KIKO-061A — Verify keyboard, labels, and focus](checkpoints/10_PRODUCT_QUALITY.md#kiko-061a)
- [ ] [KIKO-061B — Verify visual and text accessibility](checkpoints/10_PRODUCT_QUALITY.md#kiko-061b)
- [ ] [KIKO-062 — Aggregate one full product verification command](checkpoints/10_PRODUCT_QUALITY.md#kiko-062)

## Phase 11 — Installable artifacts

- [ ] [KIKO-063 — Choose and prove the macOS Core distribution](checkpoints/11_PACKAGING.md#kiko-063)
- [ ] [KIKO-064 — Build the versioned Core and CLI artifact](checkpoints/11_PACKAGING.md#kiko-064)
- [ ] [KIKO-064A — Bundle Core licenses and notices](checkpoints/11_PACKAGING.md#kiko-064a)
- [ ] [KIKO-064B — Sign and verify the Core artifact](checkpoints/11_PACKAGING.md#kiko-064b)
- [ ] [KIKO-064C — Smoke-test the Core artifact in isolation](checkpoints/11_PACKAGING.md#kiko-064c)
- [ ] [KIKO-065 — Package an installable VS Code VSIX](checkpoints/11_PACKAGING.md#kiko-065)
- [ ] [KIKO-066 — Produce reproducible versioned release output](checkpoints/11_PACKAGING.md#kiko-066)

## Phase 12 — Security, compatibility, and lifecycle hardening

- [ ] [KIKO-067 — Enforce the read-only learning boundary](checkpoints/12_HARDENING.md#kiko-067)
- [ ] [KIKO-068 — Prevent concurrent state writers](checkpoints/12_HARDENING.md#kiko-068)
- [ ] [KIKO-068A — Cancel and shut down the full process tree](checkpoints/12_HARDENING.md#kiko-068a)
- [ ] [KIKO-069 — Upgrade supported state-owner versions](checkpoints/12_HARDENING.md#kiko-069)
- [ ] [KIKO-069A — Upgrade the supported local protocol](checkpoints/12_HARDENING.md#kiko-069a)
- [ ] [KIKO-069B — Roll back a failed multi-owner migration](checkpoints/12_HARDENING.md#kiko-069b)
- [ ] [KIKO-069C — Protect future-version and downgrade paths](checkpoints/12_HARDENING.md#kiko-069c)
- [ ] [KIKO-070 — Establish the supported compatibility matrix](checkpoints/12_HARDENING.md#kiko-070)
- [ ] [KIKO-071 — Bound context and token estimates](checkpoints/12_HARDENING.md#kiko-071)
- [ ] [KIKO-071A — Report estimated model cost conservatively](checkpoints/12_HARDENING.md#kiko-071a)
- [ ] [KIKO-071B — Measure and bound lifecycle latency](checkpoints/12_HARDENING.md#kiko-071b)
- [ ] [KIKO-071C — Measure and bound process memory](checkpoints/12_HARDENING.md#kiko-071c)
- [ ] [KIKO-071D — Bound automatic retries](checkpoints/12_HARDENING.md#kiko-071d)
- [ ] [KIKO-071E — Sanitize and bound retained diagnostic logs](checkpoints/12_HARDENING.md#kiko-071e)

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
