def animalEntity(item) -> dict:
	return {
		"id": str(item["_id"]),
		"Nombre": item["Nombre"],
        "Tipo": item["Tipo"],
        "Talla":item["Talla"],
        "Motivo_ingreso":item["Motivo_ingreso"],
        "Edad":item["Edad"],
        "Fecha_Ingreso":item["Fecha_Ingreso"],
        "Fecha_salida":item["Fecha_salida"],
        "Observacion":item["Observacion"],
        "Estado":item["Estado"],
		"Image": item["Image"]
    }


def animalsEntity(entity) -> list:
	return [animalEntity(animal) for animal in entity]