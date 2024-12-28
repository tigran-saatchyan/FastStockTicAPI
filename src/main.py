"""Main module for the application."""

import uvicorn

from src.utils.factories import (
    create_app,
    setup_cors_middleware,
    custom_openapi, setup_routes,
)

app = create_app()

setup_cors_middleware(app)
setup_routes(app)

custom_openapi(app)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
