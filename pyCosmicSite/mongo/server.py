from unicodedata import name
from flask import Flask, Response
from bson.objectid import ObjectId
import json
import pymongo
import re


app  = Flask(__name__)
try:
    mongo = pymongo.MongoClient(host="localhost",port=27017,serverSelectionTimeoutMS = 1000)
    db = mongo.MFMONGODB
    db1 = mongo.School
    # This line of code will trigger the Exception
    mongo.server_info()
except Exception as ex: 
    print(f"Cant connect to DB! {ex}")
# #######################
# @app.route("/users", methods=["POST"])
def createCars(NameOfCars,PriceOfCars):
            car = {
            "Name": f"{NameOfCars}",
            "Price": f"{PriceOfCars}"
            }
            dbResponse = db1.cosmic.insert_one(car)
            print(dbResponse.inserted_id)

def createUser(firstN,lastN,UserN,PWord,Card,City,State):
    try:
        m = re.compile("[A-Za-z]")
        Name = firstN+ " " +lastN +" "+ City +" "+ State
        if not re.search(m,Name): return print(f"{Name} Only use letters! Also, You're not registered! Now, do it again!") 
        else : print("verified") 
        user = {
            "fName": f"{firstN}",
            "LName": f"{lastN}",
            "UName": f"{UserN}",
            "PassW": f"{PWord}",
            "Card/CheckInfo":Card,
            "location":{
                "City":f"{City}",
                "State":f"{State}"
            }
        } 
        dbResponse = db.users.insert_one(user)
        print(dbResponse.inserted_id)
        return Response(
            response= json.dumps({"message":"user created!","id": f"{dbResponse.inserted_id}"}),
            status='200',
            mimetype='application/json'
        )
    except Exception as ex:
        print(ex)
######################
@app.route("/users/<id>", methods=["PATCH"])

def CardInfoName(Id,Pay):
    payInfo = db.users.update_one({"_id":ObjectId(Id)},{"$set":{"Card":Pay}})
    return payInfo
def UpdateUser(id,UserN,Pass):
    try:
        dbResponse = db.users.update_one({"_id":ObjectId(id)},{"$set":{"UName":f"{UserN}","PassW":f"{Pass}"}})
        # for item in dir(dbResponse):
        #     print(f"{item}")
        return Response(
        response = json.dumps({"message":" Updated!"}),
        status='200',
        mimetype='application/json'
    )
    except Exception as Ex:
        print(Ex)
        return Response(
        response= json.dumps({"message":"Sorry! Cant update!"}),
        status='500',
        mimetype='application/json'
    )
#######################
def deleteUser(Id):
    try:
        results = db.users.delete_one({"_id":ObjectId(Id)})
        if results : print('Your account is deleted!')
    except Exception as ex:
        print(ex)    
#######################
if __name__ == '__main__':
    app.run(port=5555,debug=True)