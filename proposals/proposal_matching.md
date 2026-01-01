# Feature Proposal: Matching Methods

## Summary

Add support for matching-based causal inference methods to CausalPy, including:
- Nearest Neighbor Matching
- Coarsened Exact Matching (CEM)
- Subclassification / Stratification

## Motivation

CausalPy currently supports Inverse Propensity Weighting (`InversePropensityWeighting`), but [Chapter 5 of *Causal Inference: The Mixtape*](https://mixtape.scunning.com/05-matching_and_subclassification) covers several other matching methods that are commonly used in applied work. These methods are complementary to IPW and are often preferred in different settings.

The [Mixtape code repository](https://github.com/scunning1975/mixtape) contains implementations of these methods.

### Mixtape Coverage

| Mixtape File | Method | Current CausalPy Support |
|--------------|--------|-------------------------|
| [`teffects_nn.R`](https://github.com/scunning1975/mixtape/blob/master/R/teffects_nn.R) | Nearest Neighbor Matching | ❌ Not supported |
| [`cem.R`](https://github.com/scunning1975/mixtape/blob/master/R/cem.R) | Coarsened Exact Matching | ❌ Not supported |
| [`titanic.py`](https://github.com/scunning1975/mixtape/blob/master/python/titanic.py) | Subclassification | ❌ Not supported |

### Why These Methods Matter

1. **Nearest Neighbor Matching**: Pairs treated units with similar control units based on propensity score or covariates. Intuitive and widely used.

2. **Coarsened Exact Matching (CEM)**: Coarsens covariates into bins and matches exactly within bins. Reduces model dependence and is robust to misspecification.

3. **Subclassification**: Stratifies on propensity score or covariates, estimates effects within strata, then combines. A building block for understanding weighting methods.

## Proposed API

### Option A: Unified `Matching` Experiment Class

```python
import causalpy as cp

# Nearest Neighbor Matching
result = cp.Matching(
    data=df,
    formula="outcome ~ treatment + age + education + income",
    treatment_variable="treatment",
    method="nearest",  # or "cem", "subclassification"
    distance="propensity",  # or "mahalanobis"
    ratio=1,  # 1:1 matching
    model=cp.pymc_models.LinearRegression(),
)

# Coarsened Exact Matching
result = cp.Matching(
    data=df,
    formula="outcome ~ treatment + age + education + income",
    treatment_variable="treatment",
    method="cem",
    coarsening={"age": 5, "income": 1000},  # bin widths
    model=cp.pymc_models.LinearRegression(),
)

# Subclassification
result = cp.Matching(
    data=df,
    formula="outcome ~ treatment + age + education + income",
    treatment_variable="treatment",
    method="subclassification",
    n_strata=5,
    model=cp.pymc_models.LinearRegression(),
)
```

### Option B: Extend `InversePropensityWeighting`

Add matching as alternative weighting schemes within the existing IPW class:

```python
result = cp.InversePropensityWeighting(
    data=df,
    formula="treatment ~ age + education + income",
    outcome_variable="outcome",
    weighting_scheme="matching",  # New option
    matching_method="nearest",
    matching_ratio=1,
    model=cp.pymc_models.PropensityScore(),
)
```

## Implementation Considerations

### Core Components Needed

1. **Propensity score estimation**: Already exists in `PropensityScore` model
2. **Matching algorithm**: Nearest neighbor with/without replacement
3. **Weight calculation**: Convert matches to weights for outcome regression
4. **Balance diagnostics**: Extend existing `plot_balance_ecdf` and similar

### Bayesian Approach

CausalPy's strength is Bayesian inference. For matching:
- Estimate propensity scores with uncertainty
- Propagate uncertainty through matching to outcome estimation
- Provide posterior distributions for ATT/ATE

### Python Dependencies

Consider leveraging:
- `scikit-learn` for nearest neighbor algorithms
- Custom implementation for CEM binning
- Existing PyMC infrastructure for Bayesian outcome models

## Example Use Case

From the Mixtape NSW example:

```python
# Load NSW data with CPS controls
nsw = load_nsw()
cps = load_cps()
combined = pd.concat([nsw, cps])

# Nearest neighbor matching
result = cp.Matching(
    data=combined,
    formula="re78 ~ treat + age + educ + black + hisp + marr + nodegree + re74 + re75",
    treatment_variable="treat",
    method="nearest",
    ratio=5,  # 5:1 matching as in Mixtape
    model=cp.pymc_models.LinearRegression(),
)

# View results
result.summary()
result.plot_balance()  # Covariate balance pre/post matching
```

## References

- **Mixtape Chapter 5**: [Matching and Subclassification](https://mixtape.scunning.com/05-matching_and_subclassification)
- **Mixtape Code Repository**: [github.com/scunning1975/mixtape](https://github.com/scunning1975/mixtape)
  - R: [`teffects_nn.R`](https://github.com/scunning1975/mixtape/blob/master/R/teffects_nn.R), [`cem.R`](https://github.com/scunning1975/mixtape/blob/master/R/cem.R)
  - Python: [`titanic.py`](https://github.com/scunning1975/mixtape/blob/master/python/titanic.py), [`ipw.py`](https://github.com/scunning1975/mixtape/blob/master/python/ipw.py)
- **MatchIt R Package**: [Documentation](https://kosukeimai.github.io/MatchIt/)
- **CEM Paper**: Iacus, King, & Porro (2012). "Causal Inference without Balance Checking"
- **Ho et al. (2007)**: "Matching as Nonparametric Preprocessing for Reducing Model Dependence"

## Priority

**High** — Matching is one of the most commonly used causal inference methods in applied work, and adding it would significantly expand CausalPy's coverage of the Mixtape examples.

