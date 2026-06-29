from bases.services.base_service import BaseService
from models.dto.job_dto import JobCreateDTO, JobDTO
from services.exceptions import ObjectDoesntExistsException
from uows.job_uow import JobUOW


class JobService(BaseService):
    def __init__(self, uow: JobUOW) -> None:
        self.uow = uow

    async def create_job(self, job_create_data: JobCreateDTO) -> JobDTO:
        async with self.uow as uow:
            job = await uow.repository.create(job_create_data)
            await uow.commit()
            return job

    async def get_all_jobs(self, limit: int = 100, skip: int = 0) -> list[JobDTO]:
        """
        pолучить список всех вакансий
        """
        async with self.uow as uow:
            return await uow.repository.list(limit=limit, skip=skip)

    async def get_job_by_id(self, job_id: int) -> JobDTO:
        """
        получить вакансию по идентификатору
        """
        async with self.uow as uow:
            job = await uow.repository.retrieve(id=job_id)
            if job is None:
                raise ObjectDoesntExistsException(
                    f"Вакансия с id={job_id} не найдена"
                )
            return job