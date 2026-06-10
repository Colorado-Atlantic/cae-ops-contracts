"""Pydantic models for /westbound/api/* endpoints — spec #66 ticket #985.

All jinja-served-json routes preserve snake_case wire keys (no Field aliases).
Only routes already consumed by React use alias conventions per CONVENTIONS.md.
Complex / dynamic-shape responses use ConfigDict(extra='allow') so the existing
dict wire format is preserved exactly via model_validate() + model_dump().
"""
from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict

# ---------------------------------------------------------------------------
# Re-export shared models so callers only need to import from here
# ---------------------------------------------------------------------------
from cae_ops_contracts.eb_dispatch import AckResponse  # noqa: F401

# ---------------------------------------------------------------------------
# Reference data
# ---------------------------------------------------------------------------


class AppStatusResponse(BaseModel):
    status: str
    debug_mode: bool
    source: str
    pickups_count: int
    clients_count: int
    shippers_count: int


class ShippersResponse(BaseModel):
    shippers: list[Any]


class PayorsResponse(BaseModel):
    payors: list[Any]


class LookupPayorRequest(BaseModel):
    pickup: str = ""
    shipper: str = ""
    destination: str = ""


class LookupPayorResponse(BaseModel):
    payors: list[Any]
    count: int
    confidence: str


class RefreshResponse(BaseModel):
    model_config = ConfigDict(extra="allow")
    status: str = ""


class PickupRow(BaseModel):
    name: str
    billing_region: str = ""
    region: str = ""
    temp: str = "C"
    nyc: str = "N"
    address: str = ""


class PickupsResponse(BaseModel):
    pickups: list[PickupRow]


class DestinationRow(BaseModel):
    name: str
    region: str = ""
    interline: str = ""
    address: str = ""


class DestinationsResponse(BaseModel):
    destinations: list[DestinationRow]


class TrucksResponse(BaseModel):
    model_config = ConfigDict(extra="allow")
    trucks: list[Any]


# ---------------------------------------------------------------------------
# Dispatch
# ---------------------------------------------------------------------------


class LatestDateResponse(BaseModel):
    latestDate: str


# ---------------------------------------------------------------------------
# Locations
# ---------------------------------------------------------------------------


class LocationsPickupsResponse(BaseModel):
    pickups: list[Any]


class LocationsDeliveriesResponse(BaseModel):
    deliveries: list[Any]


class SetActiveRequest(BaseModel):
    table: str = ""
    name: str = ""
    active: bool = False


class SetActiveResponse(BaseModel):
    updated: int
    active: bool


class LocationMutationRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class LocationMutationResponse(BaseModel):
    model_config = ConfigDict(extra="allow")
    status: str


class GenerateKeyResponse(BaseModel):
    key: str


class LookupBillingRegionResponse(BaseModel):
    billing_region: str
    zip: str


class LocationContactsResponse(BaseModel):
    contacts: list[Any]


class AddContactRequest(BaseModel):
    location_name: str = ""
    contact_name: str = ""
    role: str = "Other"
    phone: str = ""
    email: str = ""
    notes: str = ""


class AddContactResponse(BaseModel):
    status: str
    id: int


class UpdateContactRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class StatusOkResponse(BaseModel):
    """Simple status-only ack for CRUD mutations."""

    status: str


# ---------------------------------------------------------------------------
# Templates
# ---------------------------------------------------------------------------


class TemplatesListResponse(BaseModel):
    templates: list[Any]


class TemplateGetResponse(BaseModel):
    model_config = ConfigDict(extra="allow")
    template: Any = None


class SaveTemplateRequest(BaseModel):
    name: str = ""
    rows: list[Any] = []
    id: int | None = None


class SaveTemplateResponse(BaseModel):
    model_config = ConfigDict(extra="allow")
    status: str
    template: Any = None


class DeleteTemplateResponse(BaseModel):
    status: str
    deleted: bool


# ---------------------------------------------------------------------------
# Order operations
# ---------------------------------------------------------------------------


class GetQuoteRequest(BaseModel):
    pickup: str = ""
    destination: str = ""
    delivery_date: str = ""
    weight: float = 0
    pallets: int = 0
    rate_type: str = "Standard"
    flat_amount: float = 0
    temp: str = ""
    fsc_mode: str | None = None
    fsc_inclusive: str | None = None


class QuoteDetail(BaseModel):
    base_rate: float
    fsc: float
    fsc_percent: float
    total: float


class QuoteLookupInfo(BaseModel):
    pickup: str
    destination: str
    region: str
    temp: str
    interline: str


class GetQuoteResponse(BaseModel):
    quote: QuoteDetail
    lookup_info: QuoteLookupInfo


class CreateOrderResponse(BaseModel):
    model_config = ConfigDict(extra="allow")
    status: str = ""


class ImportPoResponse(BaseModel):
    model_config = ConfigDict(extra="allow")
    status: str = ""


class GetOrderResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


class OrdersSearchResponse(BaseModel):
    count: int
    truncated: bool
    orders: list[Any]


class DuplicatePo(BaseModel):
    cae_key: str
    pickup: str = ""
    destination: str = ""
    delivery_date: str = ""
    payor: str = ""
    po_number: str = ""


class CheckDuplicatePoResponse(BaseModel):
    duplicates: list[DuplicatePo]


class DuplicateMatch(BaseModel):
    cae_key: str
    pickup: str = ""
    destination: str = ""
    payor: str = ""
    delivery_date: str = ""
    shipper: str = ""
    po_number: str = ""
    order_number: str = ""
    weight: float = 0
    pallets: int = 0
    pieces: int = 0


