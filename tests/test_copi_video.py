
import deposito_watcher.grava_videos as gr_v


from bson.objectid import ObjectId

import deposito_watcher.querys_feitas as qf
import deposito_watcher.eto_mongo as mg



# tem que ainda extrair manualmente 
ID_EXPERIMENTO ="5f8f5503d3d64947e0da22e0"
def test_fazer_querys():
    dict_query =  {"id_experimento": ObjectId(ID_EXPERIMENTO)}
    j = qf.Get_Juncoes(dict_query)
    cursor = j.get_cursor()
    # for juncao in cursor:
    #     video_mongo_data = mg.Video().get_by_hash(juncao["id_video"]).cliente.data
    l = len(list(cursor))
    print(l)


def test_grava_video_batch():
    gr_v.grava_videos_experimento(ID_EXPERIMENTO,"./tests/examples/arquivos_gerados/")
    # l = len(list(cursor))   

# C:\Mestrado Oficial Marino\Videos cegados
def test_video_abre():
    gravador_file = gr_v.GravaVideo("./tests/examples/arquivos_gerados/")
    vide_file = {"_id":"123123","cadastroVideo":{"dadoOriginal": {"nomeOpencv":"./tests/examples/1e3z1h4.avi"}}}
    gravador_file.grava_video(vide_file)
