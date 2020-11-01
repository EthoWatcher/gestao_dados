import json
import deposito_watcher.parser_eto as par
import deposito_watcher.eto_mongo as mg

# importar schemas
# from json import load
from pkg_resources import resource_stream

# schema = load(resource_stream('exampleproject', 'data/schema.json'))

path_usuariso = "modelo/1-usuarios.json"
path_juncao = "modelo/3-juncoes.json"
path_experimento = "modelo/2-banco_experimental.json"

def get_arquivo(arquivo):
    with open(arquivo, 'r', encoding="utf-8") as f:
        distros_dict = json.load(f)
    # f = open(arquivo, "rb")
    return distros_dict


def get_modelos_prontos(arquivo):
    arquivo_texto = resource_stream("deposito_watcher",arquivo)
    distros_dict = json.load(arquivo_texto)
    # with open(arquivo, 'r', encoding="utf-8") as f:
    #     distros_dict = json.load(f)
    # f = open(arquivo, "rb")
    return distros_dict


def parse_documento(juncao):
    doc_video = par.parser_xml_file_2_dict(juncao["id_video"])
    doc_eto = par.parser_xml_file_2_dict(juncao["id_eto"])
    doc_ras = par.parser_xml_file_2_dict(juncao["id_tra"])
    return doc_video, doc_eto, doc_ras


def envia_juncoes(path_experimento, name_exp):
    ex = mg.Experimento()
    ex.get_by_exp_name(name_exp)
    juncoes_paths = get_arquivo(path_experimento)


    for juncao in juncoes_paths:
    #pega o experimentador
        
        
        #constroi a juncao
        distros_dict = get_modelos_prontos(path_juncao)
        doc_video, doc_eto, doc_ras = parse_documento(juncao)
        jc = mg.Juncao()
        #constroi a juncao e ja da update.
        jc.create_juncao(distros_dict[0],ex).update_video(doc_video).update_eto(doc_eto).update_tra(doc_ras).update_var_inde(juncao["var_ind"])
        

def create_usuario(login="jmarcolan", senha="1234", nome="joao", lab="ieb"):
    us = mg.Usuario()
    distros_dict = get_modelos_prontos(path_usuariso)
    # distros_dict = [{"login":"", 
    #                 "lab":"", 
    #                 "nome":"",
    #                 "senha":""}]

    distros_dict[0]["login"] = login
    distros_dict[0]["senha"] = senha
    distros_dict[0]["nome"] = nome
    distros_dict[0]["lab"] = lab

    us = us.create_usuario(distros_dict[0])


def creat_experimento(login_usuario, modelo_path=None):
    us = mg.Usuario()
    # us = us.get_by_hash("5f4e8c2c93f4d5509c58d3b4")
    us = us.get_by_login(login_usuario)
    ex = mg.Experimento()

    if modelo_path == None: # workaround para nao explodir os testes e manter a compatibilidade
        distros_dict = get_modelos_prontos(path_experimento)
    else:
        distros_dict = get_arquivo(modelo_path)


    ex.create_experimento(distros_dict[0],us)



def cadastra_batch_arquivos(path_experimento, login_usuario, name_exp):
    # us = mg.Usuario()
    # us = us.get_by_login(login_usuario)
    envia_juncoes(path_experimento, name_exp)


def creat_marcacoes(marcacaoes):
    marcacao_db = mg.Marcacao()
    for marca_dic in marcacaoes:
        marcacao_db.create_marcacao(marca_dic)
    


