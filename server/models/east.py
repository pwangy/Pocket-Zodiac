# from .user_zodiac import UserZodiac
from . import SerializerMixin, validates, re, db
from importlib import import_module


class East(db.Model, SerializerMixin):
    __tablename__ = "east"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    qualities = db.Column(db.String)
    desc = db.Column(db.String)
    polarity = db.Column(db.String)
    order_12 = db.Column(db.Integer)
    order_60 = db.Column(db.Integer)
    # element_id = db.Column(db.Integer, db.ForeignKey("element.id"))
    img = db.Column(db.String)
    # user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    # Relationships
    # elements = db.relationship("Element", back_populates="east", foreign_keys=[element_id])
    # users = db.relationship("User", back_populates="east")
    # user_zodiac_id = db.Column(db.Integer, db.ForeignKey("user_zodiac.id"))

    # def get_user_zodiac_join(self):
    #     from .user_zodiac import UserZodiac
    #     return self.user_zodiac_id == UserZodiac.id

    # user_zodiac = db.relationship(
    #     "UserZodiac",
    #     back_populates="east",
    #     foreign_keys=[user_zodiac_id],
    #     remote_side="UserZodiac.east_id",
    #     primaryjoin=get_user_zodiac_join,
    # )

    # Serialize
    # serialize_rules = ("-elements.east", "-user_zodiac.east")

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
                img: {self.img}
            />
        """
                # element_id: {self.element_id}

    @validates("img")
    def validate_img(self, _, img):
        if not isinstance(img, str):
            raise TypeError("Images must be strings")
        elif not re.match(r"^https?:\/\/.*\.(?:png|jpeg|jpg)$", img):
            raise ValueError(
                f"{img} has to be a string of a valid url ending in png, jpeg or jpg"
            )
        return img
