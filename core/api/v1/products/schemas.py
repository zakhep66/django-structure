from datetime import datetime

from pydantic import BaseModel

from core.apps.products.entities.products import Product as ProductEntity


class ProductSchema(BaseModel):
    id: int  # noqa
    title: str
    description: str
    price: float
    created_at: datetime
    updated_at: datetime | None = None

    @staticmethod
    def from_entity(entity: ProductEntity) -> "ProductSchema":
        return ProductSchema(
            id=entity.id,
            title=entity.title,
            description=entity.description,
            price=entity.price,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )


ProductListSchema = list[ProductSchema]


class ProductInSchema(BaseModel):
    title: str
    description: str
    price: float
