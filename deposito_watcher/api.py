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

    