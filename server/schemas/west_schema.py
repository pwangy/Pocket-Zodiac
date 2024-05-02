from . import ma, fields, validate, West


class WestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = West
        load_instance = True

    name = fields.String(required=True)
    gloss = fields.String(required=True)
    desc = fields.String(required=True)
    qualities = fields.String(required=True)
    element = fields.String(required=True)
    modality = fields.String(required=True)
    planet = fields.String(required=True)
    house = fields.String(required=True)
    symbol = fields.String()
    img = fields.String()

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor("westbyid", values=dict(id="<id>")),
            "collection": ma.URLFor("west"),
    })


west_schema = WestSchema()
wests_schema = WestSchema(many=True)
