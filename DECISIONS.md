# Decisions

## Stay on the first edition

**Date:** 2026-10-22
**Status:** accepted

This repository implements *Causal Inference: The Mixtape* (1st ed., Yale University Press, 2021). It does not implement *Causal Inference: The Remix* (2nd ed., published 25 Aug 2026).

Do not retarget the notebooks at the Remix until there is a public code source and an explicit plan to do so.

Reader-facing copy says first edition. Ground truth is <https://mixtape-1ed.netlify.app/>. <https://mixtape.scunning.com/> is the Remix and is not a source.

### Why

The first-edition translation had a public script tree (`python/`, `R/`, `Do/`) and data in [scunning1975/mixtape](https://github.com/scunning1975/mixtape). Checked 2026-10-22, that tree was not replaced for the Remix, and there is no public Remix code repository. The Remix site embeds code in rendered chapters. It is not a cloneable source. Third-party script dumps are not a source either.

A Remix port would also be mostly new methods (staggered and event-study difference-in-differences, Callaway–Sant'Anna, Sun–Abraham, imputation, augmented synthetic control, matrix completion, synthetic difference-in-differences), not a re-run of these notebooks.

### Revisit when

A public Remix code source exists, and there is an explicit plan to retarget. Until then, do not transcribe Stata or R out of <https://mixtape.scunning.com/>.
