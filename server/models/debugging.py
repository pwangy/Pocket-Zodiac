class UserZodiac(db.Model, SerializerMixin):
    __tablename__ = "user_zodiac"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    west_id = db.Column(db.Integer, db.ForeignKey("west.id"))
    east_id = db.Column(db.Integer, db.ForeignKey("east.id"))
    east_west = db.Column(db.String)
    additional_birthdate = db.Column(
        db.DateTime, default=datetime.now().date().strftime("%Y-%m-%d")
    )

    # Relationships
    users = db.relationship("User", back_populates="user_zodiac")
    east = db.relationship(
        "East",
        back_populates="user_zodiac",
        foreign_keys=[east_id],
        uselist=False,
        primaryjoin="UserZodiac.east_id == East.id",
        remote_side="East.id",
    )
    west = db.relationship("West", back_populates="user_zodiac", foreign_keys=[west_id])

    # Serialize
    serialize_rules = ("-user.user_zodiac", "-east.user_zodiac", "-west.user_zodiac")
