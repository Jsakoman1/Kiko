# Phase 11 — Installable Artifacts

<a id="kiko-063"></a>
### KIKO-063 — Choose and prove the macOS Core distribution

- Checkpoint kind: decision
- Observable outcome: Architecture records one distribution choice proven by a clean-profile spike.
- Why it matters: Normal users must not create a virtual environment or edit Python paths manually.
- Prerequisites: KIKO-062.
- Known concepts: Python package, CLI entry point, extension/Core protocol, and product constraints.
- New concepts and syntax: Distribution tradeoff record, standalone executable or managed-runtime proof.
- Learner task: Compare artifact size, startup, upgrades, signing, and extension launch for the two allowed approaches.
- Verification: Follow the recorded clean-profile spike command in `ARCHITECTURE.md` and run `kiko --version` outside the repository.
- Expected behavior: One approach satisfies install/start/update constraints with documented evidence and fallback.
- Edge case: Unsupported architecture fails before install with a clear compatibility message.
- Not included: Marketplace publication or support for non-macOS systems.
- Exit condition: User-facing distribution decision is confirmed and unblocks both Core and VSIX packaging.

<a id="kiko-064"></a>
### KIKO-064 — Build the versioned Core and CLI artifact

- Checkpoint kind: implementation
- Observable outcome: Clean checkout produces a versioned installable Core/CLI artifact.
- Why it matters: Finished users must run Kiko without the development repository.
- Prerequisites: KIKO-063.
- Known concepts: Package metadata, versioning, clean builds, and chosen distribution.
- New concepts and syntax: Build artifact metadata and selected distribution build command.
- Learner task: Implement one clean-checkout Core build that produces the versioned artifact.
- Verification: `make package-core`
- Expected behavior: Build output contains exactly one versioned Core/CLI artifact with matching metadata.
- Edge case: Dirty or missing build input stops before producing a release artifact.
- Not included: VSIX packaging or publishing.
- Exit condition: Clean and invalid-input build fixtures prove deterministic artifact construction.

<a id="kiko-064a"></a>
### KIKO-064A — Bundle Core licenses and notices

- Checkpoint kind: implementation
- Observable outcome: Core artifact contains a validated manifest of required dependency licenses and notices.
- Why it matters: A distributable artifact must identify included software before signing or installation testing.
- Prerequisites: KIKO-064.
- Known concepts: Core artifact, dependencies, build manifest, and clean build input.
- New concepts and syntax: License/notice inventory and notice-manifest validation.
- Learner task: Generate/bundle the required license and notice files for the Core artifact.
- Verification: `make verify-core-notices`
- Expected behavior: Every packaged dependency maps to one bundled notice and no undeclared file appears.
- Edge case: Missing or mismatched notice blocks release preparation.
- Not included: Signing, notarization, installation smoke, VSIX, or publication.
- Exit condition: Complete, missing, mismatched, and unexpected-dependency notice fixtures pass.

<a id="kiko-064b"></a>
### KIKO-064B — Sign and verify the Core artifact

- Checkpoint kind: implementation
- Observable outcome: The selected distribution artifact passes the required macOS signature/notarization verification or records why notarization is inapplicable.
- Why it matters: Users must be able to identify and run the artifact under the supported macOS security model.
- Prerequisites: KIKO-064A.
- Known concepts: Core artifact, chosen distribution, release blocking, and clean build inputs.
- New concepts and syntax: Code-signing identity, signature verification, and notarization status when required.
- Learner task: Add the chosen signing step and a deterministic verification command.
- Verification: `make verify-core-signature`
- Expected behavior: Valid artifact passes; unsigned/modified/wrong-identity artifact fails before release.
- Edge case: A development-only unsigned build is labeled non-release and cannot enter release output.
- Not included: CLI smoke, VSIX signing/packaging, or publication.
- Exit condition: Valid, unsigned, modified, wrong-identity, and applicability fixtures pass.

<a id="kiko-064c"></a>
### KIKO-064C — Smoke-test the Core artifact in isolation

- Checkpoint kind: integration
- Observable outcome: Signed/noticed Core artifact runs required CLI commands outside the source tree.
- Why it matters: Build metadata is insufficient until the artifact works without repository imports or a development environment.
- Prerequisites: KIKO-064B.
- Known concepts: Core artifact, doctor/help/version workflows, clean profile, and signature/notices verification.
- New concepts and syntax: Isolated artifact smoke matrix.
- Learner task: Install/run the artifact in an isolated profile and execute the required CLI command matrix.
- Verification: `make smoke-core-artifact`
- Expected behavior: Version/help/doctor/fake status run outside source; no repository path is imported.
- Edge case: Missing Codex reaches doctor/demo guidance rather than crashing.
- Not included: VSIX packaging or external publication.
- Exit condition: Install, version, help, doctor, fake-flow, missing-Codex, and no-source-path fixtures pass.

<a id="kiko-065"></a>
### KIKO-065 — Package an installable VS Code VSIX

- Checkpoint kind: integration
- Observable outcome: Clean checkout produces a versioned `.vsix` connected to the packaged Core.
- Why it matters: The primary user surface must be installable without extension-development mode.
- Prerequisites: KIKO-064C and KIKO-055.
- Known concepts: Extension metadata, Core protocol, compatibility minimums, and extension tests.
- New concepts and syntax: VSIX packaging, bundled/located Core strategy, and extension release metadata.
- Learner task: Add package script and install the VSIX into a clean VS Code profile.
- Verification: Run `npm --prefix extension run package`, then `npm --prefix extension run smoke:vsix`.
- Expected behavior: VSIX installs, activates, finds packaged Core, and completes fake-provider help.
- Edge case: Missing/incompatible Core shows setup recovery instead of a blank sidebar.
- Not included: Marketplace upload, auto-update service, or other editors.
- Exit condition: Versioned VSIX passes clean-profile activation and Core connection smoke tests.

<a id="kiko-066"></a>
### KIKO-066 — Produce reproducible versioned release output

- Checkpoint kind: integration
- Observable outcome: One release command produces matching artifacts, manifest, checksums, and notices from a clean tree.
- Why it matters: Users and maintainers need identifiable, auditable release inputs.
- Prerequisites: KIKO-064C and KIKO-065.
- Known concepts: Artifact builds, versions, clean checkout, and verification gates.
- New concepts and syntax: Release manifest, checksum generation, and version-consistency check.
- Learner task: Orchestrate Core/VSIX builds and fail on dirty/inconsistent release metadata.
- Verification: `make release-candidate`
- Expected behavior: Output contains matching versions, checksums, manifest, licenses, and passing smoke results.
- Edge case: Dirty tree or version mismatch stops before producing a publishable candidate.
- Not included: External publication or automatic Git operations.
- Exit condition: Two clean builds produce equivalent declared artifacts and a complete release manifest.
