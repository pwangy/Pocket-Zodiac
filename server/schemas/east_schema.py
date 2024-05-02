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
    western_counterpart = fields.String()
    img = fields.String()
    element_id = fields.Integer()
    element = fields.Nested('ElementSchema')

    url = ma.Hyperlinks({
        "self": ma.URLFor("eastbyid", values=dict(id="<id>")),
        "collection":ma.URLFor("east")
    })

east_schema = EastSchema()
easts_schema = EastSchema(many=True)
