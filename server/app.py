#!/usr/bin/env python3
from flask import render_template
from config import GOOGLE_CLIENT_ID, app, api
from routes.user.users import Users
from routes.user.user_by_id import UserById
from routes.user_zodiac.user_zodiac import UserZodiac
from routes.user_zodiac.user_zodiac_by_id import UserZodiacById
from routes.east.east import Easts
from routes.east.east_by_id import EastById
from routes.west.west import Wests
from routes.west.west_by_id import WestById
from routes.element.elements import Elements
from routes.element.element_by_id import ElementById
from routes.auth.login import Login
from routes.auth.logout import Logout
from routes.auth.check_session import CheckSession
from routes.auth.refresh import Refresh
from routes.auth.oauth import OAuth
from os import environ
from dotenv import load_dotenv

api.add_resource(UserZodiacById, "/userzodiacbyid/<int:id>")
api.add_resource(UserZodiac, "/userszodiac")
api.add_resource(Elements, "/elements")
api.add_resource(ElementById, "/elementsbyid")
api.add_resource(Easts, "/east")
api.add_resource(EastById, "/eastbyid")
api.add_resource(Wests, "/west")
api.add_resource(WestById, "/westbyid")
api.add_resource(Users, "/signup")
api.add_resource(UserById, "/users/<int:id>")
api.add_resource(Login, "/login")
api.add_resource(Logout, "/logout")
api.add_resource(CheckSession, "/me")
api.add_resource(Refresh, "/refresh")
api.add_resource(OAuth, "/goauth")

@app.route("/")
@app.route("/auth")
@app.route("/zodiac")
@app.route("/explore")
@app.route("/elements/<int:id>")
@app.route("/east/<int:id>")
@app.route("/west/<int:id>")
@app.route("/edit/<int:id>")

def index(id=0):
    return render_template("index.html", GOOGLE_CLIENT_ID=environ.get("GOAUTH_CID"))

if __name__ == "__main__":
    app.run(port=5555, debug=True)
