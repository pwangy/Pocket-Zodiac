from flask_jwt_extended import jwt_required
from datetime import datetime
from models.west import West
from models.user_zodiac import UserZodiac
from config import db

@jwt_required()
def calc_w(user, app):
    with app.app_context():
        try:
            # Check if a western zodiac sign already exists for the user
            existing_sign = db.session.query(UserZodiac, West).join(West, UserZodiac.west_id == West.id).filter(UserZodiac.user_id == user.id).first()
            if existing_sign:
                print(f"Western sign already exists for {user.username}")
                return existing_sign.UserZodiac.west_id, existing_sign.West.name

            try:
                birthdate = datetime.strptime(user.birthdate, "%Y-%m-%d").date()
            except ValueError:
                print(f"Invalid birthdate format for user {user.username}")
                return None, None

            birthdate = birthdate.replace(year=2000)
            signs = West.query.all()

            for sign in signs:
                start_date = sign.start.replace(year=2000)
                end_date = sign.end.replace(year=2000)

                if start_date <= end_date:
                    # If the start date is before the end date, check if the birthdate is between them
                    if start_date <= birthdate <= end_date:
                        user_zodiac = UserZodiac(user_id=user.id, west_id=sign.id)
                        db.session.add(user_zodiac)
                        db.session.commit()
                        return sign.id, sign.name
                else:
                    # If the start date is after the end date, the sign spans two different months
                    # Check if the birthdate is after the start date or before the end date
                    if birthdate >= start_date or birthdate <= end_date:
                        user_zodiac = UserZodiac(user_id=user.id, west_id=sign.id)
                        db.session.add(user_zodiac)
                        db.session.commit()
                        return sign.id, sign.name

            print(f"Could not calculate sign for {user.username}")
            return None, None

        except Exception as e:
            print(f"error: {e}")
            db.session.rollback()
            return None, None

def calc_w_signup(user, app):
    with app.app_context():
        try:
            # Check if a western zodiac sign already exists for the user
            existing_sign = db.session.query(UserZodiac, West).join(West, UserZodiac.west_id == West.id).filter(UserZodiac.user_id == user.id).first()
            if existing_sign:
                print(f"Western sign already exists for {user.username}")
                return existing_sign.UserZodiac.west_id, existing_sign.West.name

            try:
                birthdate = datetime.strptime(user.birthdate, "%Y-%m-%d").date()
            except ValueError:
                print(f"Invalid birthdate format for user {user.username}")
                return None, None

            birthdate = birthdate.replace(year=2000)
            signs = West.query.all()

            for sign in signs:
                start_date = sign.start.replace(year=2000)
                end_date = sign.end.replace(year=2000)

                if start_date <= end_date:
                    # If the start date is before the end date, check if the birthdate is between them
                    if start_date <= birthdate <= end_date:
                        user_zodiac = UserZodiac(user_id=user.id, west_id=sign.id)
                        db.session.add(user_zodiac)
                        db.session.commit()
                        return sign.id, sign.name
                else:
                    # If the start date is after the end date, the sign spans two different months
                    # Check if the birthdate is after the start date or before the end date
                    if birthdate >= start_date or birthdate <= end_date:
                        user_zodiac = UserZodiac(user_id=user.id, west_id=sign.id)
                        db.session.add(user_zodiac)
                        db.session.commit()
                        return sign.id, sign.name

            print(f"Could not calculate sign for {user.username}")
            return None, None

        except Exception as e:
            print(f"error: {e}")
            db.session.rollback()
            return None, None
