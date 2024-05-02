# internal imports
from models.user import User
from models.user_zodiac import UserZodiac
from models.east import East
from models.element import Element
from models.west import West

from config import ma, db
from DateTime import DateTime

# external libraries imports
from marshmallow import validates, ValidationError, fields, validate
from flask_marshmallow.sqla import SQLAlchemyAutoSchema, auto_field