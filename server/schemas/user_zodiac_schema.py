from . import ma, fields, validate, DateTime, UserZodiac, validates
import re


class UserZodiacSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserZodiac
        load_instance = True
        ordered = True

    user_id = fields.Integer(required=True)
    user = fields.Nested(
        "UserSchema",
        only=("id", "username", "email", "birthdate"),
        exclude=("_password_hash",),
    )

    west_id = fields.Integer()
    west = fields.Nested(
        "WestSchema",
    )

    east_id = fields.Integer()
    east = fields.Nested(
        "EastSchema",
    )

    east_west = fields.String()
    additional_birthdate = fields.String()

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor("userzodiacbyid", values=dict(id="<id>"))
        }
    )

user_zodiac_schema = UserZodiacSchema()
users_zodiac_schema = UserZodiacSchema(many=True)
