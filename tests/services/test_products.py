"""
1. Тест на проверку количества продуктов: продуктов ноль, больше одного
2. Тест на проверку возврата продуктов всех и по пагинации
"""

import pytest
from tests.factories.products import ProductModelFactory

from core.api.filters import PaginationIn
from core.api.v1.products.filters import ProductFilters
from core.apps.products.services.products import BaseProductsService


@pytest.mark.django_db
def test_get_products_count_zero(product_service: BaseProductsService):
    """Тест на проверку количества продуктов в базе данных."""
    product_count = product_service.get_product_count(ProductFilters(), PaginationIn())

    assert product_count == 0, f"{product_count=}"


@pytest.mark.django_db
def test_get_products_count_exist(product_service: BaseProductsService):
    """Тест на проверку количества продуктов в базе данных."""
    expected_count = 5
    ProductModelFactory.create_batch(size=expected_count)

    product_count = product_service.get_product_count(ProductFilters(), PaginationIn())
    assert product_count == expected_count, f"{product_count=}"


@pytest.mark.django_db
def test_get_products_all(product_service: BaseProductsService):
    """Тест на проверку возврата продуктов всех и по пагинации."""
    expected_count = 5
    products = ProductModelFactory.create_batch(size=expected_count)
    product_titles = {product.title for product in products}

    fetched_products = product_service.get_product_list(ProductFilters(), PaginationIn())
    fetched_product_titles = {product.title for product in fetched_products}

    assert len(product_titles) == len(fetched_product_titles), f"{product_titles=} != {fetched_product_titles=}"
    assert product_titles == fetched_product_titles
