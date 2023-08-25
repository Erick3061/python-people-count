from flask import Blueprint
from .user_service import UserService

def controller(bp:Blueprint, service:UserService):
    
    @bp.route("/",methods=["POST"])
    def create():
        return {}
    
    @bp.route("/",methods=["GET"])
    def Test():
        return {}
    
    return bp
