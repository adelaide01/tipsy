"""
model.py
"""

import sqlite3
from datetime import datetime

def connect_db():
    return sqlite3.connect("tipsy.db")
    
def new_user(db, email, password, user_name):
    c = db.cursor()
    query = """INSERT INTO Users Values (NULL, ?,?,?)"""
    result = c.execute(query, (email, password, user_name))           
    db.commit()
    return result.lastrowid

def authenticate(db, email, password):
    c = db.cursor()
    query = """SELECT * FROM Users WHERE email=? AND password=?"""
    c.execute(query, (email, password))
    result = c.fetchone()
    if result:
        fields = ["user_id", "email", "password", "user_name"]
        return dict(zip(fields, result))
    return None

def get_user(db, user_id):
    """Gets a user dictionary out of the database given an id"""
    c = db.cursor()
    query = """SELECT * FROM Users WHERE user_id = ?"""
    c.execute(query, (user_id,))
    result = c.fetchone()
    if result:
        fields = ["user_id", "email", "password", "user_name"]
        return dict(zip(fields, result))
    return result.lastrowid

def new_task(db, title, task_user_id):
    """Given a title and a task_user_id, create a new task belonging to that user. Return the id of the created task"""
    time_in = datetime.now()
    c = db.cursor()
    query = """INSERT INTO Tasks Values (NULL, ?, ?, NULL, ?)"""
    result = c.execute(query, (title, time_in, task_user_id))
    db.commit()
    return result.lastrowid        

def complete_task(db, task_id):
    """Mark the task with the given id as being complete."""
    time_out = datetime.now()
    c = db.cursor()
    query = """UPDATE Tasks SET completed_at=? WHERE task_id = ?"""
    c.execute(query, (time_out, task_id))
    db.commit()
    print "Task completed %s." % time_out

def get_task(db, task_id):
    """Gets a single task, given its id. Returns a dictionary of the task data."""
    c = db.cursor()
    query = """SELECT * FROM Tasks WHERE task_id = ?"""
    c.execute(query, (task_id,))
    result = c.fetchone()
    if result:
        fields = ["task_id", "title", "created_at", "completed_at", "task_user_id"]
        return dict(zip(fields, result))
    return result.lastrowid 
    
def get_tasks(db, task_user_id = None):
    """Get all the tasks matching the user_id, getting all the tasks in the system if the user_id is not provided. Returns the results as a list of dictionaries."""
    fields = ["task_id", "title", "created_at", "completed_at", "task_user_id"]
    c = db.cursor()
    if task_user_id:
        query = """SELECT * FROM Tasks WHERE task_user_id = ?"""
        c.execute(query, (task_user_id,))
        result = c.fetchall()
        return dict(zip(fields, result))
    else:
        query = """SELECT * FROM Tasks"""
        c.execute(query,)
        result = c.fetchall()
        l = []
        for row in result:
            l.append(dict(zip(fields, row)))
        return l