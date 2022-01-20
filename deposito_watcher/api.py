"""
Arquivo que tem a api para o etho_smart
"""
from operator import le
import deposito_watcher.eto_mongo as mg
from bson.objectid import ObjectId

import deposito_watcher.fusao_variaveis as fus
import deposito_watcher.querys_feitas as qf
import deposito_watcher.parser_eto as par

import numpy as np 
import pandas as pd


def query_dados(ID_EX, dict_query, ls_categorias, ls_des_cate, ls_var_eto, ls_des_rast, lis_desc_juncao, list_des_texto_display=[]):
    r_soment_tracking = len(ls_des_cate) == 0 and len(ls_var_eto) ==0
    r_soment_categoria = len(ls_des_rast) == 0

    if r_soment_tracking :
        r_selecao_categoria = len(ls_categorias) !=0
        if r_selecao_categoria:
            fs = fus.Fusao_variaveis(dict_query)

            fs.set_variaveis_rastreamento(ls_des_rast)
            fs.set_variaveis_etografia(["nome"]) # tem q ter pelo menos o nome

            r_descritor_juncao_ativa = len(lis_desc_juncao) !=0
            if r_descritor_juncao_ativa:
                fs.set_variaveis_juncao(lis_desc_juncao)


            li_str_descritores = []
            li_str_categora = ls_categorias # todas as categorias tem q colocar elas por escrito aqui
            fs.set_variaveis_descritore_eto_experimento(li_str_descritores, li_str_categora)
            df = fs.get_dados_fundidos()

            if r_descritor_juncao_ativa:
                # aqui as keys dos dis são 0, 1, 2,3 precisam retornar
                pass


            return True, df

        else:
            fs = fus.Fusao_variaveis(dict_query)
            r_descritor_juncao_ativa = len(lis_desc_juncao) !=0
            if r_descritor_juncao_ativa:
                fs.set_variaveis_juncao(lis_desc_juncao)
            

            fs.set_variaveis_rastreamento(ls_des_rast)
            df = fs.get_dados_fundidos()
            
            if r_descritor_juncao_ativa:
                # aqui as keys dos dis são 0, 1, 2,3 precisam retornar
                pass

            return True, df

    elif r_soment_categoria:
        fs = fus.Fusao_variaveis(dict_query)

        r_descritor_juncao_ativa = len(lis_desc_juncao) !=0
        if r_descritor_juncao_ativa:
            fs.set_variaveis_juncao(lis_desc_juncao)

        # fs.set_variaveis_rastreamento(["@Vd"])
        r_ls_var_eto_empty = len(ls_var_eto) ==0
        if not r_ls_var_eto_empty:
            fs.set_variaveis_etografia(ls_var_eto)

        li_str_descritores = ls_des_cate
        li_str_categora = ls_categorias # todas as categorias tem q colocar elas por escrito aqui
        fs.set_variaveis_descritore_eto_experimento(li_str_descritores, li_str_categora)
        df = fs.get_dados_fundidos()
        
        if r_descritor_juncao_ativa:
            pass

        return True, df

    else:
        fs = fus.Fusao_variaveis(dict_query)

        r_descritor_juncao_ativa = len(lis_desc_juncao) !=0
        if r_descritor_juncao_ativa:
            fs.set_variaveis_juncao(lis_desc_juncao)

        fs.set_variaveis_rastreamento(ls_des_rast)

        r_ls_var_eto = len(ls_var_eto) != 0
        if r_ls_var_eto:
            r_nome = "nome" in ls_var_eto
            if r_nome:
                fs.set_variaveis_etografia(ls_var_eto)
            else:
                ls_var_eto.append("nome")
                fs.set_variaveis_etografia(ls_var_eto)


        li_str_descritores = ls_des_cate
        li_str_categora = ls_categorias # todas as categorias tem q colocar elas por escrito aqui
        fs.set_variaveis_descritore_eto_experimento(li_str_descritores, li_str_categora)
        df = fs.get_dados_fundidos()
        if r_descritor_juncao_ativa:
            pass

        return True, df




