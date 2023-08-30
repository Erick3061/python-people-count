from sqlalchemy.orm import Session
from sqlalchemy import exc
from ..database.mapped_classes import Contact

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
            return str(error.__dict__)