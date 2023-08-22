from flask import Flask
from ..database.database import Database

class Server:

    app : Flask
    database : Database

    def __init__(self):
        self.app = Flask(__name__)
        self.database = Database()
        self.addRegister()
        
    def addRegister(self):
        from src.auth.auth_controller import bp as bpAuth
        # self.app.register_blueprint(bpAuth)
        pass

    def getServer(self)->Flask:
        return self.app
    # def injectDB(self):
    #     self.__engine = create_engine(self.__url_object)
    #     self.__db_session = sessionmaker(autocommit=False, autoflush=False, bind=self.__engine)

    # def initDB(self):
    #     self.database = Database(engine=self.__engine)
    #     self.database.init()
        