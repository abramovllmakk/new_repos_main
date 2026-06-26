from bases.repositories.generic.base_alchemy_generic_repository import (
    BaseAlchemyGenericAsyncRepository,
)
from models.alchemy import Response
from models.dto.response_dto import ResponseCreateDTO, ResponseDTO


class ResponseRepository(
    BaseAlchemyGenericAsyncRepository[Response, ResponseDTO, ResponseCreateDTO, ResponseDTO]
):
    """
    Репозиторий для работы с откликами на вакансии
    """

    alchemy_model = Response
    output_model = ResponseDTO