from app.extensions.schema import ma
from app.models.track import Track
from app.views.albums.schemas import AlbumSchema


class TrackSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Track

    id = ma.auto_field(dump_only=True)
