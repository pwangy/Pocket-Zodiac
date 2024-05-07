from . import SerializerMixin, validates, re, db
from sqlalchemy.ext.associationproxy import association_proxy
from datetime import datetime


class East(db.Model, SerializerMixin):
    __tablename__ = "east"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    name_12 = db.Column(db.String)
    qualities = db.Column(db.String)
    desc = db.Column(db.String)
    polarity = db.Column(db.String)
    order_12 = db.Column(db.Integer)
    order_60 = db.Column(db.Integer)
    western_counterpart = db.Column(db.String)
    element_id = db.Column(db.Integer, db.ForeignKey("elements.id"), nullable=True)
    img = db.Column(db.String)
    start = db.Column(db.Date)
    end = db.Column(db.Date)
    start1 = db.Column(db.Date)
    end1 = db.Column(db.Date)
    
    # Relationships
    element = db.relationship("Element", back_populates="east_signs")
    users = association_proxy("user_zodiacs", "user")
    user_zodiacs = db.relationship("UserZodiac", back_populates="east")

    # Serialize
    serialize_rules = ("-element.east_signs", "-user_zodiacs.east", "-west.east")

    # Representation
    def __repr__(self):
        return f"""
            <East {self.id}:
                name: {self.name}
                name_12: {self.name_12}
                qualities: {self.qualities}
                description: {self.desc}
                polarity: {self.polarity}
                order_12: {self.order_12}
                order_60: {self.order_60}
                western_counterpart: {self.western_counterpart}
                element_id: {self.element_id}
                img: {self.img}
                start: {self.end}
                end: {self.img}
                start1: {self.start1}
                end1: {self.end1}
            />
        """

    @staticmethod
    def ensure_integer(value):
        try:
            return int(value)
        except (ValueError, TypeError):
            return None

    def set_order_12(self, value):
        self.order_12 = self.ensure_integer(value)

    def set_order_60(self, value):
        self.order_60 = self.ensure_integer(value)


# def convert_date(date_str):
#     try:
#         year, day, month = map(int, date_str.split("-"))
#         return datetime(year, day, month)
#     except ValueError:
#         return None