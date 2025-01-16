from enum import Enum

from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel

from typing import Annotated


app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., title="The ID of the item to get", gt=10, le=100),
    item: Item | None,
    user: User | None
):
    results = {"item_id": item_id, "item": item, "user": user}
    return results
