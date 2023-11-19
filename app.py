from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from routes.animals_routes import animal
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Item(BaseModel):
		name: str
		price: float
		is_offer: bool = None

#Un endpoint que liste todos los animales
app.include_router(animal)
