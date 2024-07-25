from django.db import models

from core.apps.common.models import TimedBaseModel


class Product(TimedBaseModel):
    title = models.CharField(
        max_length=255,
        verbose_name="Название товара",
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание"
    )
    price = models.FloatField(
        verbose_name="Цена"
    )
    is_visible = models.BooleanField(
        default=True,
        verbose_name="Видимость в каталоге",
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.title