def create_usuario_by(data):
    try:
        usuadio_esquema = {"login": data["login"], 
                            "lab": data["lab"], 
                            "nome": data["nome"],
                            "senha":data["senha"]}
        us = mg.Usuario()
        us = us.create_usuario(usuadio_esquema)
        return True
    except:
        return False


def deleta_usuario(usuario_hash):
    try:
        us = mg.Usuario()
        us.get_by_hash(usuario_hash).deleta()
        return True
    except:
        return False


def delete_experimento(experimento_hash):
    try:
        ex = mg.Experimento()
        ex.get_by_hash(experimento_hash).deleta()
        return True
    except:
        return False

def atualiza_experimento(experimento_hash, experimento):
    try:
        experimento.pop("_id", None)
        experimento.pop("id_usuario", None)
        ex = mg.Experimento()
        ex.get_by_hash(experimento_hash).update_experimento(experimento)
        return True
    except:
        return False

    # pass

def creat_experimento(usuario_hash, data):
    try:
        us = mg.Usuario()
        us = us.get_by_hash(usuario_hash) # get_by_login("jmarcolan") #us.get_by_hash("5ea1a77193f4d56a842f3a67")
        ex = mg.Experimento()
        experimento = {   
            "id_usuario":"",
            "nome_banco_experimental":data["nome_banco_experimental"],
            "var_inde":[
                # {"texto_interface" : "Sexo do animal","nome":"sexo","categorias":["macho" ,"femea"]}
                ],
            "var_depend":[
                {"texto_interface" : "Categorias comportamentais", "nome":"categoria_comportamental",
                "categorias": [] # ["Swimming","Immobility", "Climbing", "Diving", "Headshaking", "Undefined"]
                }
            ]}

        ex = ex.create_experimento(experimento,us)
        return True
    except:
        return False


def delete_experimento(experimento_hash):
    try:
        ex = mg.Experimento()
        ex.get_by_hash(experimento_hash).deleta()
    except:
        return False

def create_juncao(experimento_hash):
    try:
        juncao = {"id_experimento":"",
        "id_banco":"",
        "id_video":"",
        "id_eto":"",
        "id_tra":"",
        "var_ind":{}}

        ex = mg.Experimento()
        ex.get_by_hash(experimento_hash)
        # ex.get_by_hash("5ea0dc9393f4d55b9813bc02")

        jc = mg.Juncao()
        jc.create_juncao(juncao,ex)
        return True
    except:
        return False

def delete_juncao(juncao_hash):
    try:
        jc = mg.Juncao()
        jc.get_by_hash(juncao_hash).deleta()
        return True
    except:
        return False

def update_juncao(juncao_hash, xml_texto, r_video=False, r_eto=False, r_rast=False):
    try:
        jc = mg.Juncao()
        r_update_var_ind = not r_video and not r_eto and not r_rast
        if r_update_var_ind:
            jc.get_by_hash(juncao_hash).update_var_inde(xml_texto)
        if r_video:
            doc_video = par.parser_xml_text_2_dict(xml_texto)
            jc.get_by_hash(juncao_hash).update_video(doc_video)
        if r_eto:
            doc_video = par.parser_xml_text_2_dict(xml_texto)
            jc.get_by_hash(juncao_hash).update_eto(doc_video)
        if r_rast:
            doc_video = par.parser_xml_text_2_dict(xml_texto)
            jc.get_by_hash(juncao_hash).update_tra(doc_video)
        return True
    except:
        return False
    



def get_usuario(usuario, senha):
    try:
        us = mg.Usuario()
        us = us.get_by_login(usuario)
        r_senha = us.cliente.data["senha"] == str(senha)
        user_id = str(us.cliente.data["_id"])
        nome_user = us.cliente.data["nome"] 
        return r_senha, user_id, ""
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


