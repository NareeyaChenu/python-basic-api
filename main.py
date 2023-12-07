
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello, world!"}



@app.get("/users")
def get_user () : 
    return {"name" : "Nareeya"}
