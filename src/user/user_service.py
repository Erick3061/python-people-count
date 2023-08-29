from sqlalchemy.orm import Session
from ..database.mapped_classes import User

class UserService:
    __session:Session

    def __init__(self, session:Session) -> None:
        self.__session=session

    def create(self,user:User)-> User:

        return user

    def find(self):
        
        pass

    def findOne(self):
        
        pass

    def update(self,id:str, user:User):
        
        pass

    def delete(self, id:str):
        
        pass