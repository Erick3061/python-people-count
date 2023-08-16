from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from ..camera.camera import Camera

class Server:

    app:Flask
    db:SQLAlchemy

    def __init__(self):
        self.app = Flask(__name__)
        self.db = SQLAlchemy()
        self.injectDB()
        
    def injectDB(self):
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////home/erick/db.db" 
        self.db.init_app(self.app)
        with self.app.app_context():self.db.create_all()