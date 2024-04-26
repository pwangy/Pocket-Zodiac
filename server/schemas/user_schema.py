from . import ma, fields, validate, validates, DateTime, User

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        exclude = ('_password_hash',)

    user_zodiac = fields.Nested(
        "UserZodiac",
        only=("id", "east_west", "additional_birthdate"),
        exclude=("user_id", "west_id", "east_id"),
        many=True,
    )
    username = fields.String(required=True, unique=True, validate=validate.Length(min=2, max=20))
    email = fields.Email(required=True, unique=True)
    password_hash = fields.String(required=True, load_only=True, validate=validate.Length(min=8, max=20))
    birthdate = fields.Date()

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
            raise ValueError('Date must be in \"YYYY-MM-DD\"')

    url = ma.Hyperlinks({
    "self": ma.URLFor("userbyid", values=dict(id="<id>")),
    "collection": ma.URLFor("users"),
    })

user_schema = UserSchema()
users_schema = UserSchema(many=True)
