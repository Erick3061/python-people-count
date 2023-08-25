from .src.server.server import Server
from flask import Blueprint, render_template
from os import path


server = Server()
app=server.app


# @app.route("/")
# def hello():
#     return render_template('index.html')