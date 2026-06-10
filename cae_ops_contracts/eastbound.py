"""Pydantic models for /eastbound/api/* endpoints — spec #66 ticket #986.

Non-React routes use snake_case keys (no Field aliases).
Complex / dynamic-shape responses use ConfigDict(extra='allow').
Simple well-known shapes use tight field declarations.
"""
from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict

# ---------------------------------------------------------------------------
# Common flex pair used by most complex EB endpoints
# ---------------------------------------------------------------------------

class EbFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class EbFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Simple status / ack
# ---------------------------------------------------------------------------

class EbStatusResponse(BaseModel):
    status: str
    debug_mode: bool
    source: str


class EbAckResponse(BaseModel):
    status: str


# ---------------------------------------------------------------------------
# Reference data
# ---------------------------------------------------------------------------

class EbPickupRow(BaseModel):
    name: str
    region: str = ""
    temp: str = "C"
    address: str = ""


class EbPickupsResponse(BaseModel):
    pickups: list[EbPickupRow]


class EbDestinationRow(BaseModel):
    name: str
    region: str = ""
    interline: str = ""
    address: str = ""


class EbDestinationsResponse(BaseModel):
    destinations: list[EbDestinationRow]


class EbTrucksResponse(BaseModel):
    model_config = ConfigDict(extra="allow")
    trucks: list[Any]


class EbLookupBillingRegionResponse(BaseModel):
    billing_region: str
    zip: str


class EbGenerateLocationIdResponse(BaseModel):
    location_id: str


# ---------------------------------------------------------------------------
# Trips / stops
# ---------------------------------------------------------------------------

class EbTripStopRow(BaseModel):
    cae_key: str
    stop_number: str
    pickup: str
    destination: str
    delivery_date: str


class EbTripStopsResponse(BaseModel):
    trip_number: str
    stops: list[EbTripStopRow]


# ---------------------------------------------------------------------------
# Order operations
# ---------------------------------------------------------------------------

class EbCreateOrderResponse(BaseModel):
    model_config = ConfigDict(extra="allow")
    status: str = ""


class EbGetOrderResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


class EbUpdateOrderResponse(BaseModel):
    model_config = ConfigDict(extra="allow")
    status: str = ""


class EbVoidOrderResponse(BaseModel):
    model_config = ConfigDict(extra="allow")
    status: str = ""


class EbMergeOrderResponse(BaseModel):
    model_config = ConfigDict(extra="allow")
    status: str = ""


class EbCheckDuplicateOrderResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


class EbSearchOrdersResponse(BaseModel):
    count: int
    orders: list[Any]
    truncated: bool = False


class EbGetQuoteResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


class EbOrdersListResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Allocation (non-React EB)
# ---------------------------------------------------------------------------

class EbAllocAssignResponse(BaseModel):
    slot: int
    invoice: str


class EbAllocSuccessResponse(BaseModel):
    success: bool


class EbAllocFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class EbAllocFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Locations
# ---------------------------------------------------------------------------

class EbLocationsResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


class EbLocationMutationResponse(BaseModel):
    model_config = ConfigDict(extra="allow")
    status: str = ""


class EbSetActiveResponse(BaseModel):
    updated: int
    active: bool


# ---------------------------------------------------------------------------
# Delivery scheduler
# ---------------------------------------------------------------------------

class EbDeliverySchedulerFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class EbDeliverySchedulerFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Delivery logger
# ---------------------------------------------------------------------------

class EbDeliveryLoggerFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class EbDeliveryLoggerFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Dock operations
# ---------------------------------------------------------------------------

class EbDockFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class EbDockFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Manifests
# ---------------------------------------------------------------------------

class EbManifestFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class EbManifestFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# LTL pickups
# ---------------------------------------------------------------------------

class EbLtlFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class EbLtlFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Pickup scheduler
# ---------------------------------------------------------------------------

class EbPickupSchedulerFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class EbPickupSchedulerFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Pickup lists
# ---------------------------------------------------------------------------

class EbPickupListFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class EbPickupListFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Pickup calendar / planning
# ---------------------------------------------------------------------------

class EbPickupCalendarFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class EbPickupCalendarFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Planner (consolidation planner)
# ---------------------------------------------------------------------------

class EbPlannerFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class EbPlannerFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Billing review
# ---------------------------------------------------------------------------

class EbBillingReviewFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class EbBillingReviewFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# BOL
# ---------------------------------------------------------------------------

class EbBolFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class EbBolFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Reports
# ---------------------------------------------------------------------------

class EbReportsFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class EbReportsFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Address aliases
# ---------------------------------------------------------------------------

class EbAddressAliasFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class EbAddressAliasFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Driver email aliases
# ---------------------------------------------------------------------------

class EbDriverAliasFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class EbDriverAliasFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Interline
# ---------------------------------------------------------------------------

class EbInterlineFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class EbInterlineFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Driver pickup summary
# ---------------------------------------------------------------------------

class EbDriverPickupSummaryFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class EbDriverPickupSummaryFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Available drivers
# ---------------------------------------------------------------------------

class EbAvailableDriversFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class EbAvailableDriversFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Cover sheets
# ---------------------------------------------------------------------------

class EbCoverSheetsFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class EbCoverSheetsFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Lumper
# ---------------------------------------------------------------------------

class EbLumperFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class EbLumperFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Order entry reference data
# ---------------------------------------------------------------------------

class EbOrderEntryFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Historical averages
# ---------------------------------------------------------------------------

class EbHistoricalAveragesFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class EbHistoricalAveragesFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Delivery details / calendar
# ---------------------------------------------------------------------------

class EbDeliveryDetailsFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class EbDeliveryDetailsFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Delivery calendar
# ---------------------------------------------------------------------------

class EbDeliveryCalendarFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class EbDeliveryCalendarFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Duplicate order report
# ---------------------------------------------------------------------------

class EbDuplicateOrderReportResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Assignments history (EB-specific assignments)
# ---------------------------------------------------------------------------

class EbAssignmentsFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class EbAssignmentsFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Refresh
# ---------------------------------------------------------------------------

class EbRefreshResponse(BaseModel):
    model_config = ConfigDict(extra="allow")
    status: str = ""


# ---------------------------------------------------------------------------
# Dispatch latest date
# ---------------------------------------------------------------------------

class EbLatestDateResponse(BaseModel):
    latestDate: str
