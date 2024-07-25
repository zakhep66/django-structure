from dataclasses import dataclass


@dataclass
class Product:
    id: int
    title: str
    description: str
    price: float
    created_at: str
    updated_at: str
