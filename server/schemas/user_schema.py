from . import ma, fields, validate, validates, DateTime, User


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        exclude = ("_password_hash",)

    username = fields.String(
        required=True,
        unique=True,
        validate=validate.Length(
            min=2, max=20, error="Username must be between 2 and 20 characters"
        ),
    )
    email = fields.Email(required=True, unique=True)
    password_hash = fields.String(
        data_key="password_hash",
        required=True,
        load_only=True,
        validate=validate.Length(min=8, error="Password must be at least 8 characters long"),
    )
    birthdate = fields.Date()
    user_zodiac = fields.Nested(
        "UserZodiac",
        only=("id", "east_west"),
    )

    def load(self, data, instance=None, *, partial=False, **kwargs):
        loaded_instance = super().load(
            data, instance=instance, partial=partial, **kwargs
        )

        for key, value in data.items():
            setattr(loaded_instance, key, value)

        return loaded_instance

    @validates("birthdate")
    def validate_birthdate(self, birthdate):
        if not DateTime.strptime(birthdate, "%Y-%m-%d"):
            raise ValueError('Date must be in "YYYY-MM-DD"')

    url = ma.Hyperlinks(
        {
            "collection": ma.URLFor("users"),
        }
    )

user_schema = UserSchema()
users_schema = UserSchema(many=True)
