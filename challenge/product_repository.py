"""Repository to query Products in postgres db."""

from decimal import Decimal
from uuid import uuid4

from sqlalchemy import select
from sqlalchemy.orm import Session

from challenge import enums
from challenge.config.logger import log
from challenge.db.models import Product
from challenge.schemas import (
    IdResponse,
    ProductSchema,
    ProductsSchema,
)


def create_product(
    product: ProductSchema,
    session: Session
) -> IdResponse:
    """Create a Product Object the db."""
    product = Product(
        id=str(uuid4()),
        name=product.name,
        price=product.price,
        quantity=product.quantity,
        category=product.category,
    )

    session.add(product)
    session.commit()
    session.refresh(product)

    log.info(f"Product stored in database: {product}")

    return IdResponse(id=product.id)


def get_products(
    name: str,
    min_price: Decimal,
    max_price: Decimal,
    category: enums.Category,
    session: Session,
) -> ProductsSchema:
    """Get a list of products."""
    query = session.query(
        Product
    )
    if name:
        query = query.where(Product.name == name)
    if min_price:
        query = query.where(Product.price >= min_price)
    if max_price:
        query = query.where(Product.price <= max_price)
    if category:
        query = query.where(Product.category <= category)
    products = query.all()
    return ProductsSchema(
        products=products,
        total_count=len(products)
    )


def get_product_by_id(
    product_id: str,
    session: Session
) -> ProductSchema:
    """Get a single product by its id."""
    query = select(Product).where(Product.id == product_id)
    product = session.scalar(
        query
    )
    return ProductSchema(
        id=product.id,
        name=product.name,
        price=product.price,
        quantity=product.quantity,
        category=product.category,
    )
