# The Mixtape in CausalPy

Unofficial. This repository is not affiliated with, endorsed by, or authorized by Scott Cunningham, Yale University Press, or PyMC Labs. It re-implements the code examples from the **first edition** of Scott Cunningham's [*Causal Inference: The Mixtape*](https://mixtape-1ed.netlify.app/) (Yale University Press, 2021) using [CausalPy](https://causalpy.readthedocs.io).

It does **not** cover the second edition, [*Causal Inference: The Remix*](https://mixtape.scunning.com/) (2026). There is no public Remix code repository to translate yet. See [issue #4](https://github.com/drbenvincent/mixtape-causalpy/issues/4).

Read the chapters at **<https://drbenvincent.github.io/mixtape-causalpy/>**. GitHub shows the `.qmd` source only; the Pages site is the rendered reader surface, including the saved plots. Site credit is on the [attribution page](attribution.qmd).

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

- **Mixtape (1st ed.)**: https://mixtape-1ed.netlify.app/
- **Remix (2nd ed., not implemented here)**: https://mixtape.scunning.com/
- **Mixtape code and data repo**: https://github.com/scunning1975/mixtape
- **CausalPy docs**: https://causalpy.readthedocs.io
- **CausalPy GitHub**: https://github.com/pymc-labs/CausalPy

## License

Original code and original prose by Benjamin Vincent are MIT licensed. See `LICENSE` for what that grant does not cover. Code and data-generating processes adapted from [scunning1975/mixtape](https://github.com/scunning1975/mixtape) remain under that repository's MIT license; see `NOTICE`. Datasets are fetched at runtime, not committed, and not relicensed here. See `data/README.md`.

## Citation

Cite the book first, then this repository as the code translation. Cite CausalPy by its repository and Apache-2.0 license, not a guessed publication year.

```
Cunningham, S. (2021). Causal Inference: The Mixtape. Yale University Press.

Vincent, B. The Mixtape in CausalPy.
https://github.com/drbenvincent/mixtape-causalpy

CausalPy, Apache-2.0.
https://github.com/pymc-labs/CausalPy
```
