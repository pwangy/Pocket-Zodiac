from . import ma, fields, validate, User, validates, re

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        ordered = True
        exclude = ('_password_hash',)

    username = fields.String(
        required=True,
        unique=True,
        validate=[
            validate.Length(
                min=2,
                max=20,
                error="Username must be between 2 and 20 characters."
        )]
    )

    email = fields.String()
    password_hash = fields.String(
        data_key="password_hash",
        required=True,
        validate=validate.Length(
            min=8, error="Password must be at least 8 characters long."
        ),
        load_only=True
    )

    birthdate = fields.String()

    birthtime = fields.String()

    def load(self, data, instance=None, *, partial=False, **kwargs):
        loaded_instance = super().load(
            data, instance=instance, partial=partial, **kwargs
        )

        for key, value in data.items():
            setattr(loaded_instance, key, value)

        return loaded_instance

user_schema = UserSchema()
users_schema = UserSchema(many=True)