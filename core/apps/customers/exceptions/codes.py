from dataclasses import dataclass

from core.apps.common.exceptions import ServiceException


@dataclass
class CodeException(ServiceException):
    @property
    def message(self) -> str:
        return 'Auth code exception occurred'


@dataclass
class CodeNotFoundException(CodeException):
    code: str

    @property
    def message(self) -> str:
        return 'Code not found'


@dataclass
class CodeNotEqualException(CodeException):
    code: str
    cache_code: str
    customer_phone: str

    @property
    def message(self) -> str:
        return 'Code not equal'
