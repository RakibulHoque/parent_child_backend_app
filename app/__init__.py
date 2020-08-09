from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

print(os.path.abspath(__file__))
app = FastAPI()

app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(os.path.abspath(__file__)),"static")
), name="static")
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(os.path.abspath(__file__)),"templates")
)

from app.views import main