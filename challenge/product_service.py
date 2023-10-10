"""Module with User service."""

from decimal import Decimal
from uuid import UUID, uuid4

from sqlalchemy.orm import Session

from challenge import enums
from challenge.product_repository import (
    create_product,
    get_product_by_id,
    get_products,
)
from challenge.schemas import (
    IdResponse,
    ProductRequestSchema,
    ProductSchema,
    ProductsSchema,
)


class ProductService:
    """Service class for users features."""

    def create(
        self, data: ProductRequestSchema, session: Session
    ) -> IdResponse:
        """Create method for users."""
        product = data.model_dump()
        product["id"] = uuid4()
        product["owner_id"] = UUID("fbe890fa-d56c-4e3c-825a-6651c38d42c4")
        product = ProductSchema(**product)
        return create_product(product, session)

    def get_products(  # noqa: PLR0913
        self,
        name: str,
        min_price: Decimal,
        max_price: Decimal,
        category: enums.Category,
        db_session: Session,
    ) -> ProductsSchema:
        """Get list of Products."""
        return get_products(
            name,
            min_price,
            max_price,
            category,
            db_session,
        )

    def get_product(
        self, product_id: str, session: Session
    ) -> ProductSchema:
        """Get a single Product, looging by id."""
        return get_product_by_id(
            product_id, session
        )
