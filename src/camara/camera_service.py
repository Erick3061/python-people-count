from sqlalchemy.orm import Session
from sqlalchemy import select
from ..database.mapped_classes import Camera, Contact

class CameraService:
    __session:Session

    def __init__(self, session:Session) -> None:
        self.__session = session

    def create(self, camera:Camera) -> Camera:
        self.__session.add(camera)
        self.__session.commit()
        return camera
    
    def find(self):
        return self.__session.scalars(select(Camera))
    
    def findContact(self):
        return self.__session.scalars(select(Contact))