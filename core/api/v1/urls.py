from django.urls import path
from django.http import HttpRequest

from ninja import NinjaAPI

from core.api.v1.schemas import PingResponseSchema

api = NinjaAPI()


@api.get("/ping", response=PingResponseSchema)
def ping(request: HttpRequest) -> PingResponseSchema:
    return PingResponseSchema(result="pong")


urlpatterns = [
    path("", api.urls),
]
