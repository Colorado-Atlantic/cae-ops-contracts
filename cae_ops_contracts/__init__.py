"""Pydantic contract models for the React-consumed API surface (spec #70).

Layout: one module per domain (segments, eb_dispatch, wb_dispatch, ...).
Shared error shapes live in `errors.py`. The `@validated` decorator in
`api/glue.py` consumes these models; `scripts/generate_openapi.py` walks
the same registry to emit `docs/api_catalog/openapi.yaml`.
"""
