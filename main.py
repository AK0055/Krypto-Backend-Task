from fastapi import FastAPI
app = FastAPI()
@app.get("/my-first-api")
def hello():
  return {"Hello world!"}
@app.get("/alerts/create/")
def create():
    price=input('Enter a price limit to set alert')
    @app.get("/alerts/create/"+price)
    def create_alert():
        return {"Alert at price": price}
    return {"Endpoint created"}
def delete():
    delalert=input("enter alert price to delete")
    return delalert


    
@app.delete("/alerts/delete/{tobedel}")
def del_alert(tobedel):
    tobedel=delete()
    return {"Alert at price deleted": tobedel  }
    #return {"Access delete endpoint at":"/alerts/delete/"+tobedel}