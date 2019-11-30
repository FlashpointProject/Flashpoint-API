import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from fp_api import app
from fp_api.extensions import db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()