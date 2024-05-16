from . import ma, fields, validate, DateTime, UserZodiac, validates
import re


class UserZodiacSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserZodiac
        load_instance = True
        ordered = True

    id = fields.Integer()
    user_id = fields.Integer(required=True)

    west_id = fields.Integer()
    west = fields.Nested(
        "WestSchema",
    )

    east_id = fields.Integer()
    east = fields.Nested(
        "EastSchema",
    )

    additional_birthdate = fields.String()

    url = ma.Hyperlinks({"self": ma.URLFor("userzodiacbyid", values=dict(id="<id>"))})


user_zodiac_schema = UserZodiacSchema()
users_zodiac_schema = UserZodiacSchema(many=True)
