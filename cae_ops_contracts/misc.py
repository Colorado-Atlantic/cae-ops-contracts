"""Pydantic models for weather, tools, admin, main blueprints — spec #66 ticket #988."""
from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class WeatherFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


class ToolsFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class ToolsFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


class AdminFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class AdminFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


class AdminDriverAssignmentsFlexRequest(BaseModel):
    model_config = ConfigDict(extra="allow")


class AdminDriverAssignmentsFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


class MainFlexResponse(BaseModel):
    model_config = ConfigDict(extra="allow")
