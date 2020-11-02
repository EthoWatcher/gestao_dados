
import deposito_watcher.api as api
import deposito_watcher.eto_mongo as mg

from bson.objectid import ObjectId

def test_senha_correta():
    assert api.get_usuario("jmarcolan", 1234)[0]

def test_senha_errada():
    assert api.get_usuario("jmarcolan", 12342)[0] == False


def test_get_list_experimento():
    r_saida, documentos = api.get_list_experimento("5f4f8f39c66cad3eb1dd0d4d")

def test_get_dados():
    dict_saida = {'Variaveis_cinematicas': ['Variaveis_cinematicastodos'],
                   'Variaveis_etograficas': ['duracao_total'], 
                   'categoria_comportamental': ['Immobility'], 
                   'var_ind.dosagem': ['veiculo'], 
                   'var_ind.sexo': ['macho'], 
                   'var_ind.unidade': ['unidadetodos']}


    id_experimento = '5f4f8f39c66cad3eb1dd0d50'
    r_ecnotrn, df = api.get_csv_by_query(id_experimento, dict_saida)



def test_get_config_marca_exp():
    id_experimento = "5f8f5503d3d64947e0da22e0"
    nome_marca = "localiza_animal"
    r_ecntro, saida  = api.get_config_marca_exp(id_experimento, nome_marca)

def test_get_randon_juncao():
    get_20 = 20
    id_experimento = "5f8f5503d3d64947e0da22e0"
    nome_exper = "localiza_animal"
    qual_marcacao = "box"
    r_enco, ls = api.get_list_rand_ano(id_experimento,get_20,nome_exper,qual_marcacao )
    print(ls)


def test_atualiza_marcacao():
    id_marcacao = "5f9e336fbd51328d41f3bb20"
    qual_marca = "box"
    marcacao= {
            "x" : 0,
            "y" : 0,
            "w" : 110,
            "h" : 110,
            "anotado" : True
        }

    api.atualiza_marcacao(id_marcacao,qual_marca,marcacao)
    # jc = mg.Marcacao()
    # nova = jc.get_by_hash(ObjectId(id_marcacao)).update(marcacao)
    # print(nova)


    


    # dict_query = { "$and": [{"id_experimento": ObjectId("5ea1a82993f4d56ba41e567d")}, 
    #                     {"var_ind.sexo":"femea"},
    #                     {"$or": [{"var_ind.dosagem": "flx2.5mg"},
    #                              {"var_ind.dosagem": "veiculo"}
    #                     ]}]}