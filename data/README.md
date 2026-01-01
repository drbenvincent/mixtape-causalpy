# Data Sources

This document describes the datasets used in the Mixtape-CausalPy notebooks and their provenance.

## Data Loading Strategy

Datasets are loaded at runtime using the utilities in `src/mixtape_causalpy/data.py`. **No data files are committed to this repository.**

### Loading Priority

1. **Local cache** (`~/.cache/mixtape-causalpy/`) — if previously downloaded
2. **Mixtape GitHub repo** — direct download from https://github.com/scunning1975/mixtape

### Caching

Downloaded files are cached locally to avoid repeated network requests. The cache directory is:

```
~/.cache/mixtape-causalpy/
```

To clear the cache, simply delete this directory.

## Dataset Catalog

| Dataset | File | Chapter | Description |
|---------|------|---------|-------------|
| LMB | `lmb-data.dta` | Ch 6: RD | Lee-Moretti-Butler close elections data |
| Castle | `castle.dta` | Ch 9: DiD | Castle doctrine (Stand Your Ground) laws |
| Card | `card.dta` | Ch 7: IV | Card (1995) returns to schooling |
| Texas | `texas.dta` | Ch 10: SC | Texas incarceration for synthetic control |
| NSW | `nsw_mixtape.dta` | Ch 5: Matching | National Supported Work experimental data |
| Abortion | `abortion.dta` | Ch 9: DiD | Abortion legalization effects |
| CPS | `cps_mixtape.dta` | Ch 5: Matching | CPS control group for matching |

## Original Sources

All datasets are from Scott Cunningham's Mixtape repository:

- **Repository**: https://github.com/scunning1975/mixtape
- **Book**: https://mixtape.scunning.com

## Alternative: causaldata Package

Many of these datasets are also available via the [`causaldata`](https://github.com/NickCH-K/causaldata) Python package:

```python
# pip install causaldata
from causaldata import castle, card, etc.
```

We use direct Mixtape repo downloads to ensure consistency with the book's examples.

## Licensing

The datasets are distributed with the Mixtape repository under its license. See the [Mixtape repo](https://github.com/scunning1975/mixtape) for details.

