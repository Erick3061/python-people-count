from flask import Flask, Blueprint

from ..user.user_service import UserService
from .auth_controller import controller
from .auth_service import Service

class Auth:

    __bp:Blueprint = Blueprint("auth", __name__, url_prefix="/auth", template_folder="pages")
    __service:Service

    def __init__(self, app:Flask,userService:UserService) -> None:
        self.__service = Service(userService)
        self.__routes();
        app.register_blueprint(self.__bp)

    def __routes(self):
        controller(self.__bp,self.__service)