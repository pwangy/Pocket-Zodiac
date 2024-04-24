from . import ma, fields, validate, UserZodiac, validates, re

class UserZodiacSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserZodiac
        load_instance = True
        ordered = True
    
    user_id = fields.String()
    west_id = fields.String()
    east_id = fields.String()
    east_hour = fields.String()
    east_west = fields.String()