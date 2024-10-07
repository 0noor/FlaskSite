from flask import Flask, render_template, request,redirect,url_for
from pymongo import MongoClient     
from bson.objectid import ObjectId
import bcrypt
app = Flask(__name__)

client = MongoClient("localhost", 27017)

db = client.todoDB

todos = db.todo

users = db.user



# todo.delete_many({"Task": "Finish Workout", "done": False})

# for todo in todo.find():
#     print(todo)


@app.route('/')
def index():
    all_tasks = todos.find({}).sort({'dueDate': 1 })
    return render_template("index.html",todos = all_tasks)

@app.route('/addtodo', methods=["POST"])
def grab_task():
    todos.insert_one({"Task": request.form['task'], 
    "dueDate": request.form['dueDate'],
    "completed": False})
    return redirect(url_for('index'))

@app.route('/delete/<id>', methods=["POST"])
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))



@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":    
        bytes =  request.form["password"].encode('utf-8')
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(bytes,salt)
        users.insert_one({"username": request.form["username"],"email": request.form["email"],"salt": salt,"hash": hash})
        return redirect(url_for("index"))
    
    return render_template("register.html")

@app.route('/login', methods=["POST","GET"])
def log_in():
    if request.method == "POST":
        return redirect(url_for("index"))
    print(users.find({"email":  request.form["email"]}))
    return render_template("login.html")
    



# todo.insert_one({"Task": "Finish Workout"})



# for todo in todo.find():
#     print(todo)

