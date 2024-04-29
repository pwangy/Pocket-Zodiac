from . import SerializerMixin, validates, re, db
from sqlalchemy.ext.associationproxy import association_proxy


class East(db.Model, SerializerMixin):
    __tablename__ = "east"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    qualities = db.Column(db.String)
    desc = db.Column(db.String)
    polarity = db.Column(db.String)
    order_12 = db.Column(db.Integer)
    order_60 = db.Column(db.Integer)
    western_counterpart = db.Column(db.Integer, db.ForeignKey("west.id"))
    element_id = db.Column(db.Integer, db.ForeignKey("elements.id"))
    img = db.Column(db.String)

    # Relationships
    element = db.relationship("Element", back_populates="east_signs")
    west = db.relationship("West", back_populates="east_signs")
    uses = association_proxy("user_zodiacs", "user")
    user_zodiacs = db.relationship("UserZodiac", back_populates="east")

    # Serialize
    serialize_rules = ("-element.east_signs", "-user_zodiacs.east", "-west.east")

    # Representation
    def __repr__(self):
        return f"""
            <East {self.id}:
                name: {self.name}
                qualities: {self.qualities}
                description: {self.desc}
                polarity: {self.polarity}
                order_12: {self.order_12}
                order_60: {self.order_60}
                element_id: {self.element_id}
                img: {self.img}
            />
        """
