from flask import Flask, render_template, request,redirect,url_for
from pymongo import MongoClient     
from bson.objectid import ObjectId
app = Flask(__name__)

client = MongoClient("localhost", 27017)

db = client.todoDB

todos = db.todo



# todo.delete_many({"Task": "Finish Workout", "done": False})

# for todo in todo.find():
#     print(todo)


@app.route('/')
def index():
    all_tasks = todos.find({}).sort({'dueDate': 1 })
    return render_template("index.html",todos = all_tasks)

@app.route('/addtodo', methods=["GET","POST"])
def grab_task():
    todos.insert_one({"Task": request.form['task'], 
    "dueDate": request.form['dueDate'],
    "completed": False})
    return redirect(url_for('index'))

@app.route('/delete/<id>', methods=["POST"])
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))


# @app.route('/add_todo', methods=['POST'])
# def add_todo():
    

# @app.route('/user')
# def greet_user():
#     return "<h1>Hello User</h1>"


# todo.insert_one({"Task": "Finish Workout"})



# for todo in todo.find():
#     print(todo)

