import os
import connexion
from flask import Flask, render_template
from fp_api.config import DevelopmentConfig
from fp_api.extensions import db, ma
from fp_api.models import playlist

def create_app(config_object=DevelopmentConfig):
  connex_app = connexion.App(__name__, specification_dir=basedir)
  connex_app.add_api('api.yaml')
  app = connex_app.app
  app.config.from_object(config_object)
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  register_extensions(app)
  return app

def register_extensions(app):
  db.init_app(app)
  ma.init_app(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app = create_app()

if __name__ == "__main__":
  app.run(debug=True)