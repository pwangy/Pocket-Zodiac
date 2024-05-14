#!/usr/bin/env python3
from flask import Flask
from config import app, db
from datetime import datetime
from utils.calc_e import calc_e
from models.user import User
from models.user_zodiac import UserZodiac
from models.east import East
from models.west import West
from models.element import Element


def test_calc_e():
    with app.app_context():
        users = User.query.all()

        for user in users:
            birthdate = datetime.strptime(user.birthdate, "%Y-%m-%d").date()
            calc_e(user, app)

            user_zodiac = UserZodiac.query.filter_by(user_id=user.id).first()

            if user_zodiac and user_zodiac.east_id:
                sign = East.query.filter_by(id=user_zodiac.east_id).first()
                print(f"{user.username} is a {sign.name}")
            else:
                print(f"Could not calculate sign for {user.username}")


if __name__ == "__main__":
    test_calc_e()
