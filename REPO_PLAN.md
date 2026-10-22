# Mixtape → CausalPy Translation Repo Plan

This document outlines the structure and implementation plan for translating the code examples from Scott Cunningham's [*Causal Inference: The Mixtape*](https://mixtape.scunning.com) into a CausalPy Quarto website. Chapters are independent `.qmd` pages, not a numbered book and not Jupyter notebooks.

> **Primary source**: https://mixtape.scunning.com — use this to verify chapter content and ground truth
> 
> **Code & data repo**: https://github.com/scunning1975/mixtape (cloned locally at `/Users/benjamv/git/mixtape`)

## Scope: CausalPy-First Approach

**We implement what CausalPy supports, and skip the rest.**

- ✅ **Implement**: Examples where CausalPy has direct experiment APIs (RD, IV, DiD, SC, IPSW)
- ⏭️ **Skip with TODO**: Examples requiring methods CausalPy doesn't yet support (matching, panel FE, etc.)
- 📝 **Placeholder strategy**: Skipped sections include a `TODO` stub linking to relevant CausalPy issues/PRs, so we can return later when functionality lands

This keeps the repo focused and avoids maintaining parallel "baseline" implementations that would drift from CausalPy's direction. When CausalPy gains new capabilities, we can make targeted PRs to fill in the placeholders.

---

## Implementation Status

**Overall progress by chapter:**

| Chapter | Total | ✅ Done | ⏭️ Skip | ⬜ Todo |
|----------|-------|---------|---------|---------|
| `05_matching` | 10 | 5 | 5 | 0 |
| `06_rd` | 14 | 8 | 6 | 0 |
| `07_iv` | 1 | 1 | 0 | 0 |
| `08_panel` | 6 | 0 | 6 | 0 |
| `09_did` | 9 | 3 | 6 | 0 |
| `10_sc` | 3 | 3 | 0 | 0 |
| `00_data` | 11 | 0 | 11 | 0 |

**Status legend:**
- ⬜ Not started
- 🟡 In progress
- ✅ Done
- ⏭️ Skipped (no CausalPy support / conceptual only)

---

## Source Repository Analysis

The original Mixtape repo (`https://github.com/scunning1975/mixtape`) contains:

- **Python scripts**: 57 individual `.py` files in `/python/` (no notebooks, no saved outputs)
- **R scripts**: Parallel implementations in `/R/`
- **Stata do-files**: Original implementations in `/Do/`
- **Datasets**: `.dta` files at repo root and in `/Texas/Data/`

### Key observations from the Python code

1. **No chapter organization**: Scripts are named by example (e.g., `lmb_1.py`, `castle_1.py`) not by chapter
2. **Minimal abstraction**: Each script is standalone with repeated boilerplate (data loading, imports)
3. **Heavy statsmodels usage**: Most implementations use `statsmodels` OLS/WLS/GLM
4. **Some incomplete**: Several files contain only `# Missing python code`
5. **No saved outputs**: Scripts are meant to be run, not viewed

---

## Repo structure

```
mixtape-causalpy/
├── README.md                          # Project overview + quick start
├── REPO_PLAN.md                       # This file
├── _quarto.yml                        # Website project (freeze: auto)
├── index.qmd                          # Site home
├── requirements.txt
├── pyproject.toml
│
├── notebooks/
│   ├── 00_data_utilities.qmd          # Not started. New chapters are .qmd
│   ├── 05_matching.qmd
│   ├── 06_regression_discontinuity.qmd
│   ├── 07_instrumental_variables.qmd
│   ├── 08_panel_data.qmd              # Not started
│   ├── 09_difference_in_differences.qmd
│   └── 10_synthetic_control.qmd
│
├── _freeze/                           # Committed execution results. Do not re-sample in CI
├── .github/workflows/publish.yml      # quarto-dev/quarto-actions → GitHub Pages
│
├── data/
│   ├── README.md                      # Data provenance + licensing
│   └── (datasets downloaded at runtime or cached)
│
└── src/
    └── mixtape_causalpy/
        ├── __init__.py
        └── data.py                    # Data loading utilities
```

Reader URL: https://drbenvincent.github.io/mixtape-causalpy/ . `_site/` and `/.quarto/` are gitignored. One source format: `.qmd`. No paired `.ipynb`.

---

## Mixtape Python Examples → Chapter Mapping

