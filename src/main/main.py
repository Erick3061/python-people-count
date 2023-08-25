from flask import Blueprint, Flask
from .main_controller import controller
from os import pardir, path

class Main():
    __bp:Blueprint = Blueprint('main', __name__) 

    def __init__(self,app:Flask) -> None:
        self.__routes()
        app.register_blueprint(self.__bp)

    def __routes(self):
        controller(self.__bp)