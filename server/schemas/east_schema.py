from . import ma, fields, validate, East

class EastSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = East
        load_instance = True

    name = fields.String(required=True)
    qualities = fields.String(required=True)
    desc = fields.String(required=True)
    polarity = fields.String(required=True)
    order_12 = fields.Integer(required=True)
    order_60 = fields.Integer(required=True)
    western_counterpart = fields.String(required=True)
    img = fields.String(
        required=True, 
        validate=validate.Regexp(
            r".*\.(jpeg|png|jpg)", error="File URI must be in JPEG, JPG, or PNG format"),
    )

    url = ma.Hyperlinks({
        "self": ma.URLFor("eastbyid", values=dict(id="<id>")),
        "collection":ma.URLFor("east")
    })
    
east_schema = EastSchema()
easts_schema = EastSchema(many=True)
