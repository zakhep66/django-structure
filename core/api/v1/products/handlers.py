from django.http import HttpRequest
from ninja import (
    Query,
    Router,
)

from core.api.filters import PaginationIn
from core.api.schemas import (
    ApiResponse,
    ListPaginatedResponse,
    PaginationOut,
)
from core.api.v1.products.filters import ProductFilters
from core.api.v1.products.schemas import (
    ProductInSchema,
    ProductSchema,
)
from core.apps.products.services.products import (
    BaseProductsService,
    ORMProductsService,
)


router = Router(tags=["Products"])


@router.get("", response=ApiResponse[ListPaginatedResponse[ProductSchema]])
async def get_product_list_handler(
        request: HttpRequest,
        filters: Query[ProductFilters],
        pagination_in: Query[PaginationIn],
) -> ApiResponse[ListPaginatedResponse[ProductSchema]]:

    service: BaseProductsService = ORMProductsService()
    product_list = await service.get_product_list(filters=filters, pagination_in=pagination_in)
    product_count = await service.get_product_count(filters=filters, pagination_in=pagination_in)
    items = [ProductSchema.from_entity(obj) for obj in product_list]
    pagination_out = PaginationOut(
        offset=pagination_in.offset,
        limit=pagination_in.limit,
        total=product_count,
    )

    return ApiResponse(
        data=ListPaginatedResponse(
            items=items,
            pagination=pagination_out,
        ),
    )


@router.post("add-product", response=ApiResponse[ProductSchema])
async def add_product_handler(request: HttpRequest, product: ProductInSchema) -> ApiResponse[ProductSchema]:
    service: BaseProductsService = ORMProductsService()
    product = await service.add_product(
        title=product.title,
        description=product.description,
        price=product.price,
    )

    return ApiResponse(
        data=ProductSchema.from_entity(product),
    )
