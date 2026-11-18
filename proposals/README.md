# CausalPy Feature Proposals

This directory contains feature proposals for CausalPy, identified during the Mixtape translation work. These proposals document gaps where CausalPy doesn't yet support methods covered in *Causal Inference: The Mixtape*.

## Proposals

| Proposal | CausalPy Feature | Mixtape Chapter | Status |
|----------|------------------|-----------------|--------|
| [Matching Methods](proposal_matching.md) | `cp.Matching` | Ch 5 | 📝 Proposed |
| [Panel Fixed Effects](proposal_panel_fe.md) | `cp.PanelRegression` | Ch 8 | Superseded — shipped |
| [Triple Differences](proposal_triple_diff.md) | `cp.TripleDifferences` | Ch 9 | 📝 Proposed |

## Shipped in CausalPy 1.0

[PR #621](https://github.com/pymc-labs/CausalPy/pull/621) (staggered difference-in-differences) and [PR #610](https://github.com/pymc-labs/CausalPy/pull/610) (`donut_hole`) are merged. The pages are `notebooks/09_difference_in_differences.qmd` and `notebooks/06_regression_discontinuity.qmd`.

## Still open

| Feature | CausalPy PR | Page |
|---------|-------------|------|
| Event study | [PR #584](https://github.com/pymc-labs/CausalPy/pull/584) | `notebooks/09_difference_in_differences.qmd`. Common-timing event study, not the castle design. |

## How to Use These Proposals

These proposals are designed to:

1. **Document the gap**: Explain what's missing and why it matters
2. **Provide context**: Reference the Mixtape examples that would benefit
3. **Suggest an approach**: Outline a possible implementation strategy

To submit a proposal to CausalPy:

1. Open an issue on [CausalPy GitHub](https://github.com/pymc-labs/CausalPy/issues)
2. Reference this proposal document
3. Discuss with maintainers before implementing

## Contributing

If you'd like to implement one of these features, please:

1. Check if there's already an open issue/PR on CausalPy
2. Discuss the approach in the CausalPy issue tracker
3. Follow the CausalPy contributing guidelines

