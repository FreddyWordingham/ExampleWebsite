from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import mandybrot as mandy

from . import settings


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return settings.TEMPLATES.TemplateResponse("homepage.html", {"request": request})


@app.get("/hello/{name}")
async def hello_name(name: str):
    return f"Hello, {name}!"


class SampleInput(BaseModel):
    real: float
    imag: float


@app.post("/sample")
async def sample(input: SampleInput):
    c = input.real + input.imag * 1j
    max_iters = 100
    return mandy.sample(c, max_iters)


class ImageInput(BaseModel):
    real: float
    imag: float
    width: int
    height: int
    zoom: float
    max_iter: int


@app.post("/image")
async def image(input: ImageInput):
    data = mandy.sample.area(
        input.real, input.imag, input.width, input.height, input.zoom, input.max_iter
    )
    cols = mandy.colour.image(data, input.max_iter, mandy.colour.jet_map)
    img = mandy.colour.encode(cols)
    img.save("static/mandy.png")

    return "Done"
