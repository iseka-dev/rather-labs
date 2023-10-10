"""agenda App."""

from fastapi import FastAPI

from challenge.db.database import db_init
from challenge.product_routes import router

app = FastAPI()

app.include_router(router)


@app.on_event("startup")
def startup() -> None:
    """Execute at server startup."""
    db_init()
