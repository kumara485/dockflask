from flask import Flask,json,jsonify
from pymongo import MongoClient
import bson.json_util as json_util
from bson import ObjectId
app = Flask(__name__)

client = MongoClient('localhost', 27017)
mydb = client["mydb"]
mycol = mydb["mycol"]
@app.route("/")
def getAll():
    for x in mycol.find():
        return json_util.dumps(x)

if __name__=="__main__":
    app.run(debug=True)

