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
    east_id = fields.Nested(
        "EastSchema",
    )

    east_west = fields.String()
    additional_birthdate = fields.Date()

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor("userzodiacbyid", values=dict(id="<id>")),
            "collection": ma.URLFor("userszodiac"),
            # "users": ma.URLFor("users"),
            # "west": ma.URLFor("west"),
            # "east": ma.URLFor("east"),
        }
    )

    @validates("additional_birthdate")
    def validate_additional_birthdate(self, additional_birthdate):
        if not DateTime.strptime(additional_birthdate, "%Y-%m-%d"):
            raise ValueError('Date must be in "YYYY-MM-DD"')


user_zodiac_schema = UserZodiacSchema()
users_zodiac_schema = UserZodiacSchema(many=True)
