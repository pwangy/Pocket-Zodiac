from functools import wraps
from flask import request, g, make_response
from flask_restful import Resource
from werkzeug.exceptions import NotFound

from schemas.user_schema import user_schema, users_schema
from schemas.east_schema import east_schema, easts_schema
from schemas.west_schema import west_schema, wests_schema
from schemas.element_schema import element_schema, elements_schema
from schemas.user_zodiac_schema import user_zodiac_schema, users_zodiac_schema
from models.user import User
from models.east import East
from models.west import West
from models.element import Element
from models.user_zodiac import UserZodiac
# from .user_zodiac import UserZodiac
from config import db, app, jwt
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, get_jwt_identity, set_access_cookies, set_refresh_cookies, unset_jwt_cookies, unset_refresh_cookies, unset_access_cookies, current_user, get_jwt, verify_jwt_in_request, decode_token,)

@app.route("/")
def index():
    return "<h1>Pocket Chinese Astrology Server</h1>"

@app.errorhandler(NotFound)
def not_found(error):
    return {"error": error.description}, 404

@app.before_request
def before_request():
    path_dict = {"eastbyid": East, "westbyid": West, "elementbyid": Element, "userbyid": User, "userzodiacbyid": UserZodiac}
    if request.endpoint in path_dict:
        id = request.view_args.get("id")
        record = db.session.get(path_dict.get(request.endpoint), id)
        key_name = "user" if request.endpoint == "user_by_id" else "east" if request.endpoint == "eastbyid" else "west" if request.endpoint == "westbyid" else "element" if request.endpoint == "elementbyid" else "user_zodiac"
        setattr(g, key_name, record)

def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        # if "user_id" not in session:
            # return {"message": "Access Denied, please log in!"}, 422
        return func(*args, **kwargs)

    return decorated_function

# Register a callback function that loads a user from your database whenever
# a protected route is accessed. This should return any python object on a
# successful lookup, or None if the lookup failed for any reason (for example
# if the user has been deleted from the database).
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return db.session.get(User, identity)
