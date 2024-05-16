from flask_jwt_extended import jwt_required
from datetime import datetime
from models.east import East
from models.user_zodiac import UserZodiac
from config import db


# ? Patch
@jwt_required()
def calc_e(user, app):
    birthdate = datetime.strptime(user.birthdate, "%Y-%m-%d").date()

    # ? Check if the birthdate is before the earliest possible date
    if birthdate < datetime.strptime("1924-02-05", "%Y-%m-%d").date():
        print(f"Could not calculate sign for {user.username}")
        return None, None
    # ? Check if the user already has an eastern zodiac sign
    try:
        user_zodiac = UserZodiac.query.filter_by(user_id=user.id).first()
        if user_zodiac and user_zodiac.east_id:
            print(f"Skipping {user.username} as east_id is already assigned")
            return
        # ? Get all eastern zodiac signs
        east = East.query.all()
        # ? Loop through each sign
        for sign in east:
            start = sign.start1 if birthdate.year >= 1984 else sign.start
            end = sign.end1 if birthdate.year >= 1984 else sign.end
            # ? Check if the birthdate is between the start and end dates
            if start <= birthdate <= end:
                user_zodiac = UserZodiac.query.filter_by(user_id=user.id).first()
                # ? Check if the user already has a UserZodiac instance
                if user_zodiac:
                    user_zodiac.east_id = sign.id
                    # ? If not, create a new UserZodiac instance
                else:
                    user_zodiac = UserZodiac(user_id=user.id, east_id=sign.id)
                    db.session.add(user_zodiac)
                db.session.commit()
                return
        # ? If the birthdate does not fall within any of the signs, print an error message
        print(f"Could not calculate sign for {user.username}")
        return None, None

    except Exception as e:
        print(f"error: {e}")
        db.session.rollback()
        return None, None


# ? Post
def calc_e_signup(user, app):
    birthdate = datetime.strptime(user.birthdate, "%Y-%m-%d").date()
    if birthdate < datetime.strptime("1924-02-05", "%Y-%m-%d").date():
        print(f"Could not calculate sign for {user.username}")
        return None, None

    try:
        user_zodiac = UserZodiac.query.filter_by(user_id=user.id).first()
        if user_zodiac and user_zodiac.east_id:
            print(f"Skipping {user.username} as east_id is already assigned")
            return

        east = East.query.all()
        for sign in east:
            start = sign.start1 if birthdate.year >= 1984 else sign.start
            end = sign.end1 if birthdate.year >= 1984 else sign.end
            if start <= birthdate <= end:
                user_zodiac = UserZodiac.query.filter_by(user_id=user.id).first()
                if user_zodiac:
                    user_zodiac.east_id = sign.id
                else:
                    user_zodiac = UserZodiac(user_id=user.id, east_id=sign.id)
                    db.session.add(user_zodiac)
                db.session.commit()
                return

        print(f"Could not calculate sign for {user.username}")
        return None, None

    except Exception as e:
        print(f"error: {e}")
        db.session.rollback()
        return None, None
