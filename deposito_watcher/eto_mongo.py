from pymongo import MongoClient
from bson.objectid import ObjectId

# quando precisa converter um hast to objetcid
def hash2objectid(hashe):
    return ObjectId(hashe)

def objectid_to_hash(obj):
    pass


class Cliente():
    def __init__(self, colecao="teste", bd="ethowatcher", ip="localhost", porta=27017):

        self.mongo_client = self._tenta_conexao(ip, porta) #MongoClient(ip, porta)

        self.db = self.mongo_client[bd]
        self.col = self.db[colecao]
        self.data = {}

    def _tenta_conexao(self, ip, porta):
        try:
            conn = MongoClient(ip, porta, serverSelectionTimeoutMS = 2000)
            conn.server_info()

            if conn is None:
                pass
                # no connection, exit early
                # raise Exception("Nao conseguiu conectar com o mongo")
                # assert False
            else:
                return conn
        except:
            raise Exception("Nao conseguiu conectar com o mongo")

        # finally:
        #     return None


    def get_col(self):
        return self.col
    
    def get_by_objid(self, objid):
         self.data = self.col.find_one({"_id": objid})

    def get_by_hash(self, hashe):
        self.data = self.col.find_one({"_id": hash2objectid(hashe)})

    def crete_file(self, men_json):
        post_id = self.col.insert_one(men_json).inserted_id
        self.data = self.col.find_one({"_id": post_id})

    def up_file(self, campos_atualiza):
        r_deu = self.col.update_one({'_id': self.data["_id"]}, { "$set":campos_atualiza})
        self.get_by_hash(str(self.data["_id"]))
        return r_deu

    def del_file(self):
        self.col.delete_one({"_id": self.data["_id"]})
        self.data = {}

    def query(self, query_dic):
        cursor = self.col.find(query_dic)
        return cursor

        

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

    def deleta(self):
        c = Cliente(colecao="Experimento")
        cursor = c.col.find({"id_usuario": self.cliente.data["_id"]})
        for documento in cursor:
            c = Experimento()
            c.get_by_hash(str(documento["_id"])).deleta()

        self.cliente.del_file()
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
        men_json["id_usuario"] = user.cliente.data["_id"]
        self.cliente.crete_file(men_json)
        return self
    def get_list_experimento_by_user(self, user):
        ob_id_user = user.cliente.data["_id"]
        cursor = self.cliente.col.find({"id_usuario": ob_id_user})
        self.cliente.cursor = cursor
        return self

    def get_by_exp_name(self, exp_name):
        data = self.cliente.col.find_one({"nome_banco_experimental": exp_name})
        self.cliente.data = data
        return self


    def get_by_hash(self, hashe):
        self.cliente.get_by_hash(hashe)
        return self
    
    def atualiza(self, campos_atualiza):
        self.cliente.up_file(campos_atualiza)
        return self
    
    def deleta(self):
        c = Cliente(colecao="Juncoes")
        cursor = c.col.find({"id_experimento": self.cliente.data["_id"]})
        for documento in cursor:
            c = Juncao()
            c.get_by_hash(str(documento["_id"])).deleta()
        
        self.cliente.del_file()
    # deletar experimentos que deletar as junções.
        



class Juncao():
    def __init__(self):
        self.cliente = Cliente(colecao="Juncoes")

    def create_juncao(self, men_json, experimento):
        men_json["id_experimento"] = experimento.cliente.data["_id"]
        self.cliente.crete_file(men_json)
        return self

    def get_by_hash(self, hashe):
        self.cliente.get_by_hash(hashe)
        return self
    
    def update_var_inde(self, array_var_inde):
        self._atualiza_db({"var_ind": array_var_inde})
        return self

    # Dar uma limpada nesses métodos porque eles são muito parecido.
    def update_video(self, json_mensagem):
        vi = Video()
        r_video_vazio = self.cliente.data["id_video"] == ""
        if(r_video_vazio):
            vi.create_video(json_mensagem)
        else:
            vi.get_by_hash(self.cliente.data["id_video"]).delete_video()
            vi.create_video(json_mensagem)
            
        self.cliente.data["id_video"]= vi.cliente.data["_id"]
        self._atualiza_db(self.cliente.data)
        return self


    def update_eto(self, json_mensagem):
        eto = Etografia()
        r_eto_vazia = self.cliente.data["id_eto"] == ""
        if(r_eto_vazia):
            eto.create_eto(json_mensagem)
        else:
            eto.get_by_hash(self.cliente.data["id_eto"]).delete_etografia()
            eto.create_eto(json_mensagem)
            
        self.cliente.data["id_eto"]= eto.cliente.data["_id"]
        self._atualiza_db(self.cliente.data)
        return self


    def update_tra(self, json_mensagem):
        tra = Rastreamento()
        r_tra_vazia = self.cliente.data["id_tra"] == ""
        if(r_tra_vazia):
            tra.create_ras(json_mensagem)
        else:
            tra.get_by_hash(self.cliente.data["id_tra"]).delete_rastreamento()
            tra.create_ras(json_mensagem)
            
        self.cliente.data["id_tra"]= tra.cliente.data["_id"]
        self._atualiza_db(self.cliente.data)
        return self

    def _atualiza_db(self, campos_atualiza):
        r_atualizo = self.cliente.up_file(campos_atualiza)
        if r_atualizo:
            return True
        else:
            return False

    def deleta(self):
        data = self.cliente.data
        r_e_video = data["id_video"] != ""
        r_e_eto = data["id_eto"] != ""
        r_e_tra = data["id_tra"] != ""
        if(r_e_video):
            vi = Video()
            vi.get_by_hash(data["id_video"]).delete_video()
        
        if(r_e_eto):
            eto = Etografia()
            eto.get_by_hash(data["id_eto"]).delete_etografia()
        
        if(r_e_tra):
            tra = Rastreamento()
            tra.get_by_hash(data["id_tra"]).delete_rastreamento()
        
        self.cliente.del_file()




# arrumar para gravar o vídeo tbm
class Video():
    def __init__(self):
        self.cliente = Cliente(colecao="Video")


    def create_video(self, json_mensagem):
        self.cliente.crete_file(json_mensagem)
        return self
  

    def get_by_hash(self, objID):
        self.cliente.get_by_objid(objID)
        return self


    def delete_video(self):
       self.cliente.del_file()
       return self


class Marcacao():
    def __init__(self):
        self.cliente = Cliente(colecao="Marcacao")

    def create_marcacao(self, json_mensagem):
        self.cliente.crete_file(json_mensagem)
        return self

    def get_by_id_name(self, id_experimento):
        data = self.cliente.col.find_one({"id_experimento": id_experimento})
        self.cliente.data = data

    def get_by_hash(self, objID):
        self.cliente.get_by_objid(objID)
        return self
    
    def update(self, campos_atualiza):
        self.cliente.up_file(campos_atualiza)
        return self


        # pass
class Etografia():
    def __init__(self):
        self.cliente = Cliente(colecao="Etografia")


    def create_eto(self, json_mensagem):
        self.cliente.crete_file(json_mensagem)
        return self
  

    def get_by_hash(self, objID):
        self.cliente.get_by_objid(objID)
        return self


    def delete_etografia(self):
       self.cliente.del_file()
       return self

class Rastreamento():
    def __init__(self):
        self.cliente = Cliente(colecao="Rastreamento")


    def create_ras(self, json_mensagem):
        self.cliente.crete_file(json_mensagem)
        return self
  

    def get_by_hash(self, objID):
        self.cliente.get_by_objid(objID)
        return self


    def delete_rastreamento(self):
       self.cliente.del_file()
       return self
