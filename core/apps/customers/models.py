from uuid import uuid4

from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.customers.entities import Customer as CustomerEntity


class Customer(TimedBaseModel):
    phone = models.CharField(max_length=20, verbose_name="Телефонный номер", unique=True)
    token = models.CharField(
        max_length=255,
        verbose_name="Пользовательский токен",
        unique=True,
        default=uuid4,
    )  # noqa

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return str(self.phone)

    def to_entity(self) -> CustomerEntity:
        return CustomerEntity(
            id=self.id,
            phone=self.phone,
            token=self.token,  # noqa
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
