# Flashpoint-API
API for various networked Flashpoint tasks

### Requirements

A PostgreSQL server for database operations.

### Setup Configuration

Install python requirements through `pip3 install -r app/requirements.txt` (You may wish to use a [venv](https://docs.python.org/3/library/venv.html) instead)

For production deployments install gunicorn. Examples are linked in the Running and Maintenance section below. `pip3 install gunicorn`

Make a copy of app/config.py.example into app/config.py and open it for editing

Change the secret key to an appropriate random string

Change the database URI to the correct form of your postgresql database. Example - `postgresql://user:pass@host:port/db`

### Running and Maintenance

Run in a development environment with `python3 -m fp_api`

Run in a production environment with gunicorn. Various setups suggested [here.](https://stackoverflow.com/a/35839360)

Upgrade your database tables with the  `python3 manage.py db upgrade`

### Development

Produce database revisions with `python3 manage.py db migrate (-m <message>)`