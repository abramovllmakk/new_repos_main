from fastapi import FastAPI

from config import app_config as app_config_module
from web.entrypoints import index_entrypoint
from web.entrypoints import jobs_entrypoint

_config = app_config_module.app_config


def register_routers(app: FastAPI) -> None:
    """
    Зарегистрировать роутеры
    :param app: приложение FastAPI
    """
    app.include_router(
        index_entrypoint.router,
        prefix=f"/api/{_config.app_version}",
    )
    app.include_router(
        jobs_entrypoint.router,
        prefix=f"/api/{_config.app_version}/jobs",
    )