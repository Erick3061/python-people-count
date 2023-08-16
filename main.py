from src.server.server import Server 

server = Server()

app=server.app

# with app.app_context:
#     server.db.create_all(bind_key='__all__')


@app.teardown_appcontext
def shutdown_session(exception=None):
    server.db_session.remove()

# @server.route("/")
# def hello():
#     return "<p>Hello, World!</p>"