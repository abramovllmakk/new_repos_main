from bases.uows.generic_alchemy_uow import AlchemyAsyncGenericUOW
from models.alchemy import Job
from models.dto.job_dto import JobCreateDTO, JobDTO, JobUpdateDTO


class JobUOW(AlchemyAsyncGenericUOW[Job, JobDTO, JobCreateDTO, JobUpdateDTO]):
    pass