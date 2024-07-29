from abc import (
    ABC,
    abstractmethod,
)
from typing import Iterable

from django.db.models import Q

from asgiref.sync import sync_to_async

from core.api.filters import PaginationIn
from core.api.v1.products.filters import ProductFilters
from core.apps.products.entities.products import Product as ProductEntity
from core.apps.products.models.products import Product as ProductDTO


class BaseProductsService(ABC):
    @abstractmethod
    async def get_product_list(self, filters: ProductFilters, pagination_in: PaginationIn) -> Iterable[ProductEntity]:
        ...

    @abstractmethod
    async def get_product_count(self, filters: ProductFilters, pagination_in: PaginationIn) -> int:
        ...

    @abstractmethod
    async def add_product(self, title: str, description: str, price: float) -> ProductEntity:
        ...


# todo закинуть фильтры в сервисный слой, чтобы избежать нарушения D из SOLID
class ORMProductsService(BaseProductsService):
    def _build_product_query(self, filters: ProductFilters) -> Q:
        query = Q(is_visible=True)

        if filters.search is not None:
            query &= (Q(title__icontains=filters.search) | Q(description__icontains=filters.search))

        return query

    async def get_product_list(self, filters: ProductFilters, pagination_in: PaginationIn) -> Iterable[ProductEntity]:
        query = self._build_product_query(filters)

        qs = await sync_to_async(
            ProductDTO.objects.filter(query)[pagination_in.offset:pagination_in.offset + pagination_in.limit],
            thread_sensitive=True,
        )()

        return [product.to_entity() for product in qs]

    async def get_product_count(self, filters: ProductFilters, pagination_in: PaginationIn) -> int:
        query = self._build_product_query(filters)

        return await ProductDTO.objects.filter(query).acount()

    async def add_product(self, title: str, description: str, price: float) -> ProductEntity:
        new_product = await ProductDTO.objects.acreate(
            title=title,
            description=description,
            price=price,
        )

        return new_product.to_entity()
