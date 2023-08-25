from typing import Any
from sqlalchemy.orm import Session
from flask import Flask, Blueprint
from .user_controller import controller
from .user_service import UserService

class User:

    __bp:Blueprint = Blueprint("user", __name__,url_prefix="/user")
    __userService:UserService

    def __init__(self, app:Flask, session:Session) -> None:
        self.__userService = UserService(session)
        self.__routes();
        app.register_blueprint(self.__bp)

    def __routes(self):
        controller(self.__bp,self.__userService)

    def getService(self) -> UserService:
        return self.__userService