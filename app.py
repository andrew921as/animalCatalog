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
  
#Un endpoint que traiga la informacion de un grupo de animales

#Un endpoint que traiga la informacion de un solo animal
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# #Un endpoint que cree un animal
# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
# 		return {"item_name": item.name, "item_id": item_id}

#Un endpoint que actualice un animal

#Un endpoint que inhabilite un animal

#Un endpoint que relacione un animal con un padrino