Below is a complete catalog of the Python files in the Mixtape repo, mapped to chapter pages. Short names (`05_matching`, `06_rd`, `07_iv`, `08_panel`, `09_did`, `10_sc`) are the table refs; source files are `notebooks/<chapter>.qmd`.

### CausalPy Status Legend

| Symbol | Meaning |
|--------|---------|
| ✅ Native | Direct CausalPy experiment API available |
| ⚠️ Partial | CausalPy has related functionality, needs adaptation |
| ⏭️ Skip | No CausalPy support — will be TODO placeholder |
| 📖 Conceptual | Illustrates concepts, not a causal method |
| ❌ Missing | Original Python file is empty/placeholder |

---

### Conceptual / Foundational Examples (Chapters 2-3)

| Mixtape file | Description | Notebook | CausalPy | Status |
|--------------|-------------|----------|----------|--------|
| `ols.py` | OLS basics | | 📖 Conceptual | ⏭️ |
| `ols2.py` | OLS variations | | 📖 Conceptual | ⏭️ |
| `ols3.py` | OLS diagnostics | | 📖 Conceptual | ⏭️ |
| `ols4.py` | OLS extensions | | 📖 Conceptual | ⏭️ |
| `yule.py` | Yule's regression fallacy | | 📖 Conceptual | ⏭️ |
| `independence.py` | Statistical independence | | 📖 Conceptual | ⏭️ |
| `ks.py` | KS test for distributions | | 📖 Conceptual | ⏭️ |
| `collider_discrimination.py` | Collider bias example | | 📖 Conceptual | ⏭️ |
| `moviestar.py` | Movie star collider | | 📖 Conceptual | ⏭️ |
| `reganat.py` | Regression anatomy | | 📖 Conceptual | ⏭️ |
| `lm_3.py` | Linear model example | | 📖 Conceptual | ⏭️ |

**Notebook plan**: None — conceptual examples not targeted for CausalPy implementation.

---

### Chapter 4: Potential Outcomes Causal Model

