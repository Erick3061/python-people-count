from flask import Flask, Blueprint
from sqlalchemy.orm import Session
from .contact_controller import controller
from .contact_service import ContactService

class Contact:

    __bp:Blueprint = Blueprint("contact", __name__, url_prefix="/contact", template_folder="pages")
    __service:ContactService

    def __init__(self, app:Flask,session:Session) -> None:
        self.__service = ContactService(session)
        self.__routes()
        app.register_blueprint(self.__bp)

    def __routes(self):
        controller(self.__bp,self.__service)