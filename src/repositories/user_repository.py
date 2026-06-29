from bases.repositories.generic.base_alchemy_generic_repository import (
    BaseAlchemyGenericAsyncRepository,
)
from models.alchemy import User
from models.dto.user_dto import UserCreateDTO, UserDTO, UserUpdateDTO


class UserRepository(
    BaseAlchemyGenericAsyncRepository[User, UserDTO, UserCreateDTO, UserUpdateDTO]
):
    """
    Репозиторий для работы с пользователями
    """

    alchemy_model = User
    output_model = UserDTO