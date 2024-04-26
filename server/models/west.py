from . import SerializerMixin, db


class West(db.Model, SerializerMixin):
    __tablename__ = "west"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    qualities = db.Column(db.String)
    desc = db.Column(db.String)
    element = db.Column(db.String)
    planet = db.Column(db.String)
    symbol = db.Column(db.String)
    img = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user_zodiac_id = db.Column(db.Integer, db.ForeignKey("user_zodiac.id"))

    # Relationships
    users = db.relationship("User", back_populates="west")
    user_zodiac = db.relationship("UserZodiac", back_populates="west", foreign_keys=[user_zodiac_id])

    # Serialize
    serialize_rules = ("-user.west",)

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
