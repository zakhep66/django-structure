import random
from abc import (
    ABC,
    abstractmethod,
)

from django.core.cache import cache

from core.apps.customers.entities import Customer as CustomerEntity
from core.apps.customers.exceptions.codes import (
    CodeNotEqualException,
    CodeNotFoundException,
)


class BaseCodeService(ABC):
    @abstractmethod
    def generate_code(self, customer: CustomerEntity) -> str:
        ...

    @abstractmethod
    def validate_code(self, customer: CustomerEntity, code: str) -> None:
        ...


class DjangoCacheCodeService(BaseCodeService):
    def generate_code(self, customer: CustomerEntity) -> str:
        code = str(random.randint(100000, 999999))  # noqa
        cache.set(customer.phone, code)
        return code

    def validate_code(self, customer: CustomerEntity, code: str) -> None:
        cached_code = cache.get(customer.phone)

        if cached_code is None:
            raise CodeNotFoundException(code=code)

        if cached_code != code:
            raise CodeNotEqualException(code=code, cache_code=cached_code, customer_phone=customer.phone)

        cache.delete(customer.phone)
