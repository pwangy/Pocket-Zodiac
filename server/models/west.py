from . import SerializerMixin, validates, re, db

class West(db.Model, SerializerMixin):
    __tablename__ = 'west'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    qualities = db.Column(db.String)
    desc = db.Column(db.String)
    element = db.Column(db.String)
    planet = db.Column(db.String)
    symbol = db.Column(db.String)
    img = db.Column(db.String)

    # Relationships
    user = db.relationship("User", back_populates="west")

    # Serialize
    serialize_rules = ("-users.west",)

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
