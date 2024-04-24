from . import SerializerMixin, validates, re, db
from sqlalchemy.ext.hybrid import hybrid_property
from DateTime import DateTime
from config import flask_bcrypt

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.string(20), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    _password_hash = db.Column(db.String(50), nullable=False)
    birthdate = db.Column(db.String, default=DateTime.now().date().strftime("%Y-%m-%d"))
    birthtime = db.Column(db.String, default=DateTime.now().strftime("%H:%M"))

    # Relationships
    user_zodiac = db.relationship("UserZodiac", back_populates="users")

    serialize_rules = ("-_password_hash",)
    
    def __repr__(self):
        return f"""
            <User {self.id}:
                username: {self.username}
                email: {self.email}
                birthdate: {self.birthdate}
                birthtime: {self.birthtime}
            />
        """

    @hybrid_property
    def password_hash(self):
        raise AttributeError("Passwords cannot be inspected after setup.")

    @password_hash.setter
    def password_hash(self, new_password):
        if not len(new_password) >= 8:
            raise ValueError('Password must be 8 or more characters')
        elif not re.search(r"[$&+,:;=?@#|'<>.-^*()%!]", new_password):
            raise ValueError('Password must contain special characters')
        elif not re.search(r"[A-Z]",new_password):
            raise ValueError('Password must contain at least one capital letter')
        elif not re.search(r"[a-z]",new_password):
            raise ValueError('Password must contain at least one lowercase letter')
        elif not re.search(r"[0-9]",new_password):
            raise ValueError('Password must contain at least one number')
        else:
            hashed = flask_bcrypt.generate_password_hash(new_password)
            self._password_hash = hashed

    def auth(self, password_to_check):
        return flask_bcrypt.check_password_hash(self._password_hash, password_to_check)