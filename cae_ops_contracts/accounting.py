"""Pydantic models for /accounting/api/* and /api/trips/* endpoints — spec #66 ticket #987.

jinja-served-json routes use ConfigDict(extra='allow') flex pairs.
"""
from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class AccFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class AccFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Settlements
# ---------------------------------------------------------------------------

class AccSettlementsFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class AccSettlementsFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Trip summary
# ---------------------------------------------------------------------------

class AccTripSummaryFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Review
# ---------------------------------------------------------------------------

class AccReviewFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class AccReviewFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Evidence
# ---------------------------------------------------------------------------

class AccEvidenceFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class AccEvidenceFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Accessorials
# ---------------------------------------------------------------------------

class AccAccessorialsFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class AccAccessorialsFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# FSC review
# ---------------------------------------------------------------------------

class AccFscFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Payor rates
# ---------------------------------------------------------------------------

class AccPayorRatesFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class AccPayorRatesFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# QBO
# ---------------------------------------------------------------------------

class AccQboStatusResponse(BaseModel):
    connected: bool
    company: str | None = None


class AccQboFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class AccQboFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# PO reconciliation
# ---------------------------------------------------------------------------

class AccPoReconciliationFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Lumper split
# ---------------------------------------------------------------------------

class AccLumperFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class AccLumperFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Sorting seg
# ---------------------------------------------------------------------------

class AccSortingSegFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class AccSortingSegFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Raw data
# ---------------------------------------------------------------------------

class AccRawDataFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Trips
# ---------------------------------------------------------------------------

class TripsFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class TripsFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


# ---------------------------------------------------------------------------
# Accessorial fee type registry (spec #95)
# ---------------------------------------------------------------------------

class AccFeeTypesFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class AccFeeTypesFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")
