from pymongo import MongoClient
from bson.objectid import ObjectId


def hash2objectid(hashe):
    return ObjectId(hashe)

def objectid_to_hash(obj):
    pass


class Cliente():
    def __init__(self, colecao="teste", bd="ethowatcher", ip="localhost", porta=27017):
        self.mongo_client = MongoClient(ip, 27017)
        self.db = self.mongo_client[bd]
        self.col = self.db[colecao]
        self.data = {}

    def get_col(self):
        return self.col

    def get_by_hash(self, hashe):
        self.data = self.col.find_one({"_id": hash2objectid(hashe)})

    def crete_file(self, men_json):
        post_id = self.col.insert_one(men_json).inserted_id
        self.data = self.col.find_one({"_id": post_id})

    def up_file(self, campos_atualiza):
        self.col.update_one({'_id': self.data["_id"]}, { "$set":campos_atualiza})
        return self.get_by_hash(str(self.data["_id"]))

    def del_file(self):
        self.col.delete_one({"_id": self.data["_id"]})
        self.data = {}

        


class Usuario():
    def __init__(self):
        self.cliente = Cliente(colecao="Usuarios")

    def get_by_login(self, login):
        data = self.cliente.col.find_one({"login": login})
        self.cliente.data = data
        return self
    
    def get_by_hash(self, hashe):
        self.cliente.get_by_hash(hashe)
        return self
    
    def create_usuario(self, men_json):
        self.cliente.crete_file(men_json)
        return self
    
    def atualiza(self, campos_atualiza):
        self.cliente.up_file(campos_atualiza)
        return self

    # deletar usuario tem que deletar experimento e juncoões.
    # def deleta_usuario(self):
    #     """
    #     Ajustar para verificiar se deletou
    #     """
    #     self.col.delete_one({"_id": self.data["_id"]})
    #     return None
    


class Experimento():
    def __init__(self):
        self.cliente = Cliente(colecao="Experimento")
        # return self

    def create_experimento(self, men_json, user):
        men_json["id_experimento"] = user.cliente.data["_id"]
        self.cliente.crete_file(men_json)
        return self
    
    def get_by_hash(self, hashe):
        self.cliente.get_by_hash(hashe)
        return self
    
    def atualiza(self, campos_atualiza):
        self.cliente.up_file(campos_atualiza)
        return self

    # deletar experimentos que deletar as junções.
        



class Juncao():
    def __init__(self):
        self.cliente = Cliente(colecao="Juncoes")


    def create_juncao(self, men_json, experimento):
        men_json["id_experimento"] = experimento.data["_id"]
        self.cliente.crete_file(men_json)
        return self

    def get_by_hash(self, hashe):
        self.cliente.get_by_hash(hashe)
        return self

    def update_video(self, json_mensagem):
        vi = Video()
        r_video_vazio = self.data["id_video"] == ""
        if(r_video_vazio):
            vi.create_video(json_mensagem)
        else:
            vi.get_by_hash(self.data["id_video"]).delete_video()
            vi.create_video(json_mensagem)
            
        self.data["id_video"]= vi.data["_id"]
        self._atualiza_db(self.data)
        
    
        # self.atualiza_db()

    def update_eto(self):
        pass

    def update_tra(self):
        pass

    def _atualiza_db(self, campos_atualiza):
        _id =  self.data["_id"]

        r_atualizo = self.col.update_one({'_id': _id}, { "$set":campos_atualiza})

        if r_atualizo:
            return True
        else:
            self.data = self.col.find_one({"_id": self.data["_id"]})
            return False



        

class Video():
    def __init__(self):
        self.client_usuarios = Cliente(colecao="Video")
        self.col = self.client_usuarios.get_col()
        self.data = {}
    
    def create_video(self, json_mensagem):
        pass
        # pass
    def get_by_hash(self, objID):
        pass

    def delete_video(self):
       pass 
        
        # pass
# class Etografia():
#     pass

# class Rastreamento():
#     pass