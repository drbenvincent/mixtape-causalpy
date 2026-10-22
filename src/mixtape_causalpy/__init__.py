"""
Mixtape-CausalPy: unofficial CausalPy translations of Causal Inference: The Mixtape (1st ed., 2021) examples.

This package provides data loading utilities for the datasets used in
Scott Cunningham's "Causal Inference: The Mixtape".

Source: https://mixtape-1ed.netlify.app/
"""

from .data import (
    load_mixtape_data,
    load_lmb,
    load_castle,
    load_card,
    load_texas,
    load_nsw,
    load_abortion,
    load_cps,
    load_sasp,
)

__all__ = [
    "load_mixtape_data",
    "load_lmb",
    "load_castle",
    "load_card",
    "load_texas",
    "load_nsw",
    "load_abortion",
    "load_cps",
    "load_sasp",
]

