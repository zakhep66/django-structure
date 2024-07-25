from django.urls import path
from django.http import HttpRequest

from ninja import NinjaAPI

from core.api.schemas import PingResponseSchema
from core.api.v1.urls import router as v1_router

api = NinjaAPI()


@api.get("/ping", response=PingResponseSchema)
def ping(request: HttpRequest) -> PingResponseSchema:
    return PingResponseSchema(result="pong")


api.add_router("/v1", v1_router)

urlpatterns = [
    path("", api.urls),
]
