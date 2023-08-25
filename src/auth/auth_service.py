from ..user.user_service import UserService

class Service:
    __userService:UserService

    def __init__(self, service:UserService) -> None:
        self.__userService=service

    