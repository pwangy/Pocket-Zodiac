from . import ma, fields, validate, Element, validates, re

class ElementSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Element
        load_instance = True
        ordered = True
        