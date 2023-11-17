from flask import Blueprint


routes = Blueprint("main", __name__)



@routes.route("/test")
def test():
    return 'test'
