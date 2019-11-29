from app.extensions import db
from app.models.helpers import playlist_games
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import func

class Playlist(db.Model):
  id =                db.Column(db.Integer, primary_key=True)
  uuid =              db.Column(UUID(as_uuid=True), unique=True, nullable=False)
  author_id =         db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  date_created =      db.Column(db.DateTime, default=func.now())
  date_modified =     db.Column(db.DateTime, default=func.now())
  name =              db.Column(db.String(80), nullable=False)
  extreme =           db.Column(db.Boolean, default=False)
  games =             db.relationship('Game', secondary=playlist_games)

  def __init__(self, author_id, name, extreme):
    self.author_id = author_id
    self.name = name
    self.extreme = extreme

  def __repr__(self):
    return '<id {} - name {}>'.format(self.id, self.name)