from pydantic import BaseModel
from datetime import datetime 
from typing import Optional

class Animal(BaseModel):
#    id:Optional[str]
    Tipo:str
    Talla:str
    Motivo_ingreso:str
    Edad:int
    Fecha_Ingreso:datetime
    Fecha_salida:Optional[datetime] = None
    Observacion:str
    Estado:str