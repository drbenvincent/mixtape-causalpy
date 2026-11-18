# Contributing

## Environment

Use this repository's uv environment. Do not render with conda, miniforge, or a bare `pip install causalpy`.

From the checkout you are about to render:

```bash
uv sync
uv run python -m ipykernel install --user --name mixtape-causalpy --display-name "Mixtape CausalPy"
uv run python -c "import json, pathlib, sys; from jupyter_client.kernelspec import find_kernel_specs; spec = pathlib.Path(find_kernel_specs()['mixtape-causalpy']) / 'kernel.json'; argv0 = pathlib.Path(json.loads(spec.read_text())['argv'][0]); expected = pathlib.Path(sys.prefix) / 'bin' / 'python'; print(argv0); assert argv0 == expected, (argv0, expected)"
```

Chapters set `jupyter: mixtape-causalpy`. That name is global. `QUARTO_PYTHON` does not select it. Re-register from the checkout you are rendering, including a worktree, and do not leave the spec pointed at a deleted `.venv`. The rest of the fresh-machine steps are in `README.md`.


## Update the live site

The reader site is https://drbenvincent.github.io/mixtape-causalpy/. A local `quarto preview` and an open pull request do not change it.

Publishing is automatic. `.github/workflows/publish.yml` (`Quarto Publish`) runs on every push to `main`, and when started by hand from the Actions tab. It renders from the committed `_freeze/` and deploys the `gh-pages` branch. It does not re-run MCMC.

1. Merge the change to `main`. That push is the publish.
2. If a chapter's computations changed, that merge must include the updated `_freeze/`. Otherwise the live page keeps the old output.
3. Wait until the `Quarto Publish` run for that commit succeeds: https://github.com/drbenvincent/mixtape-causalpy/actions

Do not push `gh-pages` yourself, and do not run `quarto publish` from a laptop. To republish the current `main` with no new commit, open Actions → Quarto Publish → Run workflow.
