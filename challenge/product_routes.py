"""Test for home route."""

from decimal import Decimal
from sqlite3 import IntegrityError

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from challenge import enums
from challenge.config.logger import log
from challenge.db.database import get_db_session
from challenge.product_service import ProductService
from challenge.schemas import (
    IdResponse,
    ProductRequestSchema,
    ProductSchema,
    ProductsSchema,
)

router = APIRouter()


@router.get("/", tags=["home"])
def home() -> dict:
    """Rather Labs Challenge Home address."""
    return {"Home": "Rather Labs Challenge"}


@router.post(
    "/products/",
    status_code=status.HTTP_201_CREATED,
    response_model=IdResponse,
)
def create(
    data: ProductRequestSchema,
    db_session: Session = Depends(get_db_session),
) -> IdResponse:
    """
    Create and store a Product.

    -------------------
    Product attributes:
    - **category**: should be one of ["Food", "Electronic", "Clothing"].
    - **price**: Is a decimal number.
    - **quantity**: Is an Integer.
    - **name**: Is a string.

    -------------------
    Returns:
    - Dict with key "id"" and value of created Product object
    """
    try:
        return ProductService().create(data, db_session)
    except IntegrityError:
        error = "Products Error: The email address was already taken."
    except Exception as e:
        log.error(f"Error: {e}")
        error = "Products Error: Product was not created, please try again."
    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail={"Error": error},
    )


@router.get(
    "/products/",
    response_model=ProductsSchema,
    status_code=status.HTTP_200_OK
)
def get_products(
    name: str | None = None,
    min_price: Decimal | None = None,
    max_price: Decimal | None = None,
    category: enums.Category | None = None,
    db_session: Session=Depends(get_db_session),
) -> ProductsSchema:
    """
    Get list of products.

    Query parameters:
    -----------------
    - **name**: filter products by its name.
    - **min_price**: set a minimun price threshold to filter products.
    - **max_price**: set a maximum price threshold to filter products.
    - **category**: filter products by its category.
        ["Food", "Electronic", "Clothing"]
    """
    try:
        return ProductService().get_products(
            name,
            min_price,
            max_price,
            category,
            db_session
        )
    except Exception as e:
        log.error(f"Route Error: {e}")
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail={"Error": "Products are not available"},
    )


@router.get(
    "/{product_id}",
    response_model=ProductSchema,
    status_code=status.HTTP_200_OK
)
def get_product(
    product_id: str,
    db_session: Session = Depends(get_db_session)
) -> ProductSchema:
    """Get a signle product by its id."""
    try:
        return ProductService().get_product(
            product_id,
            db_session
        )
    except Exception as e:
        log.error(f"Route Error: {e}")
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail={"Error": "Product was not found. Please try again."},
    )
