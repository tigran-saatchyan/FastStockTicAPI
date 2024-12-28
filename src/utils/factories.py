"""Factories for creating FastAPI application instances and setting
up middleware and routes.
"""

from typing import Dict

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from starlette.middleware.cors import CORSMiddleware

from src.api.v1.auth import set_up_auth_routes
from src.settings.config import settings


def create_app() -> FastAPI:
    """Create a FastAPI application instance with configuration settings.

    Returns:
        FastAPI: The FastAPI application instance.
    """
    return FastAPI(**settings.FASTAPI_SETTINGS)


def setup_cors_middleware(application: FastAPI) -> None:
    """Set up Cross-Origin Resource Sharing (CORS) middleware
    for the FastAPI application.

    Args:
        application (FastAPI): The FastAPI application instance.
    """
    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def custom_openapi(application: FastAPI) -> Dict[str, dict]:
    """Customize the OpenAPI schema for the FastAPI application.

    Args:
        application (FastAPI): The FastAPI application instance.

    Returns:
        Dict[str, dict]: The customized OpenAPI schema.
    """
    if application.openapi_schema:
        return application.openapi_schema
    openapi_schema = get_openapi(
        title="UniMart by EvoQ API",
        version="1.0.0",
        description="**UniMart by EvoQ API** is a tool that allows "
        "developers to integrate e-commerce features "
        "like product management, inventory control, "
        "order processing, and customer data management "
        "into their applications or websites, making it "
        "easier to run online stores.",
        routes=application.routes,
        terms_of_service="",
        contact={
            "name": "Tigran Saatchyan (EvoQ) - Backend Developer",
            "url": "https://github.com/tigran-saatchyan",
        },
        license_info={
            "name": "MIT License",
            "url": "https://opensource.org/licenses/MIT",
        },
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    application.openapi_schema = openapi_schema
    return application.openapi_schema


def setup_routes(application: FastAPI) -> None:
    """Set up API routes for the FastAPI application.

    Args:
        application (FastAPI): The FastAPI application instance.
    """
    from src.api.v1.routers import all_routers

    set_up_auth_routes(application)

    for router in all_routers:
        application.include_router(router)
