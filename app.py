from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


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


class Subtract(Resource):
    pass


api.add_resource(Add, "/add")


@app.route('/')
def hello_world():
    return "Hello World"


@app.route('/users')
def get_users():
    users = [
        {
            "name": "user1",
            "email": "user1@mail.com"
        }
    ]
    return jsonify(users)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
