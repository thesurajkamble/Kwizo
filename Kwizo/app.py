from flask import Flask, request , jsonify , render_template , json
from flask_restful import Api , Resource
import bcrypt
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.KwizoDB
gk = db['ganeral-knowledge']
current_affairs = db['current-affairs']
indian_polity = db['indian-polity']


@app.route("/questoins/<category>",methods=['POST'])
def Add_questions(category):
    print(category)

    questionname = request.form['questionname']
    optA = request.form['optA']
    optB = request.form['optB']
    optC = request.form['optC']
    optD = request.form['optD']
    Answer = request.form['Answer']

    try:
        if category == "gk":
            gk.insert({
           "questionname": questionname,
           "optA": optA,
           "optB": optB,
           "optC":optC,
           "optD": optD,
           "answer" :Answer
          })
        elif category == "current_affairs":
            current_affairs.insert({
            "questionname": questionname,
            "optA": optA,
            "optB": optB,
            "optC":optC,
            "optD": optD,
            "answer" :Answer
             })
        elif category == "indian_polity":
            gk.insert({
            "questionname": questionname,
            "optA": optA,
            "optB": optB,
            "optC":optC,
            "optD": optD,
            "answer" :Answer
        })

        else:
            error ={
                "msg": "invalid category"
            }
            return jsonify(error)


        saved_json = {
        "msg": "questions saved successfully"
        }
        return jsonify(saved_json)

    except Exception:
          Exception_json = {
                 "msg": "error saving questions "
                           }
          return jsonify(Exception_json)

      


@app.route("/questions?/getQuestions/<category>",methods=['GET'])
def get_questions(category):
     documents = category.find()
     response = []
     for document in documents:
        document['_id'] = str(document['_id'])
        response.append(document)
     return json.dumps(response)



if __name__ == "__main__":
    app.run(debug=True)
