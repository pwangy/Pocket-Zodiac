from . import ma, fields, validate, West

class WestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = West
        load_instance = True

    user = fields.Nested(
        "UserSchema",
        only=("id", "username", "email", "birthdate"),
        exclude=("_password_hash",),
        many=True,
    )
    name = fields.String(required=True)
    qualities = fields.String(required=True)
    desc = fields.String(required=True)
    element = fields.String(required=True)
    planet = fields.String(required=True)
    symbol = fields.String(required=True)
    img = fields.String(
        required=True, 
        validate=validate.Regexp(
            r".*\.(jpeg|png|jpg)", error="File URI must be in JPEG, JPG, or PNG format"),
    )

    url = ma.Hyperlinks({
        "self": ma.URLFor("westbyid", values=dict(id="<id>")),
        "collection": ma.URLFor("west"),
        "users": ma.URLFor("users"),
    })

west_schema = WestSchema()
wests_schema = WestSchema(many=True, exclude=("users",))