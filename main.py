# from src.server.server import Server
# from flask import render_template
# server = Server()

# app=server.app
# app.config['EXPLAIN_TEMPLATE_LOADING'] = True

# # @app.teardown_appcontext
# # def shutdown_session(exception=None):
# #     server.database.session.remove()


# from flask import Blueprint, render_template

# from . import app

# @app.route("/")
# def hello():
#     return render_template('index.html')