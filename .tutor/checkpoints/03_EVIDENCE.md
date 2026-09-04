# Phase 3 — Conservative Learner Evidence

<a id="kiko-019"></a>
### KIKO-019 — Create one minimal evidence record

- Checkpoint kind: implementation
- Observable outcome: A pure function returns one privacy-safe evidence dictionary.
- Why it matters: Kiko needs observable learning evidence before it may update competence.
- Prerequisites: KIKO-015C.
- Known concepts: Functions, arguments, dictionaries, return values, and unit tests.
- New concepts and syntax: `date.today().isoformat()` for a stable local date string.
- Learner task: Build an evidence record from project, checkpoint, action, help, and date values.
- Verification: `.venv/bin/python -m unittest tests.test_evidence.EvidenceRecordTests -v`
- Expected behavior: The record has exactly the required fields and serializes to JSON.
- Edge case: Empty project, checkpoint, or learner action is rejected.
- Not included: File writes, stage promotion, raw conversation, or source snapshots.
- Exit condition: Valid and invalid evidence fixtures behave deterministically.

<a id="kiko-020"></a>
### KIKO-020 — Update one encountered concept conservatively

- Checkpoint kind: implementation
- Observable outcome: One concept receives evidence without losing unrelated concepts or fields.
- Why it matters: Cross-project adaptation must never overstate knowledge or damage existing history.
- Prerequisites: KIKO-019.
- Known concepts: Lists, dictionaries, loops, conditions, `append`, return values, and tests.
- New concepts and syntax: Sentinel value `None` for “not found” and identity check `is None`.
- Learner task: Return an updated in-memory learner dictionary for existing and absent concept IDs.
- Verification: `.venv/bin/python -m unittest tests.test_learner_state.ConceptUpdateTests -v`
- Expected behavior: Existing evidence is appended; an absent assisted concept is added conservatively.
- Edge case: Task-specific help cannot promote a concept to `independent` or `reliable`.
- Not included: Disk writes, reference updates, or reinforcement from a single typo.
- Exit condition: Existing, absent, and over-promotion fixtures all pass.

<a id="kiko-021"></a>
### KIKO-021 — Save learner state without losing unrelated data

- Checkpoint kind: implementation
- Observable outcome: An accepted learner update persists atomically while preserving profile and unrelated concepts.
- Why it matters: Kiko writes private cross-project state only after verified learner work.
- Prerequisites: KIKO-016C and KIKO-020.
- Known concepts: Validated state, atomic JSON writes, dictionaries, and test paths.
- New concepts and syntax: Copy-before-update behavior and injected storage paths.
- Learner task: Persist a provided learner update only after an accepted review decision.
- Verification: `.venv/bin/python -m unittest tests.test_learner_state.LearnerSaveTests -v`
- Expected behavior: Reloaded JSON contains the new evidence and preserves unrelated fixture data.
- Edge case: Failed/unaccepted review performs no write; simulated write failure preserves old data.
- Not included: Personal-reference mutation or concurrent-process locking.
- Exit condition: Approved, rejected, and failed-write fixtures pass without touching the real global profile.

<a id="kiko-022"></a>
### KIKO-022 — Add a used syntax entry to the personal reference

- Checkpoint kind: implementation
- Observable outcome: One genuinely used syntax entry is appended once after accepted work.
- Why it matters: The reference becomes a memory aid without becoming competence evidence.
- Prerequisites: KIKO-016C and KIKO-021.
- Known concepts: Paths, text I/O, conditions, strings, backups, and isolated tests.
- New concepts and syntax: Text membership checks and newline-safe append behavior.
- Learner task: Add a short syntax entry to an injected reference path only when absent.
- Verification: `.venv/bin/python -m unittest tests.test_reference.ReferenceUpdateTests -v`
- Expected behavior: First update adds one entry; repeating it creates no duplicate.
- Edge case: Reference-only changes never modify concept stage or evidence.
- Not included: Markdown semantic parsing or additions based only on model output.
- Exit condition: Add, duplicate, failed-write, and competence-separation fixtures pass.
