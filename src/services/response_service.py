from bases.services.base_service import BaseService
from models.dto.response_dto import ResponseCreateDTO, ResponseDTO
from services.exceptions import NoPermissionException, ObjectDoesntExistsException
from uows.job_uow import JobUOW
from uows.response_uow import ResponseUOW
from uows.user_uow import UserUOW


class ResponseService(BaseService):
    """
    Сервис для работы с откликами на вакансии
    """

    def __init__(self, uow: ResponseUOW, user_uow: UserUOW, job_uow: JobUOW) -> None:
        """
        Инициализировать сервис
        """
        self.uow = uow
        self.user_uow = user_uow
        self.job_uow = job_uow

    async def create_response(
        self,
        response_create_data: ResponseCreateDTO,
    ) -> ResponseDTO:
        """
        Выполнить логику создания отклика
        """
        # Проверяем что пользователь существует и не является компанией
        async with self.user_uow as user_uow:
            user = await user_uow.repository.retrieve(id=response_create_data.user_id)
            if user is None:
                raise ObjectDoesntExistsException(
                    f"Пользователь с id={response_create_data.user_id} не найден"
                )
            if user.is_company:
                raise NoPermissionException(
                    "Компании не могут откликаться на вакансии"
                )

        # Проверяем что вакансия существует
        async with self.job_uow as job_uow:
            job = await job_uow.repository.retrieve(id=response_create_data.job_id)
            if job is None:
                raise ObjectDoesntExistsException(
                    f"Вакансия с id={response_create_data.job_id} не найдена"
                )

        # Создаём отклик
        async with self.uow as uow:
            response = await uow.repository.create(response_create_data)
            await uow.commit()
            return response

    async def get_responses_by_job_id(
        self,
        job_id: int,
    ) -> list[ResponseDTO]:
        """
        Получить все отклики на вакансию
        """
        async with self.uow as uow:
            return await uow.repository.list(job_id=job_id)