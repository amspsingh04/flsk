import sqlite3

import click
from flask import current_app, g #g(store data) and current_app(points to the flask app) are special objects

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect( 
            current_app.config['DATABASE'], 
            detect_types=sqlite3.PARSE_DECLTYPES
        ) #connects with the database file
        g.db.row_factory=sqlite3.Row
        #accessing database
        return g.db
    
def close_db(e=None):
    db=g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db=get_db() 

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
    
@click.command('init-db')
def init_db_command():
    init_db()
    click.echo('Initialised the database')
    #make new DB

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)