from bases.repositories import base_alchemy_repository
from bases.uows import base_alchemy_uow as alchemy_uow
from config import pg_config
from dependency_injector import containers, providers
from repositories.job_repository import JobRepository
from repositories.response_repository import ResponseRepository
from repositories.user_repository import UserRepository
from storage.sqlalchemy import connection_proxy
from tools.factories import alchemy_engine_factory
from uows.job_uow import JobUOW
from uows.response_uow import ResponseUOW
from uows.user_uow import UserUOW

config = pg_config.pg_config


class AlchemySyncContainer(containers.DeclarativeContainer):
    """
    DI-контейнер с провайдерами для работы с БД Postgres через синхронную сессию Алхимии
    """

    wiring_config = containers.WiringConfiguration(modules=None)

    engine_factory = providers.Singleton(
        alchemy_engine_factory.AlchemySyncEngineFactory,
        config.postgres_dsn,
        config.connection_pool_size,
    )
    connection_proxy = providers.Factory(
        connection_proxy.AlchemySyncConnectionProxy, engine_factory
    )
    repository: providers.Provider = providers.Factory(  # type: ignore[type-arg]
        base_alchemy_repository.BaseAlchemySyncRepository, connection_proxy
    )
    uow = providers.Factory(alchemy_uow.BaseAlchemySyncUOW, repository)


class AlchemyAsyncContainer(containers.DeclarativeContainer):
    """
    DI-контейнер с провайдерами для работы с БД Postgres через асинхронную сессию Алхимии
    """

    wiring_config = containers.WiringConfiguration(modules=None)

    engine_factory = providers.Singleton(
        alchemy_engine_factory.AlchemyAsyncEngineFactory,
        config.postgres_async_dsn,
        config.connection_pool_size,
    )
    connection_proxy = providers.Factory(
        connection_proxy.AlchemyAsyncConnectionProxy, engine_factory
    )
    repository: providers.Provider = providers.Factory(  # type: ignore[type-arg]
        base_alchemy_repository.BaseAlchemyAsyncRepository, connection_proxy
    )
    uow = providers.Factory(alchemy_uow.BaseAlchemyAsyncUOW, repository)

    # Репозитории
    user_repo = providers.Factory(UserRepository, connection_proxy)
    job_repo = providers.Factory(JobRepository, connection_proxy)
    response_repo = providers.Factory(ResponseRepository, connection_proxy)

    # UoW
    user_uow = providers.Factory(UserUOW, repository=user_repo)
    job_uow = providers.Factory(JobUOW, repository=job_repo)
    response_uow = providers.Factory(ResponseUOW, repository=response_repo)