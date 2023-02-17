from fastapi import FastAPI
import datetime

app = FastAPI()

@app.get("/")
def homepage():
    time = datetime.datetime.now()
    return f"The time is {time}"