def arruma_juncao(juncao_data):
    juncao_data["_id"] = str(juncao_data["_id"])
    juncao_data["id_experimento"] = str(juncao_data["id_experimento"])
    juncao_data["id_video"] = str(juncao_data["id_video"])
    r_tem_video = juncao_data["id_video"] != ''

    if(r_tem_video):
        vi = mg.Video().get_by_hash(juncao_data["id_video"])
        juncao_data["video_data"] = vi.cliente.data
        juncao_data["video_data"]["_id"] = str(juncao_data["video_data"]["_id"])
    else:
        juncao_data["video_data"] = {}

    juncao_data["id_eto"] = str(juncao_data["id_eto"])
    juncao_data["id_tra"] = str(juncao_data["id_tra"])

    return juncao_data

def get_juncao_by_hash(juncao_hash):
    try:
        jc = mg.Juncao().get_by_hash(juncao_hash)
        data = arruma_juncao(jc.cliente.data)

        return True, data
    except:
        return False, {}

def get_list_juncao(experimento_hash):
    try:
        ex = mg.Experimento().get_by_hash(experimento_hash)
        
        jc = mg.Juncao().get_list_juncao_by_exp(ex)
        documentos = []
        for documento in jc.cliente.cursor:
            data = arruma_juncao(documento)
            # documento["_id"] = str(documento["_id"])
            # documento["id_experimento"] = str(documento["id_experimento"])
            # documento["id_video"] = str(documento["id_video"])
            # r_tem_video = documento["id_video"] != ''

            # if(r_tem_video):
            #     vi = mg.Video().get_by_hash(documento["id_video"])
            #     documento["video_data"] = vi.cliente.data
            #     documento["video_data"]["_id"] = str(documento["video_data"]["_id"])
            # else:
            #     documento["video_data"] = {}

            # documento["id_eto"] = str(documento["id_eto"])
            # documento["id_tra"] = str(documento["id_tra"])
            
            documentos.append(data)
            
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
    
def get_csv_by_query(hash_experimento, dict_query):
    try:
        dict_template = constroi_a_query_inteira(hash_experimento, dict_query)
        print(dict_template)

        lis_de_juncao = ["sexo", "dosagem", "unidade"]
        
        fs = fus.Fusao_variaveis(dict_template)
        fs.set_variaveis_juncao(lis_de_juncao)
        li_str_descritores = ["duracao", "duracao_total", "path_experimento"]
        li_str_categora = dict_query["categoria_comportamental"]

        
        fs.set_variaveis_descritore_eto_experimento(li_str_descritores, li_str_categora)
        df = fs.get_dados_fundidos()

        # fs = fus.Fusao_variaveis(dict_template)
        # fs.set_variaveis_rastreamento(["@Vd", "@Van"])
        # fs.set_variaveis_etografia(["nome", "trecho", "q_inicial", "q_final"])
        # fs.set_variaveis_juncao(["sexo", "dosagem", "unidade"])
        # df = fs.get_dados_fundidos()
        return True, df
    except:
        return False, None

   
def constroi_a_query_inteira(hash_experimento, dict_query):
    def constroi_query(key, lista, dict_query):
        r_lista_sem_nada = len(lista) == 0 
        r_tamanho_lista_maior_1 = len(lista) > 1
        if r_tamanho_lista_maior_1:
            dict_query = {"$or": []}
            for elemento in lista:
                dic_template = {key: elemento}
                dict_query["$or"].append(dic_template)
            return dict_query
        else:
            dict_query = {key: lista[0]}
            return dict_query


    

    r_var_unidade = "unidadetodos" in  dict_query["var_ind.unidade"]
    r_var_sexo = "sexotodos" in  dict_query["var_ind.sexo"]
    r_var_dosagem = "dosagemtodos" in  dict_query["var_ind.dosagem"]


    dict_unidade = {}
    dict_sexo = {}
    dict_dosagem = {}
    dict_template = { "$and": [{"id_experimento": ObjectId(hash_experimento)}]}


    if r_var_unidade:
        pass
    else:
        dict_unidade = constroi_query("var_ind.unidade", dict_query["var_ind.unidade"],dict_query)
        dict_template["$and"].append(dict_unidade)

    if r_var_sexo:
        pass
    else:
        dict_sexo = constroi_query("var_ind.sexo", dict_query["var_ind.sexo"], dict_query)
        dict_template["$and"].append(dict_sexo)

    if r_var_dosagem:
        pass
    else:
        dict_dosagem = constroi_query("var_ind.dosagem", dict_query["var_ind.dosagem"], dict_query)
        dict_template["$and"].append(dict_dosagem)
    
    return dict_template

