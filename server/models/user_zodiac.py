from . import SerializerMixin, db
from datetime import datetime


class UserZodiac(db.Model, SerializerMixin):
    __tablename__ = "user_zodiacs"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    east_id = db.Column(db.Integer, db.ForeignKey("east.id"))
    west_id = db.Column(db.Integer, db.ForeignKey("west.id"))
    additional_birthdate = db.Column(db.String)

    # Relationships
    user = db.relationship("User", back_populates="user_zodiacs")
    east = db.relationship("East", back_populates="user_zodiacs")
    west = db.relationship("West", back_populates="user_zodiacs")

    # Serialize
    serialize_rules = ("-user.user_zodiacs", "-east.user_zodiacs", "-west.user_zodiacs")

    # Representation
    def __repr__(self):
        return f"""
            <UserZodiac {self.id}:
                user: {self.user_id}
                eastern: {self.east_id}
                western: {self.west_id}
            />
        """
