from datetime import datetime

from pydantic import BaseModel


class ProductSchema(BaseModel):
    title: str
    description: str
    price: float
    created_at: datetime
    updated_at: datetime | None = None


ProductListSchema = list[ProductSchema]
