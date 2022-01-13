
import deposito_watcher.api as api
import deposito_watcher.eto_mongo as mg
import deposito_watcher.parser_eto as par

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

def test_pega_dados():
    nome_exper = "localiza_animal"
    id_experimento = "5f8f5503d3d64947e0da22e0"
    qual_marca = "box"
    df_saida = api.get_pega_todas_marcacaoes(id_experimento, nome_exper, qual_marca)
    print(df_saida)

def test_pega_list_juncao():
    id_experimento = "5f8f5503d3d64947e0da22e0"
    resposta = api.get_list_juncao(id_experimento)
    print(resposta)

def test_create_experimento():
    data = {}
    data["nome_banco_experimental"] = "teste"
    api.creat_experimento("5f8f5503d3d64947e0da22dd", data)

def test_create_juncao():
    api.create_juncao("61df0823c66d84974a791c4b")

def test_up_juncao_eto():
    path_etoxml = "./tests/examples/1e3z1h4.etoxml"
    xml_text = par.parser_xml_file_as_text(path_etoxml)
    api.update_juncao("61df0b4c3915224806eb3728",xml_text, r_eto=True)
    
def test_up_juncao_video():
    path_video = "./tests/examples/1e3z1h4.vxml"
    xml_text = par.parser_xml_file_as_text(path_video)
    api.update_juncao("61df0b4c3915224806eb3728",xml_text, r_video=True)


def test_up_juncao_ras():
    path_ras = "./tests/examples/1e3z1h4.tkin"
    xml_text = par.parser_xml_file_as_text(path_ras)
    api.update_juncao("61df0b4c3915224806eb3728",xml_text, r_rast=True)

def test_up_juncao_var_ind():
    xml_text = {"sexo":"femea"}
    api.update_juncao("61df0b4c3915224806eb3728",xml_text)




if __name__== "__main__":
    test_create_experimento()



    # dict_query = { "$and": [{"id_experimento": ObjectId("5ea1a82993f4d56ba41e567d")}, 
    #                     {"var_ind.sexo":"femea"},
    #                     {"$or": [{"var_ind.dosagem": "flx2.5mg"},
    #                              {"var_ind.dosagem": "veiculo"}
    #                     ]}]}