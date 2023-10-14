
from fastapi import FastAPI
from pymongo import MongoClient


# Conexión a la base de datos de MongoDB
client = MongoClient("mongodb+srv://sacuto310:contramongodb123@cluster0.5m5jcwq.mongodb.net/test?retryWrites=true&w=majority")
# db = client.catalogo_animales  # Reemplaza "test_database" con el nombre de tu base de datos

# client = MongoClient()

# Definir una ruta de ejemplo para verificar la conexión

# import pymongo
# from urllib.parse import quote_plus
# username = quote_plus('<sacuto310>')
# password = quote_plus('<Himelda10%40>')
# password2 = contramongodb123
# cluster = '<Cluster0>'
# authSource = '<authSource>'
# authMechanism = '<authMechanism>'
# uri = 'mongodb+srv://' + username + ':' + password + '@' + cluster + '/?authSource=' + authSource + '&authMechanism=' + authMechanism
# client = pymongo.MongoClient(uri)
# result = client["<catalogo.animales"]["<collName>"].find()

# # print results
# for i in result:
#     print(i)