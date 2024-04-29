from . import SerializerMixin, db
from sqlalchemy.ext.associationproxy import association_proxy
from datetime import datetime


class West(db.Model, SerializerMixin):
    __tablename__ = "west"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    gloss = db.Column(db.String)
    desc = db.Column(db.String)
    qualities = db.Column(db.String)
    element = db.Column(db.String)
    modality = db.Column(db.String)
    planet = db.Column(db.String)
    house = db.Column(db.Integer)
    symbol = db.Column(db.String)
    img = db.Column(db.String)

    # Relationships
    user_zodiacs = db.relationship("UserZodiac", back_populates="west")
    users = association_proxy("user_zodiacs", "user")

    # Serialize
    serialize_rules = ("-user_zodiacs.west",)

    # Representation
    def __repr__(self):
        return f"""
            <West {self.id}:
                name: {self.name}
                qualities: {self.qualities}
                description: {self.desc}
                element: {self.element}
                planet: {self.planet}
                symbol: {self.symbol}
                image: {self.img}
            />
        """
