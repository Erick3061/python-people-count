from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session
from sqlalchemy import Engine, create_engine, URL, select, insert
# from mapped_classes import User

from .mapped_classes import base, User, Role

class Database:

    url_object = URL.create(
        'sqlite',
        database='cameraDeclarative.db',
    )

    engine:Engine
    marker:sessionmaker[Session]
    session:Session
    base: DeclarativeBase

    def __init__(self) -> None:
        self.engine = create_engine(self.url_object)
        self.base = base
        self.marker = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.session = self.marker()
        self.initDB()
        pass
    
    def initDB(self):
        # from mapped_classes import User,Address
        # User(self.base)
        self.base.metadata.create_all(self.engine)
        try:
            user = User()
            # user.id=10,
            user.user="Erick"
            user.password="Erick"
            # user.role=Role.ADMIN
            # user.isActive=True
            self.session.add(user)
            # self.session.commit()
        except Exception as err:
             print(f"Unexpected {err}, {type(err)}")

    def seedUser():
        user=User(user="Administrador",password="1234")