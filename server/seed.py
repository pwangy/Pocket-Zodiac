#!/usr/bin/env python3
import csv
from random import randint, choice as rc
from faker import Faker

# from app import app
from config import app
from models.__init__ import db

from models.east import East
from models.west import West
from models.element import Element
from models.user import User
from models.user_zodiac import UserZodiac

fake = Faker()


with app.app_context():
    # start
    print('Start seed file!')
    
    # drop tables
    try:
        East.query.delete()
        West.query.delete()
        Element.query.delete()
        User.query.delete()
        UserZodiac.query.delete()
        print('Tables dropped')
    except Exception as e:
        print('Could not drop tables')

    # east
    

    # west


    # element
    

    # user
    

    # user zodiac
    

# if __name__ == "__main__":
#     fake = Faker()
#     with app.app_context():
#         print("Starting seed...")
#         # Seed code goes here!
