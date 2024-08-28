#!/usr/bin/env python3
import csv
from faker import Faker
from config import app
from models.__init__ import db
from models.east import East, convert_date
from models.west import West, convert_date_w
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
#             return True  # success
#         except Exception as e:
#             print("Users not created")
#             return False  # failure


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

        # clear existing data
        # try:
        #     East.query.delete()
        #     West.query.delete()
        #     Element.query.delete()
        #     # User.query.delete()
        #     # UserZodiac.query.delete()
        #     db.session.commit()
        #     print("Tables dropped")
        # except Exception as e:
        #     print("Could not drop tables")

        # ? Freeze changes to Element, East, & West db
        # # element
        # with open("seeds/final_elements.csv", "r") as file:
        #     reader = csv.DictReader(file, delimiter="\t")
        #     for row in reader:
        #         row["id"] = int(row["id"]) if row["id"].isdigit() else None
        #         element = Element(**row)
        #         db.session.add(element)
        # db.session.commit()
        # print("Elements seeded")

        # # east
        # with open("seeds/final_east.csv", "r") as file:
        #     reader = csv.DictReader(file, delimiter="\t")
        #     for row in reader:
        #         row["id"] = int(row["id"]) if row["id"].isdigit() else None
        #         row["start"] = convert_date(row["start"])
        #         row["end"] = convert_date(row["end"])
        #         row["start1"] = convert_date(row["start1"])
        #         row["end1"] = convert_date(row["end1"])
        #         east = East(**row)
        #         db.session.add(east)
        # db.session.commit()
        # print("East seeded")

        # # west
        # with open("seeds/final_west.csv", "r") as file:
        #     reader = csv.DictReader(file, delimiter="\t")
        #     for row in reader:
        #         row["id"] = int(row["id"]) if row["id"].isdigit() else None
        #         row["start"] = convert_date_w(row["start"])
        #         row["end"] = convert_date_w(row["end"])
        #         west = West(**row)
        #         db.session.add(west)
        # db.session.commit()
        # print("West seeded")

        # users_created = seed_users()
        # if users_created:
        #     seed_user_zodiacs()

        print("Done seeding!")


if __name__ == "__main__":
    seed()

# for deployment
# the seed file needs some major refactoring. 
# need to seperate out functions for each table and then they need to be run in the correct order. : elements, west, east, user, user_zodiac
