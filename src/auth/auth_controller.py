from src.server.server import Server
from flask import Blueprint

bp = Blueprint("auth", __name__,url_prefix="/auth")

server = Server.getServer();

@bp.route("/",methods=["POST"])
def logIn():
    return {}