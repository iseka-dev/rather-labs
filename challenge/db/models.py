"""This module has the product model for the project."""

from datetime import datetime
from uuid import uuid4

from sqlalchemy import TIMESTAMP, Enum, Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from challenge.db.database import Base
from challenge.enums import Category


class Product(Base):
    """Products Base Class."""

    __tablename__ = "products"

    id: Mapped[str] = mapped_column(
        Text, # UUID field not supported by SQLite
        primary_key=True,
        index=True,
        nullable=False,
        default=uuid4,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    price: Mapped[float] = mapped_column(
        Numeric(
            scale=2,
            decimal_return_scale=2,
        ),
        nullable=False
    )
    quantity: Mapped[str] = mapped_column(
        Integer(),
        nullable=False,
    )
    category: Mapped[str] = mapped_column(
        Enum(Category),
        nullable=False,
    )

    created_datetime: Mapped[str] = mapped_column(
        TIMESTAMP,
        default=datetime.utcnow,
    )
    last_update_datetime: Mapped[str] = mapped_column(
        TIMESTAMP,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    removed_datetime: Mapped[str] = mapped_column(
        TIMESTAMP,
        nullable=True,
        default=None
    )
