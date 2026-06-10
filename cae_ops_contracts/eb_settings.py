"""Pydantic models for EB settings + changes endpoints (spec #70 #798).

Covers:
  GET  /eastbound/api/settings/audit-log
  GET  /eastbound/api/changes/summary
  GET  /eastbound/api/changes/truck/<trip_number>
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

# ── Audit log ─────────────────────────────────────────────────────────────────


class AuditLogRow(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int
    timestamp: str
    user_email: str | None = None
    section: str
    setting_key: str
    before_value: int | str | None = None
    after_value: int | str | None = None
    snapshot_id: int | None = None
    delta_summary: str | None = None
    pending: bool | None = None


class AuditLogResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    rows: list[AuditLogRow]
    limit: int
    count: int


# ── Changes summary ───────────────────────────────────────────────────────────


class PerTruckChange(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    trip_number: str
    driver_name: str | None = None
    impact_sum: int
    change_count: int


class ChangesSummaryResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    direction: str
    ship_date: str
    per_truck: list[PerTruckChange]
    global_sum: int
    last_solve_at: str | None = None
    threshold_n: int
    prompt_global_realloc: bool


# ── Truck audit ───────────────────────────────────────────────────────────────


class TruckAuditChange(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int
    timestamp: str
    cae_key: str | None = None
    updated_fields: str | None = None
    impact_level: int = 0
    user_email: str | None = None
    trip_number: str
    kind: str
    is_cancellation: bool = False
    field_name: str | None = None
    before_value: str | None = None
    after_value: str | None = None


class TruckAuditResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    trip_number: str
    ship_date: str
    last_solve_at: str | None = None
    changes: list[TruckAuditChange]
