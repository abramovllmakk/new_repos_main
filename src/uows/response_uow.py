from bases.uows.generic_alchemy_uow import AlchemyAsyncGenericUOW
from models.alchemy import Response
from models.dto.response_dto import ResponseCreateDTO, ResponseDTO


class ResponseUOW(AlchemyAsyncGenericUOW[Response, ResponseDTO, ResponseCreateDTO, ResponseDTO]):
    pass