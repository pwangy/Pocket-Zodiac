#!/usr/bin/env python3
from flask import Flask
from config import app, db
from utils.calc_w import calc_w
from models.user import User
from models.user_zodiac import UserZodiac 
from models.east import East 
from models.west import West 
from models.element import Element 


def test_calc_w():
    with app.app_context():
        users = User.query.all()
        for user in users:
            sign_id, sign_name = calc_w(user.birthdate)
            print(f'{user.name} is a {sign_name}')


if __name__ == '__main__':
    test_calc_w()