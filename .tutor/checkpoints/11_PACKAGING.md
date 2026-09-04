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
### KIKO-064A — Complete Core signing, notices, and isolated smoke

- Checkpoint kind: integration
- Observable outcome: Core artifact carries required notices/signing and passes required CLI smoke outside the source tree.
- Why it matters: A built artifact is not safely distributable until users can identify/trust/run it.
- Prerequisites: KIKO-064.
- Known concepts: Core artifact, doctor/help workflows, selected distribution, and clean profile.
- New concepts and syntax: License notice bundle and signing/notarization verification when required.
- Learner task: Add required notices/signing step and run the artifact through the isolated command matrix.
- Verification: Run `make prepare-core-release`, then `make smoke-core-artifact`.
- Expected behavior: Verification accepts signature/notices and all required CLI commands run outside source tree.
- Edge case: Missing Codex reaches doctor/demo guidance; invalid signature or notice manifest blocks release.
- Not included: VSIX packaging or external publication.
- Exit condition: Notice, signature/notarization, install, command-smoke, and missing-Codex fixtures pass.

<a id="kiko-065"></a>
### KIKO-065 — Package an installable VS Code VSIX

- Checkpoint kind: integration
- Observable outcome: Clean checkout produces a versioned `.vsix` connected to the packaged Core.
- Why it matters: The primary user surface must be installable without extension-development mode.
- Prerequisites: KIKO-064A and KIKO-055.
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
- Prerequisites: KIKO-064A and KIKO-065.
- Known concepts: Artifact builds, versions, clean checkout, and verification gates.
- New concepts and syntax: Release manifest, checksum generation, and version-consistency check.
- Learner task: Orchestrate Core/VSIX builds and fail on dirty/inconsistent release metadata.
- Verification: `make release-candidate`
- Expected behavior: Output contains matching versions, checksums, manifest, licenses, and passing smoke results.
- Edge case: Dirty tree or version mismatch stops before producing a publishable candidate.
- Not included: External publication or automatic Git operations.
- Exit condition: Two clean builds produce equivalent declared artifacts and a complete release manifest.
