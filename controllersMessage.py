# #*Import de la base de datos del archvo database.py
from database import MongoDB
# #*Import para la id de los objetos de la base de datos MongoDb
from bson.objectid import ObjectId
# #*Import para encryptar el mensaje creado
from cryptography.fernet import Fernet

encryptionPDB = MongoDB.client['EncryptionP']
collectionEncryptionDB = encryptionPDB['messageEncrypted']


class ControllersMessage:
    def __init__(self):
        # ? json of get
        self._getMessageJson = []

    # ? Metodo post
    def postMessage(self, message):
        try:
            # ?Generar una clave en formato de secuencia de bytes:
            key = Fernet.generate_key()

            print(key)
            objectEncryption = Fernet(key)


            textEncrypted = objectEncryption.encrypt(str.encode(message))


            print("cifrado",textEncrypted)
            textDecryptedBytes = objectEncryption.decrypt(textEncrypted)
            textDecrypted = textDecryptedBytes.decode()
            print("Texto desencriptado: ", textDecrypted)
            self.__data = {"messageEncrypted": textEncrypted, "messageSimple":textDecrypted, "status": True}
            collectionEncryptionDB.insert_one(self.__data)
        except TypeError as messageTypeError:
            print("ErrorPost => " + messageTypeError)


    # ?Metodo Get
    def getMessage(self):
        try:
            print("             *******          Lista de mensajes          *******")
            for message in collectionEncryptionDB.find():
                self._getMessageJson.append(message)
                print("||\033[1;36mid: \033[0;37m",message['_id'],"||\033[1;36mstatus: \033[0;37m", message['status'],"||\033[1;36mmessageSimple: \033[0;37m",message['messageSimple'],"||",
                    "\n||\033[1;36mmessageEncrypted: \033[0;37m", message['messageEncrypted'],"||\n");
                #print("**",self._getMessageJson[1]['messageSimple'],"**")
        except TypeError as messageTypeError:
            print("ErrorGet => No hay datos.")

    # ?Metodo Update
    def UpdateMessage(self, id, message):
        try:
            selectMessage = collectionEncryptionDB.find_one({"_id":ObjectId(id)})
            if selectMessage:
                # ?Generar una clave en formato de secuencia de bytes:
                key = Fernet.generate_key()
                objectEncryption = Fernet(key)
                textEncrypted = objectEncryption.encrypt(str.encode(message))
                print("cifrado",textEncrypted)
                textDecryptedBytes = objectEncryption.decrypt(textEncrypted)
                textDecrypted = textDecryptedBytes.decode()
                print("Texto desencriptado: ", textDecrypted)
                updateMessage = collectionEncryptionDB.update_one({"_id":ObjectId(id)}, {"$set": {"messageEncrypted": textEncrypted, "messageSimple":textDecrypted}})
            else:
                print("No se encontro el id del mensaje.")
        except TypeError as messageTypeError:
            print("ErrorUpdate => No se encontro el id del mensaje.")

    # ?Metodo Delete
    def deleteMessage(self, id):
        try:
            selectMessage = collectionEncryptionDB.find_one({"_id":ObjectId(id)})
            if selectMessage:
                deleteMessage = collectionEncryptionDB.delete_one({"_id":ObjectId(id)})
                print("Se elimino mensaje exitosamente.")
            else:
                print("No se encontro el id del mensaje.")

        except TypeError as messageTypeError:
            print("ErrorDelete => No se encontro el mensaje")



#collectionZ = ControllersMessage()

#collectionZ.UpdateMessage("63c4b6cbe23a5f89d3f35452", "League of Legends")
#collectionZ.deleteMessage("63c47cdfffdcc2f7a1fef3ac")
#collectionZ.postMessage("Valorant")
#collectionZ.getMessage()