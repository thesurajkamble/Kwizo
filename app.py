from flask import Flask, request , jsonify , render_template
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
        #user previlage decides whether the user is admin or normal user
        previlage = posteddata["previlage"]

        hashed_pw = bcrypt.hashpw(password.encode('utf8'),bcrypt.gensalt())

        users.insert({
            "Username":username,
            "password":hashed_pw,
            "previlage":previlage
        })

        retJson = {
            "status code": 200,
            "message": "successfully signed up "
        }

        return jsonify(retJson)


def verifyPw(username,password):
    hashed_pw = users.find({
        "Username":username
    })[0]["password"]
    
    if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
        return True
    else:
      return  False


class adminlogin(Resource):
    def post(self):
       
       username = request.form['username']
       password = request.form['password']
       correct_pw = verifyPw(username,password)
       if not correct_pw:
            login_error_json = {
                "staus code":302
            }
            return jsonify(login_error_json)
            return render_template('admin.html')
        
   
@app.route("/admin")
def admin():
    return render_template('index.html')


api.add_resource(Register,"/register")

@app.route("/test")
def test():
    return "works"

if __name__ == "__main__":
    app.run(debug=True)