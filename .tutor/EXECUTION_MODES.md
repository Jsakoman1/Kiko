# Kiko Hybrid Execution Modes

## Authority and scope

This file assigns one development execution mode to every pending checkpoint.
It changes who may author a bounded implementation, not checkpoint order,
product scope, acceptance behavior, or progress. `LEARNING_PLAN.md` remains the
only progress authority and detailed contracts remain under `checkpoints/`.

The learner accepted this hybrid development mode to preserve meaningful
learning while reaching a finished product faster. The mode may be overridden
for one checkpoint by an explicit learner request; the change must remain
visible and must not retroactively overstate competence.

## Modes

- `learner-owned`: the learner writes substantive source. Codex teaches,
  hints, debugs, and reviews without implementing the checkpoint.
- `pair-programmed`: learner and Codex may edit the bounded checkpoint
  together after the learner understands the problem, syntax, and intended
  design. The review records which parts were learner-authored.
- `agent-delegated`: Codex may implement the bounded checkpoint because it is
  repetitive, integration glue, or scaffolding after a representative pattern.
  It must show the plan/diff, run exact verification, and hand the code back for
  learner review.
- `acceptance-only`: no new substantive product behavior should be authored.
  Codex may prepare commands/evidence, but the learner runs or witnesses the
  scenario and owns the accept/reject decision.

## Evidence and safety rules

- Agent-written code can complete product progress after verification, but is
  not evidence of learner competence.
- `pair-programmed` evidence records only the behavior the learner actually
  explained, changed, or debugged.
- `agent-delegated` work becomes learning evidence only after a separate
  learner-authored modification or independent explanation/diagnosis.
- Agent work never broadens the active checkpoint, rewrites unrelated source,
  bypasses destructive-action approval, or combines unmet prerequisites.
- Several delegated checkpoints may share one implementation session only when
  they repeat one established pattern; every checkpoint retains its own test,
  verdict, and progress update.
- Before starting a checkpoint, the Tutor reads its row here and states the
  execution mode in the progress header.

## Distribution

- Learner-owned: 40
- Pair-programmed: 46
- Agent-delegated: 54
- Acceptance-only: 11
- Total pending: 151

## Pending checkpoint assignments

