import json
from bson import json_util
import pydantic
from bson.objectid import ObjectId
import requests
pydantic.json.ENCODERS_BY_TYPE[ObjectId]=str
from fastapi import FastAPI
import pymongo
import jwt
import smtplib, ssl

alerts=[]
myclient = pymongo.MongoClient("mongodb://ak2:1234@cluster0-shard-00-00.lrmw0.mongodb.net:27017,cluster0-shard-00-01.lrmw0.mongodb.net:27017,cluster0-shard-00-02.lrmw0.mongodb.net:27017/?ssl=true&replicaSet=atlas-111t6w-shard-0&authSource=admin&retryWrites=true&w=majority")
mydb = myclient["mydb"]
mycol = mydb["alerts"]
app = FastAPI()
@app.get("/")
def hello():
  return {"CryptoAlert is running"}
@app.get("/alerts/create/")
def create():
    price=input('Enter a price limit to set alert')
    mydict = { "alert": price, "status":"created" }
    x = mycol.insert_one(mydict)
    print('New alert created') if x else print('Error creating alert')

    @app.get("/alerts/create/"+price)
    def create_alert():
        return {"Alert at price": price}
    return {"Alert for price:"+price+" created"}


@app.get("/alerts/delete")
def del_alert():
    tobedel=input("enter alert price to delete")
    myquery = { "alert": tobedel }
    newvalues = { "$set": { "status": "deleted" } }

    mycol.update_one(myquery, newvalues)

    #mycol.delete_one(myquery)
    return {"Alert at price deleted": tobedel  }

@app.get("/alerts/")

def fetchall():
    i=1
    global alerts
    arr={i:"0"}
    for x in mycol.find():
        print(x)
        arr2={"alert":x["alert"],"status":x["status"]}
        arr[i]=arr2
        alerts.append(x["alert"]) if x["status"]=="created" else print('Current alert is deleted')
        i+=1
    i=0
    token = jwt.encode(
    payload=arr,
    key='mysecret'
    )
    print('Your JWT token is:'+token)
    
    
    return jwt.decode(token, key='mysecret', algorithms=['HS256', ])

def getcurrent():
    api_url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false"
    response = requests.get(api_url)
    res=response.json()
    currprice=res[0]["current_price"]
    return currprice

@app.get("/trigger/")
def trigger():
    global alerts
    useremail=input("Please enter your email")
    

    port = 587  # For starttls
    smtp_server = "smtp-mail.outlook.com"
    sender_email = "ak_0055@outlook.com"
    receiver_email = useremail
    password = "Ajay@2001"
    message = """\
    Subject: Alert triggered!

    Your alert that has been set for BTC value is now triggered and the current price has exceeded"""

    
    #print(alerts)
    if alerts:
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo() 
            server.starttls(context=context)
            server.ehlo() 
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            print("The mail was sent successfully")
        for i in alerts:
            #print(i,getcurrent())
            if  getcurrent()<= int(i):
                print("Triggering "+i)
                myquery = { "alert": i }
                newvalues = { "$set": { "status": "triggered" } }
                mycol.update_one(myquery, newvalues)
        return {"Triggered"}

@app.get("/alerts/filter")
def filter():
    statuser=input("enter status to filter")
    myquery = { "status": statuser }
    mydoc = mycol.find(myquery)
    i=0
    arr={i:"Not found"}
    for x in mydoc:
        print(x)
        arr2={"alert":x["alert"],"status":x["status"]}
        arr[i]=arr2
       
        i+=1
    i=0

    return arr