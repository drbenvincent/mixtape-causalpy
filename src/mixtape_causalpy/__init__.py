"""
Mixtape-CausalPy: CausalPy implementations of Causal Inference: The Mixtape examples.

This package provides data loading utilities for the datasets used in
Scott Cunningham's "Causal Inference: The Mixtape".

Source: https://mixtape.scunning.com
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
]

