import deposito_watcher.fusao_variaveis as fus
import pandas as pd
from bson.objectid import ObjectId


ID_EXPERIMENTO ="5ea1a82993f4d56ba41e567d"
def test_fusa():
    dict_query = { "$and": [{"id_experimento": ObjectId(ID_EXPERIMENTO)}, 
                        {"var_ind.sexo":"macho"},{"$or": [{"var_ind.dosagem": "flx2.5mg"},
                                 {"var_ind.dosagem": "veiculo"} ]}
                        ]}
    fs = fus.Fusao_variaveis(dict_query)
    fs.set_variaveis_rastreamento(["@Vd", "@Van"])
    fs.set_variaveis_etografia(["nome", "trecho", "q_inicial", "q_final"])
    fs.set_variaveis_juncao(["sexo", "dosagem", "unidade"])
    df = fs.get_dados_fundidos()


def test_fusa_q_inicial_analise():
    dict_query = { "$and": [{"id_experimento": ObjectId(ID_EXPERIMENTO)}, 
                        {"var_ind.sexo":"macho"},{"$or": [{"var_ind.dosagem": "flx2.5mg"},
                                 {"var_ind.dosagem": "veiculo"} ]}
                        ]}
    fs = fus.Fusao_variaveis(dict_query)
    # fs.set_variaveis_rastreamento(["@Vd", "@Van"])
    fs.set_variaveis_etografia(["nome", "trecho", "q_inicial", "q_final","q_inicio_analise"])
    fs.set_variaveis_juncao(["sexo", "dosagem", "unidade"])
    df = fs.get_dados_fundidos()