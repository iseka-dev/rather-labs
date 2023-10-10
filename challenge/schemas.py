"""Product Schemas."""

from collections.abc import Sequence
from decimal import Decimal
from uuid import UUID

from pydantic import (
    BaseModel,
    ConfigDict,
)

from challenge import enums


class ProductSchema(BaseModel):
    """Base Schema Class for Products."""

    id: UUID
    name: str
    price: Decimal
    quantity: int
    category: enums.Category

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "examples": [
                {
                    "name": "coca-cola",
                    "price": 10.50,
                    "quantity": 1,
                    "category": enums.Category.FOOD
                }
            ]
        }
    )


class ProductRequestSchema(BaseModel):
    """Base Schema Class to be used with Product Requests."""

    name: str
    price: Decimal
    quantity: int
    category: enums.Category

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "name": "coca-cola",
                    "price": 10.50,
                    "quantity": 1,
                    "category": enums.Category.FOOD
                }
            ]
        }
    )

class ProductsSchema(BaseModel):
    """Schema with a list of Products and a counter for them."""

    products: Sequence[ProductSchema]
    total_count: int

class IdResponse(BaseModel):
    """Schema class with and ID only, to be used in responses."""

    id: UUID

    model_config = ConfigDict(from_attributes=True)
