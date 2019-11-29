import os
from flask import Flask, render_template
from app.config import DevelopmentConfig
from app.extensions import db
from app.models import playlist

def create_app(config_object=DevelopmentConfig):
  app = Flask(__name__)
  app.config.from_object(config_object)
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  register_extensions(app)
  return app

def register_extensions(app):
  db.init_app(app)

app = create_app()

@app.route("/", methods=['GET'])
def hello():
  return render_template('index.html')

if __name__ == "__main__":
  app.run()