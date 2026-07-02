from http import HTTPStatus

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from models.dto.job_dto import JobCreateDTO
from services.job_service import JobService
from tools.di_containers.service_container import ServiceContainer
from web.schemas.job_schemas import Job, JobCreate

router = APIRouter(tags=["jobs"])
@router.post(
    "",
    response_model=Job,
    status_code=HTTPStatus.CREATED,
)
@inject
async def create_job(
    job_create_data: JobCreate,
    job_service: JobService = Depends(Provide[ServiceContainer.job_service]),
) -> Job:
    job_create_dto = JobCreateDTO(**job_create_data.model_dump())
    created_job = await job_service.create_job(job_create_dto)
    return Job.model_validate(created_job)
@router.get(
    "",
    response_model=list[Job],
    status_code=HTTPStatus.OK,
)
@inject
async def get_all_jobs(
    limit: int = 100,
    skip: int = 0,
    job_service: JobService = Depends(Provide[ServiceContainer.job_service]),
) -> list[Job]:
    jobs = await job_service.get_all_jobs(limit=limit, skip=skip)
    return [Job.model_validate(job) for job in jobs]
@router.get(
    "/{job_id}",
    response_model=Job,
    status_code=HTTPStatus.OK,
)
@inject
async def get_job_by_id(
    job_id: int,
    job_service: JobService = Depends(Provide[ServiceContainer.job_service]),
) -> Job:
    job = await job_service.get_job_by_id(job_id)
    return Job.model_validate(job)