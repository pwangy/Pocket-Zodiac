from . import ma, fields, validate, East


class EastSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = East
        load_instance = True

    name = fields.String()
    name_12 = fields.String()
    qualities = fields.String()
    desc = fields.String()
    polarity = fields.String()
    order_12 = fields.Integer()
    order_60 = fields.Integer()
    western_counterpart = fields.String()
    img = fields.String()
    element_id = fields.Integer()
    element = fields.Nested("ElementSchema")
    start = fields.Date()
    end = fields.Date()
    start1 = fields.Date()
    end1 = fields.Date()
    # start = fields.String()
    # end = fields.String()
    # start1 = fields.String()
    # end1 = fields.String()


east_schema = EastSchema()
easts_schema = EastSchema(many=True)
