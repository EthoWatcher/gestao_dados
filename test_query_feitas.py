import querys_feitas as qf
from bson.objectid import ObjectId
import eto_mongo as et_m
import etho_dados as et_d
import pandas as pd 

def test_fazer_querys():
    dict_query = { "$and": [{"id_experimento": ObjectId("5ea1a82993f4d56ba41e567d")}, 
                        {"var_ind.sexo":"macho"},
                        {"var_ind.dosagem": "flx2.5mg"}]}
    j = qf.Get_Juncoes(dict_query)
    cursor = j.get_cursor()
    l = len(list(cursor))   
    print(l)

def test_query_get_etografia():
    dict_query = { "$and": [{"id_experimento": ObjectId("5ea1a82993f4d56ba41e567d")}, 
                        {"var_ind.sexo":"macho"},
                        {"var_ind.dosagem": "flx2.5mg"}]}
    j = qf.Get_Juncoes(dict_query)
    cursor = j.get_cursor()

    def get_etografias(juncao):
        eto = et_m.Etografia()
        eto.get_by_hash(juncao["id_eto"])
        return eto

    etografias = list(map(get_etografias,cursor))
    print(etografias)


def test_query_get_descritores_experimentais():
    dict_query = { "$and": [{"id_experimento": ObjectId("5ea1a82993f4d56ba41e567d")}, 
                        {"var_ind.sexo":"macho"},
                        {"var_ind.dosagem": "flx2.5mg"}]}
    # j = qf.Get_Juncoes(dict_query)
    # cursor = j.get_cursor()

    # def get_etografias(juncao):
    #     eto = et_m.Etografia()
    #     eto = eto.get_by_hash(juncao["id_eto"])
    #     e_dados = et_d.Etografia(eto.cliente.data)
    #     return {"eto": e_dados, "id_j": str(juncao["_id"])}


    li_str_descritores = ["duracao", "frequencia"]
    li_str_categora = ["Immobility", "Swimming"]

    # l_u_eto_jun_id = list(map(get_etografias,cursor))
    des_experimental = qf.Constru_descritor_experimental(li_str_descritores, li_str_categora, dict_query)
    descritores_pegados = des_experimental.get_descritores_etografia()

    print(descritores_pegados)


# def test_query_get_descritores_experimentais_class():
#     dict_query = { "$and": [{"id_experimento": ObjectId("5ea1a82993f4d56ba41e567d")}, 
#                         {"var_ind.sexo":"macho"},
#                         {"var_ind.dosagem": "flx2.5mg"}]}
#     cs = qf.Get_CSV(dict_query)
#     li_str_descritores = ["duracao", "frequencia"]
#     li_str_categora = ["Immobility", "Swimming"]

#     data = cs.set_descritores_experimentais(li_str_descritores, li_str_categora )


def test_query_juncao_des():
    dict_query = { "$and": [{"id_experimento": ObjectId("5ea1a82993f4d56ba41e567d")}, 
                        {"var_ind.sexo":"macho"},
                        {"var_ind.dosagem": "flx2.5mg"}]}

    j = qf.Get_Juncoes(dict_query)
    cursor = j.get_cursor()

    lis_de_juncao = ["sexo", "dosagem", "unidade"]


    cdj = qf.Constru_descritor_juncao(lis_de_juncao, dict_query)
    # resultado = cdj.get_descritor(list(cursor))
    resultado = cdj.get_descritor()
    print(resultado)
    # df = pd.DataFrame(data)
    # print(df)

def test_get_df():
    dict_query = { "$and": [{"id_experimento": ObjectId("5ea1a82993f4d56ba41e567d")}, 
                        {"var_ind.sexo":"macho"},
                        {"var_ind.dosagem": "flx2.5mg"}]}

    # j = qf.Get_Juncoes(dict_query)
    # cursor = j.get_cursor()

    lis_de_juncao = ["sexo", "dosagem", "unidade"]


    cdj = qf.Constru_descritor_juncao(lis_de_juncao, dict_query)
    resultado = cdj.get_descritor() #list(cursor)

    print(resultado)
    # tr = qf.Transforma_Estrutura_Dados_Panda(resultado)

    # print(tr.get_df())

def test_get_descritor_eto():
    dict_query = { "$and": [{"id_experimento": ObjectId("5ea1a82993f4d56ba41e567d")}, 
                        {"var_ind.sexo":"macho"},
                        {"var_ind.dosagem": "flx2.5mg"}]}

    list_des_etografia =["nome", "trecho", "q_inicial", "q_final"]
    de_eto = qf.Construcao_descritor_etografia(list_des_etografia, dict_query)
    result = de_eto.get_descritor()
    
    # tr = qf.Transforma_Estrutura_Dados_Panda_list_dados(result)
    # df = tr.get_df()

    print(result)


def test_get_descritor_rastreamento():
    dict_query = { "$and": [{"id_experimento": ObjectId("5ea1a82993f4d56ba41e567d")}, 
                        {"var_ind.sexo":"macho"},
                        {"var_ind.dosagem": "flx2.5mg"}]}

    list_var_rastreamento =["@Vd", "@Van"]
    de_ras = qf.Constru_descritor_rastreamento(list_var_rastreamento, dict_query)
    result = de_ras.get_descritor()
    
    # tr = qf.Transforma_Estrutura_Dados_Panda_list_dados(result)
    # df = tr.get_df()

    print(result)
    