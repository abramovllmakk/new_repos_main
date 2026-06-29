from bases.uows.generic_alchemy_uow import AlchemyAsyncGenericUOW
from models.alchemy import User
from models.dto.user_dto import UserCreateDTO, UserDTO, UserUpdateDTO


class UserUOW(AlchemyAsyncGenericUOW[User, UserDTO, UserCreateDTO, UserUpdateDTO]):
    pass