import pymongo
# #*Conexion a MongoDB
from  pymongo import MongoClient
# #*Variables de entorno
from decouple import  config


class MongoDB:
    try:
        client = MongoClient(config('MONGO_URL'), serverSelectionTimeoutMS = config('MONGO_TIME_OUTSIDE'))
        client.server_info()
        print('¡Conexion exitosa con MongoDB!')
    except pymongo.errors.ServerSelectionTimeoutError as errorType:
        print("Tiempo exedido:" + errorType)
    except pymongo.errors.ConnectionError as errorConnection:
        print("Fallo al conectarse a MongoDB:" + errorConnection)