from app.extensions import db

class User(db.Model):
  id =            db.Column(db.Integer, primary_key=True)
  name =          db.Column(db.String(80), nullable=False)
  playlists =     db.relationship('Playlist', backref='author', lazy=True)