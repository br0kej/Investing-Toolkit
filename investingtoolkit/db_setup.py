import os
from investingtoolkit import database


def db_presence_check():
    if os.path.isfile('./db.sqlite'):
        return True

def db_creation():
    dbms = database.Database(database.SQLITE, dbname='db.sqlite')
    print('[+] Creating Datbase')
    dbms.create_db_tables()