from . import ma, fields, Element


class ElementSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Element
        load_instance = True

    name = fields.String(required=True)
    qualities = fields.String(required=True)
    desc = fields.String(required=True)
    season = fields.String(required=True)
    direction = fields.String(required=True)
    planet = fields.String(required=True)
    number = fields.Integer(required=True)
    smell = fields.String(required=True)
    taste = fields.String(required=True)
    organ = fields.String(required=True)
    color = fields.String(required=True)
    img = fields.String()


element_schema = ElementSchema()
elements_schema = ElementSchema(many=True)
