from flask import Flask, request
import sqlite3  # Our DB
from db import DB
import logging

# Configure application
app = Flask(__name__)

# path to database
DATABASE = 'Lauren.db'


# set as configuration? 
connection = sqlite3.connect(DATABASE)

### to do:
# update doc strings with input/output types
# 


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

# default path
@app.route('/')
def home():
    return "home"
    #return render_template("home.html")


@app.route("/create", methods=["POST"])
def create():
    """creates event - loads new event into  database
    input: start date, start time, title
        optional: end time, notes, category, end date (multi day events)
    output: none
    """
    db = DB(get_db_conn())

    #gets json params
    post_body = request.json

    # gets parameters from URL
    #post_body = request.args
    
    if not post_body:
        #logging.error("No post body")
        return Response(status=400)

    event_id = db.create_event(post_body)
    logging.debug("created", event_id)
    db.conn.commit()

    return {"event_id": event_id}, 201

    # try:
    #     # add a record via the DB class
    #     created = db.create_event(post_body)
    #     logging.debug("created", created)
    #     # update for a check before commiting?
    #     # if app.config["INSPEC_COUNTER"] == app.config["TRANSACTION_SIZE"]:
    #     #     db.conn.commit() #only commit if # of times inspection posted = transaction size
    #     #     logging.debug("committed transaction")
    #     #     app.config["INSPEC_COUNTER"]=0
    #     if created:
    #         db.conn.commit()
    #         return event_data, 200         
    # #except BadRequest as e:
    # except Exception as e: 
    #     db.conn.rollback() #rollback if error
    #     #update errors.py to use this
    #     #raise InvalidUsage(e.message, status_code=e.error_code)
    #     return 400
    # except sqlite3.Error as e:
    #     logging.error(e) # confirm what this is doing
    #     db.conn.rollback() #rollback if error
    #     #raise InvalidUsage(str(e))
    #     return 400

    # event_data = post_body ##formattt, may get from create_event resp

    # if created:
    #     return event_data, 200
    # else:
    #     return 400

@app.route("/schedule",  methods=["GET", "POST"])
def get_schedule():
    """creates event
    input: year 
        optional: month, day, timeframe
    output: events scheduled in given time frame 
    """

    # get date from user to retrieve events in given timeframe


@app.route("/update/<int:event_id>", methods=["POST"])
def update():
    """cupdates pre_exisiting event
    input: event id (int)
    output: updated event information (str or dict??)
    """

    # update option appears on schedule page, automatically sends through event_id when
    # click on specific event to update

    # display event in form that can be updated?


@app.route("/delete/<int:event_id>", methods=["POST"])
def delete():
    """creates event
    input: event id (int)
    output: "Event: {event_title}, has been deleted" (str)
    """

    # delete option appears on schedule page, automatically sends through event_id



