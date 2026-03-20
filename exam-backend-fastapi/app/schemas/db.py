from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel


class FilterItem(BaseModel):
    op: Literal["eq", "in", "not"]
    column: str
    value: Any = None
    operator: str | None = None


class QueryOrder(BaseModel):
    column: str
    ascending: bool = True


class DBQueryIn(BaseModel):
    table: str
    select: str = "*"
    filters: list[FilterItem] = []
    order: QueryOrder | None = None
    limit: int | None = None
    count: str | None = None
    head: bool = False
    single: bool = False
    maybe_single: bool = False


class DBInsertIn(BaseModel):
    table: str
    data: dict[str, Any] | list[dict[str, Any]]


class DBUpdateIn(BaseModel):
    table: str
    data: dict[str, Any]
    filters: list[FilterItem] = []


class DBDeleteIn(BaseModel):
    table: str
    filters: list[FilterItem] = []
