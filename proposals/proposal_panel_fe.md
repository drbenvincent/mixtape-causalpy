# Feature Proposal: Panel Fixed Effects

## Summary

Add a `PanelRegression` experiment wrapper that enables panel-aware visualization and diagnostics, with support for both dummy variable and within-transformation approaches to fixed effects.

## Motivation

Panel data methods are foundational in applied econometrics. [Chapter 8 of *Causal Inference: The Mixtape*](https://mixtape.scunning.com/08-panel_data) covers fixed effects estimation, which is a workhorse for causal inference when there are unobserved time-invariant confounders.

The [Mixtape code repository](https://github.com/scunning1975/mixtape) contains Python and R implementations of these methods.

### Mixtape Coverage

| Mixtape File | Method | Current CausalPy Support |
|--------------|--------|-------------------------|
| [`sasp.py`](https://github.com/scunning1975/mixtape/blob/master/python/sasp.py) | Entity fixed effects (within estimator) | ⚠️ Works via formula, no experiment wrapper |
| [`bail.py`](https://github.com/scunning1975/mixtape/blob/master/python/bail.py) | Judge fixed effects with IV | ⚠️ Works via formula, no experiment wrapper |

See also the R implementations: [`sasp.R`](https://github.com/scunning1975/mixtape/blob/master/R/sasp.R) and [`bail_1.R`](https://github.com/scunning1975/mixtape/blob/master/R/bail_1.R).

### Why Panel FE Matters

1. **Controls for time-invariant confounders**: FE removes all unit-level characteristics that don't vary over time
2. **Common in applied work**: Most observational panel studies use FE as a baseline
3. **Foundation for DiD**: Understanding FE is key to understanding two-way fixed effects (TWFE) in DiD

## Current State

Panel fixed effects **already works** with `LinearRegression` using patsy formula syntax:

```python
import causalpy as cp

# Entity fixed effects via formula
model = cp.pymc_models.LinearRegression()
model.fit(
    formula="y ~ C(unit) + treatment + controls",
    data=panel_data,
)
```

What's missing is a dedicated experiment class that provides panel-aware visualization, diagnostics, and efficient handling of large panels.

## Proposed API

### Core Parameters

```python
result = cp.PanelRegression(
    data=panel_data,
    formula=str,                    # User controls the formula
    unit_fe_variable=str,           # Column name for unit identifier
    time_fe_variable=str | None,    # Column name for time identifier (optional)
    fe_method="dummies" | "within", # How to handle fixed effects
    model=cp.pymc_models.LinearRegression(),
)
```

### Two Approaches: Dummies vs Within

#### 1. Dummy Variables (`fe_method="dummies"`)

User includes `C(unit)` in the formula explicitly:

```python
result = cp.PanelRegression(
    data=panel_data,
    formula="y ~ C(unit) + C(time) + treatment + controls",
    unit_fe_variable="unit",
    time_fe_variable="time",
    fe_method="dummies",  # Default
    model=cp.pymc_models.LinearRegression(),
)
```

**Pros:**
- Get individual unit effect estimates (αᵢ coefficients)
- Can predict for units in training data
- Familiar patsy syntax

**Cons:**
- Creates N-1 dummy columns for N units
- Slow/impossible for large N (e.g., 10,000+ units)

#### 2. Within Transformation (`fe_method="within"`)

User does NOT include `C(unit)` — the experiment class demeans the data:

```python
result = cp.PanelRegression(
    data=panel_data,
    formula="y ~ treatment + controls",  # No C(unit) needed
    unit_fe_variable="unit",
    time_fe_variable="time",
    fe_method="within",  # Demeans data internally
    model=cp.pymc_models.LinearRegression(),
)
```

**Pros:**
- No dummy columns needed
- Scales to very large N
- Mathematically equivalent to dummy approach

**Cons:**
- Individual unit effects not directly estimated (can be recovered post-hoc)
- Time-invariant covariates drop out (demeaned to zero)

### Design Matrix Comparison

| Method | Design Matrix Size | Formula |
|--------|-------------------|---------|
| `dummies` | N_obs × (N_units + K_covariates) | `y ~ C(unit) + X` |
| `within` | N_obs × K_covariates | `y ~ X` (on demeaned data) |

For 10,000 units with 5 covariates:
- **Dummies**: 10,000 × 10,005 matrix
- **Within**: 10,000 × 5 matrix

## Implementation

### Main Class

```python
class PanelRegression(ExperimentalDesign):
    def __init__(
        self,
        data: pd.DataFrame,
        formula: str,
        unit_fe_variable: str,
        time_fe_variable: str | None = None,
        fe_method: str = "dummies",
        model=None,
    ):
        self.unit_fe_variable = unit_fe_variable
        self.time_fe_variable = time_fe_variable
        self.fe_method = fe_method
        
        # Validate
        if unit_fe_variable not in data.columns:
            raise ValueError(f"unit_fe_variable '{unit_fe_variable}' not in data")
        if time_fe_variable and time_fe_variable not in data.columns:
            raise ValueError(f"time_fe_variable '{time_fe_variable}' not in data")
        
        # Store panel dimensions
        self.n_units = data[unit_fe_variable].nunique()
        self.n_periods = data[time_fe_variable].nunique() if time_fe_variable else None
        
        # Apply within transformation if requested
        if fe_method == "within":
            data = self._within_transform(data, unit_fe_variable)
            if time_fe_variable:
                data = self._within_transform(data, time_fe_variable)
        
        # Fit using standard LinearRegression
        super().__init__(data=data, formula=formula, model=model)
    
    def _within_transform(self, data: pd.DataFrame, group_var: str) -> pd.DataFrame:
        """Demean all numeric columns by group (within transformation)."""
        data = data.copy()
        
        # Store group means for recovering unit effects later
        numeric_cols = data.select_dtypes(include=[np.number]).columns
        numeric_cols = [c for c in numeric_cols if c != group_var]
        
        self._group_means[group_var] = data.groupby(group_var)[numeric_cols].mean()
        
        # Demean each numeric column
        for col in numeric_cols:
            group_mean = data.groupby(group_var)[col].transform('mean')
            data[col] = data[col] - group_mean
        
        return data
    
    def summary(self):
        """Panel-aware summary with dimensions."""
        print(f"Panel Fixed Effects Regression")
        print(f"  Units: {self.n_units} ({self.unit_fe_variable})")
        if self.n_periods:
            print(f"  Periods: {self.n_periods} ({self.time_fe_variable})")
        print(f"  FE method: {self.fe_method}")
        # ... coefficient summary ...
```

### Plotting Methods

Rather than a single `plot()` method, `PanelRegression` provides multiple specialized plotting methods. For panels with many units, each plot supports subsetting to prevent visual clutter.

#### 1. `plot_coefficients()`

Shows posterior distributions for treatment and control covariates (excluding unit/time FE coefficients):

```python
def plot_coefficients(self, var_names: list | None = None) -> plt.Figure:
    """
    Forest plot of covariate coefficients with credible intervals.
    
    Parameters
    ----------
    var_names : list, optional
        Specific coefficients to plot. If None, plots all non-FE coefficients.
    """
    # Filter out C(unit)[...] and C(time)[...] coefficients
    # Show forest plot with HDI
    pass
```

#### 2. `plot_unit_effects()`

Shows the distribution of unit fixed effects (only available with `fe_method="dummies"`):

```python
def plot_unit_effects(
    self, 
    highlight: list | None = None,
    label_extreme: int = 0,
) -> plt.Figure:
    """
    Histogram/density of unit fixed effects.
    
    Parameters
    ----------
    highlight : list, optional
        List of unit IDs to highlight on the distribution.
    label_extreme : int, default 0
        Number of extreme units to label (top N + bottom N).
    """
    # Works for any number of units (histogram scales fine)
    pass
```

#### 3. `plot_trajectories()`

Shows within-unit time series of actual vs predicted values. Essential for panels with a time dimension. Supports subsetting for large N:

```python
def plot_trajectories(
    self,
    units: list | None = None,
    n_sample: int = 10,
    select: str = "random",
    show_mean: bool = True,
) -> plt.Figure:
    """
    Small multiples of unit trajectories over time.
    
    Parameters
    ----------
    units : list, optional
        Specific unit IDs to plot. If provided, ignores n_sample.
    n_sample : int, default 10
        Number of units to sample if units not specified.
    select : str, default "random"
        How to select units when sampling:
        - "random": Random sample
        - "extreme": Units with largest positive and negative effects
        - "high_variance": Units with most within-unit variation
    show_mean : bool, default True
        Whether to overlay the population mean trajectory.
    
    Notes
    -----
    If n_units <= n_sample, all units are shown automatically.
    """
    if units is not None:
        plot_units = units
    elif self.n_units <= n_sample:
        plot_units = self._all_units
    else:
        if select == "random":
            plot_units = np.random.choice(self._all_units, n_sample, replace=False)
        elif select == "extreme":
            # Top and bottom by unit effect
            plot_units = self._get_extreme_units(n_sample)
        elif select == "high_variance":
            plot_units = self._get_high_variance_units(n_sample)
    # ... faceted line plots ...
    pass
```

#### 4. `plot_residuals()`

Diagnostic plots for residual patterns:

```python
def plot_residuals(
    self,
    kind: str = "scatter",
    by: str | None = None,
) -> plt.Figure:
    """
    Residual diagnostic plots.
    
    Parameters
    ----------
    kind : str, default "scatter"
        Type of residual plot:
        - "scatter": Residuals vs fitted values
        - "histogram": Distribution of residuals
        - "qq": Q-Q plot for normality check
    by : str, optional
        Group residuals by a variable (e.g., "unit" or "time").
        If "unit", shows boxplot of residuals by unit (samples if n_units > 30).
    """
    pass
```

### Subsetting Examples

```python
# Large panel: 10,000 individuals over 10 waves
result = cp.PanelRegression(
    data=large_panel,
    formula="y ~ treatment + controls",
    unit_fe_variable="id",
    time_fe_variable="wave",
    fe_method="within",
)

# Coefficients - always works (just K covariates)
result.plot_coefficients()

# Trajectories - random sample of 12 units
result.plot_trajectories(n_sample=12)

# Trajectories - most extreme units (6 highest + 6 lowest effects)
result.plot_trajectories(n_sample=12, select="extreme")

# Trajectories - specific units of interest
result.plot_trajectories(units=["ID_001", "ID_002", "ID_003"])

# Residuals by unit - automatically samples if too many units
result.plot_residuals(kind="scatter", by="unit")
```

### Two-Way FE with Within Transformation

For two-way FE using the within approach, we demean by both unit AND time sequentially:

```python
result = cp.PanelRegression(
    data=panel_data,
    formula="y ~ treatment + controls",
    unit_fe_variable="unit",
    time_fe_variable="time",
    fe_method="within",
)
```

The implementation applies demeaning first by unit, then by time. This is the standard approach for two-way fixed effects.

## Example Use Cases

### Small Panel (50 states × 20 years) — Use Dummies

```python
result = cp.PanelRegression(
    data=state_year_data,
    formula="y ~ C(state) + C(year) + policy + controls",
    unit_fe_variable="state",
    time_fe_variable="year",
    fe_method="dummies",
    model=cp.pymc_models.LinearRegression(),
)
```

### Large Panel (10,000 individuals × 10 waves) — Use Within

```python
result = cp.PanelRegression(
    data=individual_panel,
    formula="y ~ treatment + age + income",  # No C(id) needed
    unit_fe_variable="id",
    time_fe_variable="wave",
    fe_method="within",
    model=cp.pymc_models.LinearRegression(),
)
```

### From the Mixtape SASP example

```python
sasp = load_sasp_panel()

# Using within transformation (many individuals)
result = cp.PanelRegression(
    data=sasp,
    formula="lnw ~ age + unsafe + provider_second + llength",
    unit_fe_variable="id",
    time_fe_variable="session",
    fe_method="within",
    model=cp.pymc_models.LinearRegression(),
)

result.summary()
# Output:
# Panel Fixed Effects Regression
#   Units: 254 (id)
#   Periods: 8 (session)
#   FE method: within
#   ...coefficients...
```

## Future: Mixed Models with Formulaic

CausalPy currently uses patsy for formula parsing. There's an open PR ([#463](https://github.com/pymc-labs/CausalPy/pull/463)) to migrate to [formulaic](https://github.com/matthewwardrop/formulaic).

With formulaic, we could support **mixed model syntax** for random effects:

```python
# Random effects syntax (requires formulaic)
result = cp.PanelRegression(
    data=panel_data,
    formula="y ~ treatment + (1|unit)",  # Random intercept per unit
    unit_fe_variable="unit",
    fe_method="random",  # New option
    model=cp.pymc_models.MixedEffectsModel(),
)
```

This would enable:
- `(1|unit)` — Random intercept per unit (partial pooling)
- `(1 + time|unit)` — Random intercept and slope per unit
- Shrinkage toward population mean

This is out of scope for the initial implementation but worth noting for the future.

## Connection to Existing CausalPy Methods

Panel FE is closely related to:

1. **DifferenceInDifferences**: TWFE is a special case of DiD
2. **SyntheticControl**: Both handle panel data, SC is for single treated unit
3. **InterruptedTimeSeries**: Both model outcomes over time

A `PanelRegression` class could share infrastructure with these methods.

## References

- **Mixtape Chapter 8**: [Panel Data](https://mixtape.scunning.com/08-panel_data)
- **Mixtape Code Repository**: [github.com/scunning1975/mixtape](https://github.com/scunning1975/mixtape)
  - Python: [`sasp.py`](https://github.com/scunning1975/mixtape/blob/master/python/sasp.py), [`bail.py`](https://github.com/scunning1975/mixtape/blob/master/python/bail.py)
  - R: [`sasp.R`](https://github.com/scunning1975/mixtape/blob/master/R/sasp.R), [`bail_1.R`](https://github.com/scunning1975/mixtape/blob/master/R/bail_1.R)
- **Wooldridge (2010)**: Econometric Analysis of Cross Section and Panel Data
- **linearmodels Python package**: [Documentation](https://bashtage.github.io/linearmodels/)
- **formulaic**: [GitHub](https://github.com/matthewwardrop/formulaic)

## Priority

**Medium** — Panel FE largely works today via formula syntax. The value-add is:
1. Efficient within-transformation for large panels
2. Panel-aware visualization with subsetting for large N:
   - `plot_coefficients()` — Treatment effect posteriors
   - `plot_unit_effects()` — Distribution of unit heterogeneity
   - `plot_trajectories()` — Within-unit time series (sampled for large N)
   - `plot_residuals()` — Diagnostic plots
3. Cleaner API for common panel workflows
