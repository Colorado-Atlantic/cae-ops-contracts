from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class SortingSegRate(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    max_weight: int | None = Field(alias="maxWeight")
    rate: float


class SortingSegConfigResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    rates: list[SortingSegRate]
