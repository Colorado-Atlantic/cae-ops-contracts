"""Pydantic models for /eastbound/api/address-aliases endpoints (spec #66 #981).

Phase 3 tracer — establishes the API-driven Jinja conversion pattern.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class AddressAlias(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int
    destination_name: str = Field(alias="destinationName")
    physical_address: str = Field(alias="physicalAddress")
    notes: str
    updated_at: str | None = Field(alias="updatedAt", default=None)


class AddressAliasesResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    aliases: list[AddressAlias]
    pickup_names: list[str] = Field(alias="pickupNames")
