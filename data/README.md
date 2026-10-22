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
| SASP | `sasp_panel.dta` | Ch 8: Panel | Cunningham & Kendall sex-worker survey; panel of recent client sessions. Provenance: Mixtape repo (`scunning1975/mixtape`). |
| Titanic | `titanic.dta` | Ch 5: Matching | Simple difference in outcomes example. Fetched for `python/titanic.py`. The script names no paper. Not committed and not relicensed here. |

## Original sources

Files are not committed to this repository. They are fetched at runtime from Scott Cunningham's code repository and are not relicensed here. Cunningham's MIT grant cannot license third-party data he does not own. Rights stay with the original authors. See `NOTICE` and the [attribution page](../attribution.qmd).

- **Code and data repository**: https://github.com/scunning1975/mixtape
- **Book (1st ed.)**: https://mixtape-1ed.netlify.app/

## Citations

| File | Citation |
| --- | --- |
| `card.dta` | Card (1995); labeled "Public domain" in the `causaldata` docs, not a grant here. NLS Young Men extract. |
| `cps_mixtape.dta` | Dehejia and Wahba (1999); labeled "Public domain" there. CPS extract. |
| `nsw_mixtape.dta` | LaLonde (1986) / NSW experiment. Cite the paper. |
| `lmb-data.dta` | Lee, Moretti, and Butler (2004), *QJE* 119(3): 807–859. |
| `castle.dta` | Cheng and Hoekstra (2013), *JHR* 48(3): 821–854. FBI UCR plus law dates. |
| `abortion.dta` | Donohue and Levitt (2001). Cite the paper. |
| `texas.dta` | Texas prison synthetic control. Cite the Mixtape code repository and the series source used there (`python/synth_1.py`, `Do/synth_1.do`: black male prisoners (per capita), `bmprison`). Do not invent a public-domain claim. |
| `sasp_panel.dta` | Cunningham and Kendall, Survey of Adult Service Providers. Panel of recent client sessions. Fetched from the Mixtape code repository. Not relicensed here. |
| `titanic.dta` | Fetched at runtime for the `python/titanic.py` example. The Mixtape script names no paper. Not committed, not a license grant from this project, and not labeled MIT or public domain here. |

## Alternative: causaldata package

Many of these datasets are also listed in the [`causaldata`](https://github.com/NickCH-K/causaldata) Python package. This loader does not call it. Per-dataset `COPYRIGHT` strings there are attributions, not a license grant, and that repository has no `Python/LICENSE` to rely on. Do not describe those files as permissively licensed by this project or by the Mixtape code repository.

```python
# pip install causaldata
from causaldata import castle, card, etc.
```

Runtime loads stay on the Mixtape code repository so the files match the first-edition examples.

## Licensing

The files are not committed, not relicensed, and fetched from the Mixtape code repository. Do not say they are distributed under that repository's license. Cite the papers in the table above.

