from abc import (
    ABC,
    abstractmethod,
)
from uuid import uuid4

from core.apps.customers.entities import Customer as CustomerEntity
from core.apps.customers.models import Customer as CustomerDTO


class BaseCustomerService(ABC):

    @abstractmethod
    def get(self, phone: str) -> CustomerEntity:
        ...

    @abstractmethod
    def get_or_create(self, phone: str) -> CustomerEntity:
        ...

    @abstractmethod
    def generate_token(self, customer: CustomerEntity) -> str:
        ...


class ORMCustomerService(BaseCustomerService):

    def get(self, phone: str) -> CustomerEntity:
        customer_dto = CustomerDTO.objects.get(phone=phone)

        return customer_dto.to_entity()

    def get_or_create(self, phone: str) -> CustomerEntity:
        customer_dto, _ = CustomerDTO.objects.get_or_create(
            phone=phone,
        )

        return customer_dto.to_entity()

    def generate_token(self, customer: CustomerEntity) -> str:
        new_token = str(uuid4())
        CustomerDTO.objects.filter(phone=customer.phone).update(
            token=new_token,
        )

        return new_token
