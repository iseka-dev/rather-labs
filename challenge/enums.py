"""Useful project enumerations."""

from enum import Enum


class Category(str, Enum):
    """Categories for products."""

    ELECTRONIC = "Electronic"
    CLOTHING = "Clothing"
    FOOD = "Food"
