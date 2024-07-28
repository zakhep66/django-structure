from dataclasses import dataclass


@dataclass
class Customer:
    id: int  # noqa
    phone: str
    token: str
    created_at: str
    updated_at: str
