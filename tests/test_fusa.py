import deposito_watcher.fusao_variaveis as fus
import pandas as pd
from bson.objectid import ObjectId


ID_EXPERIMENTO ="5f4f8f39c66cad3eb1dd0d50"
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