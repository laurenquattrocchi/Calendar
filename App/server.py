from flask import Flask
import sqlite3  # Our DB

# Configure application
app = Flask(__name__)

# path to database
DATABASE = 'Lauren.db'


# set as configuration? 
connection = sqlite3.connect(DATABASE)


# can pass get_db_conn() to DB object
def get_db_conn():
    """ 
    gets connection to database
    """
    if "_database" not in app.config:
        app.config["_database"] = sqlite3.connect(DATABASE)
        return app.config["_database"] 
    else:
        return app.config["_database"]
