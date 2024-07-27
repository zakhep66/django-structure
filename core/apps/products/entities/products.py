from dataclasses import dataclass


@dataclass
class Product:
    id: int  # noqa
    title: str
    description: str
    price: float
    created_at: str
    updated_at: str
