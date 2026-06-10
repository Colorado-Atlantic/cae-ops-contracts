from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class ApiKeyItem(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: int
    label: str
    created_by: str = Field(alias="createdBy")
    created_at: str = Field(alias="createdAt")
    last_used_at: str | None = Field(alias="lastUsedAt", default=None)
    active: bool


class ApiKeysListResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    keys: list[ApiKeyItem]


class StatusConfigSection(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    cache_mode: str = Field(alias="cacheMode")
    write_mode: str = Field(alias="writeMode")
    cache_ttl: int = Field(alias="cacheTtl")


class FailedQueueItem(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: int
    operation: str
    sheet_name: str = Field(alias="sheetName")
    attempts: int
    error_message: str = Field(alias="errorMessage")


class PendingQueueItem(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: int
    operation: str
    sheet_name: str = Field(alias="sheetName")
    created_at: str = Field(alias="createdAt")


class StatusPageConfigResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    config: StatusConfigSection
    worker_running: bool = Field(alias="workerRunning")
    queue_enabled: bool = Field(alias="queueEnabled")
    queue_pending: int = Field(alias="queuePending")
    queue_processing: int = Field(alias="queueProcessing")
    queue_synced: int = Field(alias="queueSynced")
    queue_failed: int = Field(alias="queueFailed")
    cache: dict
    api_metrics: dict = Field(alias="apiMetrics")
    failed_items: list[FailedQueueItem] = Field(alias="failedItems")
    pending_items: list[PendingQueueItem] = Field(alias="pendingItems")


class SyncHealthResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    window_days: int = Field(alias="windowDays")
    error_count: int = Field(alias="errorCount")
    last_error_ts: str | None = Field(alias="lastErrorTs", default=None)
    last_error_cae_key: str | None = Field(alias="lastErrorCaeKey", default=None)
    last_error_message: str | None = Field(alias="lastErrorMessage", default=None)


class DriverAssignmentsConfigResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    calendar_id: str = Field(alias="calendarId")
