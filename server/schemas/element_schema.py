from . import ma, fields, Element

class ElementSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Element
        load_instance = True

    # east = fields.Nested(
    #     "EastSchema",
    #     only=("name", "qualities", "desc", "polarity", "order_12", "order_60", "img"),
    #     exclude=("element",),
    #     many=True,
    # )
    name = fields.String(required=True)
    qualities = fields.String(required=True)
    desc = fields.String(required=True)
    season = fields.String(required=True)
    direction = fields.String(required=True)
    planet = fields.String(required=True)
    number = fields.String(required=True)
    smell = fields.String(required=True)
    taste = fields.String(required=True)
    organ = fields.String(required=True)
    color = fields.String(required=True)

    url = ma.Hyperlinks({
        "self": ma.URLFor("elementbyid", values=dict(id="<id>")),
        "collection": ma.URLFor("elements"),
        # "east": ma.URLFor("east"),
    })

element_schema = ElementSchema()
elements_schema = ElementSchema(many=True)
