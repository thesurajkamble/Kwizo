from flask import Flask, request , jsonify
from flask_restful import Api , Resource
import bcrypt
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

#database connection
DBclient = MongoClient("mongodb://localhost:27017/")

#created questionsDB database
questionsDB = DBclient.questionsDB

#users db
users = questionsDB["users"]

#create 'general knowledge' collection
GeneralKnowledgeCollection = questionsDB["GeneralKnowledgeCollection"]

#create 'current affairs ' collections
CurrentAffairsCollection = questionsDB["CurrentAffairsCollection"]

class Register(Resource):
    def post(self):
        posteddata = request.get_json(force=True)

        username = posteddata["username"]
        password = posteddata["password"]

        hashed_pw = bcrypt.hashpw(password.encode('utf8'),bcrypt.gensalt())

        users.insert({
            "Username":username,
            "password":hashed_pw,
        })

        retJson = {
            "status code": 200,
            "message": "successfully signed up "
        }

        return jsonify(retJson)


api.add_resource(Register,"/register")

@app.route("/test")
def test():
    return "works"

if __name__ == "__main__":
    app.run(debug=True)