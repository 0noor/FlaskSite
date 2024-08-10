from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1><b>Hello, Brother!</b></h1>"

@app.route('/user')
def greet_user():
    return "<h1>Hello User</h1>"