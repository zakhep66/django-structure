import pytest

from core.apps.products.services.products import (
    BaseProductsService,
    ORMProductsService,
)


@pytest.fixture
def product_service() -> BaseProductsService:
    return ORMProductsService()
