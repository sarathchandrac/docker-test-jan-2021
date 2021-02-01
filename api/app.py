from pymongo import MongoClient
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from bson.json_util import dumps
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
api = Api(app)

mongoCluster = MongoClient(
    "mongodb+srv://csc:data%40123@cluster0.saqhn.mongodb.net/test?authSource=admin&replicaSet=atlas-vp6kfn-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
db = mongoCluster["test"]
test_collection = db["test"]


class Users(Resource):
    def post(self):
        return "x"

    def get(self):
        return jsonify(dumps(test_collection.find({})))



@app.errorhandler(404)
def not_found(error=None):
    message = {
        status: 404,
        'message': 'Not Found' + request.url
    }
    return jsonify(message)


def checkPostedData(postedData, functionName):
    if(functionName == "add"):
        if "num1" not in postedData or "num2" not in postedData:
            return 301
        else:
            return 200

            

class Add(Resource):
    def post(self):
        params = request.get_json()
        if "num2" not in params or "num1" not in params:
            return "Parameter num2  or num1 is not passed", 305

        num1 = params["num1"]
        num2 = params["num2"]
        status_code = checkPostedData(params, "add")
        if(status_code != 200):
            retJson = {
                "Message": "An error happend",
                "Status Code": status_code
            }
            return jsonify(retJson)
        return jsonify({
            'Message': num1 + num2,
            'Status Code': 200
        })


api.add_resource(Add, "/add")
api.add_resource(Users, "/users")


@app.route('/users1')
def get_users():
    users = [
        {
            "name": "user1",
            "email": "user1@mail.com"
        }
    ]
    return jsonify(users)


#############################


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
