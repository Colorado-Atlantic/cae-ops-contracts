"""Pydantic models for GET /api/communications (spec #98 outgoing-communications-log)."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class RelatedTo(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    trip_number: str | None = Field(alias="tripNumber", default=None)
    cae_keys: list[str] = Field(alias="caeKeys", default_factory=list)
    location: str | None = None
    date: str | None = None


class CommunicationEvent(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    sent_at: str | None = Field(alias="sentAt", default=None)
    channel: str
    type: str
    direction: str | None = None
    status: str
    to: str | None = None
    cc: str | None = None
    from_: str | None = Field(alias="from", default=None)
    subject: str | None = None
    message_id: str | None = Field(alias="messageId", default=None)
    error_message: str | None = Field(alias="errorMessage", default=None)
    related_to: RelatedTo = Field(alias="relatedTo", default_factory=RelatedTo)
    sent_by: str | None = Field(alias="sentBy", default=None)
    source: str


class CommunicationsRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    direction: str | None = None
    type: str | None = None
    status: str | None = None
    trip_number: str | None = Field(alias="tripNumber", default=None)
    cae_key: str | None = Field(alias="caeKey", default=None)
    start_date: str | None = Field(alias="startDate", default=None)
    end_date: str | None = Field(alias="endDate", default=None)
    limit: int = 100
    offset: int = 0


class CommunicationsResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    communications: list[CommunicationEvent]
    total: int
    limit: int
    offset: int
