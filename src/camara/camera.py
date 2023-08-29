from flask import Flask, Blueprint
from sqlalchemy.orm import Session
from .camera_controller import controller
from .camera_service import CameraService

class Camera:

    __bp:Blueprint = Blueprint("camera", __name__, url_prefix="/camera", template_folder="pages")
    __service:CameraService

    def __init__(self, app:Flask,session:Session) -> None:
        self.__service = CameraService(session)
        self.__routes()
        app.register_blueprint(self.__bp)

    def __routes(self):
        controller(self.__bp,self.__service)