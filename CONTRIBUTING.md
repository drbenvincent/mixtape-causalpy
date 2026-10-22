# Contributing

## Update the live site

The reader site is https://drbenvincent.github.io/mixtape-causalpy/. A local `quarto preview` and an open pull request do not change it.

Publishing is automatic. `.github/workflows/publish.yml` (`Quarto Publish`) runs on every push to `main`, and when started by hand from the Actions tab. It renders from the committed `_freeze/` and deploys the `gh-pages` branch. It does not re-run MCMC.

1. Merge the change to `main`. That push is the publish.
2. If a chapter's computations changed, that merge must include the updated `_freeze/`. Otherwise the live page keeps the old output.
3. Wait until the `Quarto Publish` run for that commit succeeds: https://github.com/drbenvincent/mixtape-causalpy/actions

Do not push `gh-pages` yourself, and do not run `quarto publish` from a laptop. To republish the current `main` with no new commit, open Actions → Quarto Publish → Run workflow.
