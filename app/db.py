import click
import pymongo
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    mongocon = current_app.config['MONGO_CON']
    dbclient = pymongo.MongoClient(mongocon)
    g.db = dbclient[current_app.config['DATABASE']]
    return g.db

def get_collection(colname):
    if 'db' not in g:
        print("HERE")
        get_db()
    return g.db[colname]

"""
Helper function to query all pond on system 
"""
def get_ponds(filter={}):
    collection = get_collection("pond")
    return collection.find(filter)

def get_pond(filter={}):
    collection = get_collection("pond")
    return collection.find_one(filter)

def insert_pond(data):
    collection = get_collection("pond")
    collection.insert_one(data)
    return 1

def update_pond(filter, update):
    collection = get_collection("pond")    
    return collection.update_one(filter, update, upsert=False)    

def delete_pond(data):
    collection = get_collection("pond")
    collection.delete_one(data)

def close_db(e=None):
    db = g.pop(current_app.config['DATABASE'], None)
    
    if db is not None:
        db.close() 

def init_db():
    """clear the existing data and create new tables."""    
    db = get_db()    
    db.client.drop_database(current_app.config['DATABASE'])
    
@click.command('init-db')
@with_appcontext
def init_db_command():    
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)



