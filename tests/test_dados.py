import deposito_watcher.etho_dados as et_d
import json


path_eto = "./tests/examples/eto_conver_.json"
path_junca_teste = "./tests/examples/juncao_teste.json"
path_trak = "./tests/examples/rastreamento.json"

def get_arquivo(arquivo):
    with open(arquivo, 'r', encoding="utf-8") as f:
        distros_dict = json.load(f)
    # f = open(arquivo, "rb")
    return distros_dict


def test_etografia_contrucao():
    dic = get_arquivo(path_eto)
    e = et_d.Etografia(dic)
    print(e)


def test_etografia_get_categorias():
    dic = get_arquivo(path_eto)
    e = et_d.Etografia(dic)
    anot_swiming = e.get_anotacoes_eto_categoria("Swimming")
    print(anot_swiming)


def test_etografia_get_dados_video():
    dic = get_arquivo(path_eto)
    e = et_d.Etografia(dic)
    anot_swiming = e.get_dados_video_analisado()
    print(anot_swiming)



def test_descritor_duraca():
    dic = get_arquivo(path_eto)
    e = et_d.Etografia(dic)
    duracao = et_d.Descritor_duracao_expe_cate(e, "Swimming")
    print(duracao.get_resultado())


def test_descritor_frequencia():
    dic = get_arquivo(path_eto)
    e = et_d.Etografia(dic)
    freq = et_d.Descritor_frequencia_expe_cate(e, "Swimming")
    print(freq.get_resultado())


def test_descritor_latencia():
    dic = get_arquivo(path_eto)
    e = et_d.Etografia(dic)
    lat = et_d.Descritor_latencia_expe_cate(e, "Swimming")
    print(lat.get_resultado())


def test_descritor_inicio_analise():
    dic = get_arquivo(path_eto)
    e = et_d.Etografia(dic)
    q_inicio_analise = et_d.Descritores_inicio_analise(e,"Immobility")
    print(q_inicio_analise.get_resultado())

def test_descritor_fps():
    dic = get_arquivo(path_eto)
    e = et_d.Etografia(dic)
    q_inicio_analise = et_d.Descritores_fps(e,"Immobility")
    print(q_inicio_analise.get_resultado())



def test_descritor_todos():
    dic = get_arquivo(path_eto)
    e = et_d.Etografia(dic)
    lat = et_d.Descritor_latencia_expe_cate(e, "Immobility")
    freq = et_d.Descritor_frequencia_expe_cate(e, "Immobility")
    duracao = et_d.Descritor_duracao_expe_cate(e, "Immobility")
    print(duracao)

def test_descritor_juncao_experimento():
     dic = get_arquivo(path_junca_teste)
     de = et_d.Descritor_Juncao_experimento(dic,"sexo")
     print(de.resultado)


def test_descritor_juncao_experimento_id_video():
     dic = get_arquivo(path_junca_teste)
     de = et_d.Descritor_Juncao_experimento_id_video(dic,"sexo")
     print(de.resultado)



def test_descritor_nome_etografia():
    dic = get_arquivo(path_eto)
    e = et_d.Etografia(dic)
    de = et_d.Descritores_nome_categoria_etografia(e,"")
    de1 = et_d.Descritores_q_inicio_categoria_etografia(e,"")
    print(de.resultado)


def test_descritor_path_etografia():
    dic = get_arquivo(path_eto)
    e = et_d.Etografia(dic)
    de = et_d.Descritor_nome_caminho_experimento(e,"")

    print(de.resultado)

def test_dados_rastreamento():
    dic = get_arquivo(path_trak)
    e = et_d.Rastreamento(dic)
    print(e)
    