# The Mixtape in CausalPy

Unofficial. This repository is not affiliated with, endorsed by, or authorized by Scott Cunningham, Yale University Press, or PyMC Labs. It re-implements the code examples from the **first edition** of Scott Cunningham's [*Causal Inference: The Mixtape*](https://mixtape-1ed.netlify.app/) (Yale University Press, 2021) using [CausalPy](https://causalpy.readthedocs.io).

It does **not** cover the second edition, [*Causal Inference: The Remix*](https://mixtape.scunning.com/) (2026). There is no public Remix code repository to translate yet. See [DECISIONS.md](DECISIONS.md).

Read the chapters at **<https://drbenvincent.github.io/mixtape-causalpy/>**. GitHub shows the `.qmd` source only; the Pages site is the rendered reader surface, including the saved plots. Site credit is on the [attribution page](attribution.qmd).

## Purpose

The goal is to provide a practical on-ramp for users who:
- Know the Mixtape's examples and want to see them in CausalPy
- Are learning CausalPy and want real-world applied examples
- Want to compare Bayesian (PyMC) vs frequentist implementations

This is a **translation repo**, not a copy of the book. We recreate analyses and figures, but link to the book for narrative context.

## Setup

A fresh machine needs [uv](https://docs.astral.sh/uv/), system [Quarto](https://quarto.org/docs/get-started/), and git. Do not install Quarto inside `.venv`. Do not use conda, miniforge, or `pip install causalpy`. A bare pip install still resolves to CausalPy 0.9.0. This project pins the 1.0 line (`causalpy>=1.0.0rc1,<2`) and PyMC 6 through `uv.lock`. `uv sync` is the only install path.

```bash
git clone https://github.com/drbenvincent/mixtape-causalpy.git
cd mixtape-causalpy
uv sync
uv run python -m ipykernel install --user --name mixtape-causalpy --display-name "Mixtape CausalPy"
```

`uv sync` creates `.venv` from `pyproject.toml` and `uv.lock`, and installs the Python in `.python-version` (3.13) if you do not already have it.

Every chapter sets `jupyter: mixtape-causalpy`. Quarto runs that kernelspec's `argv`. It does not follow `QUARTO_PYTHON`, the active shell, or a kernel that only shares the display name. Register the kernel from this checkout's `.venv/bin/python`, then prove the spec points there:

```bash
uv run python -c "import json, pathlib, sys; from jupyter_client.kernelspec import find_kernel_specs; spec = pathlib.Path(find_kernel_specs()['mixtape-causalpy']) / 'kernel.json'; argv0 = pathlib.Path(json.loads(spec.read_text())['argv'][0]); expected = pathlib.Path(sys.prefix) / 'bin' / 'python'; print(argv0); assert argv0 == expected, (argv0, expected)"
uv run python -c "import causalpy, nutpie, pymc, sys; print(sys.executable); print('causalpy', causalpy.__version__); print('pymc', pymc.__version__); print('nutpie', nutpie.__version__); assert causalpy.__version__.startswith('1.'); assert pymc.__version__.split('.')[0] == '6'"
```

`causalpy` must be a 1.0 version, not `0.9.0`. `pymc` must be 6.x. `nutpie` must import. The assertion fails when the kernel points at another checkout. Do not compare resolved binaries: two `.venv` directories can symlink to the same uv Python while using different site-packages. `quarto check` listing the name is not this check.

Re-run the `ipykernel install` command after every `uv sync` that replaces `.venv`, and before rendering a different checkout. The kernelspec name is global. A second clone or a git worktree has its own `.venv`. Point the spec at the checkout you are about to render. Do not leave it pointed at a deleted worktree or an abandoned environment.

```bash
export QUARTO_PYTHON="$(pwd)/.venv/bin/python"
quarto preview
```

`QUARTO_PYTHON` is only for Quarto's own imports (`ipykernel`, `nbclient`, `nbformat`, `pyyaml`). Those packages are in the lock for that reason. They are not analysis dependencies. Setting the variable does not select the chapter kernel.

Copy `.vscode/settings.json.example` to `.vscode/settings.json` if you use the editor preview button. That file is gitignored.

`quarto preview` serves the website. A full `quarto render` republishes from `_freeze/` and does not re-sample unless a `.qmd` changed. Preview and single-file render re-execute the chapter you are editing, which re-runs MCMC. After that, commit the updated `_freeze/` so CI can publish without sampling.

## Chapter → page mapping

| Mixtape Chapter | Page | Status |
|-----------------|------|--------|
| Ch 5: Matching & Subclassification | [`05_matching.qmd`](notebooks/05_matching.qmd) | ✅ Done |
| Ch 6: Regression Discontinuity | [`06_regression_discontinuity.qmd`](notebooks/06_regression_discontinuity.qmd) | ✅ Done |
| Ch 7: Instrumental Variables | [`07_instrumental_variables.qmd`](notebooks/07_instrumental_variables.qmd) | ✅ Done |
| Ch 8: Panel Data | [`08_panel_data.qmd`](notebooks/08_panel_data.qmd) | ✅ Done |
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
- ✅ Panel fixed effects (`PanelRegression`)
- ⚠️ Inverse Propensity Weighting (`InversePropensityWeighting`) — partial matching support

For methods not yet in CausalPy (NN matching, and so on), we include TODO placeholders linking to CausalPy issues. When CausalPy adds support, we can make targeted PRs to fill in those sections.

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
