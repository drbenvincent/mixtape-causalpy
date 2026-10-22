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

Install with [uv](https://docs.astral.sh/uv/). `uv sync` is the only install path. It creates `.venv` from `pyproject.toml` and `uv.lock`, including the Python in `.python-version` (3.13) if you do not already have it. PyMC 6 installs from PyPI; conda is not required.

```bash
uv sync
uv run python -m ipykernel install --user --name mixtape-causalpy --display-name "Mixtape CausalPy"
export QUARTO_PYTHON="$(pwd)/.venv/bin/python"
quarto preview
```

The lock includes `ipykernel`, `nbclient`, `nbformat`, and `pyyaml` because Quarto imports them from `QUARTO_PYTHON` when it executes a chapter. They are not analysis dependencies.

Quarto discovers Python on its own. Point `QUARTO_PYTHON` at this project's `.venv` so it does not pick up another interpreter. Copy `.vscode/settings.json.example` to `.vscode/settings.json` if you use the editor preview button. That file is gitignored.

`quarto preview` serves the website. A full `quarto render` republishes from `_freeze/` and does not re-sample unless a `.qmd` changed. Preview and single-file render re-execute the chapter you are editing, which re-runs MCMC. After that, commit the updated `_freeze/` so CI can publish without sampling.

### Verify the stack

A bare `pip install causalpy` still resolves to 0.9.0 until 1.0.0 final is the PyPI default. This project pins the 1.0 line (`causalpy>=1.0.0rc1,<2`) and PyMC 6. Confirm the environment `uv sync` created:

```bash
uv run python -c "import causalpy, pymc; print('causalpy', causalpy.__version__); print('pymc', pymc.__version__)"
```

`causalpy` must be a 1.0 version, not `0.9.0`. `pymc` must be 6.x (6.3.2 or a newer 6.x).

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
