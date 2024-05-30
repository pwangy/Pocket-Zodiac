#!/usr/bin/env python3
import csv
from faker import Faker
from config import app
from models.__init__ import db
from models.east import East
from models.west import West
from models.element import Element
from models.user import User
from models.user_zodiac import UserZodiac


fake = Faker()


# def seed_users():
#     with app.app_context():
#         try:
#             users = []
#             usernames = []

#             for _ in range(30):
#                 username = fake.first_name()
#                 while username in usernames:
#                     username = fake.first_name()
#                 usernames.append(username)
#                 user = User(
#                     username=username,
#                     email=fake.email(),
#                     birthdate=fake.date_of_birth(),
#                 )
#                 user.password_hash = user.username + "Passw1!"
#                 users.append(user)
#             db.session.add_all(users)
#             db.session.commit()
#             print("Users created")
#             return True
#         except Exception as e:
#             print("Users not created")
#             return False


# def seed_user_zodiacs():
#     with app.app_context():
#         try:
#             users = User.query.all()
#             for user in users:
#                 user_zodiac = UserZodiac(
#                     user_id=user.id,
#                     east_west=fake.random_element(elements=("East", "West")),
#                     additional_birthdate=fake.date_time_between(
#                         start_date="-50y", end_date="now"
#                     ),
#                 )
#                 db.session.add(user_zodiac)
#             db.session.commit()
#             print("UserZodiacs created")
#             return True
#         except Exception as e:
#             print("User Zodiacs not created.")
#             return False


def seed():
    with app.app_context():
        print("Start seed file!")

        try:
            East.query.delete()
            West.query.delete()
            Element.query.delete()
            User.query.delete()
            UserZodiac.query.delete()
            db.session.commit()
            print("Tables dropped")
        except Exception as e:
            print("Could not drop tables")

        with open("seeds/elements.csv", "r") as file:
            reader = csv.DictReader(file, delimiter="\t")
            for row in reader:
                element = Element(**row)
                db.session.add(element)
        db.session.commit()
        print("Elements seeded")

# ! to seed: change Date to String in east and west models and schemas
        with open("seeds/east.csv", "r") as file:
            reader = csv.DictReader(file, delimiter="\t")
            for row in reader:
                east = East(**row)
                db.session.add(east)
        db.session.commit()
        print("East seeded")

        with open("seeds/west.csv", "r") as file:
            reader = csv.DictReader(file, delimiter="\t")
            for row in reader:
                west = West(**row)
                db.session.add(west)
        db.session.commit()
        print("West seeded")

# ! users and user_zodiacs should not be used in production
        # users_created = seed_users() 
        # if users_created:
        #     seed_user_zodiacs()
        # print("Done seeding!")


if __name__ == "__main__":
    seed()
