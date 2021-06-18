from flask import Flask
from flask import request
from flask_cors import CORS
from flask.templating import render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
CORS(app)

mongodb_client = PyMongo(app, uri="mongodb+srv://goeun:goeunrealpassword@cluster0.5xfl6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = mongodb_client.db

@app.route('/')
def hello_world():
    return render_template('inputEmail.html')

@app.route('/post',methods=['POST'])
def post():
    value = request.form['email']
    print(value)
    data=db.board
    nowPost={
        "email":value
    }

    data.insert_one(nowPost)
    return "done! waiting for alarm😍"

if __name__=='__main__':
    app.run()