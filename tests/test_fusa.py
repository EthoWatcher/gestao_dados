import deposito_watcher.fusao_variaveis as fus
import pandas as pd
from bson.objectid import ObjectId


ID_EXPERIMENTO ="5f8f534fafd56c628fdd1441"
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



def test_fusao_tudo():
    ID_EX = "5f8f5503d3d64947e0da22e0"
    dict_query = { "$and": [{"id_experimento": ObjectId(ID_EX)}, 
                        {"var_ind.sexo":"macho"},
                        {"var_ind.dosagem": "flx2.5mg"}]}
    fs = fus.Fusao_variaveis(dict_query)

    fs.set_variaveis_rastreamento(["@Vd"])
    fs.set_variaveis_etografia(["nome", "trecho", "q_inicial", "q_final"])

    li_str_descritores = ["duracao", "frequencia", "duracao_total"]
    li_str_categora = ["Swimming"] # todas as categorias tem q colocar elas por escrito aqui
    fs.set_variaveis_descritore_eto_experimento(li_str_descritores, li_str_categora)
    df = fs.get_dados_fundidos()
    print(df)

def test_fusao_so_descritor_rastreamento():
    ID_EX = "5f8f5503d3d64947e0da22e0"
    dict_query = { "$and": [{"id_experimento": ObjectId(ID_EX)}, 
                        {"var_ind.sexo":"macho"},
                        {"var_ind.dosagem": "flx2.5mg"}]}
    fs = fus.Fusao_variaveis(dict_query)

    fs.set_variaveis_rastreamento(["@Vd"])
    fs.set_variaveis_etografia(["nome", "trecho", "q_inicial", "q_final"])

    li_str_descritores = []
    li_str_categora = ["Swimming"] # todas as categorias tem q colocar elas por escrito aqui
    fs.set_variaveis_descritore_eto_experimento(li_str_descritores, li_str_categora)
    df = fs.get_dados_fundidos()
    print(df)



def test_fusao_so_descritor_rastreamento_apenas():
    ID_EX = "5f8f5503d3d64947e0da22e0"
    dict_query = { "$and": [{"id_experimento": ObjectId(ID_EX)}, 
                        {"var_ind.sexo":"macho"},
                        {"var_ind.dosagem": "flx2.5mg"}]}
    fs = fus.Fusao_variaveis(dict_query)

    fs.set_variaveis_rastreamento(["@Vd"])
    fs.set_variaveis_etografia(["nome"]) # tem q ter pelo menos o nome

    li_str_descritores = []
    li_str_categora = ["Swimming"] # todas as categorias tem q colocar elas por escrito aqui
    fs.set_variaveis_descritore_eto_experimento(li_str_descritores, li_str_categora)
    df = fs.get_dados_fundidos()
    print(df)


def test_fusao_so_descritor_rastreamento_apenas_sem_selecao_cat():
    ID_EX = "5f8f5503d3d64947e0da22e0"
    dict_query = { "$and": [{"id_experimento": ObjectId(ID_EX)}, 
                        {"var_ind.sexo":"macho"},
                        {"var_ind.dosagem": "flx2.5mg"}]}
    fs = fus.Fusao_variaveis(dict_query)

    fs.set_variaveis_rastreamento(["@Vd"])
    # fs.set_variaveis_etografia(["nome"]) # tem q ter pelo menos o nome

    # li_str_descritores = []
    # li_str_categora = ["Swimming"] # todas as categorias tem q colocar elas por escrito aqui
    # fs.set_variaveis_descritore_eto_experimento(li_str_descritores, li_str_categora)
    df = fs.get_dados_fundidos()
    print(df)


def test_fusa_q_inicial_analise():
    ID_EX = "5f8f5503d3d64947e0da22e0"
    dict_query = { "$and": [{"id_experimento": ObjectId(ID_EX)}, 
                        {"var_ind.sexo":"macho"},{"$or": [{"var_ind.dosagem": "flx2.5mg"},
                                 {"var_ind.dosagem": "veiculo"} ]}
                        ]}
    fs = fus.Fusao_variaveis(dict_query)
    # fs.set_variaveis_rastreamento(["@Vd", "@Van"])
    # fs.set_variaveis_etografia(["nome", "trecho", "q_inicial", "q_final","q_inicio_analise"])
    fs.set_variaveis_juncao(["sexo", "dosagem", "unidade"])
    fs.set_variaveis_rastreamento(["@Vd"])

    df = fs.get_dados_fundidos()
    print(df)


