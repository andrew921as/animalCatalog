from fastapi import APIRouter
from config.db import client
from schemas.animals_schemas import animalEntity, animalsEntity
from models.animal_model import Animal
from bson import ObjectId


animal = APIRouter()

@animal.get('/animals')
def read_root():
    return animalsEntity(client.catalogo_animales.animales.find())
    
@animal.post('/animals')
def create_animal(animal: Animal):
    new_animal = dict(animal)
    #del new_animal["id"]
    id = client.catalogo_animales.animales.insert_one(new_animal).inserted_id
    animal = client.catalogo_animales.animales.find_one({"_id": id})
    return animalEntity(animal)

@animal.patch('/animals/{animalID}')
def update_animal(update_data: dict, animalID: str):
    #updateAnimal = dict(animal)
    #animal = client.catalogo_animales.animales.find_one_and_update({"_id": id},{"$set": updateAnimal})
    #del new_animal["id"]
    animalEdited = client.catalogo_animales.animales.find_one_and_update({"_id": ObjectId(animalID)},{"$set": update_data})
    return animalEntity(animalEdited)