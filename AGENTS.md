# Agent Guidelines

Work practices for AI assistants (and humans) contributing to this repo.

## Before Starting Work

- [ ] Read `REPO_PLAN.md` to understand what's done and what's next
- [ ] Check the Implementation Status summary table for current progress
- [ ] Identify which chapter page you'll be working on

## While Working

- [ ] Focus on CausalPy-native examples first (✅ Native status)
- [ ] For examples marked ⏭️ Skip, add a TODO placeholder instead of implementing
- [ ] Follow the chapter template in `REPO_PLAN.md`
- [ ] Use the data loading utilities in `src/mixtape_causalpy/data.py`
- [ ] Execute with the `mixtape-causalpy` Jupyter kernel. Set `QUARTO_PYTHON` to the project `.venv` created by `uv sync`; do not render with WebAssembly or a stray interpreter

## After Completing Work

- [ ] **Update `REPO_PLAN.md`**: Change status from ⬜ to ✅ for completed files
- [ ] **Update the summary table**: Increment the Done count, decrement Todo count
- [ ] If you changed computational source, render that chapter locally and commit the updated `_freeze/`
- [ ] Do not re-execute MCMC in CI. Project `quarto render` must succeed from the committed freeze
- [ ] Commit with a descriptive message referencing the Mixtape file(s) covered

## Chapter conventions

- One `.qmd` per Mixtape chapter (e.g., `notebooks/06_regression_discontinuity.qmd`). Do not add `.ipynb` sources
- Use short references in tables: `06_rd`, `07_iv`, `09_did`, `10_sc`
- Include a link to the corresponding Mixtape chapter at the top
- Note any differences from the book's results (Bayesian vs OLS, etc.)
- The reader surface is the Quarto website (`quarto preview` / GitHub Pages), not JupyterLab

## Status Symbols

| Symbol | Meaning |
|--------|---------|
| ⬜ | Not started |
| 🟡 | In progress |
| ✅ | Done |
| ⏭️ | Skipped (no CausalPy support) |

## CausalPy Support Symbols

| Symbol | Meaning |
|--------|---------|
| ✅ Native | CausalPy has direct API — implement |
| ⚠️ Partial | CausalPy has related functionality — implement what's possible |
| ⏭️ Skip | No CausalPy support — add TODO placeholder |
| 📖 Conceptual | Not a causal method — skip or briefly reference |
| ❌ Missing | Original Mixtape code is empty — skip |

## Data Loading

- Prefer `causaldata` package when dataset is available there
- Fall back to direct URL loading from Mixtape repo
- Use caching to avoid repeated downloads
- Document any data transformations needed

## When CausalPy Adds New Features

1. Check the Phase 3 table in `REPO_PLAN.md` for relevant PRs
2. When a PR is merged, update the CausalPy status from ⚠️ Partial to ✅ Native
3. Implement the TODO placeholder
4. Update status to ✅ Done

## Reporting Bugs in CausalPy

If you encounter a bug in CausalPy while working on this repo:

1. **Isolate the bug**: Find the specific file and line in the CausalPy source (local clone at `/Users/benjamv/git/CausalPy`)
2. **Write up the issue**: Create a markdown file with:
   - Summary of the bug
   - Location (file and line number)
   - Current vs expected behavior
   - Minimal reproduction code
   - Suggested fix (if obvious)
3. **Create the issue via GitHub CLI**:

```bash
cd /Users/benjamv/git/CausalPy
gh issue create \
  --title "Bug: <short description>" \
  --body-file /path/to/issue.md \
  --label "bug"
```

4. **Work around the bug** in this repo until it's fixed upstream

