from ninja import Router

from core.api.v1.customers.handlers import router as customers_router
from core.api.v1.products.handlers import router as products_router


router = Router(tags=["v1"])
router.add_router("/products", products_router)
router.add_router("/customers", customers_router)
