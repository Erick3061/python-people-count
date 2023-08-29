from sqlalchemy.orm import Session
from ..database.mapped_classes import Camera

class CameraService:
    __session:Session

    def __init__(self, session:Session) -> None:
        self.__session = session

    def create(self, camera:Camera) -> Camera:
        print(camera)
        return camera