from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session
from sqlalchemy import Engine, create_engine, URL
from .mapped_classes import base

class Database:

    __url_object = URL.create(
        'mysql+pymysql',
        username='root',
        password='root',
        host='0.0.0.0',
        port= 3306,
        database='peoplecount'
    )

    __engine:Engine
    __base: DeclarativeBase
    __marker:sessionmaker[Session]
    session:Session

    def __init__(self) -> None:
        self.__engine = create_engine(self.__url_object)
        self.__base = base
        self.__marker = sessionmaker(autocommit=False, autoflush=False, bind=self.__engine)
        self.session = self.__marker()
        self.initDB()
        pass
    
    def initDB(self):
        self.__base.metadata.create_all(self.__engine)
        try:
            # user = User()
            # user.id=10,
            # user.user="Erick"
            # user.password="Erick"
            # user.role=Role.ADMIN
            # user.isActive=True
            # self.session.add(user)
            # self.session.commit()
            print("Holis")
        except Exception as err:
            print(f"Unexpected {err}, {type(err)}")

    # def seedUser():
    #     user=User(user="Administrador",password="1234")