| Checkpoint | Title | Mode | Reason |
| --- | --- | --- | --- |
| `KIKO-015` | Validate the project-state root and version | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-015A` | Validate project-state required fields and types | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-015B` | Enforce the project-state contract during loading | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-015C` | Validate the learner-state contract | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-015D` | Validate the session-state contract | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-015E` | Validate the Tutor-feedback-state contract | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-016` | Write state through atomic replacement | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-016A` | Preserve a recoverable state backup | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-016B` | Restore a validated state backup | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-016C` | Migrate a supported state schema version | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-017` | Define the versioned JSONL request/result envelope | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-017A` | Define the protocol error result | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-017B` | Define protocol progress events | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-017C` | Define protocol cancellation messages | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-018` | Enforce workspace file containment | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-018A` | Accept only bounded repository text | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-018B` | Filter likely repository secrets | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-018C` | Label repository text as untrusted model data | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-019` | Create one minimal evidence record | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-020` | Update one encountered concept conservatively | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-021` | Save learner state without losing unrelated data | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-022` | Add a used syntax entry to the personal reference | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-023` | Represent and validate one learner request | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-024` | Select the interaction intent | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-024A` | Select the assistance level | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-025` | Build and audit a code-syntax preflight | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-025A` | Build and audit a configuration-format preflight | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-026` | Compile allowed Tutor context | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-026A` | Enforce the Tutor-context size boundary | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-027` | Build the canonical new-checkpoint interaction | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-027A` | Validate reminder interactions | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-027B` | Validate hint interactions | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-027C` | Validate failed-review interactions | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-027D` | Validate passing-review interactions | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-027E` | Validate debug interactions | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-027F` | Validate completion-handoff interactions | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-028` | Classify Tutor-quality feedback | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-028A` | Repair the current interaction | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-028B` | Sanitize a feedback candidate | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-028C` | Deduplicate feedback candidates | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-029` | Classify facts, decisions, assumptions, and future ideas | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-030` | Run beginner-friendly discovery rounds | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-030A` | Apply one discovery answer safely | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-031` | Enforce brief readiness | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-031A` | Record separate brief acceptance | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-032` | Validate required checkpoint fields | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-032A` | Validate unique stable checkpoint IDs | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-032B` | Validate prerequisite references and ordering | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-032C` | Reject vague or multi-outcome checkpoints | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-032D` | Require lesson readiness for every final checkpoint | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-033` | Trace requirements to implementation and verification | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-033A` | Audit user-experience coverage | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-033B` | Audit data-lifecycle coverage | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-033C` | Audit external-integration coverage | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-033D` | Audit engineering-quality coverage | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-033E` | Audit delivery and lifecycle coverage | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-033F` | Audit teaching-order coverage | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-034` | Present a plan without overwhelming beginners | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-034A` | Accept one validated plan candidate | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-034B` | Revise or reopen a plan candidate | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-034C` | Cancel a plan candidate safely | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-035` | Define tutoring expert request and result contracts | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-035A` | Define candidate-plan expert contracts | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-035B` | Define plan-critique expert contracts | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-035C` | Define plan-repair expert contracts | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-036` | Define the single ExpertProvider operation | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-036A` | Inject and call an ExpertProvider | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-037` | Prove tutoring with a deterministic fake expert | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-038` | Produce a fake candidate plan | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-038A` | Critique a fake candidate plan | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-038B` | Repair or reopen a fake plan | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-039` | Start and stop the App Server process | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-040` | Complete the initialize handshake | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-041` | Start one project thread | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-041A` | Resume or replace one project thread | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-042` | Read and correlate JSONL messages | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-042A` | Dispatch known and unknown App Server events | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-042B` | Terminate timeout, cancel, and process-exit paths | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-043` | Complete one validated read-only tutoring turn | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-044` | Generate one live candidate plan | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-044A` | Run one live plan critique turn | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-044B` | Repair or reopen a live plan candidate | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-045` | Defend the expert boundary from unsafe repository content | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-046` | Add stable learner-facing CLI commands | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-047` | Connect the complete help interaction | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-048` | Render one failed CLI review | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-048A` | Persist one passing review transaction | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-049` | Complete CLI discovery and brief acceptance | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-049A` | Generate and review a CLI plan candidate | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-049B` | Stage and validate accepted Tutor files | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-049C` | Commit or roll back Tutor-file creation | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-050` | Repair feedback and preview its CLI candidate | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-050A` | Keep, edit, or discard a CLI feedback candidate | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-050B` | Export a sanitized feedback candidate | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-051` | Create the TypeScript extension development environment | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-051A` | Activate a static Kiko sidebar | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-052` | Start and stop Core from the extension | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-052A` | Correlate one extension/Core JSONL request | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-052B` | Handle extension/Core cancel and failure disposal | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-053` | Render setup, ready, and working states | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-053A` | Render response and review sidebar states | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-053B` | Render recoverable-error and blocked states | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-054` | Connect sidebar help and hint actions | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-054A` | Connect the sidebar review action | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-054B` | Connect the sidebar planning action | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-054C` | Connect cancel and retry actions | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-054D` | Connect the unclear-feedback action | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-055` | Test the extension against a fake Core | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-056` | Pass the v0.1 end-to-end vertical proof | `acceptance-only` | Decision or release proof over existing behavior; learner runs, interprets, and approves the evidence. |
| `KIKO-057` | Diagnose dependencies and authentication | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-058` | Recognize workspace and show setup readiness | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-058A` | Complete onboarding discovery and approvals | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-058B` | Create or resume the project transactionally | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-059` | Define stable product error codes and recovery mapping | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-059A` | Present recovery actions consistently across surfaces | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-060` | Inspect learner and feedback data | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-060A` | Export learner and feedback data | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-060B` | Reset one selected local data owner | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-060C` | Delete one selected local data owner | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-061` | Localize headings without changing technical literals | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-061A` | Verify keyboard, labels, and focus | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-061B` | Verify visual and text accessibility | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-062` | Aggregate one full product verification command | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-063` | Choose and prove the macOS Core distribution | `acceptance-only` | Decision or release proof over existing behavior; learner runs, interprets, and approves the evidence. |
| `KIKO-064` | Build the versioned Core and CLI artifact | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-064A` | Bundle Core licenses and notices | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-064B` | Sign and verify the Core artifact | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-064C` | Smoke-test the Core artifact in isolation | `acceptance-only` | Decision or release proof over existing behavior; learner runs, interprets, and approves the evidence. |
| `KIKO-065` | Package an installable VS Code VSIX | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-066` | Produce reproducible versioned release output | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-067` | Enforce the read-only learning boundary | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-068` | Prevent concurrent state writers | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-068A` | Cancel and shut down the full process tree | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-069` | Upgrade supported state-owner versions | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-069A` | Upgrade the supported local protocol | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-069B` | Roll back a failed multi-owner migration | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-069C` | Protect future-version and downgrade paths | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-070` | Establish the supported compatibility matrix | `acceptance-only` | Decision or release proof over existing behavior; learner runs, interprets, and approves the evidence. |
| `KIKO-071` | Bound context and token estimates | `learner-owned` | First representative pattern or central product policy; learner writes the implementation. |
| `KIKO-071A` | Report estimated model cost conservatively | `pair-programmed` | Risky state, provider, security, or cross-boundary integration; learner and agent implement/review together. |
| `KIKO-071B` | Measure and bound lifecycle latency | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-071C` | Measure and bound process memory | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-071D` | Bound automatic retries | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-071E` | Sanitize and bound retained diagnostic logs | `agent-delegated` | Repetitive variant, integration glue, or build/UI scaffolding after its core pattern; agent may implement the bounded checkpoint. |
| `KIKO-072` | Install on a clean supported macOS profile | `acceptance-only` | Decision or release proof over existing behavior; learner runs, interprets, and approves the evidence. |
| `KIKO-073` | Complete and resume a real learning journey | `acceptance-only` | Decision or release proof over existing behavior; learner runs, interprets, and approves the evidence. |
| `KIKO-074` | Prove cross-project knowledge and progress isolation | `acceptance-only` | Decision or release proof over existing behavior; learner runs, interprets, and approves the evidence. |
| `KIKO-074A` | Prove release failure and feedback recovery | `acceptance-only` | Decision or release proof over existing behavior; learner runs, interprets, and approves the evidence. |
| `KIKO-075` | Prove packaged upgrade without data loss | `acceptance-only` | Decision or release proof over existing behavior; learner runs, interprets, and approves the evidence. |
| `KIKO-075A` | Prove uninstall and data-retention choices | `acceptance-only` | Decision or release proof over existing behavior; learner runs, interprets, and approves the evidence. |
| `KIKO-076` | Create the v1.0 release record | `acceptance-only` | Decision or release proof over existing behavior; learner runs, interprets, and approves the evidence. |
