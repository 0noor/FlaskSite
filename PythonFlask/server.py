from flask import Flask, render_template, request,redirect, session,url_for
from pymongo import MongoClient     
from bson.objectid import ObjectId
import bcrypt
app = Flask(__name__)

client = MongoClient("localhost", 27017)

db = client.todoDB

todos = db.todo

users = db.users

app.secret_key = 'BAD_SECRET_KEY'

tasks_validator = {
    '$jasonScema': {
        'bsonType': 'object',
        'required': ['Task','dueDate'],
        'properties': {
            'Task': {'bsontype': 'string'},
            'dueDate':{'bsontype': 'date'},
        }
    }
}

#     }
# }
users_validator= {
    '$jsonSchema': {
    'bsonType': "object",
    'required': ["username", "email", "salt", "hash" ],
    'properties': {
        'username':{
            'bsonType': 'string'},
        'email':{
            'bsonType': "string",
            
        },
        'salt':{
            'bsonType': 'binData'
        },
        'hash':{
            'bsonType': 'binData'
        }

            }
        }
    }


# todos.command('collMod','todo', validator = tasks_validator)
# todo.delete_many({"Task": "Finish Workout", "done": False})

# for todo in todo.find():
#     print(todo)


@app.route('/')
def index():
    all_tasks = todos.find({}).sort({'dueDate': 1 })
    return render_template("index.html",todos = all_tasks)

@app.route('/addtodo', methods=["POST"])
def grab_task():
    if session['username']:
        todos.insert_one({"Task": request.form['task'], 
        "dueDate": request.form['dueDate'],
        "username": session['username']})
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
        filter = {"name": "users"}
        if(db.list_collection_names(filter = filter) == []):
            
            db.create_collection("users",validator=users_validator)
            users.create_index('email', unique = True)
            users.insert_one({"username": request.form["username"],"email": request.form["email"],"salt": salt,"hash": hash})
            
        else:
            # print(request.form['email'])
            session['username'] =request.form["username"]
            users.insert_one({"username": request.form["username"],"email": request.form["email"],"salt": salt,"hash": hash})
            

        

        
        return redirect(url_for("index"))
    
    return render_template("register.html")

@app.route('/login', methods=["POST","GET"])
def log_in():
    if request.method == "POST":
        user = users.find_one({'email': request.form['email']})
        if(user):
            passBytes = request.form['password'].encode('utf-8')
            if(bcrypt.checkpw(passBytes, user['hash'])):
                session['username'] = user["username"]
                return redirect(url_for("index"))
            
    return render_template("login.html")
    







# for todo in todo.find():
#     print(todo)

