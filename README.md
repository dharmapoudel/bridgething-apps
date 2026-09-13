# bridgething-apps

One combined Bridgething app catalog covering every app by Dharma Poudel,
in the same shape as the official https://apps.bridgething.com/catalog.json.

**Live catalog:** https://dharmapoudel.github.io/bridgething-apps/catalog.json

## What's inside

The catalog merges these per-app sources:

- Radio Atlas — https://dharmapoudel.github.io/atlas-radio-source/catalog.v1.json
- Calendar — https://dharmapoudel.github.io/bridgething-calendar-source/catalog.v1.json
- Block Drop — https://dharmapoudel.github.io/bridgething-block-drop-source/catalog.v1.json
- Market Pulse — https://dharmapoudel.github.io/bridgething-market-pulse-source/catalog.v1.json

## Refreshing

`python3 merge.py` re-fetches the four sources and rewrites `catalog.json`.
The `refresh` GitHub Actions workflow does this daily (and on demand via
workflow dispatch) and publishes the result to the `gh-pages` branch.
