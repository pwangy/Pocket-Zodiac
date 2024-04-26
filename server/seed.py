#!/usr/bin/env python3
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
    w1 = West(
        name="Aries",
        qualities="",
        element="",
        planet="",
        symbol="",
        img="",
        # user_id="",
        # user_zodiac_id="",
    )
    w2 = West(
        name="Taurus",
        qualities="",
        element="",
        planet="",
        symbol="",
        img="",
        # user_id="",
        # user_zodiac_id="",
    )
    w3 = West(
        name="Gemini",
        qualities="",
        element="",
        planet="",
        symbol="",
        img="",
        # user_id="",
        # user_zodiac_id="",
    )
    w4 = West(
        name="Cancer",
        qualities="",
        element="",
        planet="",
        symbol="",
        img="",
        # user_id="",
        # user_zodiac_id="",
    )
    w5 = West(
        name="Leo",
        qualities="",
        element="",
        planet="",
        symbol="",
        img="",
        # user_id="",
        # user_zodiac_id="",
    )
    w6 = West(
        name="Virgo",
        qualities="",
        element="",
        planet="",
        symbol="",
        img="",
        # user_id="",
        # user_zodiac_id="",
    )
    w7 = West(
        name="Libra",
        qualities="",
        element="",
        planet="",
        symbol="",
        img="",
        # user_id="",
        # user_zodiac_id="",
    )
    w8 = West(
        name="Scorpio",
        qualities="",
        element="",
        planet="",
        symbol="",
        img="",
        # user_id="",
        # user_zodiac_id="",
    )
    w9 = West(
        name="Sagittarius",
        qualities="",
        element="",
        planet="",
        symbol="",
        img="",
        # user_id="",
        # user_zodiac_id="",
    )
    w10 = West(
        name="Capricorn",
        qualities="",
        element="",
        planet="",
        symbol="",
        img="",
        # user_id="",
        # user_zodiac_id="",
    )
    w11 = West(
        name="",
        qualities="Aquarius",
        element="",
        planet="",
        symbol="",
        img="",
        # user_id="",
        # user_zodiac_id="",
    )
    w12 = West(
        name="Pisces",
        qualities="",
        element="",
        planet="",
        symbol="",
        img="",
        # user_id="",
        # user_zodiac_id="",
    )

    # element
    

    # user
    

    # user zodiac
    

# if __name__ == "__main__":
#     fake = Faker()
#     with app.app_context():
#         print("Starting seed...")
#         # Seed code goes here!