| Mixtape file | Description | Notebook | CausalPy | Status |
|--------------|-------------|----------|----------|--------|
| `ri.py` | Randomization inference (Fisher's exact test) | | 📖 Conceptual | ⏭️ |
| `thornton_ri.py` | Thornton HIV incentives + RI | | 📖 Conceptual | ⏭️ |
| `tea.py` | Lady tasting tea example | | 📖 Conceptual | ⏭️ |

**Notebook plan**: None — conceptual examples not targeted for CausalPy implementation.

---

### Chapter 5: Matching & Subclassification

| Mixtape file | Description | Notebook | CausalPy | Status |
|--------------|-------------|----------|----------|--------|
| `titanic.py` | Simple difference in outcomes | `05_matching` | 📖 Conceptual | ✅ |
| `titanic_subclassification.py` | Subclassification example | `05_matching` | ⏭️ Skip | ⏭️ |
| `training_example.py` | Training program example | `05_matching` | ⏭️ Skip | ⏭️ |
| `training_bias_reduction.py` | Bias reduction via matching | `05_matching` | ⏭️ Skip | ⏭️ |
| `nsw_experimental.py` | NSW experimental benchmark | `05_matching` | 📖 Conceptual | ✅ |
| `nsw_pscore.py` | Propensity score estimation | `05_matching` | ⚠️ Partial | ✅ |
| `ipw.py` | Inverse propensity weighting | `05_matching` | ✅ Native | ✅ |
| `teffects_ipw.py` | Treatment effects via IPW | `05_matching` | ✅ Native | ✅ |
| `teffects_nn.py` | Nearest neighbor matching | `05_matching` | ❌ Missing | ⏭️ |
| `cem.py` | Coarsened exact matching | `05_matching` | ❌ Missing | ⏭️ |

**Page**: `notebooks/05_matching.qmd`
- Demonstrate CausalPy's `InversePropensityWeighting` with NSW data
- Include balance diagnostics and overlap plots
- **TODO placeholder** for: NN matching, subclassification, CEM (not yet in CausalPy)

---

### Chapter 6: Regression Discontinuity

| Mixtape file | Description | Notebook | CausalPy | Status |
|--------------|-------------|----------|----------|--------|
| `lmb_1.py` | Lee, Moretti, Butler - close elections RD | `06_rd` | ✅ Native | ✅ |
| `lmb_2.py` | LMB with polynomial | `06_rd` | ✅ Native | ✅ |
| `lmb_3.py` | LMB first stage | `06_rd` | ✅ Native | ✅ |
| `lmb_4.py` | LMB IK bandwidth | `06_rd` | ✅ Native | ✅ |
| `lmb_5.py` | LMB quadratic interactions | `06_rd` | ✅ Native | ✅ |
| `lmb_6.py` | LMB kernel-weighted | `06_rd` | ✅ Native | ✅ |
| `lmb_7.py` | LMB visualization | `06_rd` | ✅ Native | ✅ |
| `lmb_8.R` | LMB kernel-smoothed visualization | `06_rd` | ✅ Native | ✅ |
| `lmb_9.py` | LMB donut RD | `06_rd` | ❌ Missing | ⏭️ |
| `lmb_10.py` | LMB robustness | `06_rd` | ❌ Missing | ⏭️ |
| `rdd_simulate1.py` | RD simulation - potential outcomes | `06_rd` | 📖 Conceptual | ⏭️ |
| `rdd_simulate2.py` | RD simulation - treatment effect | `06_rd` | 📖 Conceptual | ⏭️ |
| `rdd_simulate3.py` | RD simulation - nonlinear | `06_rd` | 📖 Conceptual | ⏭️ |
| `rdd_simulate4.py` | RD simulation - no discontinuity | `06_rd` | 📖 Conceptual | ⏭️ |

**Page**: `notebooks/06_regression_discontinuity.qmd`
- Main example: Lee-Moretti-Butler close elections using `RegressionDiscontinuity`
- Show sharp RD estimation with bandwidth sensitivity
- Demonstrate diagnostic plots (binned scatter, bandwidth sensitivity)
- Kernel-smoothed RD visualization (from R's `lmb_8.R`)
- Reference: donut RD via PR #610 when merged

---

### Chapter 7: Instrumental Variables

| Mixtape file | Description | Notebook | CausalPy | Status |
|--------------|-------------|----------|----------|--------|
| `card.py` | Card (1995) returns to schooling | `07_iv` | ✅ Native | ✅ |

**Page**: `notebooks/07_instrumental_variables.qmd`
- Card's proximity to college as instrument for education
- Use CausalPy's `InstrumentalVariable` experiment
- Show first-stage diagnostics, compare OLS vs 2SLS
- Reference: fuzzy RD (issue #221) for connection to RD chapter

---

### Chapter 8: Panel Data

| Mixtape file | Description | Notebook | CausalPy | Status |
|--------------|-------------|----------|----------|--------|
| `sasp.py` | Sex worker panel data - FE estimation | `08_panel` | ⏭️ Skip | ⏭️ |
| `bail.py` | Bail judge FE | `08_panel` | ⏭️ Skip | ⏭️ |
| `cluster1.py` | Clustering standard errors | `08_panel` | ⏭️ Skip | ⏭️ |
| `cluster2.py` | Clustering variations | `08_panel` | ⏭️ Skip | ⏭️ |
| `cluster3.py` | Clustering variations | `08_panel` | ⏭️ Skip | ⏭️ |
| `cluster4.py` | Clustering variations | `08_panel` | ⏭️ Skip | ⏭️ |

**Page**: `notebooks/08_panel_data.qmd` — **SKIP (placeholder only, not created yet)**
- ⏭️ CausalPy does not have a dedicated panel FE experiment
- Create a placeholder `.qmd` with the TODO template when that work starts
- Reference: CausalPy panel workhorse proposal in issue tracker
- Transition note: the DiD page covers the TWFE-adjacent use case

---

### Chapter 9: Difference-in-Differences

| Mixtape file | Description | Notebook | CausalPy | Status |
|--------------|-------------|----------|----------|--------|
| `abortion_dd.py` | Abortion legalization DiD | `09_did` | ✅ Native | ✅ |
| `abortion_dd2.py` | Abortion DiD variations | `09_did` | ✅ Native | ✅ |
| `abortion_ddd.py` | Triple differences | `09_did` | ⏭️ Skip | ⏭️ |
| `abortion_ddd2.py` | Triple differences variations | `09_did` | ⏭️ Skip | ⏭️ |
| `castle_1.py` | Castle doctrine - basic DiD | `09_did` | ✅ Native | ✅ |
| `castle_2.py` | Castle doctrine - event study | `09_did` | ⚠️ Partial | ⏭️ |
| `castle_3.py` | Castle doctrine - robustness | `09_did` | ⚠️ Partial | ⏭️ |
| `castle_4.py` | Castle doctrine - extensions | `09_did` | ⚠️ Partial | ⏭️ |
| `castle_5.py` | Castle doctrine - placebo | `09_did` | ❌ Missing | ⏭️ |

**Page**: `notebooks/09_difference_in_differences.qmd`
- Main examples: Castle doctrine + abortion legalization
- Use CausalPy's `DifferenceInDifferences` experiment
- Show parallel trends checks, event study plots
- Reference: staggered DiD (PR #621), event study (PR #584)
- Include placebo/robustness tests

---

### Chapter 10: Synthetic Control

| Mixtape file | Description | Notebook | CausalPy | Status |
|--------------|-------------|----------|----------|--------|
| `synth_1.py` | Texas incarceration SC | `10_sc` | ✅ Native | ✅ |
| `synth_2.py` | Texas SC - weights | `10_sc` | ✅ Native | ✅ |
| `synth_3_7.R` | Texas SC - placebo-in-space tests | `10_sc` | ✅ Native | ✅ |

**Page**: `notebooks/10_synthetic_control.qmd`
- Texas prison reform as main example
- Use CausalPy's `SyntheticControl` experiment
- Show donor weights, pre-treatment fit
- Placebo-in-space tests with permutation p-value (from R's `synth_3_7.R`)
- Treatment effect gap plots with uncertainty

---

## Awaiting CausalPy Features

Some Mixtape examples require CausalPy features that don't exist yet. This section tracks open PRs and feature proposals.

### Open PRs (In Progress)

These features are being actively developed in CausalPy:

| Feature | CausalPy PR | Page to update |
|---------|-------------|----------------|
| Staggered DiD | [PR #621](https://github.com/pymc-labs/CausalPy/pull/621) | `notebooks/09_difference_in_differences.qmd` |
| Event Study | [PR #584](https://github.com/pymc-labs/CausalPy/pull/584) | `notebooks/09_difference_in_differences.qmd` |
| Donut RD | [PR #610](https://github.com/pymc-labs/CausalPy/pull/610) | `notebooks/06_regression_discontinuity.qmd` |

### Feature Proposals (Not Yet Started)

These features have been proposed but don't have open PRs yet. See `proposals/` for detailed writeups:

| Feature | Proposal | Page to update |
|---------|----------|----------------|
| Matching (NN, CEM) | [`proposal_matching.md`](proposals/proposal_matching.md) | `notebooks/05_matching.qmd` |
| Panel Fixed Effects | [`proposal_panel_fe.md`](proposals/proposal_panel_fe.md) | `notebooks/08_panel_data.qmd` |
| Triple Differences | [`proposal_triple_diff.md`](proposals/proposal_triple_diff.md) | `notebooks/09_difference_in_differences.qmd` |

---

## Data Strategy

### Primary sources (in order of preference)

1. **`causaldata` package**: Many Mixtape datasets are available via `pip install causaldata`
   - Preferred for: NSW, Castle, Card, others
   - Advantages: Clean, documented, permissively licensed

2. **Mixtape GitHub repo**: Direct download from `https://github.com/scunning1975/mixtape/raw/master/`
   - Fallback for datasets not in `causaldata`
   - Use URL-based loading (no vendoring of .dta files)

3. **Local caching**: Download once, cache in `~/.cache/mixtape-causalpy/`

See `src/mixtape_causalpy/data.py` for the implemented data loading utilities.

---

## Chapter template

Each chapter is one `.qmd` page. Quarto lifts the H1 into `title:`; keep the Mixtape link, overview, setup, examples, comparison to the book, CausalPy-specific notes, and TODO placeholders.

```markdown
---
title: "Chapter X: [Method Name]"
jupyter: mixtape-causalpy
---

## Causal Inference: The Mixtape → CausalPy

### Overview
- Brief description of the identification strategy
- Link to the corresponding Mixtape chapter
- Summary of what this page covers

### Setup
- Imports (CausalPy, data utilities)
- Data loading

### Example 1: [Primary Example Name]
- Data exploration
- CausalPy experiment setup
- Results and interpretation
- Key diagnostic plots

### Example 2: [Secondary Example] (if applicable)

### Comparison to Mixtape Results
- Note any differences from book's results
- Explain sources of difference (Bayesian vs OLS, priors, etc.)

### CausalPy-Specific Features
- Demonstrate unique CausalPy capabilities
- Show both PyMC and OLS backends where applicable

### References
- Link to Mixtape chapter
- Link to CausalPy documentation
- Link to original papers
```

### TODO Placeholder Template

For sections/examples we skip due to missing CausalPy support:

```markdown
## [Example Name] — TODO

> **Not yet implemented**: This example requires [matching / panel FE / etc.]
> which CausalPy does not currently support as a first-class experiment.

**Mixtape reference**: [Link to relevant chapter section]

**CausalPy tracking**:
- Issue: [link to GitHub issue if exists]
- PR: [link to PR if in progress]

**When to revisit**: Once CausalPy adds `cp.[MethodName]`, return here to implement.
```

---

## Success Criteria

Per `mixtape_causalpy_translation_repo.md`, "done" means:

- [x] **Implemented chapters** (RD, IV, DiD, SC) each have a page that:
  - [x] Loads the chapter dataset
  - [x] Runs a comparable identification strategy in CausalPy
  - [x] Reproduces key result figure(s) in spirit
  - [x] Clearly states differences vs book's implementation

- [x] **Partial chapters** (Matching) have a page that:
  - [x] Demonstrates what CausalPy supports (IPSW)
  - [x] Includes TODO placeholders for unsupported methods
  - [x] Links to CausalPy issue tracker for future work

- [ ] **Skipped chapters** (Panel) have a placeholder `.qmd` that:
  - [ ] Explains why the chapter is not yet implemented
  - [ ] Links to Mixtape chapter for reference
  - [ ] Links to relevant CausalPy issues/PRs
  - [ ] Can be filled in when CausalPy adds support

- [x] README provides:
  - [x] Quick start instructions (`quarto preview`, not JupyterLab)
  - [x] Chapter → page mapping table (with status indicators)
  - [x] Link to the GitHub Pages site
  - [x] Link to CausalPy docs
  - [x] Link to Mixtape book

- [x] Data layer:
  - [x] `data/README.md` documents all datasets and provenance
  - [x] Loading works without manual download steps

- [x] Website:
  - [x] `quarto render` builds from committed `_freeze/` without re-sampling
  - [x] Publish workflow is `.github/workflows/publish.yml` (`quarto-dev/quarto-actions`)

---

## Dependencies

We use Conda for environment management due to PyMC dependencies. See `environment.yml` for the full specification. Quarto itself is installed system-wide; set `QUARTO_PYTHON` to the `mixtape-causalpy` env so it does not pick up another interpreter.

**Key dependencies:**
- **Python**: 3.13
- **CausalPy**: Development version from GitHub (`git+https://github.com/pymc-labs/CausalPy.git@main`)
- **PyMC**: >=5.10
- **ArviZ**: >=0.17
- **Jupyter kernel**: `mixtape-causalpy` (local re-execution only; the site does not use WASM). CI registers that name so publish can resolve it. Committed `_freeze/` is what renders.

> **Note**: We use the development version of CausalPy to access bug fixes (e.g., RD bandwidth parameter fix in issue #625) and upcoming features.

---

## Next Steps

- [x] **Initialize repo structure**: Create folders, requirements.txt, data utilities
- [x] **Implement Phase 1 pages**: RD, IV, DiD, SC (full CausalPy coverage)
- [x] **Implement Phase 2 pages**: Matching (IPSW only, with TODO stubs)
- [x] **Quarto website**: `.qmd` sources, frozen outputs, GitHub Pages workflow
- [ ] **Create placeholder page**: Panel data chapter as `.qmd` with the TODO template
- [ ] **Monitor CausalPy PRs**: When new features land, revisit TODO placeholders

---

## References

- **Mixtape book**: https://mixtape.scunning.com
- **Mixtape repo**: https://github.com/scunning1975/mixtape
- **CausalPy docs**: https://causalpy.readthedocs.io
- **CausalPy GitHub**: https://github.com/pymc-labs/CausalPy
- **causaldata package**: https://github.com/NickCH-K/causaldata
- **Rendered site**: https://drbenvincent.github.io/mixtape-causalpy/
- **Quarto**: https://quarto.org

