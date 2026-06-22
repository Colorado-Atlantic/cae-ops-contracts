"""Pydantic models for GET /api/trips/<trip_id>/change-log.

Spec: dispatch-change-log (imperator-luci FORTIFY, decision_log id=112).
Audit trail of changes to a trip's orders AFTER the first driver dispatch was
sent. Wire keys are camelCase (per CONVENTIONS.md); Python attrs stay snake_case
via Field aliases, the same pattern as `communications.py`.

The response shape is load-bearing — the trip drawer's "Change Log" section and
the `dispatch_change_log` read projection are both built against it. The C5
discriminator lives in the shape: `firstDispatchSentAt: null` (never sent /
anchor unresolved) is distinct from `changes: []` (sent, no post-dispatch change),
and `implemented` distinguishes "backend not built" from both.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class ChangeLogEntry(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    cae_key: str = Field(alias="caeKey")
    # one of: field_update | appt_changed | order_added | order_removed | reallocated
    change_type: str = Field(alias="changeType")
    field: str | None = None                                  # null for add/remove
    old_value: str | None = Field(alias="oldValue", default=None)
    new_value: str | None = Field(alias="newValue", default=None)
    from_trip_id: int | None = Field(alias="fromTripId", default=None)   # reallocated only
    to_trip_id: int | None = Field(alias="toTripId", default=None)       # reallocated only
    # pickup_scheduler | trip_logger | allocation | order_updater
    source: str
    changed_by: str | None = Field(alias="changedBy", default=None)
    changed_at: str = Field(alias="changedAt")                # ISO-8601


class ChangeLogResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    implemented: bool
    trip_id: int = Field(alias="tripId")
    trip_number: str | None = Field(alias="tripNumber", default=None)   # display only
    # null = never sent / anchor unresolved (C5 discriminator — distinct from changes:[])
    first_dispatch_sent_at: str | None = Field(alias="firstDispatchSentAt", default=None)
    changes: list[ChangeLogEntry] = Field(default_factory=list)
