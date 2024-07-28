from abc import (
    ABC,
    abstractmethod,
)

from core.apps.customers.entities import Customer as CustomerEntity


class BaseSenderService(ABC):
    @abstractmethod
    def send_code(self, code: str, customer: CustomerEntity) -> None:
        ...


class DummySenderService(BaseSenderService):
    def send_code(self, code: str, customer: CustomerEntity) -> None:
        print(f'Code to customer: {customer}, sent: {code}')
