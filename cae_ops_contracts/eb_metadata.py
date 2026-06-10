"""Pydantic models for EB metadata endpoints (spec #70 #797).

Covers:
  GET  /eastbound/api/config/maps-key
  GET  /eastbound/api/history/matrix
  GET  /eastbound/api/settings/order-change-impact
  POST /eastbound/api/settings/order-change-impact
"""

from __future__ import annotations

from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field

# ── Maps key ─────────────────────────────────────────────────────────────────


class MapsKeyResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    api_key: str = Field(alias="apiKey", description="Google Maps JS API key. Same trust boundary as embedding in HTML.")


# ── History matrix ────────────────────────────────────────────────────────────


class HistoryWeekInfo(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    iso_week: str = Field(alias="isoWeek", description='ISO year-week label (e.g. "2026-W15").')
    label: str = Field(description='Display label (e.g. "Apr 6").')
    start_date: str = Field(alias="startDate", description="ISO date of the Monday that starts this week.")
    is_future: bool = Field(alias="isFuture")
    is_current: bool = Field(alias="isCurrent")


class HistoryDeliveryStatus(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    early: int = Field(ge=0)
    on_time: int = Field(alias="onTime", ge=0)
    late: int = Field(ge=0)


class HistoryCell(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    orders: int = Field(ge=0)
    pallets: float
    weight: float
    revenue: float
    shippers: list[str]
    temps: list[str]
    trucks: list[str]
    delivery_dates: list[str] = Field(alias="deliveryDates")
    dwell_avg: float | None = Field(alias="dwellAvg", default=None, description="Average dwell minutes for the cell; null when no observations.")
    delivery_status: HistoryDeliveryStatus = Field(alias="deliveryStatus")
    volume_std_dev: float | None = Field(alias="volumeStdDev", default=None, description="stdev of per-order pallet counts; null with <2 orders.")


class HistoryMatrixResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    weeks: list[HistoryWeekInfo]
    destinations: list[str]
    shippers: list[str]
    temps: list[str]
    cells: dict[str, dict[str, HistoryCell]] = Field(description="Nested map — destination → isoWeek → cell.")
    current_week: str = Field(alias="currentWeek", description="ISO year-week label for today's week.")


# ── Impact settings ───────────────────────────────────────────────────────────


class ImpactRow(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    direction: Literal['eb', 'wb']
    scope: Literal['order', 'receiver']
    field_name: str
    default_level: Annotated[int, Field(ge=0, le=5)]
    condition: str | None = Field(default=None, description="Optional condition key (e.g. `over_capacity`) for conditional rows.")
    updated_at: str | None = None
    updated_by: str | None = None


class ImpactSettingsResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    direction: Literal['eb', 'wb']
    rows: list[ImpactRow]
    threshold_n: Annotated[int, Field(ge=1)]


class ImpactSettingsRequest(BaseModel):
    """Flat union covering both kind='field' and kind='threshold' mutations.

    The handler validates the kind-specific required fields itself.
    """

    model_config = ConfigDict(populate_by_name=True)

    direction: str
    kind: str
    scope: str | None = None
    field_name: str | None = None
    default_level: int | None = None
    condition: str | None = None
    value: int | None = None
    ship_date: str | None = None


class ImpactSettingsMutationResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    change_id: int
    snapshot_id: int
    before_value: int | None = None
    after_value: int
