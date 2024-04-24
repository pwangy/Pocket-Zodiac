from . import SerializerMixin, validates, re, db
from models.user import User
from models.east import East
from models.west import West

class UserZodiac(db.Model, SerializerMixin):
    __tablename__ = 'user_zodiac'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    west_id = db.Column(db.Integer, db.ForeignKey('west.id'))
    east_id = db.Column(db.Integer, db.ForeignKey('east.id'))
    east_hour = db.Column(db.Integer, db.ForeignKey('east.id'))
    east_west = db.Column(db.String)
    # additional_birthdate = db.Column(db.DateTime)

    # Relationships
    user = db.relationship("User", back_populates="user_zodiac")
    east = db.relationship("East", back_populates="user_zodiac")
    east_hour = db.relationship("East", back_populates="user_zodiac")
    west = db.relationship("West", back_populates="user_zodiac")

    # Serialize
    serialize_rules = ("-user.user_zodiac","-east.user_zodiac", "-west.user_zodiac")

    # Representation
    def __repr__(self):
        return f"""
            <UserZodiac {self.id}:
                user: {self.user_id}
                eastern: {self.east_id}
                hour: {self.east_hour}
                western: {self.west_id}
            />
        """
