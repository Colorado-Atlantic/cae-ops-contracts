"""Pydantic models for the paperwork/intake endpoints (spec #101, ticket #1177).

Covers the order-owned-documents surface:
  - /accounting/intake/api/*    (unlinked scan queue + triage)
  - /accounting/paperwork/api/* (missing-doc view by trip / by week)

These are jinja-served (paperwork.html / intake.html fetch JSON), but per the
docs/api_catalog/CONVENTIONS.md rule for new endpoints the wire keys are
camelCase via Field aliases; populate_by_name=True keeps snake_case accepted on
input so the server can build models from the existing snake_case dicts.
Dates are ISO-8601 strings.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

# ── Intake queue ────────────────────────────────────────────────────────


class IntakeQueueItem(BaseModel):
    """One pending scan in the unlinked intake queue (metadata, no blob)."""

    model_config = ConfigDict(populate_by_name=True)

    id: int
    filename: str
    file_size: int = Field(alias="fileSize", default=0)
    mime_type: str = Field(alias="mimeType", default="")
    status: str
    assigned_summary: str | None = Field(alias="assignedSummary", default=None)
    uploaded_by: str = Field(alias="uploadedBy", default="")
    notes: str | None = ""
    created_at: str | None = Field(alias="createdAt", default=None)
    updated_at: str | None = Field(alias="updatedAt", default=None)


class IntakeListResponse(BaseModel):
    """GET /api/list — pending queue."""

    items: list[IntakeQueueItem]


class IntakeUploadResponse(BaseModel):
    """POST /api/upload — multipart in, JSON ack out (queue ids minted)."""

    model_config = ConfigDict(populate_by_name=True)

    queue_ids: list[int] = Field(alias="queueIds", default_factory=list)
    count: int = 0


class IntakeOrderMatch(BaseModel):
    """One order in the triage order-search results."""

    model_config = ConfigDict(populate_by_name=True)

    cae_key: str | None = Field(alias="caeKey", default=None)
    direction: str
    trip_stop: str = Field(alias="tripStop", default="")
    po: str | None = None
    pickup: str | None = None
    shipper: str | None = None
    dest: str | None = None


class IntakeSearchResponse(BaseModel):
    """GET /api/search-orders."""

    orders: list[IntakeOrderMatch]


class IntakeAssignRequest(BaseModel):
    """POST /api/assign request body — file a queued doc onto order(s)."""

    model_config = ConfigDict(populate_by_name=True)

    queue_id: int = Field(alias="queueId")
    cae_keys: list[str] = Field(alias="caeKeys", default_factory=list)
    data_point: str = Field(alias="dataPoint", default="")
    notes: str = ""


class IntakeAssignResult(BaseModel):
    """Per-order outcome of a triage assignment."""

    model_config = ConfigDict(populate_by_name=True)

    cae_key: str = Field(alias="caeKey")
    evidence_id: int | None = Field(alias="evidenceId", default=None)
    filed: str


class IntakeAssignResponse(BaseModel):
    """POST /api/assign response."""

    model_config = ConfigDict(populate_by_name=True)

    queue_id: int = Field(alias="queueId")
    data_point: str = Field(alias="dataPoint")
    results: list[IntakeAssignResult]
    summary: str


class IntakeDeleteResponse(BaseModel):
    """DELETE /api/delete/<id> response."""

    model_config = ConfigDict(populate_by_name=True)

    deleted: bool
    queue_id: int = Field(alias="queueId")


# ── Paperwork views (by trip / by week) ──────────────────────────────────


class PaperworkOrder(BaseModel):
    """One order with its completeness score, folder link, and age."""

    model_config = ConfigDict(populate_by_name=True)

    cae_key: str | None = Field(alias="caeKey", default=None)
    direction: str
    trip_number: str = Field(alias="tripNumber", default="")
    trip_stop: str = Field(alias="tripStop", default="")
    pickup: str | None = None
    destination: str | None = None
    shipper: str | None = None
    date: str | None = None
    age_days: int | None = Field(alias="ageDays", default=None)
    folder_url: str | None = Field(alias="folderUrl", default=None)
    required_total: int = Field(alias="requiredTotal", default=0)
    required_captured: int = Field(alias="requiredCaptured", default=0)
    missing_required: list[str] = Field(alias="missingRequired", default_factory=list)
    missing_optional: list[str] = Field(alias="missingOptional", default_factory=list)


class TripRollup(BaseModel):
    """Per-trip missing-paperwork rollup."""

    model_config = ConfigDict(populate_by_name=True)

    order_count: int = Field(alias="orderCount", default=0)
    orders_missing_required: int = Field(alias="ordersMissingRequired", default=0)
    total_missing_required: int = Field(alias="totalMissingRequired", default=0)


class TripPaperworkResponse(BaseModel):
    """GET /api/trip/<trip_no> — one trip's orders + rollup."""

    trip: str
    orders: list[PaperworkOrder]
    rollup: TripRollup


class WeekTrip(BaseModel):
    """A trip group within a week."""

    model_config = ConfigDict(populate_by_name=True)

    trip: str
    orders: list[PaperworkOrder]
    oldest_age_days: int | None = Field(alias="oldestAgeDays", default=None)
    rollup: TripRollup


class WeekRollup(BaseModel):
    """Whole-week rollup across all trips."""

    model_config = ConfigDict(populate_by_name=True)

    trip_count: int = Field(alias="tripCount", default=0)
    order_count: int = Field(alias="orderCount", default=0)
    orders_missing_required: int = Field(alias="ordersMissingRequired", default=0)
    total_missing_required: int = Field(alias="totalMissingRequired", default=0)


class WeekPaperworkResponse(BaseModel):
    """GET /api/week — trips grouped for a Mon–Sun week."""

    model_config = ConfigDict(populate_by_name=True)

    start_date: str = Field(alias="startDate")
    end_date: str = Field(alias="endDate")
    direction: str
    trips: list[WeekTrip]
    rollup: WeekRollup
