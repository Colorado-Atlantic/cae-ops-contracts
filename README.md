# cae-ops-contracts

Pydantic contract models for the [cae-ops](https://github.com/Colorado-Atlantic/cae-ops-api) platform API surface.

This package is the shared type layer between `cae-ops-api` (Flask backend) and future clients (`cae-ops-web`, `cae-ops-dock`). It is a standalone pip-installable package — no Flask, no database dependencies.

## Install

Requires a GitHub PAT with `contents:read` on this repo. Add to `~/.netrc`:

```
machine github.com login x-access-token password <YOUR_PAT>
```

Then install, pinned to a release tag:

```bash
pip install "cae-ops-contracts @ git+https://github.com/Colorado-Atlantic/cae-ops-contracts.git@v0.1.0"
```

## Usage

```python
from cae_ops_contracts.errors import ApiError
from cae_ops_contracts.westbound import WbOrderRow
from cae_ops_contracts.eb_dispatch import EbAllocationRow
```

## Versioning

Follows [semver](https://semver.org/). Breaking model changes bump the minor version. Additive changes (new fields with defaults, new models) bump patch.

Pin to a specific tag in `requirements.txt`. Never use `@main` in production.

## Releasing

Push a tag matching `v*.*.*` — the publish workflow builds and attaches artifacts to a GitHub Release automatically.

```bash
git tag v0.1.1
git push origin v0.1.1
```
