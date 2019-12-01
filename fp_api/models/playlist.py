from fp_api import app
from fp_api.extensions import db, ma
from fp_api.models.game import Game
from fp_api.models.helpers import playlist_games
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import func
import uuid
from flask import jsonify

class Playlist(db.Model):
  playlist_id =       db.Column(db.Integer, primary_key=True)
  uuid =              db.Column(UUID(as_uuid=True), unique=True, nullable=False, default=uuid.uuid4)
  author_id =         db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
  date_created =      db.Column(db.DateTime, default=func.now())
  date_modified =     db.Column(db.DateTime, default=func.now())
  name =              db.Column(db.String(80), nullable=False)
  extreme =           db.Column(db.Boolean, default=False)
  games =             db.relationship('Game', secondary=playlist_games)

  def __repr__(self):
    return '<Playlist id {} - name "{}">'.format(self.playlist_id, self.name)

class PlaylistSchema(ma.ModelSchema):
  class Meta:
    model = Playlist
    sqla_session = db.session

playlist_schema = PlaylistSchema()

def get_many():
  playlists = db.session.query(Playlist).all()
  playlists_schema = PlaylistSchema(many=True)
  return playlists_schema.dump(playlists)