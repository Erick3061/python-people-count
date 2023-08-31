from sqlalchemy.orm import Session
from sqlalchemy import exc, select, Select, String
from ..database.mapped_classes import Contact
from flask import flash


class ContactService:
    __session:Session

    def __init__(self, session:Session) -> None:
        self.__session = session

    def create(self, contact:Contact):
        try:
            self.__session.add(contact)
            self.__session.commit()
            return contact
        except exc.SQLAlchemyError as error:
            self.__session.rollback()
            if '1062, "Duplicate entry' in str(error.__dict__['orig']):
                flash("Correo duplicado, Inserte uno nuevo","error")     
            flash(str(error.__dict__['orig']))

    def find(self):
        return self.__session.scalars(select(Contact))
    
    def deleteMore(self, stmt: Select[String[Contact]]):
        print(stmt)