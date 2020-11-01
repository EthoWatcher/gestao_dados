import deposito_watcher.cadastra_arquivos_mongo as c_a_m
import json

# import deposito_watcher as dp_w
path_descricao_experimento = "./tests/examples/2-banco_experimental.json"
path_junca_teste = "./tests/examples/db_juncao_melhorada.json"

path_marcacao = "./tests/examples/data_marcacao.json"
# precisa atualizar data_marcacao.json
def test_envia_em_batch_arquivos():
    path_list_juncao_experimento = path_junca_teste #str(arguments['<path_list_juncao_experimento>'])
    path_descrivao_experimento  = path_descricao_experimento #str(arguments['<path_descrivao_experimento>'])
    # path_experimento = "./modelo/db_juncao_melhorada.json"

    c_a_m.create_usuario()
    c_a_m.creat_experimento("jmarcolan", path_descrivao_experimento)

    # Lugar aonde esta o banco de dados.
    
    c_a_m.cadastra_batch_arquivos(path_list_juncao_experimento, "jmarcolan", "fluoxetina_gian")



def test_envia_marcacoes():
    with open(path_marcacao) as json_file: 
        marcacoes = json.load(json_file)
        c_a_m.creat_marcacoes(marcacoes)
        # print(data) 
    
    

    # c_a_m.create_usuario()
    # c_a_m.creat_experimento("jmarcolan")

    # # Lugar aonde esta o banco de dados.
    # path_experimento = "./modelo/db_juncao_melhorada.json"
    # c_a_m.cadastra_batch_arquivos(path_experimento, "jmarcolan", "fluoxetina_gian")


# def test_2():
#     c_a_m.eto_mongo