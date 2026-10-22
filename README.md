# The Mixtape in CausalPy

This repository re-implements the code examples from Scott Cunningham's [*Causal Inference: The Mixtape*](https://mixtape.scunning.com) using [CausalPy](https://causalpy.readthedocs.io).

Read the chapters at **<https://drbenvincent.github.io/mixtape-causalpy/>**. GitHub shows the `.qmd` source only; the Pages site is the rendered reader surface, including the saved plots.

## Purpose

The goal is to provide a practical on-ramp for users who:
- Know the Mixtape's examples and want to see them in CausalPy
- Are learning CausalPy and want real-world applied examples
- Want to compare Bayesian (PyMC) vs frequentist implementations

This is a **translation repo**, not a copy of the book. We recreate analyses and figures, but link to the book for narrative context.

## Setup

Conda is required due to the PyMC dependency. The environment uses **Python 3.13**. CausalPy is installed from GitHub `main`. Rendering uses that conda env's Jupyter kernel, not WebAssembly.

```bash
# Create the environment
conda env create -f environment.yml

# Activate it
conda activate mixtape-causalpy

# Install the local data utilities package
pip install -e .

# Register the kernel Quarto executes against
python -m ipykernel install --user --name mixtape-causalpy --display-name "Mixtape CausalPy"
```

Quarto discovers Python on its own, and `pyproject.toml` can send it to the wrong interpreter. Point it at this env:

```bash
export QUARTO_PYTHON="$(which python)"
quarto preview
```

`quarto preview` serves the website. A full `quarto render` republishes from `_freeze/` and does not re-sample unless a `.qmd` changed. Preview and single-file render re-execute the chapter you are editing, which re-runs MCMC. After that, commit the updated `_freeze/` so CI can publish without sampling.

Copy `.vscode/settings.json.example` to `.vscode/settings.json` and set `<CONDA_ENV_PATH>` if you use the editor preview button. That file is gitignored because the path is machine-specific.

### Verify Installation

```python
import causalpy as cp
print(cp.__version__)  # Development version from GitHub main branch
```

> **Note**: This repo uses the development version of CausalPy installed directly from GitHub to access the latest bug fixes and features.

## Chapter → page mapping

| Mixtape Chapter | Page | Status |
|-----------------|------|--------|
| Ch 5: Matching & Subclassification | [`05_matching.qmd`](notebooks/05_matching.qmd) | ✅ Done |
| Ch 6: Regression Discontinuity | [`06_regression_discontinuity.qmd`](notebooks/06_regression_discontinuity.qmd) | ✅ Done |
| Ch 7: Instrumental Variables | [`07_instrumental_variables.qmd`](notebooks/07_instrumental_variables.qmd) | ✅ Done |
| Ch 8: Panel Data | `08_panel_data.qmd` | ⏭️ TODO |
| Ch 9: Difference-in-Differences | [`09_difference_in_differences.qmd`](notebooks/09_difference_in_differences.qmd) | ✅ Done |
| Ch 10: Synthetic Control | [`10_synthetic_control.qmd`](notebooks/10_synthetic_control.qmd) | ✅ Done |

Short names used in the plan (`05_matching`, `06_rd`, `07_iv`, `09_did`, `10_sc`) refer to these pages. New chapters are `.qmd` from the start. There is no paired `.ipynb`.

## CausalPy-First Approach

**We implement what CausalPy supports, and skip the rest with TODO placeholders.**

CausalPy provides direct support for:
- ✅ Regression Discontinuity (`RegressionDiscontinuity`)
- ✅ Instrumental Variables (`InstrumentalVariable`)
- ✅ Difference-in-Differences (`DifferenceInDifferences`)
- ✅ Synthetic Control (`SyntheticControl`)
- ⚠️ Inverse Propensity Weighting (`InversePropensityWeighting`) — partial matching support

For methods not yet in CausalPy (NN matching, panel FE, etc.), we include TODO placeholders linking to CausalPy issues. When CausalPy adds support, we can make targeted PRs to fill in those sections.

## Project Planning

See [REPO_PLAN.md](REPO_PLAN.md) for:
- Complete catalog of Mixtape Python examples
- Chapter-by-example mapping with CausalPy status
- Implementation priority matrix
- Data loading strategy
- Success criteria

## References

- **Mixtape book**: https://mixtape.scunning.com
- **Mixtape code repo**: https://github.com/scunning1975/mixtape
- **CausalPy docs**: https://causalpy.readthedocs.io
- **CausalPy GitHub**: https://github.com/pymc-labs/CausalPy

## License

Code in this repository is MIT licensed. The datasets are sourced from the Mixtape repo and [causaldata](https://github.com/NickCH-K/causaldata) package — see `data/README.md` for provenance.

## Citation

If you use this repo, please cite both the Mixtape and CausalPy:

```
Cunningham, S. (2021). Causal Inference: The Mixtape. Yale University Press.

CausalPy Developers. (2024). CausalPy: A Python package for causal inference. 
https://github.com/pymc-labs/CausalPy
```
