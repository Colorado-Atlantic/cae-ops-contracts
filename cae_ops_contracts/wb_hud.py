from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class HudOrderRow(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    cae_key: str = Field(alias="caeKey")
    po_number: str = Field(alias="poNumber")
    pickup: str
    pickup_driver: str = Field(alias="pickupDriver")


class HudOrdersPopoutResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    destination: str
    delivery_date: str = Field(alias="deliveryDate")
    orders: list[HudOrderRow]
