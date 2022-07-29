import json
from bson import json_util
import pydantic
from bson.objectid import ObjectId
pydantic.json.ENCODERS_BY_TYPE[ObjectId]=str
from fastapi import FastAPI
import pymongo
myclient = pymongo.MongoClient("mongodb://ak2:1234@cluster0-shard-00-00.lrmw0.mongodb.net:27017,cluster0-shard-00-01.lrmw0.mongodb.net:27017,cluster0-shard-00-02.lrmw0.mongodb.net:27017/?ssl=true&replicaSet=atlas-111t6w-shard-0&authSource=admin&retryWrites=true&w=majority")
mydb = myclient["mydb"]
mycol = mydb["alerts"]
app = FastAPI()
@app.get("/my-first-api")
def hello():
  return {"Hello world!"}
@app.get("/alerts/create/")
def create():
    price=input('Enter a price limit to set alert')
    mydict = { "alert": price, "status":"created" }
    x = mycol.insert_one(mydict)
    print('New alert created') if x else print('Error creating alert')

    @app.get("/alerts/create/"+price)
    def create_alert():
        return {"Alert at price": price}
    return {"Alert "+price+" created"}
def delete():
    delalert=input("enter alert price to delete")
    return delalert

@app.get("/alerts/delete/{tobedel}")
def del_alert(tobedel):
    tobedel=delete()
    myquery = { "alert": tobedel }
    newvalues = { "$set": { "status": "deleted" } }

    mycol.update_one(myquery, newvalues)

    #mycol.delete_one(myquery)
    return {"Alert at price deleted": tobedel  }

@app.get("/alerts/")
def fetchall():
    i=1
    arr={i:"0"}
    for x in mycol.find():
        print(x)
        arr2={"alert":x["alert"],"status":x["status"]}
        arr[i]=arr2
        i+=1
    i=0

    return arr
