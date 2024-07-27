from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.products.entities.products import Product as ProductEntity


class Product(TimedBaseModel):
    title = models.CharField(
        max_length=255,
        verbose_name="Название товара",
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание",
    )
    price = models.FloatField(
        verbose_name="Цена",
    )
    is_visible = models.BooleanField(
        default=True,
        verbose_name="Видимость в каталоге",
    )

    def to_entity(self) -> ProductEntity:
        return ProductEntity(
            id=self.id,
            title=self.title,
            description=self.description,
            price=self.price,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.title
