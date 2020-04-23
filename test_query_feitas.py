import querys_feitas as qf
from bson.objectid import ObjectId
import eto_mongo as et_m
import etho_dados as et_d
import pandas as pd 

def test_fazer_querys():
    dict_query = { "$and": [{"id_experimento": ObjectId("5ea1a82993f4d56ba41e567d")}, {"var_inde": { "$all": ["macho","flx2.5mg"]}}]}
    j = qf.Get_Juncoes(dict_query)
    cursor = j.get_cursor()
    l = len(list(cursor))   
    print(l)

def test_query_get_etografia():
    dict_query = { "$and": [{"id_experimento": ObjectId("5ea1a82993f4d56ba41e567d")}, {"var_inde": { "$all": ["macho","flx2.5mg"]}}]}
    j = qf.Get_Juncoes(dict_query)
    cursor = j.get_cursor()

    def get_etografias(juncao):
        eto = et_m.Etografia()
        eto.get_by_hash(juncao["id_eto"])
        return eto

    etografias = list(map(get_etografias,cursor))
    print(etografias)


def test_query_get_descritores_experimentais():
    dict_query = { "$and": [{"id_experimento": ObjectId("5ea1a82993f4d56ba41e567d")}, {"var_inde": { "$all": ["macho","flx2.5mg"]}}]}
    j = qf.Get_Juncoes(dict_query)
    cursor = j.get_cursor()

    def get_etografias(juncao):
        eto = et_m.Etografia()
        eto = eto.get_by_hash(juncao["id_eto"])
        e_dados = et_d.Etografia(eto.cliente.data)
        return {"eto": e_dados, "id_j": str(juncao["_id"])}


    li_str_descritores = ["duracao", "frequencia"]
    li_str_categora = ["Immobility", "Swimming"]

    l_u_eto_jun_id = list(map(get_etografias,cursor))
    des_experimental = qf.Constru_descritor_experimental(li_str_descritores, li_str_categora)
    descritores_pegados = des_experimental.get_descritores_etografia(l_u_eto_jun_id)

    print(descritores_pegados)


def test_query_get_descritores_experimentais_class():
    dict_query = { "$and": [{"id_experimento": ObjectId("5ea1a82993f4d56ba41e567d")}, {"var_inde": { "$all": ["macho","flx2.5mg"]}}]}
    cs = qf.Get_CSV(dict_query)
    li_str_descritores = ["duracao", "frequencia"]
    li_str_categora = ["Immobility", "Swimming"]

    data = cs.set_descritores_experimentais(li_str_descritores, li_str_categora )
    
    # df = pd.DataFrame(data)
    # print(df)