class CheckDuplicateOrderResponse(BaseModel):
    matches: list[DuplicateMatch]


class MergeOrderRequest(BaseModel):
    target_cae_key: str = ""
    source_cae_key: str = ""


class MergedOrderDetail(BaseModel):
    weight: float = 0
    pallets: int = 0
    pieces: int = 0
    shipper: str = ""
    po_number: str = ""
    order_number: str = ""


class MergeOrderResponse(BaseModel):
    status: str
    cae_key: str
    source_voided: bool
    order: MergedOrderDetail


class OrdersCountResponse(BaseModel):
    count: int
    orders: list[Any]


class OrdersCountTruncatedResponse(BaseModel):
    count: int
    orders: list[Any]
    truncated: bool


class SearchByPickupRequest(BaseModel):
    pickup: str = ""
    delivery_date: str = ""


class UpdateOrderResponse(BaseModel):
    model_config = ConfigDict(extra="allow")
    status: str = ""


class VoidOrderResponse(BaseModel):
    model_config = ConfigDict(extra="allow")
    status: str = ""


# ---------------------------------------------------------------------------
# Trip stops
# ---------------------------------------------------------------------------


class TripStopRow(BaseModel):
    cae_key: str
    stop_number: str
    pickup: str
    destination: str
    delivery_date: str


class TripStopsResponse(BaseModel):
    trip_number: str
    stops: list[TripStopRow]


# ---------------------------------------------------------------------------
# Reports
# ---------------------------------------------------------------------------


class LastStopDetail(BaseModel):
    stop_number: Any
    customer: str
    city: str
    state: str
    appointment_date: str
    appointment_time: str
    pallets: Any
    weight: Any


class LastStopTrip(BaseModel):
    trip_number: str
    driver: str
    company: str
    truck: str
    total_stops: int
    last_stop: LastStopDetail


class LastStopsResponse(BaseModel):
    ship_date: str
    trip_count: int
    trips: list[LastStopTrip]


class DuplicatesResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


class LogsSearchResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


class ShipperHistoryRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class ShipperHistoryResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


class HistoricalAveragesRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class HistoricalAveragesResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------------


class ToolsFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class ToolsFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


class RateVarianceSummaryResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


class IntegrityCheckResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


class IntegrityPreviewResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


class IntegrityApplyResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Pickup scheduler
# ---------------------------------------------------------------------------


class PickupsByDateRequest(BaseModel):
    delivery_date: str = ""


class PickupsByDateResponse(BaseModel):
    count: int
    pickups: list[Any]


class PickupSchedulerFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class PickupSchedulerFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


class GetActivitiesResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Week overview
# ---------------------------------------------------------------------------


class WeekOverviewRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class WeekOverviewResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Allocations (non-React)
# ---------------------------------------------------------------------------


class AllocAssignRequest(BaseModel):
    cae_key: str = ""
    trip_number: str = ""
    delivery_date: str = ""


class AllocAssignResponse(BaseModel):
    slot: int
    invoice: str


class AllocUnassignRequest(BaseModel):
    cae_key: str = ""


class AllocSuccessResponse(BaseModel):
    success: bool


class AllocReorderRequest(BaseModel):
    trip_number: str = ""
    ordered_cae_keys: list[str] = []


class DriverEmailRequest(BaseModel):
    truck: str = ""


class DriverEmailResponse(BaseModel):
    driver_email: str
    driver_name: str


class SendTripEmailRequest(BaseModel):
    trip_number: str = ""
    delivery_date: str = ""


class SendTripEmailResponse(BaseModel):
    status: str
    mode: str
    message: str
    recipient: str
    subject: str


class AllocFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class AllocFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Trip logger
# ---------------------------------------------------------------------------


class SaveTripRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class SaveTripResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Date anomalies
# ---------------------------------------------------------------------------


class DateAnomaliesResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Manifests
# ---------------------------------------------------------------------------


class ManifestFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class ManifestFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Delivery reports
# ---------------------------------------------------------------------------


class DeliveryReportFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class DeliveryReportFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Dispatch calendar
# ---------------------------------------------------------------------------


class DispatchCalendarFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class DispatchCalendarFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Delivery scheduler
# ---------------------------------------------------------------------------


class DeliverySchedulerFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class DeliverySchedulerFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Appointment tracker
# ---------------------------------------------------------------------------


class RecurringApptResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


class RecurringApptRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class WeeklySummaryRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class WeeklySummaryResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Local HUD
# ---------------------------------------------------------------------------


class HudFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class HudFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Standard appointments
# ---------------------------------------------------------------------------


class StandardApptFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class StandardApptFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Driver delivery summary
# ---------------------------------------------------------------------------


class DriverDeliveryFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class DriverDeliveryFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Pickup lists
# ---------------------------------------------------------------------------


class PickupListFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class PickupListFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


class PickupListMappingResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


class PickupListLogEditResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Weight finalizer + weight sheet
# ---------------------------------------------------------------------------


class WeightFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class WeightFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Pallet weight report / review
# ---------------------------------------------------------------------------


class PalletFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class PalletFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Customer summary report
# ---------------------------------------------------------------------------


class CustomerSummaryRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class CustomerSummaryResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Multi-pick dispatch
# ---------------------------------------------------------------------------


class MultiPickFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class MultiPickFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# BOL
# ---------------------------------------------------------------------------


class BolFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class BolFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Customer prefs
# ---------------------------------------------------------------------------


class CustomerPrefsResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


class CustomerPrefsRequest(BaseModel):
    model_config = ConfigDict(extra="allow")
