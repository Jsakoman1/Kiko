# Kiko Checkpoint Size Audit

## Audit basis

Date: 2026-09-04

Baseline: KIKO-005 introduced one mental model, one learner-owned refactor, and
one observable behavior-preservation check. Later implementation checkpoints may
be moderately larger, but should stay within roughly two to four baseline-sized
changes. Integration and acceptance checkpoints may verify several existing
behaviors when they introduce no unrelated feature.

Decision meanings:

- `keep`: one sufficiently coherent implementation/decision behavior
- `split`: contained independently teachable or verifiable behaviors
- `integration`: combines existing components to answer one integration question
- `acceptance`: validates one release outcome without adding product behavior

## Audit of all originally pending checkpoints

| Original | Decision | Normalized result | Reason |
| --- | --- | --- | --- |
| KIKO-011 | keep | KIKO-011 | One read-only reference-loading behavior. |
| KIKO-012 | split | KIKO-012, KIKO-012A | Environment creation and package migration are independently learnable. |
| KIKO-013 | keep | KIKO-013 | One progress-ownership correction. |
| KIKO-014 | keep | KIKO-014 | One isolated test foundation. |
| KIKO-015 | split | KIKO-015, KIKO-015A | Defining one contract and applying it to remaining state owners are independently reviewable. |
| KIKO-016 | split | KIKO-016, KIKO-016A, KIKO-016B | Atomic replacement, backup recovery, and schema migration are separate failure models. |
| KIKO-017 | split | KIKO-017, KIKO-017A | Request/result envelopes and lifecycle event shapes are separate protocol responsibilities. |
| KIKO-018 | split | KIKO-018, KIKO-018A, KIKO-018B | Workspace containment, secret/size filtering, and prompt-injection labeling are distinct controls. |
| KIKO-019 | keep | KIKO-019 | One pure evidence record. |
| KIKO-020 | keep | KIKO-020 | One conservative concept-update rule. |
| KIKO-021 | keep | KIKO-021 | One accepted-review learner-state transaction. |
| KIKO-022 | keep | KIKO-022 | One idempotent personal-reference update. |
| KIKO-023 | keep | KIKO-023 | One learner-request value and validation boundary. |
| KIKO-024 | keep | KIKO-024 | Intent and assistance are one deterministic policy decision. |
| KIKO-025 | keep | KIKO-025 | Selection and audit serve one Syntax-preflight invariant. |
| KIKO-026 | keep | KIKO-026 | Inclusion/exclusion/size checks serve one bounded-context output. |
| KIKO-027 | split | KIKO-027, KIKO-027A, KIKO-027B, KIKO-027C | New lessons, short interactions, reviews, and debug/handoff interactions have different contracts. |
| KIKO-028 | split | KIKO-028, KIKO-028A | Feedback classification/immediate repair and candidate sanitization/deduplication are separate effects. |
| KIKO-029 | keep | KIKO-029 | One uncertainty-classification model. |
| KIKO-030 | keep | KIKO-030 | One next-question-round selection. |
| KIKO-031 | keep | KIKO-031 | One deterministic brief-readiness gate. |
| KIKO-032 | split | KIKO-032, KIKO-032A, KIKO-032B | Fields/IDs, prerequisite order, and semantic atomicity are independent validators. |
| KIKO-033 | split | KIKO-033, KIKO-033A, KIKO-033B | Traceability, product/data coverage, and engineering/release coverage are separate audits. |
| KIKO-034 | split | KIKO-034, KIKO-034A | Presenting a plan and committing the user's plan decision have different state effects. |
| KIKO-035 | split | KIKO-035, KIKO-035A | Tutoring and planning provider contracts carry different required result fields. |
| KIKO-036 | keep | KIKO-036 | One provider seam. |
| KIKO-037 | integration | KIKO-037 | One fake-expert tutoring flow using existing Core behavior. |
| KIKO-038 | split | KIKO-038, KIKO-038A, KIKO-038B | Candidate, critique, and repair/reopen are separate provider stages. |
| KIKO-039 | keep | KIKO-039 | One process-lifecycle boundary. |
| KIKO-040 | keep | KIKO-040 | One protocol handshake. |
| KIKO-041 | keep | KIKO-041 | One thread start/resume responsibility. |
| KIKO-042 | split | KIKO-042, KIKO-042A, KIKO-042B | Line correlation, event dispatch, and terminal timeout/cancel paths are distinct. |
| KIKO-043 | integration | KIKO-043 | One complete read-only tutoring turn. |
| KIKO-044 | split | KIKO-044, KIKO-044A, KIKO-044B | Live plan candidate, critique, and repair/reopen are separate turns. |
| KIKO-045 | integration | KIKO-045 | One enforcement proof over previously defined repository controls. |
| KIKO-046 | keep | KIKO-046 | One parser/dispatch skeleton; command workflows remain separate. |
| KIKO-047 | integration | KIKO-047 | One complete help interaction. |
| KIKO-048 | split | KIKO-048, KIKO-048A | Failed-review guidance and passing-review state transaction have different effects. |
| KIKO-049 | split | KIKO-049, KIKO-049A, KIKO-049B | Discovery/brief, plan review, and accepted file creation are separate user commitments. |
| KIKO-050 | integration | KIKO-050 | One CLI feedback journey over existing feedback policy. |
| KIKO-051 | keep | KIKO-051 | One extension shell. |
| KIKO-052 | split | KIKO-052, KIKO-052A, KIKO-052B | Core process ownership, request correlation, and error/cancel disposal are distinct. |
| KIKO-053 | split | KIKO-053, KIKO-053A, KIKO-053B | Setup/ready, response/review, and error/blocked views have separate UI behavior. |
| KIKO-054 | split | KIKO-054, KIKO-054A, KIKO-054B, KIKO-054C | Help, review, planning, and support/feedback action groups are independent. |
| KIKO-055 | integration | KIKO-055 | One extension-host proof against fake Core. |
| KIKO-056 | acceptance | KIKO-056 | One v0.1 vertical-slice release question. |
| KIKO-057 | keep | KIKO-057 | One diagnostic report with homogeneous capability entries. |
| KIKO-058 | split | KIKO-058, KIKO-058A, KIKO-058B | Workspace recognition, discovery/approval, and transactional creation/resume are distinct. |
| KIKO-059 | split | KIKO-059, KIKO-059A | Error taxonomy and cross-surface recovery presentation are separate. |
| KIKO-060 | split | KIKO-060, KIKO-060A | Read-only inspect/export and destructive reset/delete need different safety contracts. |
| KIKO-061 | split | KIKO-061, KIKO-061A | Localization and accessibility are independent quality domains. |
| KIKO-062 | integration | KIKO-062 | One aggregate deterministic verification gate. |
| KIKO-063 | decision | KIKO-063 | One distribution decision backed by a spike. |
| KIKO-064 | split | KIKO-064, KIKO-064A | Artifact construction and signing/notices/isolated smoke are separate release concerns. |
| KIKO-065 | integration | KIKO-065 | One installable VSIX outcome over established Core/extension behavior. |
| KIKO-066 | integration | KIKO-066 | One reproducible release-candidate output. |
| KIKO-067 | integration | KIKO-067 | One read-only invariant proof. |
| KIKO-068 | split | KIKO-068, KIKO-068A | State-writer locking and process cancellation/shutdown are separate lifecycles. |
| KIKO-069 | split | KIKO-069, KIKO-069A | Supported migration and failed-migration rollback/downgrade are separate outcomes. |
| KIKO-070 | integration | KIKO-070 | One compatibility-matrix gate. |
| KIKO-071 | split | KIKO-071, KIKO-071A, KIKO-071B | Context/cost, latency/memory, and logs/retries have different measurements. |
| KIKO-072 | acceptance | KIKO-072 | One clean-machine installation question. |
| KIKO-073 | acceptance | KIKO-073 | One real learning-journey question. |
| KIKO-074 | split | KIKO-074, KIKO-074A | Cross-project isolation and injected failure recovery are separate release questions. |
| KIKO-075 | split | KIKO-075, KIKO-075A | Upgrade preservation and uninstall/data control are independently reversible flows. |
| KIKO-076 | acceptance | KIKO-076 | One final release-record decision. |

## Result

- Originally pending checkpoints audited: 66
- Kept implementation checkpoints: 21
- Decision checkpoints kept: 1
- Integration/acceptance checkpoints kept intentionally broader: 15
- Original checkpoints split: 29
- New split checkpoints added: 45
- Normalized roadmap total: 121 checkpoints
- Verified historical checkpoints: 10
- Pending normalized checkpoints: 111