def get_config_marca_exp(id_experimento,nome_exper):
    try:
        exper_mongo  = mg.Experimento().get_by_hash(id_experimento)
        l = list(filter(lambda marcacao: marcacao['nome'] == nome_exper, exper_mongo.cliente.data["list_banco_imagem"]))
        if len(l) == 1:
            marcacao_config = l[0]["marcacoes"]
            quais_marcacoes = list(marcacao_config.keys())
            return True, {"marcacao_config": marcacao_config, "quais_marcacoes":quais_marcacoes}
        else:
            return False, None
    except:
        return False, None

# https://colab.research.google.com/drive/1Te1yubf8wxnbN2wfgt6E4UPwvCMfWZqc#scrollTo=4KE_S4YkXvqO
def get_list_rand_ano(id_experimento, qnt, nome_exper, qual_marcacao):
    try:
        marcacao_cursor = qf.Get_Marcacoes(id_experimento,nome_exper).get_cursor()
        ls = []
        for marcacao in marcacao_cursor:
            r_n_marcado =  not qual_marcacao in marcacao["marcacoes"] #len(marcacao["marcacoes"]) == 0 
            if r_n_marcado:
                marcacao["id_experimento"] = str(marcacao["id_experimento"])
                marcacao["_id"] = str(marcacao["_id"] )
                ls.append(marcacao)

        r_tem_qnt_marcacoes = len(ls) > qnt

        if r_tem_qnt_marcacoes:    
            return True, np.random.choice(ls, qnt, replace=False).tolist()
        else:
            return True, ls

    except:
        return False, None
        # print(j)


# tem que modificar para ficar generico.
def atualiza_marcacao(id_marcacao, qual_marca, marcacao):
    # id_marcacao = "5f9e336fbd51328d41f3bb20"
    # qual_marca = "box"
    try:
        marcacao_upd = { f"marcacoes.{qual_marca}" : {
                "x" : marcacao["x"],
                "y" : marcacao["y"],
                "w" : marcacao["w"],
                "h" : marcacao["h"],
                "anotado" : True
            }}
        jc = mg.Marcacao()
        nova = jc.get_by_hash(ObjectId(id_marcacao)).update(marcacao_upd)
        return True, nova
    except:
        return False, None


    
def get_pega_todas_marcacaoes(id_experimento, nome_exper, marcacao_nome):
    marcacao_cursor = qf.Get_Marcacoes(id_experimento,nome_exper).get_cursor()
    lis_marcacao = []
    for marcacao in marcacao_cursor:
        saida = {
            "@f": marcacao["@f"],
            "id_video": marcacao["id_video"],
            "x": marcacao["marcacoes"][marcacao_nome]["x"],
            "y": marcacao["marcacoes"][marcacao_nome]["y"],
            "h": marcacao["marcacoes"][marcacao_nome]["h"],
            "w": marcacao["marcacoes"][marcacao_nome]["w"],
            "img_str_b64": marcacao["img_str_b64"]
            }
        lis_marcacao.append(saida)
    
    df_saida = pd.DataFrame(lis_marcacao)

    return df_saida
