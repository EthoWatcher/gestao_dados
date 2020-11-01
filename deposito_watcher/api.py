"""
Arquivo que tem a api para o etho_smart
"""
import deposito_watcher.eto_mongo as mg
from bson.objectid import ObjectId

import deposito_watcher.fusao_variaveis as fus
import deposito_watcher.querys_feitas as qf

import numpy as np 

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
            return True, np.random.choice(ls, qnt, replace=False)
        else:
            return True, ls
    except:
        return False, None
        # print(j)





    
