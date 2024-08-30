from flask import Flask, render_template, request,redirect,url_for
import pymongo
from pymongo import MongoClient     
app = Flask(__name__)

client = MongoClient("localhost", 27017)

db = client.todoDB

todo = db.todo



# todo.delete_many({"Task": "Finish Workout"})

# for todo in todo.find():
#     print(todo)


@app.route('/')
def hello_world():
    return render_template("index.html")

# @app.route('/user')
# def greet_user():
#     return "<h1>Hello User</h1>"