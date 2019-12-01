from fp_api.models import Playlist
from fp_api.models import User
from fp_api.extensions import db
from fp_api.app import app

USERS = [
  {
    'name': 'Bob'
  },
  {
    'name': 'Derek'
  }
]

PLAYLISTS = [
  {
    'author_id': '1',
    'name': 'Test Playlist One'
  },
  {
    'author_id': '1',
    'name': 'Test Playlist Two'
  },
  {
    'author_id': '2',
    'name': 'Test Playlist Three'
  }
]

with app.app_context():
  for user in USERS:
    u = User(name=user['name'])
    db.session.add(u)

  for playlist in PLAYLISTS:
    p = Playlist(author_id=playlist['author_id'], name=playlist['name'])
    db.session.add(p)

  db.session.commit()