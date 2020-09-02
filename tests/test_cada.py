import deposito_watcher.cadastra_arquivos_mongo as c_a_m

# import deposito_watcher as dp_w

def test_envia_em_batch_arquivos():
    c_a_m.create_usuario()
    c_a_m.creat_experimento("jmarcolan")

    # Lugar aonde esta o banco de dados.
    path_experimento = "./modelo/db_juncao_melhorada.json"
    c_a_m.cadastra_batch_arquivos(path_experimento, "jmarcolan", "fluoxetina_gian")


# def test_2():
#     c_a_m.eto_mongo