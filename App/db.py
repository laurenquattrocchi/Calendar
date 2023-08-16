import logging # Logging Library
#from errors import KeyNotFound, BadRequest, InspError
from datetime import datetime


class DB:
    def __init__(self, connection):
        self.conn = connection

    def create_event(self, post_body):
	    """
	    inserts a new event in database
	    input:
	    returns: True is succesful, False otherwise 
	    """

	    try:
	        end_time = post_body['end_time']
	    except KeyError as e:
	    	end_time = None

	    try:
	    	notes=post_body['notes']
	    except KeyError as e:
	    	notes = None

	    try:
	    	category = post_body['category']
	    except KeyError as e:
	    	category = None

	    try:
	    	end_date = post_body['end_date']
	    except KeyError as e:
	    	end_date = None

	    c = self.conn.cursor()

	    insert_event = """INSERT INTO events (title, start_date, start_time, end_date, end_time, notes, category) VALUES (?,?,?,?,?,?,?)"""
	    c.execute(insert_event, [post_body['title'], post_body['start_date'], post_body['start_time'], end_date, end_time, notes, category])
	    event_id = c.lastrowid
	    return event_id
	    #wrap this in try? or enough for function call to be wrapped in server.py
