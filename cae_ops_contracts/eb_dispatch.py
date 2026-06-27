"""Pydantic models for /eastbound/api/dispatch/* endpoints (spec #70 #796).

Wire shapes preserved verbatim — these endpoints are already camelCase on
the wire (built that way before the Pydantic migration). Python field names
use snake_case with Field(alias=...) where the wire key diverges.
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class DispatchDriver(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    truck_id: str = Field(alias="truckId")
    driver_name: str = Field(alias="driverName")
    company: str
    status: str
    mode: str = 'LTL'


class DispatchLeg(BaseModel):
    """One cached route leg in the segments nested dict (originId → destId → leg)."""

    model_config = ConfigDict(populate_by_name=True)

    origin_id: str = Field(alias="originId")
    dest_id: str = Field(alias="destId")
    miles: float
    hours: float
    polyline: str
    road_names: str = Field(alias="roadNames")
    toll_flag: bool = Field(alias="tollFlag")
    origin_name: str = Field(alias="originName")
    dest_name: str = Field(alias="destName")


class DispatchDwellStat(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    dest_id: str = Field(alias="destId")
    obs: int
    avg: float
    median: float
    p25: float
    p75: float


class DispatchLocation(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    lat: float
    lon: float
    window_open: float | None = Field(alias="windowOpen", default=None)
    window_close: float | None = Field(alias="windowClose", default=None)
    name: str = ""
    address: str = ""
    city: str = ""
    state: str = ""
    zip: str = ""


class DispatchTripPlan(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    temp_class: str | None = Field(alias="tempClass", default=None)
    driver_id: int | None = Field(alias="driverId", default=None)
    departure_at: str | None = Field(alias="departureAt", default=None)
    notes: str | None = None


class DispatchOrderRow(BaseModel):
    """One order in the /dispatch/data response.

    Fields marked Optional are not currently sent by the handler — they exist
    so the generated TypeScript type is a superset of what the FE accesses
    (enabling `o.pickupCity || ''` without a type error).
    """

    model_config = ConfigDict(populate_by_name=True)

    cae_key: str = Field(alias="caeKey")
    destination: str
    destination_id: str = Field(alias="destinationId")
    shipper: str
    pickup: str
    pallets: float
    weight: float
    temp: str
    base_rate: float = Field(alias="baseRate")
    fsc: float
    po_number: str = Field(alias="poNumber")
    order_number: str = Field(alias="orderNumber")
    created_at: str = Field(alias="createdAt")
    last_updated: str = Field(alias="lastUpdated")
    delivery_date: str = Field(alias="deliveryDate")
    region: str
    truck_id: str | None = Field(alias="truckId")
    stop_number: int | None = Field(alias="stopNumber")
    invoice: str
    tl: str = 'N'
    lamb: str = 'N'
    # Location enrichment
    lat: float = 0.0
    lon: float = 0.0
    window_open: float | None = Field(alias="windowOpen", default=None)
    window_close: float | None = Field(alias="windowClose", default=None)
    dwell_minutes: int = Field(alias="dwellMinutes", default=0)
    # Appointment enrichment
    appointment_time: str | None = Field(alias="appointmentTime", default=None)
    appointment_date: str | None = Field(alias="appointmentDate", default=None)
    appointment_hour: float | None = Field(alias="appointmentHour", default=None)
    appointment_status: str = Field(alias="appointmentStatus", default="")
    due_date: str = Field(alias="dueDate", default="")
    # Optional fields not currently sent; present for FE type completeness
    pickup_city: str | None = Field(alias="pickupCity", default=None)
    pickup_state: str | None = Field(alias="pickupState", default=None)
    pickup_zip: str | None = Field(alias="pickupZip", default=None)
    activity_count: int | None = Field(alias="activityCount", default=None)
    confirmation: str | None = None
    called_in: str | None = Field(alias="calledIn", default=None)
    client_notes: str | None = Field(alias="clientNotes", default=None)
    dispatch_notes: str | None = Field(alias="dispatchNotes", default=None)
    picked_up: bool | None = Field(alias="pickedUp", default=None)


class DispatchLastStop(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    city: str
    state: str
    appt_date: str = Field(alias="apptDate")
    appt_time: str = Field(alias="apptTime")
    lat: float | None = None
    lon: float | None = None
    location_id: str | None = Field(alias="locationId", default=None)
    address: str | None = None
    destination: str | None = None
    delivered: bool | None = None


class DispatchData(BaseModel):
    """Bundled response for GET /eastbound/api/dispatch/data.

    tripPlans domain key preserved — intentional per spec #70 (direction-specific,
    not a generic normalized name). lastStops is optional; absent when no EB
    last-delivery data is available for the ship date.
    """

    model_config = ConfigDict(populate_by_name=True)

    orders: list[DispatchOrderRow]
    drivers: list[DispatchDriver]
    segments: dict[str, dict[str, DispatchLeg]]
    dwell_stats: dict[str, DispatchDwellStat] = Field(alias="dwellStats")
    locations: dict[str, DispatchLocation]
    trip_plans: dict[str, DispatchTripPlan] = Field(alias="tripPlans", default_factory=dict)
    ship_date: str = Field(alias="shipDate")
    last_stops: dict[str, DispatchLastStop] | None = Field(alias="lastStops", default=None)


# ── Mutation models ──────────────────────────────────────────────────────────


class AckResponse(BaseModel):
    ok: bool = True


class AssignRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    cae_key: str = Field(alias="caeKey")
    truck_id: str = Field(alias="truckId")
    delivery_date: str = Field(alias="deliveryDate")


class AssignResponse(BaseModel):
    ok: bool
    trip_number: str
    slot: int


class UnassignRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    cae_key: str = Field(alias="caeKey")


class TruckConfigRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    ship_date: str = Field(alias="shipDate")
    truck_id: str = Field(alias="truckId")
    field: str
    value: Any = None
    direction: str | None = None


class TruckConfigResponse(BaseModel):
    ok: bool
    plan: dict[str, Any]


class TruckConfigListResponse(BaseModel):
    plans: list[dict[str, Any]]


# ── Allocation notes models (WB /api/allocations/notes) ──────────────────────


class AllocationNote(BaseModel):
    """One activity entry from pickup_activity_log. Wire format is snake_case."""

    id: int
    cae_key: str
    activity_type: str
    summary: str
    logged_by: str
    created_at: str


class AllocationNotesResponse(BaseModel):
    notes: list[AllocationNote]


class AllocationNoteCreateRequest(BaseModel):
    cae_key: str
    summary: str
    activity_type: str = 'note'


class AllocationNoteDeleteRequest(BaseModel):
    note_id: int


# ── Dispatch packet models (EB /eastbound/api/dispatch/packet — spec #125) ───


class DispatchPacketLumper(BaseModel):
    """Lumper requirement for a stop's destination, classified from the
    destination's free-text lumper_fee attribute."""

    model_config = ConfigDict(populate_by_name=True)

    type: str                                  # Comcheck | Credit Card | Relay | RFS | Other
    amount: str = ""                           # parsed dollar amount e.g. "150"; "" if none
    raw: str = ""                              # original lumper_fee string
    actionable: bool = False                   # True for Comcheck / Credit Card (cash to send)


class DispatchPacketOrder(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    cae_key: str = Field(alias="caeKey")
    shipper: str = ""
    destination: str = ""
    po_number: str = Field(alias="poNumber", default="")
    bol_in: bool = Field(alias="bolIn", default=False)
    lumper: DispatchPacketLumper | None = None


class DispatchPacketResponse(BaseModel):
    """Per-trip dispatch packet summary (spec #125). departedAt/By are null
    until the departure store lands (ticket #1341/#1343)."""

    model_config = ConfigDict(populate_by_name=True)

    ship_date: str = Field(alias="shipDate")
    trip_number: str = Field(alias="tripNumber")
    driver: str = ""
    truck: str = ""
    departed_at: str | None = Field(alias="departedAt", default=None)
    departed_by: str | None = Field(alias="departedBy", default=None)
    orders: list[DispatchPacketOrder] = Field(default_factory=list)
