from typing import Any, Generic, TypeVar

from ninja import Schema, Field


TData = TypeVar("TData")
TListItem = TypeVar("TListItem")


class PingResponseSchema(Schema):
    result: str


class PaginationOut(Schema):
    offset: int
    limit: int
    total: int


class ListPaginatedResponse(Schema, Generic[TListItem]):
    items: list[TListItem]
    pagination: PaginationOut


class ApiResponse(Schema, Generic[TData]):
    data: TData | dict = Field(default_factory=dict)
    meta: dict[str, Any] = Field(default_factory=dict)
    errors: list[Any] = Field(default_factory=list)
