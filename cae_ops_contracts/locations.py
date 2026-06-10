"""Pydantic models for /api/locations/* endpoints (spec #92, ticket #997).

Covers location rename + alias surface area. The integer `pk` referenced by
these endpoints maps to the master location row's primary-key `id` column
in `data/locations.db` — not the text `location_id` business identifier
some tables carry.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class LocationRenameRequest(BaseModel):
    """POST /api/locations/<kind>/<pk>/rename request body."""

    model_config = ConfigDict(populate_by_name=True)

    new_name: str = Field(alias="newName", min_length=1)
    note: str = Field(default="")


class RenameAck(BaseModel):
    """Lightweight success ack — server-filled actor + alias landed."""

    ok: bool = True


class LocationAlias(BaseModel):
    """One historical name for a location."""

    model_config = ConfigDict(populate_by_name=True)

    alias: str
    note: str = ""
    created_at: str = Field(alias="createdAt")
    created_by: str = Field(alias="createdBy", default="")


class LocationAliases(BaseModel):
    """GET /api/locations/<kind>/<pk>/aliases response."""

    aliases: list[LocationAlias]
