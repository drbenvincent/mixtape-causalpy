# Feature Proposal: Panel Fixed Effects

## Summary

Add support for panel data methods with fixed effects to CausalPy, enabling causal inference with longitudinal data where unit-level confounders need to be controlled.

## Motivation

Panel data methods are foundational in applied econometrics. The Mixtape's Chapter 8 covers fixed effects estimation, which is a workhorse for causal inference when there are unobserved time-invariant confounders.

### Mixtape Coverage

| Mixtape File | Method | Current CausalPy Support |
|--------------|--------|-------------------------|
| `sasp.py` | Entity fixed effects (within estimator) | ❌ Not supported |
| `bail.py` | Judge fixed effects with IV | ❌ Not supported |
| `cluster1-4.py` | Clustered standard errors | ⚠️ Partial (via PyMC) |

### Why Panel FE Matters

1. **Controls for time-invariant confounders**: FE removes all unit-level characteristics that don't vary over time
2. **Common in applied work**: Most observational panel studies use FE as a baseline
3. **Foundation for DiD**: Understanding FE is key to understanding two-way fixed effects (TWFE) in DiD

## Proposed API

### Option A: Dedicated `PanelRegression` Experiment

```python
import causalpy as cp

# Entity fixed effects
result = cp.PanelRegression(
    data=df,
    formula="outcome ~ treatment + time_varying_controls",
    unit_variable="id",
    time_variable="year",
    fixed_effects="unit",  # or "time", "twoway"
    model=cp.pymc_models.PanelModel(
        sample_kwargs={"draws": 1000, "chains": 4}
    ),
)

# Two-way fixed effects (unit + time)
result = cp.PanelRegression(
    data=df,
    formula="outcome ~ treatment + controls",
    unit_variable="id",
    time_variable="year",
    fixed_effects="twoway",
    cluster_variable="id",  # For clustered SEs
    model=cp.pymc_models.PanelModel(),
)
```

### Option B: Extend Existing LinearRegression

Add fixed effects support as a parameter:

```python
result = cp.pymc_models.LinearRegression(
    fixed_effects=["id"],  # Entity FE
    cluster="id",  # Clustered posterior
)
```

## Implementation Considerations

### Core Components Needed

1. **Within transformation**: Demean data by group (Frisch-Waugh-Lovell)
2. **Fixed effects as hierarchical priors**: Bayesian treatment of FE
3. **Clustered inference**: Account for within-unit correlation
4. **Balance checking**: Verify panel is balanced or handle unbalanced panels

### Bayesian Approach Options

**Option 1: Correlated Random Effects**
- Model unit effects as draws from a common distribution
- More efficient than classical FE, allows prediction for new units
- Requires stronger assumptions

**Option 2: Within Transformation + Bayesian OLS**
- Demean data first (classical within estimator)
- Apply Bayesian regression to demeaned data
- Simpler, closer to classical FE interpretation

**Option 3: Full Hierarchical Model**
```python
with pm.Model() as panel_model:
    # Unit-level random effects
    sigma_unit = pm.HalfNormal("sigma_unit", 1)
    unit_effects = pm.Normal("unit_effects", 0, sigma_unit, dims="unit")
    
    # Time-level random effects (optional)
    sigma_time = pm.HalfNormal("sigma_time", 1)
    time_effects = pm.Normal("time_effects", 0, sigma_time, dims="time")
    
    # Covariates
    beta = pm.Normal("beta", 0, 1, dims="covariates")
    
    # Outcome
    mu = unit_effects[unit_idx] + time_effects[time_idx] + X @ beta
    y = pm.Normal("y", mu, sigma, observed=y_obs)
```

### Clustered Standard Errors

For frequentist-equivalent inference, implement:
- Cluster-robust posterior via bootstrap
- HAC corrections for time series correlation

## Example Use Case

From the Mixtape SASP example:

```python
# Load sex worker panel data
sasp = load_sasp_panel()

# Entity fixed effects model
result = cp.PanelRegression(
    data=sasp,
    formula="lnw ~ age + unsafe + provider_second + llength",
    unit_variable="id",
    time_variable="session",
    fixed_effects="unit",
    cluster_variable="id",
    model=cp.pymc_models.PanelModel(),
)

# Compare to pooled OLS
pooled = cp.pymc_models.LinearRegression()
pooled.fit(X, y)

# View results
result.summary()
result.plot()  # Coefficient comparison pooled vs FE
```

## Connection to Existing CausalPy Methods

Panel FE is closely related to:

1. **DifferenceInDifferences**: TWFE is a special case of DiD
2. **SyntheticControl**: Both handle panel data, SC is for single treated unit
3. **InterruptedTimeSeries**: Both model outcomes over time

A `PanelRegression` class could serve as a building block for these methods.

## References

- **Mixtape Chapter 8**: [Panel Data](https://mixtape.scunning.com/08-panel_data)
- **Wooldridge (2010)**: Econometric Analysis of Cross Section and Panel Data
- **linearmodels Python package**: [Documentation](https://bashtage.github.io/linearmodels/)
- **plm R package**: [Panel Linear Models](https://cran.r-project.org/web/packages/plm/)

## Priority

**Medium** — Panel FE is important but somewhat overlaps with DiD functionality. Could be implemented as a building block that DiD leverages internally.

