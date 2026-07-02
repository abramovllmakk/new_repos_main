from decimal import Decimal
from typing import Optional
import datetime

from bases.base_web_schema import BaseWebSchema, ConfigMixin


class JobCreate(ConfigMixin, BaseWebSchema):
    """
    Схема для создания вакансии
    """
    user_id: int
    title: str
    description: str
    salary_from: Optional[Decimal] = None
    salary_to: Optional[Decimal] = None
    is_active: bool = True


class Job(ConfigMixin, BaseWebSchema):
    """
    Схема для отображения вакансии
    """
    id: int
    user_id: int
    title: str
    description: str
    salary_from: Optional[Decimal] = None
    salary_to: Optional[Decimal] = None
    is_active: bool
    created_at: datetime.datetime