"""
Arquivo que tem a api para o etho_smart
"""
import deposito_watcher.eto_mongo as mg

def get_usuario(usuario, senha):
    try:
        us = mg.Usuario()
        us = us.get_by_login(usuario)
        r_senha = us.cliente.data["senha"] == str(senha)
        user_id = str(us.cliente.data["_id"])
        nome_user = us.cliente.data["nome"] 
        return r_senha, user_id
        # return True
    except:
        return False , None, ""


def get_list_experimento(usuario_id):
    try:
        us = mg.Usuario()
        us = us.get_by_hash(usuario_id) #us.get_by_hash("5ea1a77193f4d56a842f3a67")
        
        ex = mg.Experimento()
        ex = ex.get_list_experimento_by_user(us)
        documentos = []
        for documento in ex.cliente.cursor:
            documento["_id"] = str(documento["_id"])
            documento["id_usuario"] = str(documento["id_usuario"])
            documentos.append(documento)
            

        return True, documentos
    except:
        return False, []


def get_exp_by_hash(hash_experimento, usuario_id):
    try:
        # tem que verificar se o experimento é do usuario
        ex = mg.Experimento()
        ex = ex.get_by_hash(hash_experimento)
        data = ex.cliente.data
        data["_id"] = str(data["_id"])
        data["id_usuario"] = str(data["id_usuario"])
        r_user_requisitiando = data["id_usuario"] == usuario_id

        if r_user_requisitiando:
            return True, data
        else:
            return False, {}
    except:
        return False, {}