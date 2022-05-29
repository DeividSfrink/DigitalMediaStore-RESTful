from app.extensions.database import BaseModelMixin, db


class Track(db.Model, BaseModelMixin):
    __tablename__ = "Track"
    id = db.Column(name="ArtistId", type_=db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(name="Name", type_=db.Unicode(120), nullable=False, unique=True)
    media_type_id = db.Column(name="MediaTypeId", type_=db.Integer, nullable=False, default=1)
    composer = db.Column(name="Composer", type_=db.Unicode(220))
    milliseconds = db.Column(name="Milliseconds", type_=db.Integer, nullable=False)
    bytes = db.Column(name="Bytes", type_=db.Integer, default=None, nullable=False)
    unit_price = db.Column(name="UnitPrice", type_=db.Numeric(10, 2), nullable=False, default=1)

    #albums = db.relationship(
    #    "Album", backref=db.backref("artist", cascade_backrefs=False), lazy="select", cascade="all, delete-orphan"
    #)

    def __repr__(self):
        return f"<Track {self.name}>"

    def __str__(self):
        return self.name

    # def save(self):
    #     BaseModelMixin.save(self)
    #     self.id

    @classmethod
    def find_track_by_name(cls, name):
        return cls.simple_filter(name=name).first()
