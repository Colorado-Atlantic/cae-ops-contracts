"""Pydantic models for /api/location-hours/* endpoints (spec #73)."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class HourWindow(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    weekday: int = Field(description="ISO weekday: 1=Mon … 7=Sun")
    open_minutes: int = Field(alias="openMinutes", description="Minutes since midnight")
    close_minutes: int = Field(alias="closeMinutes", description="Minutes since midnight")
    appt_only: bool = Field(alias="apptOnly", default=False)
    notes: str | None = Field(default=None)
    timezone: str | None = Field(default=None)


class LocationHoursSet(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    location_id: str = Field(alias="locationId")
    windows: list[HourWindow]
    source: str = Field(description="'sheet' or 'manual'")
    updated_at: str | None = Field(alias="updatedAt", default=None)


class LocationHoursBatch(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    location_hours: dict[str, list[HourWindow]] = Field(alias="locationHours")


class LocationHoursImportSummary(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    rows_imported: int = Field(alias="rowsImported")
    locations_covered: int = Field(alias="locationsCovered")
    locations_skipped: int = Field(alias="locationsSkipped")
    ran_at: str = Field(alias="ranAt")
