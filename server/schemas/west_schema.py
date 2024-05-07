from . import ma, fields, West, DateTime


class WestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = West
        load_instance = True

    name = fields.String()
    gloss = fields.String()
    desc = fields.String()
    qualities = fields.String()
    element = fields.String()
    modality = fields.String()
    planet = fields.String()
    house = fields.String()
    symbol = fields.String()
    img = fields.String()
    start = fields.Date()
    end = fields.Date()


west_schema = WestSchema()
wests_schema = WestSchema(many=True)
