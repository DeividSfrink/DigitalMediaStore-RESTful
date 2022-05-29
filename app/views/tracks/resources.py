from flask.views import MethodView
from flask_smorest import Page

from app.extensions.api import CursorPage  # noqa:F401
from app.extensions.api import Blueprint
from app.models.track import Track

from .schemas import TrackSchema

blp = Blueprint("Track", __name__, url_prefix="/api/Tracks", description="API endpoints about Track")


@blp.route("/")
class Tracks(MethodView):
    @blp.etag
    # @blp.arguments(ArtistQueryArgsSchema, location="query")
    @blp.response(200, TrackSchema(many=True))
    @blp.paginate(Page)
    @blp.doc(description="Get information for multiple artists")
    def get(self):
        """List artists"""
        ret = Track.find_all()
        return ret

    @blp.etag
    @blp.arguments(TrackSchema)
    @blp.response(201, TrackSchema)
    @blp.doc(description="Add information for a single artist")
    def post(self, new_track):
        """Add a new artist"""
        item = Track(**new_track)
        item.create()
        return item


@blp.route("/<int:id>")
class TrackById(MethodView):
    @blp.etag
    @blp.response(200, TrackSchema)
    @blp.doc(description="Get information for a single artist")
    def get(self, id):
        """Get artist by ID"""
        ret = Track.find_by_id(id)
        return ret

    @blp.etag
    @blp.arguments(TrackSchema)
    @blp.response(200, TrackSchema)
    @blp.doc(description="Update information for an artist")
    def put(self, data, id):
        """Update an existing artist"""
        item = Track.find_by_id(id)
        blp.check_etag(item, TrackSchema)
        TrackSchema().update(item, data)
        item.update()
        return item

    @blp.etag
    @blp.response(204)
    @blp.doc(description="Delete information for a single artist")
    def delete(self, id):
        """Delete an existing artist"""
        item = Track.find_by_id(id)
        blp.check_etag(item, TrackSchema)
        item.delete()
