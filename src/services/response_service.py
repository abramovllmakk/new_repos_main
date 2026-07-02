from bases.services.base_service import BaseService
from models.dto.response_dto import ResponseCreateDTO, ResponseDTO
from services.exceptions import ObjectDoesntExistsException
from uows.response_uow import ResponseUOW


class ResponseService(BaseService):
    def __init__(self, uow: ResponseUOW) -> None:
        self.uow = uow

    async def create_response(
        self,
        response_create_data: ResponseCreateDTO,
    ) -> ResponseDTO:
        """
         логика создания отклика
        """
        async with self.uow as uow:
            response = await uow.repository.create(response_create_data) 
            await uow.commit()
            return response

    async def get_responses_by_job_id(
        self,
        job_id: int,
    ) -> list[ResponseDTO]:
        """
        плучить все отклики на вакансию
        """
        async with self.uow as uow:
            return await uow.repository.list(job_id=job_id)  