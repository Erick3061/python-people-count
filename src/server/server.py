from flask import Flask
from ..database.database import Database
from ..auth.auth import Auth
from ..user.user import User
from ..main.main import Main
 
class Server:

    app : Flask
    database : Database

    user:User

    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['EXPLAIN_TEMPLATE_LOADING'] = True
        self.database = Database()
        self.addRegister()
        
    def addRegister(self):
        Main(self.app)
        self.user = User(self.app,self.database.session)
        Auth(self.app, self.user.getService())
        