def test_soment_cat():
    ID_EX = "5f8f5503d3d64947e0da22e0"
    dict_query = { "$and": [{"id_experimento": ObjectId(ID_EX)}, 
                        {"var_ind.sexo":"macho"},
                        {"var_ind.dosagem": "flx2.5mg"}]}
    fs = fus.Fusao_variaveis(dict_query)

    # fs.set_variaveis_rastreamento(["@Vd"])
    fs.set_variaveis_etografia(["nome", "trecho", "q_inicial", "q_final"])

    li_str_descritores = ["duracao", "frequencia", "duracao_total"]
    li_str_categora = ["Swimming"] # todas as categorias tem q colocar elas por escrito aqui
    fs.set_variaveis_descritore_eto_experimento(li_str_descritores, li_str_categora)
    df = fs.get_dados_fundidos()
    print(df)


def test_soment_descritores_cat():
    ID_EX = "5f8f5503d3d64947e0da22e0"
    dict_query = { "$and": [{"id_experimento": ObjectId(ID_EX)}, 
                        {"var_ind.sexo":"macho"},
                        {"var_ind.dosagem": "flx2.5mg"}]}
    fs = fus.Fusao_variaveis(dict_query)

    # fs.set_variaveis_rastreamento(["@Vd"])
    # fs.set_variaveis_etografia(["nome", "trecho", "q_inicial", "q_final"])
    fs.set_variaveis_juncao(["sexo", "dosagem", "unidade"])
    li_str_descritores = ["duracao", "frequencia", "duracao_total"]
    li_str_categora = ["Swimming"] # todas as categorias tem q colocar elas por escrito aqui
    fs.set_variaveis_descritore_eto_experimento(li_str_descritores, li_str_categora)
    df = fs.get_dados_fundidos()
    print(df)
# def test_fusao_tudo_todas_categorias():
#     ID_EX = "5f8f5503d3d64947e0da22e0"
#     dict_query = { "$and": [{"id_experimento": ObjectId(ID_EX)}, 
#                         {"var_ind.sexo":"macho"},
#                         {"var_ind.dosagem": "flx2.5mg"}]}
#     fs = fus.Fusao_variaveis(dict_query)

#     fs.set_variaveis_rastreamento(["@Vd"])
#     fs.set_variaveis_etografia(["nome", "trecho", "q_inicial", "q_final"])

#     li_str_descritores = ["duracao", "frequencia", "duracao_total"]
#     # se nao colocar categoria da merda.
#     li_str_categora = []

#     fs.set_variaveis_descritore_eto_experimento(li_str_descritores, li_str_categora)
#     df = fs.get_dados_fundidos()
#     print(df)

def test_fusao_so_etografia():
    pass
    # naoest funcionando
    # ID_EX = "5f8f5503d3d64947e0da22e0"
    # dict_query = { "$and": [{"id_experimento": ObjectId(ID_EXPERIMENTO)}, 
    #                     {"var_ind.sexo":"macho"},
    #                     {"var_ind.dosagem": "flx2.5mg"}]}

    # fs = fus.Fusao_variaveis(dict_query)

    # # fs.set_variaveis_rastreamento(["@Vd"])
    # fs.set_variaveis_etografia(["nome", "trecho", "q_inicial", "q_final"])

    # # lis_de_juncao = []
    # # fs.set_variaveis_juncao(lis_de_juncao)

    # li_str_descritores = ["duracao", "frequencia", "duracao_total"]
    # li_str_categora = ["Swimming"]
    # fs.set_variaveis_descritore_eto_experimento(li_str_descritores, li_str_categora)

if __name__ == "__main__":
    test_soment_descritores_cat()
