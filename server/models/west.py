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
    house = db.Column(db.String)
    img = db.Column(db.String)
    start = db.Column(db.Date)
    end = db.Column(db.Date)

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
                gloss: {self.gloss}
                qualities: {self.qualities}
                description: {self.desc}
                element: {self.element}
                modality: {self.modality}
                planet: {self.planet}
                house: {self.house}
                image: {self.img}
                start: {self.start}
                end: {self.end}
            />
        """

def convert_date_w(date_str):
    try:
        day, month = map(int, date_str.split("-"))
        year = 2024
        return datetime(year, day, month)
    except ValueError:
        return None