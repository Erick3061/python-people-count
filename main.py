from src.server.server import Server
server = Server()

app=server.app


# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     server.database.session.remove()

@app.route("/")
def hello():
    return "<p>Hello, World!</p>"

