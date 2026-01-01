# Feature Proposal: Triple Differences (DDD)

## Summary

Add support for Triple Differences (Difference-in-Difference-in-Differences, DDD) to CausalPy, extending the existing `DifferenceInDifferences` class to handle a third differencing dimension.

## Motivation

Triple differences is an extension of DiD that adds a third comparison group to further isolate causal effects. It's useful when standard DiD assumptions may be violated but there's a within-treatment-group comparison available.

### Mixtape Coverage

| Mixtape File | Method | Current CausalPy Support |
|--------------|--------|-------------------------|
| `abortion_ddd.py` | Triple differences with year FE | ❌ Not supported |
| `abortion_ddd2.py` | Triple differences variations | ❌ Not supported |

### Why DDD Matters

1. **Relaxes parallel trends**: DDD allows for group-specific trends that differ between treated/control
2. **Controls for confounders**: The third difference removes biases that affect one subgroup but not another
3. **Common in health/labor economics**: Used when treatment affects subgroups differently

## The DDD Estimator

### Standard DiD (2x2)
```
DiD = (Y_treated_post - Y_treated_pre) - (Y_control_post - Y_control_pre)
```

### Triple Differences (2x2x2)
```
DDD = [(Y_treated_exposed_post - Y_treated_exposed_pre) - (Y_control_exposed_post - Y_control_exposed_pre)]
    - [(Y_treated_unexposed_post - Y_treated_unexposed_pre) - (Y_control_unexposed_post - Y_control_unexposed_pre)]
```

Where:
- **Treated/Control**: Geographic or policy treatment (e.g., repeal states vs non-repeal)
- **Exposed/Unexposed**: Subgroup affected vs unaffected (e.g., younger vs older cohorts)
- **Pre/Post**: Time periods before and after treatment

## Proposed API

### Option A: Extend `DifferenceInDifferences`

```python
import causalpy as cp

# Triple Differences
result = cp.DifferenceInDifferences(
    data=df,
    formula="outcome ~ 1 + treated * post * exposed",
    time_variable_name="year",
    group_variable_name="state",
    exposure_variable_name="age_cohort",  # New: third dimension
    model=cp.pymc_models.LinearRegression(),
)

# The DDD effect is the three-way interaction: treated × post × exposed
```

### Option B: Dedicated `TripleDifferences` Class

```python
result = cp.TripleDifferences(
    data=df,
    formula="outcome ~ controls",
    treated_variable="repeal_state",
    post_variable="post_1973",
    exposed_variable="younger_cohort",
    time_variable="year",
    unit_variable="state",
    model=cp.pymc_models.LinearRegression(),
)

# Access results
result.summary()  # Shows DDD estimate
result.plot()     # Event study for exposed vs unexposed
```

## Implementation Considerations

### Core Components Needed

1. **Three-way interaction**: Compute `treated × post × exposed` term
2. **Standard errors**: Cluster at appropriate level (usually unit)
3. **Event study extension**: Plot dynamics for each subgroup
4. **Diagnostics**: Test for differential pre-trends across subgroups

### Regression Specification

The full DDD model includes:
```
Y_ist = α + β₁(Treated_s) + β₂(Post_t) + β₃(Exposed_i) 
      + β₄(Treated_s × Post_t) + β₅(Treated_s × Exposed_i) + β₆(Post_t × Exposed_i)
      + β₇(Treated_s × Post_t × Exposed_i)  # ← DDD effect
      + γ(Controls) + ε_ist
```

With fixed effects:
```
Y_ist = α_s + δ_t + β₃(Exposed_i) 
      + β₄(Treated_s × Post_t) + β₅(Treated_s × Exposed_i) + β₆(Post_t × Exposed_i)
      + β₇(Treated_s × Post_t × Exposed_i)  # ← DDD effect
      + γ(Controls) + ε_ist
```

### Bayesian Approach

```python
with pm.Model() as ddd_model:
    # Priors for main effects
    alpha = pm.Normal("alpha", 0, 10)
    beta_treated = pm.Normal("beta_treated", 0, 1)
    beta_post = pm.Normal("beta_post", 0, 1)
    beta_exposed = pm.Normal("beta_exposed", 0, 1)
    
    # Two-way interactions
    beta_treated_post = pm.Normal("beta_treated_post", 0, 1)
    beta_treated_exposed = pm.Normal("beta_treated_exposed", 0, 1)
    beta_post_exposed = pm.Normal("beta_post_exposed", 0, 1)
    
    # Three-way interaction (DDD effect)
    ddd_effect = pm.Normal("ddd_effect", 0, 1)  # ← Key parameter
    
    # Linear predictor
    mu = (alpha + beta_treated * treated + beta_post * post + beta_exposed * exposed
          + beta_treated_post * treated * post
          + beta_treated_exposed * treated * exposed
          + beta_post_exposed * post * exposed
          + ddd_effect * treated * post * exposed)
    
    # Likelihood
    y = pm.Normal("y", mu, sigma, observed=y_obs)
```

## Example Use Case

From the Mixtape abortion example:

```python
# Load abortion data
abortion = load_abortion()

# Filter to relevant subgroups
# Exposed: younger cohort (age 15) who could be affected by abortion legalization
# Unexposed: older cohort (age 25) already born before legalization
abortion_ddd = abortion[abortion["age"].isin([15, 25])]
abortion_ddd["younger"] = (abortion_ddd["age"] == 15).astype(int)

# Triple differences
result = cp.TripleDifferences(
    data=abortion_ddd,
    formula="lnr ~ acc + ir + pi + alcohol + crack + poverty + income + ur",
    treated_variable="repeal",
    post_variable="post_1973",
    exposed_variable="younger",
    time_variable="year",
    unit_variable="fip",
    weights="totpop",
    cluster_variable="fip",
    model=cp.pymc_models.LinearRegression(),
)

# View results
result.summary()
print(f"DDD Effect: {result.ddd_effect.mean():.3f}")

# Event study plot showing differential effects
result.plot_event_study()
```

## Connection to Existing CausalPy Methods

DDD builds directly on `DifferenceInDifferences`:

1. **Same underlying logic**: Just adds one more differencing dimension
2. **Shared infrastructure**: Unit/time fixed effects, clustering, event studies
3. **Compatible diagnostics**: Parallel trends tests, placebo tests

Could be implemented as:
- Extension to `DifferenceInDifferences` with optional `exposure_variable`
- Subclass `TripleDifferences(DifferenceInDifferences)`
- Standalone class that shares base utilities

## References

- **Mixtape Chapter 9**: [Difference-in-Differences](https://mixtape.scunning.com/09-difference_in_differences) (DDD section)
- **Gruber (1994)**: "The Incidence of Mandated Maternity Benefits" (classic DDD application)
- **Olden & Møen (2022)**: "The Triple Difference Estimator"

## Priority

**Medium** — DDD is less common than standard DiD but provides important additional flexibility. Implementation would be relatively straightforward given existing DiD infrastructure.

