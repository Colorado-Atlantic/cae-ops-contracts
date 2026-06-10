"""Pydantic models for /api/segments/* endpoints (spec #70 #795).

Wire shapes preserved verbatim from pre-Pydantic handlers; field names
that were already camelCase on the wire are expressed via Field(alias=...)
so the Python side uses snake_case throughout.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, NonNegativeInt


class QuotaStatus(BaseModel):
    """Today's Maps API daily quota state.

    Shared by GET /quota-status and POST /quota/set-limit — collapses the
    legacy QuotaState/QuotaStatus split (#789 gotcha 1). The enabled flag
    (previously absent from the set-limit response) is now always included.
    """

    date: str
    used: NonNegativeInt
    limit: NonNegativeInt
    remaining: NonNegativeInt
    enabled: bool


# ── /quota/set-limit ─────────────────────────────────────────────────────────


class SetLimitRequest(BaseModel):
    limit: NonNegativeInt


# ── /list ────────────────────────────────────────────────────────────────────


class SegmentRow(BaseModel):
    origin_id: str
    origin_name: str
    origin_addr: str
    origin_lat: float
    origin_lon: float
    dest_id: str
    dest_name: str
    dest_addr: str
    dest_lat: float
    dest_lon: float
    miles: float
    hours: float
    polyline_len: int
    polyline: str | None = None
    source: str
    road_names: str
    toll_flag: bool
    flag: str | None = None
    lane: str | None = None
    notes: str | None = None
    timestamp: str


class SegmentListResponse(BaseModel):
    segments: list[SegmentRow]
    count: int


# ── /tolls ───────────────────────────────────────────────────────────────────


class TollSegment(BaseModel):
    origin_id: str
    dest_id: str
    origin_name: str
    dest_name: str
    miles: float
    hours: float
    road_names: str
    source: str
    created_at: str
    matched_facilities: list[str]


class TollsResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    tolls: list[TollSegment]
    count: int
    total_segments: int = Field(alias="totalSegments")
    segments_with_roads: int = Field(alias="segmentsWithRoads")


# ── /refresh-tolls ───────────────────────────────────────────────────────────


class RefreshTollsResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    newly_flagged: int = Field(alias="newlyFlagged")
    total_tolled: int = Field(alias="totalTolled")


# ── /backfill-addresses ──────────────────────────────────────────────────────


class BackfillAddressesResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    updated: int
    dest_updated: int = Field(alias="destUpdated")
    origin_updated: int = Field(alias="originUpdated")


# ── /mal-list ────────────────────────────────────────────────────────────────


class MALEntry(BaseModel):
    id: str
    name: str
    address: str
    lat: float | None = None
    lon: float | None = None
    timezone: str


class MALListResponse(BaseModel):
    entries: list[MALEntry]
    count: int
    spreadsheet_id: str


# ── /batch-fetch ─────────────────────────────────────────────────────────────


class LegRequest(BaseModel):
    origin_id: str
    dest_id: str
    origin_lat: float
    origin_lon: float
    dest_lat: float
    dest_lon: float
    origin_name: str = ""
    dest_name: str = ""


class BatchFetchRequest(BaseModel):
    legs: list[LegRequest]


class SegmentFetchResult(BaseModel):
    origin_id: str
    dest_id: str
    cached: bool
    miles: float = 0.0
    hours: float = 0.0
    polyline: str = ""
    road_names: str = ""
    same_location: bool | None = None


class BatchFetchResponse(BaseModel):
    fetched: int
    results: list[SegmentFetchResult]
    error: str | None = None


# ── /import-resolved ─────────────────────────────────────────────────────────


class RejectedRow(BaseModel):
    row: int
    reason: str


class ImportResolvedResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    accepted: int
    rejected: list[RejectedRow]
    rejected_count: int = Field(alias="rejectedCount")


# ── admin-only / flex (status, seed, fetch, sync, rank, backfill) ─────────────


class SegFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class SegFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")
