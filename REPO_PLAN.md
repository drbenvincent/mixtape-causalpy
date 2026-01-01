# Mixtape → CausalPy Translation Repo Plan

This document outlines the structure and implementation plan for translating the code examples from Scott Cunningham's [*Causal Inference: The Mixtape*](https://mixtape.scunning.com) into CausalPy-based Jupyter notebooks.

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

**Overall progress by notebook:**

| Notebook | Total | ✅ Done | ⏭️ Skip | ⬜ Todo |
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

## Proposed Repo Structure

```
mixtape-causalpy/
├── README.md                          # Project overview + quick start
├── REPO_PLAN.md                       # This file
├── requirements.txt                   # Pinned dependencies
├── pyproject.toml                     # Optional: modern packaging
│
├── notebooks/
│   ├── 00_data_utilities.ipynb        # Data loading + inspection utilities
│   ├── 05_matching.ipynb              # Matching & Subclassification
│   ├── 06_regression_discontinuity.ipynb
│   ├── 07_instrumental_variables.ipynb
│   ├── 08_panel_data.ipynb
│   ├── 09_difference_in_differences.ipynb
│   └── 10_synthetic_control.ipynb
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

---

## Mixtape Python Examples → Chapter Mapping

Below is a complete catalog of the Python files in the Mixtape repo, mapped to our notebooks with implementation status.

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
| `ols.py` | OLS basics | `00_data` | 📖 Conceptual | ⏭️ |
| `ols2.py` | OLS variations | `00_data` | 📖 Conceptual | ⏭️ |
| `ols3.py` | OLS diagnostics | `00_data` | 📖 Conceptual | ⏭️ |
| `ols4.py` | OLS extensions | `00_data` | 📖 Conceptual | ⏭️ |
| `yule.py` | Yule's regression fallacy | `00_data` | 📖 Conceptual | ⏭️ |
| `independence.py` | Statistical independence | `00_data` | 📖 Conceptual | ⏭️ |
| `ks.py` | KS test for distributions | `00_data` | 📖 Conceptual | ⏭️ |
| `collider_discrimination.py` | Collider bias example | `00_data` | 📖 Conceptual | ⏭️ |
| `moviestar.py` | Movie star collider | `00_data` | 📖 Conceptual | ⏭️ |
| `reganat.py` | Regression anatomy | `00_data` | 📖 Conceptual | ⏭️ |
| `lm_3.py` | Linear model example | `00_data` | 📖 Conceptual | ⏭️ |

**Notebook plan**: `00_data_utilities.ipynb`
- Data loading utilities
- Quick dataset inspection
- Links to conceptual material in the book
- Not a methods notebook

---

### Chapter 4: Potential Outcomes Causal Model

| Mixtape file | Description | Notebook | CausalPy | Status |
|--------------|-------------|----------|----------|--------|
| `ri.py` | Randomization inference (Fisher's exact test) | `00_data` | 📖 Conceptual | ⏭️ |
| `thornton_ri.py` | Thornton HIV incentives + RI | `00_data` | 📖 Conceptual | ⏭️ |
| `tea.py` | Lady tasting tea example | `00_data` | 📖 Conceptual | ⏭️ |

**Notebook plan**: Not a CausalPy estimation target. Conceptual examples linked from data utilities notebook.

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

**Notebook plan**: `05_matching.ipynb`
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

**Notebook plan**: `06_regression_discontinuity.ipynb`
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

**Notebook plan**: `07_instrumental_variables.ipynb`
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

**Notebook plan**: `08_panel_data.ipynb` — **SKIP (placeholder only)**
- ⏭️ CausalPy does not have a dedicated panel FE experiment
- Create placeholder notebook with TODO template
- Reference: CausalPy panel workhorse proposal in issue tracker
- Transition note: DiD notebook covers the TWFE-adjacent use case

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

**Notebook plan**: `09_difference_in_differences.ipynb`
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

**Notebook plan**: `10_synthetic_control.ipynb`
- Texas prison reform as main example
- Use CausalPy's `SyntheticControl` experiment
- Show donor weights, pre-treatment fit
- Placebo-in-space tests with permutation p-value (from R's `synth_3_7.R`)
- Treatment effect gap plots with uncertainty

---

## Implementation Priority Matrix

### Phase 1: Implement — Full CausalPy Coverage

| Notebook | Key Examples | CausalPy Method | Estimated Effort |
|----------|--------------|-----------------|------------------|
| `06_regression_discontinuity.ipynb` | LMB close elections | `RegressionDiscontinuity` | Medium |
| `07_instrumental_variables.ipynb` | Card (1995) | `InstrumentalVariable` | Low |
| `09_difference_in_differences.ipynb` | Castle, Abortion | `DifferenceInDifferences` | Medium |
| `10_synthetic_control.ipynb` | Texas prisons | `SyntheticControl` | Medium |

### Phase 2: Implement — Partial CausalPy Coverage

| Notebook | Key Examples | Approach | Estimated Effort |
|----------|--------------|----------|------------------|
| `05_matching.ipynb` | NSW | CausalPy IPSW only; TODO stubs for matching | Medium |

### Skip with TODO Placeholders

| Notebook | Reason | Future CausalPy Work |
|----------|--------|----------------------|
| `08_panel_data.ipynb` | No panel FE experiment | Awaiting `cp.PanelRegression` |
| Matching (NN, CEM, subclass) | Not first-class in CausalPy | Awaiting `cp.Matching` |
| Triple differences | Not supported | Would need new experiment |

### Phase 3: Fill in When CausalPy PRs Land

| Feature | CausalPy PR/Issue | Notebook to Update |
|---------|-------------------|-------------------|
| Staggered DiD | PR #621 | `09_difference_in_differences.ipynb` |
| Event study plots | PR #584 | `09_difference_in_differences.ipynb` |
| Donut RD | PR #610 | `06_regression_discontinuity.ipynb` |
| Matching | TBD | `05_matching.ipynb` |
| Panel FE | TBD | `08_panel_data.ipynb` |

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

### Data loading utility

```python
# src/mixtape_causalpy/data.py

