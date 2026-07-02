from dependency_injector import containers, providers

from services.job_service import JobService
from services.user_service import UserService
from services.response_service import ResponseService
from tools.di_containers.alchemy_container import AlchemyAsyncContainer


class ServiceContainer(containers.DeclarativeContainer):
    """
    DI-контейнер с провайдерами для работы с сервисами
    """

    wiring_config = containers.WiringConfiguration(packages=["web"])

    alchemy_container = providers.Container(AlchemyAsyncContainer)

    user_service = providers.Factory(
        UserService,
        uow=alchemy_container.user_uow,
    )
    job_service = providers.Factory(
        JobService,
        uow=alchemy_container.job_uow,
    )
    response_service = providers.Factory(
        ResponseService,
        uow=alchemy_container.response_uow,
    )