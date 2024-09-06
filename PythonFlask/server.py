from flask import Flask, render_template, request,redirect,url_for
import pymongo
from pymongo import MongoClient     
app = Flask(__name__)

client = MongoClient("localhost", 27017)

db = client.todoDB

todo = db.todo



# todo.delete_many({"Task": "Finish Workout", "done": False})

# for todo in todo.find():
#     print(todo)


@app.route('/')
def index():
    return render_template("index.html",)

@app.route('/addtodo', methods=["GET","POST"])
def grab_task():
    todo.insert_one({"Task": request.form['task'], 
    "StartDate": request.form['startDate'],
    "EndDate": request.form['endDate'],
    "localTime": request.form['todaysDate']})
    return redirect(url_for('index'))

# @app.route('/user')
# def greet_user():
#     return "<h1>Hello User</h1>"