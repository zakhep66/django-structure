from abc import ABC, abstractmethod
from typing import Iterable

from django.db.models import Q

from core.api.filters import PaginationIn
from core.api.v1.products.filters import ProductFilters
from core.apps.products.entities.products import Product
from core.apps.products.models.products import Product as ProductDTO


class BaseProductsService(ABC):
    @abstractmethod
    def get_product_list(self, filters: ProductFilters, pagination_in: PaginationIn) -> Iterable[Product]:
        ...

    @abstractmethod
    def get_product_count(self, filters: ProductFilters, pagination_in: PaginationIn) -> int:
        ...


# todo закинуть фильтры в сервисный слой, чтобы избежать нарушения D из SOLID
class ORMProductsService(BaseProductsService):
    def _build_product_query(self, filters: ProductFilters) -> Q:
        query = Q(is_visible=True)

        if filters.search is not None:
            query &= (Q(title__icontains=filters.search) | Q(description__icontains=filters.search))

        return query

    def get_product_list(self, filters: ProductFilters, pagination_in: PaginationIn) -> Iterable[Product]:
        query = self._build_product_query(filters)

        qs = ProductDTO.objects.filter(query)[pagination_in.offset:pagination_in.offset + pagination_in.limit]

        return [product.to_entity() for product in qs]

    def get_product_count(self, filters: ProductFilters, pagination_in: PaginationIn) -> int:
        query = self._build_product_query(filters)

        return ProductDTO.objects.filter(query).count()
