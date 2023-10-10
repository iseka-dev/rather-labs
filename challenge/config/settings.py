"""
This module has the main settings for a FastApi project.

Classes
-------
- Settings: Has the necessary settings for the project
"""

import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    This class has most settings var for the project.

    Vars are loadeds from an .env file.
    """

    load_dotenv()

    # Database
    SQLITE_URL: str = os.getenv(
        "SQLITE_URL", ""
    )

    # Pagination
    PAGE_LIMIT: str = os.getenv(
        "PAGE_LIMIT", "100"
    )

settings = Settings()
