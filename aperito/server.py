from flask import Flask, jsonify,send_file, render_template,request
import json
from flask_cors import CORS, cross_origin
import datetime
app = Flask(__name__, template_folder ='build',static_folder='build/static')

CORS(app)
users = {}
users["RODJ"] = {'password':"test1"}
users["PONI"] = {'password':"test2"}

loggedUser = {}


@app.route('/')
def index():
    print(request.remote_addr)
    return render_template('index.html')

@app.route('/test', methods=['POST','GET','PUT'])
def test():
    #print(request.remote_addr)
    print(request.get_json(silent=True))
    items = [{"id": 1, "value": 3, "label": 'Algie'}]
    json_obj = json.dumps(items)
    return json_obj


@app.route('/isUserLoggedIn', methods=['POST','GET'])
def isUserLoggedIn():
    result = {"result": "False"}
    print(request.get_json(silent=True))
    username = request.get_json(silent=True)['username']
    if username in loggedUser:
        if loggedUser[username]["logged_in"]:
            result["result"] = True
    json_obj = json.dumps(result)
    return json_obj


@app.route('/login', methods=['POST','GET'])
def login():
    #print(request.remote_addr)
    username = request.get_json(silent=True)['username']
    password = request.get_json(silent=True)['password']
    print(request.get_json(silent=True))
    print(username)
    print(password)
    result = {"result":"False"}
    if username in users:
        if password == users[username]['password']:
            loggedUser[username]={"logged_in":True, "timestamp": datetime.datetime.now()}
            result["result"] = True

    json_obj = json.dumps(result)
    return json_obj



if __name__ == '__main__':
    app.run(host='localhost', debug=True, port=5050)