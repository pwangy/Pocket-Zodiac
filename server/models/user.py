from . import SerializerMixin, validates, re, db
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime
from DateTime import DateTime
from config import flask_bcrypt


class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=True, unique=True)
    _password_hash = db.Column(db.String, nullable=False)
    birthdate = db.Column(db.String, nullable=True)

    # Relationships
    user_zodiacs = db.relationship(
        "UserZodiac", back_populates="user", cascade="all, delete-orphan"
    )

    serialize_rules = ("-_password_hash",)

    def __repr__(self):
        return f"""
            <User {self.id}:
                username: {self.username}
                email: {self.email}
                birthdate: {self.birthdate}
            />
        """

    @hybrid_property
    def password_hash(self):
        raise AttributeError("Inaccessable!")

    @password_hash.setter
    def password_hash(self, new_password):
        if len(new_password) < 8:
            raise ValueError("Password must be at least 8 characters")
        elif not re.search(r"[$&+,:;=?@#|'<>.-^*()%!]", new_password):
            raise ValueError("Password must contain special characters")
        elif not re.search(r"[A-Z]", new_password):
            raise ValueError("Password must contain at least one capital letter")
        elif not re.search(r"[a-z]", new_password):
            raise ValueError("Password must contain at least one lowercase letter")
        elif not re.search(r"[0-9]", new_password):
            raise ValueError("Password must contain at least one number")
        else:
            hashed_password = flask_bcrypt.generate_password_hash(new_password).decode(
                'utf-8'
            )
            self._password_hash = hashed_password

    def authenticate(self, password_to_check):
        return flask_bcrypt.check_password_hash(self._password_hash, password_to_check)

    @validates("username")
    def validate_username(self, _, username):
        if not isinstance(username, str):
            raise TypeError("Username must be a string.")
        elif 2 > len(username) > 20:
            raise ValueError("Username must be between 2 and 20 characters.")
        return username

    @validates("email")
    def validate_email(self, _, email):
        if not re.match(r"^[\w\-\.]+@([\w\-]+\.)+[\w\-]{2,4}$", email):
            raise ValueError("Invalid email address")
        return email
