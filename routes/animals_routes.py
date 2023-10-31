from fastapi import APIRouter, UploadFile, File
from config.db import client
from schemas.animals_schemas import animalEntity, animalsEntity
from models.animal_model import Animal
from bson import ObjectId
from pymongo import MongoClient
import cloudinary
import cloudinary.uploader
import cloudinary.api

animal = APIRouter()
db = client['catalogo_animales']
collection = db['images']

cloudinary.config( 
    cloud_name = "dpi9ixsws", 
    api_key = "392739482868893", 
    api_secret = "bgI59ip8IGYXEKzMiL-HkYqEULk" 
)

def upload_image(file: UploadFile = File(...)):
        # Subir la imagen a Cloudinary
        upload_result = cloudinary.uploader.upload(file.file, folder="my_folder")
        image_link = upload_result['secure_url']
        # Guardar el enlace en la base de datos
        result = collection.insert_one({"image_link": image_link})
        return {"image_link": image_link, "database_id": str(result.inserted_id)}

def get_image(database_id: str):
    image_data = collection.find_one({"_id": ObjectId(database_id)})
    return {"image_link": image_data['image_link']}

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