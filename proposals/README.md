# CausalPy Feature Proposals

This directory contains feature proposals for CausalPy, identified during the Mixtape translation work. These proposals document gaps where CausalPy doesn't yet support methods covered in *Causal Inference: The Mixtape*.

## Proposals

| Proposal | CausalPy Feature | Mixtape Chapter | Status |
|----------|------------------|-----------------|--------|
| [Matching Methods](proposal_matching.md) | `cp.Matching` | Ch 5 | 📝 Proposed |
| [Panel Fixed Effects](proposal_panel_fe.md) | `cp.PanelRegression` | Ch 8 | 📝 Proposed |
| [Triple Differences](proposal_triple_diff.md) | `cp.TripleDifferences` | Ch 9 | 📝 Proposed |

## Already In Progress

These features are already being worked on in CausalPy:

| Feature | CausalPy PR | Mixtape Notebook |
|---------|-------------|------------------|
| Staggered DiD | [PR #621](https://github.com/pymc-labs/CausalPy/pull/621) | `09_difference_in_differences.ipynb` |
| Donut RD | [PR #610](https://github.com/pymc-labs/CausalPy/pull/610) | `06_regression_discontinuity.ipynb` |
| Event Study | [PR #584](https://github.com/pymc-labs/CausalPy/pull/584) | `09_difference_in_differences.ipynb` |

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

