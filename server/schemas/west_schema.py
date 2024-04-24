from . import ma, fields, validate, West, validates, re

class WestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = West
        load_instance = True
        ordered = True
        