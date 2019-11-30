from fp_api.extensions import db, ma
from sqlalchemy.dialects.postgresql import UUID

class User(db.Model):
  user_id =       db.Column(db.Integer, primary_key=True)
  uuid =          db.Column(UUID(as_uuid=True), unique=True, nullable=False)
  name =          db.Column(db.String(80), nullable=False)
  playlists =     db.relationship('Playlist', backref='author', lazy=True)

  def __repr__(self):
    return '<User id {} - name {}>'.format(self.id, self.name)

class UserSchema(ma.Schema):
  class Meta:
    model = User
    sqla_session = db.session