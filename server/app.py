#!/usr/bin/env python3
from config import app, api
from routes.user.users import Users
from routes.user.user_by_id import UserById
from routes.user_zodiac.user_zodiac import UserZodiac
from routes.user_zodiac.user_zodiac_by_id import UserZodiacById
from routes.east.east import East
from routes.east.east_by_id import EastById
from routes.west.west import West
from routes.west.west_by_id import WestById
from routes.element.elements import Elements
from routes.element.element_by_id import ElementById
from routes.auth.login import Login
from routes.auth.logout import Logout
from routes.auth.session import Session
from routes.auth.refresh import Refresh

api.add_resource(Login, "/login")
api.add_resource(Logout, "/logout")
api.add_resource(Session, "/me")
api.add_resource(Users, "/signup")
api.add_resource(Refresh, "/refresh")
api.add_resource(East, "/east")
api.add_resource(EastById, "/eastbyid")
api.add_resource(West, "/west")
api.add_resource(WestById, "/westbyid")
api.add_resource(UserZodiac, "/userszodiac")
api.add_resource(UserZodiacById, "/userzodiacbyid")
api.add_resource(Elements, "/elements")
api.add_resource(ElementById, "/elementsbyid")

if __name__ == "__main__":
    app.run(port=5555, debug=True)
