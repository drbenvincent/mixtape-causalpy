# The Mixtape in CausalPy

This repository re-implements the code examples from Scott Cunningham's [*Causal Inference: The Mixtape*](https://mixtape.scunning.com) using [CausalPy](https://causalpy.readthedocs.io).

## Purpose

The goal is to provide a practical on-ramp for users who:
- Know the Mixtape's examples and want to see them in CausalPy
- Are learning CausalPy and want real-world applied examples
- Want to compare Bayesian (PyMC) vs frequentist implementations

This is a **translation repo**, not a copy of the book. We recreate analyses and figures, but link to the book for narrative context.

## Setup

Conda is required due to the PyMC dependency. The environment uses **Python 3.13**.

```bash
# Create the environment
conda env create -f environment.yml

# Activate it
conda activate mixtape-causalpy

# Install the local data utilities package
pip install -e .

# Add the environment as a Jupyter kernel
python -m ipykernel install --user --name mixtape-causalpy --display-name "Mixtape CausalPy"

# Launch Jupyter
jupyter lab notebooks/
```

In Jupyter, select the **"Mixtape CausalPy"** kernel when running notebooks.

### Verify Installation

```python
import causalpy as cp
print(cp.__version__)  # Development version from GitHub main branch
```

> **Note**: This repo uses the development version of CausalPy installed directly from GitHub to access the latest bug fixes and features.

## Chapter → Notebook Mapping

| Mixtape Chapter | Notebook | Status |
|-----------------|----------|--------|
| Ch 5: Matching & Subclassification | `05_matching.ipynb` | ⚠️ Partial (IPSW only) |
| Ch 6: Regression Discontinuity | `06_regression_discontinuity.ipynb` | ✅ Done |
| Ch 7: Instrumental Variables | `07_instrumental_variables.ipynb` | ✅ Done |
| Ch 8: Panel Data | `08_panel_data.ipynb` | ⏭️ TODO placeholder |
| Ch 9: Difference-in-Differences | `09_difference_in_differences.ipynb` | ✅ Done |
| Ch 10: Synthetic Control | `10_synthetic_control.ipynb` | ✅ Done |

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
