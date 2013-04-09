"""
tipsy.py -- A flask-based todo list
"""
from flask import Flask, render_template, request, redirect, session, url_for, escape
import model

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html", user_name="Adelaide")

@app.route("/tasks")
def list_tasks():
	db = model.connect_db()
	tasks_from_db =	model.get_tasks(db, ) #imports the get_tasks function from model.py
	return render_template("list_tasks.html", tasks=tasks_from_db) #sends retrieved data to a Flask template

@app.route("/done_task", methods=["POST"])
def done_tasks():
	timestamp = request.form['task_complete']
	db = model.connect_db()
	model.complete_task(db, timestamp) #imports the complete_task function from model.py
	return redirect("/tasks") #/tasks page is updated with the {{completed_at}} field

# @app.route("/new_task")
# def new_tasks():
# 	return render_template("new_task.html")

@app.route("/save_task", methods=["POST"])
def save_task():
	title = request.form['title']
	db = model.connect_db()
	task_id = model.new_task(db, title, 2)
	#Assume that all tasks are attached to user 2.
	return redirect("/tasks")

if __name__ == "__main__":
	app.run(debug=True)