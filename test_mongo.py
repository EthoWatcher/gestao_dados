import eto_mongo as mg
import json


path_usuariso = "./examples/1-usuarios.json"
path_experimento = "./examples/2-banco_experimental.json"


def get_arquivo(arquivo):
    with open(arquivo, 'r', encoding="utf-8") as f:
        distros_dict = json.load(f)
    # f = open(arquivo, "rb")
    return distros_dict[0]
    

def test_get_arquivo():
    distros_dict = get_arquivo(path_usuariso)
    # print(distros_dict)

def test_liga_banco():
    cliente = mg.Cliente()

def test_cria_usuario():
    us = mg.Usuario()
    distros_dict = get_arquivo(path_usuariso)
    us = us.create_usuario(distros_dict)

def test_get_ususario():
    us = mg.Usuario()
    us = us.get_by_login("jmarcolan")
    print(us)

def test_get_ususario_ob():
    us = mg.Usuario()
    us = us.get_by_hash("5ea09ee693f4d54eac22fb05")
    print(us)
    # us.get_usuario_id(ObjectId("5ea09ee693f4d54eac22fb05"))
    
def test_get_atualiza():
    us = mg.Usuario()
    us = us.get_by_hash("5ea09ee693f4d54eac22fb05")
    us = us.atualiza({"nome": "rei dos codegos"})
    print(us)

def test_curiosidade():
    us = mg.Usuario()
    us.get_by_hash("5ea09ee693f4d54eac22fb05").atualiza({"nome": "rei dos 2"})


def test_create_experimento():
    us = mg.Usuario()
    us = us.get_by_hash("5ea09ee693f4d54eac22fb05")
    ex = mg.Experimento()
    distros_dict = get_arquivo(path_experimento)
    ex.create_experimento(distros_dict,us)

def test_get_experimento():
    ex = mg.Experimento()
    ex.get_by_hash("5ea0b45893f4d51de40e00cd")
    print(ex)


# def test_liga_banco():
#     mongo_client = MongoClient('localhost', 27017)
