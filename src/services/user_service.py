from bases.services.base_service import BaseService
from models.dto.user_dto import UserCreateDTO, UserDTO
from services.exceptions import ObjectDoesntExistsException
from uows.user_uow import UserUOW


class UserService(BaseService):
    def __init__(self, uow: UserUOW) -> None:
        self.uow = uow
    async def create_user(self, user_create_data: UserCreateDTO) -> UserDTO:
        """
        создание пользователя
        """
        async with self.uow as uow:
            user = await uow.repository.create(user_create_data)
            await uow.commit()
            return user

    async def get_user_by_id(self, user_id: int) -> UserDTO:
        """
        получать пользователя по идентификатору
        """
        async with self.uow as uow:
            user = await uow.repository.retrieve(id=user_id)
            if user is None:
                raise ObjectDoesntExistsException(
                    f"Пользователь с id={user_id} не найден"
                )
            return user