# Phase 13 — Finished-Product Release

<a id="kiko-072"></a>
### KIKO-072 — Install on a clean supported macOS profile

- Checkpoint kind: acceptance
- Observable outcome: Release Core/CLI and VSIX install without source checkout, manual Python path, or developer command.
- Why it matters: Installability distinguishes the finished product from a repository demo.
- Prerequisites: KIKO-066, KIKO-069A, KIKO-070, and KIKO-071B.
- Known concepts: Release artifacts, compatibility, doctor, and clean-profile smoke tests.
- New concepts and syntax: Release acceptance record and installation evidence capture.
- Learner task: Perform the documented install and first-run checks from release artifacts only.
- Verification: Follow `docs/install.md`, then run `kiko doctor` and the VS Code activation smoke.
- Expected behavior: Doctor is ready, sidebar opens, packaged Core connects, and no development repository is referenced.
- Edge case: Missing Codex/auth enters a clear recoverable setup or demo state.
- Not included: Marketplace publication or unsupported operating systems.
- Exit condition: Clean-profile installation evidence records exact artifacts, versions, and successful first run.

<a id="kiko-073"></a>
### KIKO-073 — Complete and resume a real learning journey

- Checkpoint kind: acceptance
- Observable outcome: A learner initializes, learns, edits, reviews, closes, and resumes one real Python project.
- Why it matters: The finished release must deliver learning value, not only technical installation.
- Prerequisites: KIKO-072.
- Known concepts: Golden journeys, canonical interactions, read-only review, and durable evidence.
- New concepts and syntax: Manual usability evidence rubric.
- Learner task: Dogfood the full journey and record observable comprehension/ownership outcomes.
- Verification: Run the release acceptance script in `docs/release-acceptance.md`.
- Expected behavior: Syntax is explained before use; learner authors code; accepted review updates correct state; resume finds next checkpoint.
- Edge case: Side question and hint leave progress unchanged and do not reveal the full solution prematurely.
- Not included: Measuring learner speed as competence or collecting remote analytics.
- Exit condition: Automated evidence plus one beginner usability session passes every relevant product/lesson gate.

<a id="kiko-074"></a>
### KIKO-074 — Prove cross-project knowledge and progress isolation

- Checkpoint kind: acceptance
- Observable outcome: A second project reuses only relevant knowledge while each project's progress remains isolated.
- Why it matters: Kiko's durable advantage depends on useful transfer without project leakage or data loss.
- Prerequisites: KIKO-072 and KIKO-073.
- Known concepts: Global/project ownership, concept relevance, personal reference, and release fixtures.
- New concepts and syntax: Cross-project release acceptance record.
- Learner task: Run Python-to-Java/general-concept transfer across two isolated project fixtures.
- Verification: `make release-cross-project-acceptance`
- Expected behavior: Only relevant knowledge transfers; neither roadmap/handoff nor language-specific syntax leaks.
- Edge case: Opening/asking in the second project does not modify the first project's state.
- Not included: Cloud sync, collaboration, or claiming perfect recovery from hardware loss.
- Exit condition: Relevance, general transfer, language exclusion, progress isolation, and no-write fixtures pass.

<a id="kiko-074a"></a>
### KIKO-074A — Prove release failure and feedback recovery

- Checkpoint kind: acceptance
- Observable outcome: Common product failures and unclear-teaching feedback recover safely on packaged artifacts.
- Why it matters: Release behavior must match tested recovery policy outside the development environment.
- Prerequisites: KIKO-059A, KIKO-068A, KIKO-069A, KIKO-071B, KIKO-072, and KIKO-074.
- Known concepts: Error taxonomy, backups, process cleanup, feedback isolation, and packaged product.
- New concepts and syntax: Failure-injection release acceptance matrix.
- Learner task: Run corrupt state, missing auth, provider crash, cancel/restart, and unclear-feedback scenarios.
- Verification: `make release-failure-acceptance`
- Expected behavior: Each scenario names one safe recovery, preserves relevant state, leaves no duplicate process, and never lowers competence.
- Edge case: Recovery preserves corrupt input/backup for inspection and cannot self-modify installed Kiko.
- Not included: Hardware-loss recovery, cloud sync, or remote feedback telemetry.
- Exit condition: Every required failure/feedback scenario has packaged-artifact passing evidence.

<a id="kiko-075"></a>
### KIKO-075 — Prove packaged upgrade without data loss

- Checkpoint kind: acceptance
- Observable outcome: Previous supported beta upgrades to v1.0 while preserving all compatible user-owned data.
- Why it matters: A finished local product must respect user data before, during, and after installation.
- Prerequisites: KIKO-069A, KIKO-070, and KIKO-072.
- Known concepts: Migration, rollback, artifacts, and separate data owners.
- New concepts and syntax: Packaged upgrade acceptance manifest.
- Learner task: Execute the documented beta-to-v1.0 upgrade on isolated profiles.
- Verification: Follow the upgrade part of `docs/upgrade-and-uninstall.md`, then run `make smoke-upgrade`.
- Expected behavior: Core/VSIX upgrade succeeds and project, learner, reference, feedback, and settings remain valid.
- Edge case: Failed upgrade rolls back through KIKO-069A without partial owner versions.
- Not included: Automatic remote updates or deleting unrelated Codex/VS Code data.
- Exit condition: Supported upgrade, rollback, owner preservation, and version-consistency evidence pass.

<a id="kiko-075a"></a>
### KIKO-075A — Prove uninstall and data-retention choices

- Checkpoint kind: acceptance
- Observable outcome: Kiko uninstalls binaries/extension while the user separately chooses retain, export, or delete for each data owner.
- Why it matters: Product removal must remain reversible and respect private learning history.
- Prerequisites: KIKO-060A and KIKO-075.
- Known concepts: Data owners, selective destructive confirmation, exports, and packaged artifacts.
- New concepts and syntax: Uninstall acceptance manifest.
- Learner task: Execute uninstall on isolated profiles for retain, export, delete, and cancel choices.
- Verification: Follow the uninstall part of `docs/upgrade-and-uninstall.md`, then run `make smoke-uninstall`.
- Expected behavior: App artifacts are removed; each selected data choice affects exactly its declared owner.
- Edge case: Cancel preserves installation/data and uninstall never deletes unrelated Codex/VS Code files.
- Not included: Remote account deletion or unsupported operating systems.
- Exit condition: Retain, export, delete, cancel, reinstall, and unrelated-data-preservation evidence pass.

<a id="kiko-076"></a>
### KIKO-076 — Create the v1.0 release record

- Checkpoint kind: acceptance
- Observable outcome: Versioned artifacts and complete quality evidence are archived as an approved v1.0 candidate.
- Why it matters: “Finished” needs a reproducible definition and traceable proof.
- Prerequisites: KIKO-066, KIKO-067, KIKO-068A, KIKO-070, KIKO-071B, KIKO-073, KIKO-074A, and KIKO-075A.
- Known concepts: Release manifests, checksums, compatibility, acceptance evidence, and dogfood feedback.
- New concepts and syntax: Release sign-off checklist and known-limitations record.
- Learner task: Assemble artifacts, checksums, install/privacy docs, changelog, matrix, test reports, and accepted feedback traceability.
- Verification: `make release-audit`
- Expected behavior: Audit finds no missing gate, unresolved blocking feedback, inconsistent version, or unimplemented accepted regression.
- Edge case: Marketplace publication remains a separately authorized external action.
- Not included: Speculative v1.1 features or automatic publishing.
- Exit condition: User approves a complete local v1.0 release record and next backlog derives only from observed use.
