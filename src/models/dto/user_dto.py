import datetime
from typing import Optional

from bases.base_dto import BaseDTO


class UserCreateDTO(BaseDTO):


    email: str
    name: str
    hashed_password: str
    is_company: bool = False


class UserDTO(BaseDTO):

    id: int
    email: str
    name: str
    hashed_password: str
    is_company: bool
    created_at: datetime.datetime


class UserUpdateDTO(BaseDTO):

    email: Optional[str] = None
    name: Optional[str] = None
    hashed_password: Optional[str] = None
    is_company: Optional[bool] = None