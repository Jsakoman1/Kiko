# Phase 1 — Global Personal Reference

<a id="kiko-011"></a>
### KIKO-011 — Read the personal reference (legacy Step 4C)

- Checkpoint kind: implementation
- Observable outcome: `show` displays a small preview loaded from global `REFERENCE.md`.
- Why it matters: Kiko can reuse known syntax without copying the personal reference into project state.
- Prerequisites: KIKO-010.
- Known concepts: `Path.home`, `/` path joining, `exists`, `read_text`, functions, and safe defaults.
- New concepts and syntax: `splitlines()` and list slicing used to bound a text preview.
- Learner task: Add one reference-loading function and show only a small preview.
- Verification: `python3 kiko.py show`
- Expected behavior: A bounded reference preview appears and `.tutor/state.json` contains no reference text.
- Edge case: A missing `REFERENCE.md` returns empty text and `show` does not crash.
- Not included: Parsing Markdown sections, searching syntax, or writing the reference.
- Exit condition: Normal and missing-reference behavior pass while all three state sources remain separate.
