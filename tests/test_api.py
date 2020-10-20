
import deposito_watcher.api as api



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

    

    


    # dict_query = { "$and": [{"id_experimento": ObjectId("5ea1a82993f4d56ba41e567d")}, 
    #                     {"var_ind.sexo":"femea"},
    #                     {"$or": [{"var_ind.dosagem": "flx2.5mg"},
    #                              {"var_ind.dosagem": "veiculo"}
    #                     ]}]}