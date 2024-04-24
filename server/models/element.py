from . import SerializerMixin, validates, re, db

class Element(db.Model, SerializerMixin):
    __tablename__ = 'elements'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    qualities = db.Column(db.String)
    desc = db.Column(db.Text)
    season = db.Column(db.String)
    direction = db.Column(db.String)
    planet = db.Column(db.String)
    number = db.Column(db.String)
    smell = db.Column(db.String)
    taste = db.Column(db.String)
    organ = db.Column(db.String)
    color = db.Column(db.String)

    # Relationships
    east = db.relationship("East", back_populates="elements")

    # Serialize
    # serialize_rules = ("-",)

    # Representation
    def __repr__(self):
        return f"""
            <Element {self.id}:
                name: {self.name}
                qualities: {self.qualities}
                description: {self.desc}
                season: {self.season}
                direction: {self.direction}
                planet: {self.planet}
                number: {self.number}
                smell: {self.smell}
                taste: {self.taste}
                organ: {self.organ}
                color: {self.color}
            />
        """
