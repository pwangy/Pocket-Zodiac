from . import ma, fields, validate, East

class EastSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = East
        load_instance = True

    element_id = fields.Integer(required=True)
    element = fields.Nested(
        "EastSchema",
        only=("id", "name", "qualities", "desc", "polarity", "order_12", "order_60", "img"),
        exclude=("element", "user"),
        many=True,
    )
    user_id = fields.Integer(required=True)
    user = fields.Nested(
        "UserSchema",
        only=("id", "username", "email", "birthdate"),
        exclude=("_password_hash",),
        many=True,
    )
    name = fields.String(required=True)
    qualities = fields.String(required=True)
    desc = fields.String(required=True)
    polarity = fields.String(required=True)
    order_12 = fields.Integer(required=True)
    order_60 = fields.Integer(required=True)
    img = fields.String(
        required=True, 
        validate=validate.Regexp(
            r".*\.(jpeg|png|jpg)", error="File URI must be in JPEG, JPG, or PNG format"),
    )

    url = ma.Hyperlinks({
        "self": ma.URLFor("eastbyid", values=dict(id="<id>")),
        "collection":ma.URLFor("east"),
        "elements": ma.URLFor("elements"),
    })
    
east_schema = EastSchema()
easts_schema = EastSchema(many=True, exclude=("elements", "users"))
