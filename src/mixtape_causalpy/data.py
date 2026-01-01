"""
Data loading utilities for Mixtape-CausalPy examples.

Primary sources (in order of preference):
1. causaldata package - clean, documented, permissively licensed
2. Mixtape GitHub repo - direct download from scunning1975/mixtape
3. Local cache - downloaded once, cached in ~/.cache/mixtape-causalpy/
"""

from pathlib import Path

import pandas as pd

MIXTAPE_BASE_URL = "https://github.com/scunning1975/mixtape/raw/master/"
CACHE_DIR = Path.home() / ".cache" / "mixtape-causalpy"


def load_mixtape_data(filename: str, use_cache: bool = True) -> pd.DataFrame:
    """
    Load a dataset from the Mixtape repo, with optional caching.

    Parameters
    ----------
    filename : str
        The filename to load (e.g., "lmb-data.dta", "castle.dta")
    use_cache : bool, default True
        Whether to cache the downloaded file locally

    Returns
    -------
    pd.DataFrame
        The loaded dataset
    """
    cache_path = CACHE_DIR / filename

    if use_cache and cache_path.exists():
        return pd.read_stata(cache_path)

    url = MIXTAPE_BASE_URL + filename
    df = pd.read_stata(url)

    if use_cache:
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        # Save as pickle for faster loading (Stata write can be lossy)
        cache_path_pkl = cache_path.with_suffix(".pkl")
        df.to_pickle(cache_path_pkl)

    return df


# =============================================================================
# Convenience functions for common datasets
# =============================================================================


def load_lmb() -> pd.DataFrame:
    """
    Lee-Moretti-Butler close elections data for RD.

    Used in Chapter 6: Regression Discontinuity.
    """
    return load_mixtape_data("lmb-data.dta")


def load_castle() -> pd.DataFrame:
    """
    Castle doctrine (Stand Your Ground) data for DiD.

    Used in Chapter 9: Difference-in-Differences.
    """
    return load_mixtape_data("castle.dta")


def load_card() -> pd.DataFrame:
    """
    Card (1995) returns to schooling data for IV.

    Used in Chapter 7: Instrumental Variables.
    """
    return load_mixtape_data("card.dta")


def load_texas() -> pd.DataFrame:
    """
    Texas incarceration data for synthetic control.

    Used in Chapter 10: Synthetic Control.
    """
    return load_mixtape_data("texas.dta")


def load_nsw() -> pd.DataFrame:
    """
    National Supported Work data for matching/IPW.

    Used in Chapter 5: Matching and Subclassification.
    """
    return load_mixtape_data("nsw_mixtape.dta")


def load_abortion() -> pd.DataFrame:
    """
    Abortion legalization data for DiD.

    Used in Chapter 9: Difference-in-Differences.
    """
    return load_mixtape_data("abortion.dta")


def load_cps() -> pd.DataFrame:
    """
    CPS control group data for matching examples.

    Used in Chapter 5: Matching and Subclassification.
    """
    return load_mixtape_data("cps_mixtape.dta")
