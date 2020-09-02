import deposito_watcher.eto_mongo as mg
import json
import deposito_watcher.parser_eto as par
# from EW_preprocess_pkg import xml2json as pa



path_usuariso = "./tests/examples/1-usuarios.json"
path_experimento = "./tests/examples/2-banco_experimental.json"
path_juncao = "./tests/examples/3-juncoes.json"

path_etoxml = "./tests/examples/1e3z1h4.etoxml"
path_video = "./tests/examples/1e3z1h4.vxml"
path_ras = "./tests/examples/1e3z1h4.tkin"

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

# Cria experimento ObjectId("5ea1a77193f4d56a842f3a67")
def test_create_experimento():
    us = mg.Usuario()
    us = us.get_by_login("jmarcolan") #us.get_by_hash("5ea1a77193f4d56a842f3a67")
    ex = mg.Experimento()
    distros_dict = get_arquivo(path_experimento)
    ex.create_experimento(distros_dict,us)

def test_get_experimento():
    ex = mg.Experimento()
    ex.get_by_exp_name("fluoxetina_gian")
    # ex.get_by_hash("5ea0b45893f4d51de40e00cd")
    print(ex)

# create juncao ObjectId("5ea0dc9393f4d55b9813bc02")
def test_create_juncao():
    ex = mg.Experimento()
    ex.get_by_exp_name("fluoxetina_gian")
    # ex.get_by_hash("5ea0dc9393f4d55b9813bc02")

    distros_dict = get_arquivo(path_juncao)

    jc = mg.Juncao()
    jc.create_juncao(distros_dict,ex)

    # f = open(path_video, "rb") 
    # parser = pa.Parse_XML(f)
    # men_json = parser.get_data()

def test_update_juncao():
    doc = par.parser_xml_file_2_dict(path_video)
    jc = mg.Juncao()
    jc.get_by_hash("5ea0d73393f4d55e28a9240a").update_video(doc)
    

# ObjectId("5ea0dcc993f4d5424809f73f")
def test_update_juncao_tudo():
    doc_video = par.parser_xml_file_2_dict(path_video)
    doc_eto = par.parser_xml_file_2_dict(path_etoxml)
    doc_ras = par.parser_xml_file_2_dict(path_ras)
    jc = mg.Juncao()
    jc.get_by_hash("5ea0dcc993f4d5424809f73f").update_video(doc_video).update_eto(doc_eto).update_tra(doc_ras)


def test_deleta_juncao():
    jc = mg.Juncao() 
    jc.get_by_hash("5ea0d73393f4d55e28a9240a").deleta() 




def test_deleta_experimento():
    ex = mg.Experimento()
    ex.get_by_hash("5ea0b45893f4d51de40e00cd").deleta()


# deleta usaurio ObjectId("5ea0dc2f93f4d51f103cabb8")
def test_deleta_usuario():
    us = mg.Usuario()
    us.get_by_hash("5ea0dc2f93f4d51f103cabb8").deleta()


    # men_json = json.dumps(doc)
    # # men_json = get_arquivo(path_usuariso)
    # jc = mg.Juncao()
    # jc.create_juncao(doc,ex)
# def test_liga_banco():
#     mongo_client = MongoClient('localhost', 27017)
