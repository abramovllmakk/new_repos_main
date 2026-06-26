from bases.repositories.generic.base_alchemy_generic_repository import (
    BaseAlchemyGenericAsyncRepository,
)
from models.alchemy import Job
from models.dto.job_dto import JobCreateDTO, JobDTO, JobUpdateDTO


class JobRepository(
    BaseAlchemyGenericAsyncRepository[Job, JobDTO, JobCreateDTO, JobUpdateDTO]
):
    """
    Репозиторий для работы с вакансиями
    """

    alchemy_model = Job
    output_model = JobDTO