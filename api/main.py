from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def homepage():
    return f"Hello, world!"


@app.get("/hello/{name}")
async def hello_name(name: str):
    return f"Hello, {name}!"
