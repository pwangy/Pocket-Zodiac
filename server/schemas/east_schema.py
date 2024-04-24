from . import ma, fields, validate, East, validates, re

class EastSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = East
        load_instance = True
        ordered = True