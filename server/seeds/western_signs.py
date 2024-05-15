#!/usr/bin/env python3
from flask import Flask
from config import app, db
from datetime import datetime
from utils.calc_w import calc_w
from models.user import User
from models.user_zodiac import UserZodiac
from models.east import East
from models.west import West
from models.element import Element


def test_calc_w():
    with app.app_context():
        users = User.query.all()

    # ! check birthdate data types
    # for user in users:
    #     print(f"Birthdate for {user.username}: {user.birthdate}, type: {type(user.birthdate)}")
    # ! check formatting
    # for user in users:
    #             try:
    #                 # Try to convert the birthdate string to a datetime object
    #                 datetime.strptime(user.birthdate, '%Y-%m-%d')
    #                 print(f"Birthdate for {user.username} is in the correct format: {user.birthdate}")
    #             except ValueError:
    #                 print(f"Birthdate for {user.username} is NOT in the correct format: {user.birthdate}")

    for user in users:
        sign_id, sign_name = calc_w(user, app)

        if sign_id and sign_name:
            print(f"{user.username} is a {sign_name}")
        else:
            print(f"Could not calculate sign for {user.username}")


if __name__ == "__main__":
    test_calc_w()
