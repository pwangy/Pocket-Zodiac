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
    print("Start seed file!")

    # drop tables
    try:
        East.query.delete()
        West.query.delete()
        Element.query.delete()
        User.query.delete()
        UserZodiac.query.delete()
        print("Tables dropped")
    except Exception as e:
        print("Could not drop tables")

    # element
    def seed_elements():
        with open("seeds/elements.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['id'] = int(row['id']) if row['id'].isdigit()else None
                element = Element(**row)
                db.session.add(element)
        db.session.commit()
        print("Elements created")

    # east
    def seed_east():
        with open("seeds/east.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['id'] = int(row['id']) if row['id'].isdigit()else None
                east = East(**row)
                db.session.add(east)
        db.session.commit()
        print("East created")

    # west
    def seed_west():
        with open("seeds/west.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['id'] = int(row['id']) if row['id'].isdigit()else None
                west = West(**row)
                db.session.add(west)
        db.session.commit()
        print("West created")

    # user
    def seed_users(num_users):
        for _ in range(num_users):
            user = User(
                username=fake.user_name(),
                email=fake.email(),
                _password_hash=fake.password(),
                birthdate=fake.date_of_birth()
            )
            db.session.add(user)
        db.session.commit()
        print("Users created")

    # user zodiac
    def seed_user_zodiac(num_users):
        users = User.query.limit(num_users).all()
        for user in users:
            user_zodiac = UserZodiac(
                user_id=user.id,
                east_west=fake.random_element(elements=('East', 'West')),
                additional_birthdate=fake.date_time_between(start_date="-50y", end_date="now")
            )
            db.session.add(user_zodiac)
        db.session.commit()
        print("UserZodiacs created")

    seed_elements()
    seed_east()
    seed_west()
    seed_users(50)
    seed_user_zodiac(50)
    print("Done seeding!")

# if __name__ == "__main__":
#     fake = Faker()
#     with app.app_context():
#         print("Starting seed...")
#         # Seed code goes here!
