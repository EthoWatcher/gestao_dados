import etho_dados as et_d
import json


path_eto = "./examples/eto_conver_.json"


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

def test_descritor_todos():
    dic = get_arquivo(path_eto)
    e = et_d.Etografia(dic)
    lat = et_d.Descritor_latencia_expe_cate(e, "Immobility")
    freq = et_d.Descritor_frequencia_expe_cate(e, "Immobility")
    duracao = et_d.Descritor_duracao_expe_cate(e, "Immobility")
    print(duracao)