import pandas as pd
from pathlib import Path

MIXTAPE_BASE_URL = "https://github.com/scunning1975/mixtape/raw/master/"
CACHE_DIR = Path.home() / ".cache" / "mixtape-causalpy"

def load_mixtape_data(filename: str, use_cache: bool = True) -> pd.DataFrame:
    """Load a dataset from the Mixtape repo, with optional caching."""
    cache_path = CACHE_DIR / filename
    
    if use_cache and cache_path.exists():
        return pd.read_stata(cache_path)
    
    url = MIXTAPE_BASE_URL + filename
    df = pd.read_stata(url)
    
    if use_cache:
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        df.to_stata(cache_path)
    
    return df

# Convenience functions for common datasets
def load_lmb() -> pd.DataFrame:
    """Lee-Moretti-Butler close elections data for RD."""
    return load_mixtape_data("lmb-data.dta")

def load_castle() -> pd.DataFrame:
    """Castle doctrine data for DiD."""
    return load_mixtape_data("castle.dta")

def load_card() -> pd.DataFrame:
    """Card (1995) returns to schooling data for IV."""
    return load_mixtape_data("card.dta")

def load_texas() -> pd.DataFrame:
    """Texas incarceration data for synthetic control."""
    return load_mixtape_data("texas.dta")

def load_nsw() -> pd.DataFrame:
    """National Supported Work data for matching."""
    return load_mixtape_data("nsw_mixtape.dta")

def load_abortion() -> pd.DataFrame:
    """Abortion legalization data for DiD."""
    return load_mixtape_data("abortion.dta")
```

---

## Notebook Template

Each notebook should follow this structure:

```markdown
# Chapter X: [Method Name]
## Causal Inference: The Mixtape → CausalPy

### Overview
- Brief description of the identification strategy
- Link to the corresponding Mixtape chapter
- Summary of what this notebook covers

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

- [ ] **Implemented chapters** (RD, IV, DiD, SC) each have a notebook that:
  - [ ] Loads the chapter dataset
  - [ ] Runs a comparable identification strategy in CausalPy
  - [ ] Reproduces key result figure(s) in spirit
  - [ ] Clearly states differences vs book's implementation

- [ ] **Partial chapters** (Matching) have a notebook that:
  - [ ] Demonstrates what CausalPy supports (IPSW)
  - [ ] Includes TODO placeholders for unsupported methods
  - [ ] Links to CausalPy issue tracker for future work

- [ ] **Skipped chapters** (Panel) have a placeholder notebook that:
  - [ ] Explains why the chapter is not yet implemented
  - [ ] Links to Mixtape chapter for reference
  - [ ] Links to relevant CausalPy issues/PRs
  - [ ] Can be filled in when CausalPy adds support

- [ ] README provides:
  - [ ] Quick start instructions
  - [ ] Chapter → notebook mapping table (with status indicators)
  - [ ] Link to CausalPy docs
  - [ ] Link to Mixtape book

- [ ] Data layer:
  - [ ] `data/README.md` documents all datasets and provenance
  - [ ] Loading works without manual download steps

---

## Dependencies

We use Conda for environment management due to PyMC dependencies. See `environment.yml` for the full specification.

**Key dependencies:**
- **Python**: 3.13
- **CausalPy**: Development version from GitHub (`git+https://github.com/pymc-labs/CausalPy.git@main`)
- **PyMC**: >=5.10
- **ArviZ**: >=0.17

> **Note**: We use the development version of CausalPy to access bug fixes (e.g., RD bandwidth parameter fix in issue #625) and upcoming features.

---

## Next Steps

1. **Initialize repo structure**: Create folders, requirements.txt, data utilities
2. **Implement Phase 1 notebooks**: RD, IV, DiD, SC (full CausalPy coverage)
3. **Implement Phase 2 notebooks**: Matching (IPSW only, with TODO stubs)
4. **Create placeholder notebooks**: Panel data chapter with TODO template
5. **CI setup**: Run notebooks on push to ensure reproducibility
6. **Monitor CausalPy PRs**: When new features land, revisit TODO placeholders

---

## References

- **Mixtape book**: https://mixtape.scunning.com
- **Mixtape repo**: https://github.com/scunning1975/mixtape
- **CausalPy docs**: https://causalpy.readthedocs.io
- **CausalPy GitHub**: https://github.com/pymc-labs/CausalPy
- **causaldata package**: https://github.com/NickCH-K/causaldata

