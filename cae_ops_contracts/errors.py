"""Shared error envelope for API responses (spec #70).

Pre-adopts the RFC 7807 `detail` key so a future move to full Problem
Details is a non-breaking expansion. HTTP status carries the category;
the model only carries the human-readable explanation plus optional
machine-readable hints.
"""

from __future__ import annotations

from pydantic import BaseModel


class FieldError(BaseModel):
    """One row in a 400 validation_error response."""

    field: str
    detail: str


class ApiError(BaseModel):
    detail: str
    code: str | None = None
    fields: list[FieldError] | None = None
