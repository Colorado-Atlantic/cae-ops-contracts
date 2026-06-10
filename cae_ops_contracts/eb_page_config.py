from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class DriverEmailAlias(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: int
    driver_name: str = Field(alias="driverName")
    email: str
    source: str
    updated_at: str | None = Field(alias="updatedAt", default=None)


class DriverEmailAliasListResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    aliases: list[DriverEmailAlias]


class DeliveryLoggerConfigResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    debug: bool
    detention_excluded_pickups: list[str] = Field(alias="detentionExcludedPickups")
    detention_excluded_destinations: list[str] = Field(alias="detentionExcludedDestinations")


class DeliverySchedulerConfigResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    debug: bool
    company_address: str = Field(alias="companyAddress")
    denver_id: str = Field(alias="denverId")
    denver_lat: float = Field(alias="denverLat")
    denver_lon: float = Field(alias="denverLon")
