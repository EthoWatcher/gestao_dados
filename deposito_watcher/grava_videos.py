from shutil import copyfile

from bson.objectid import ObjectId

import deposito_watcher.querys_feitas as qf
import deposito_watcher.eto_mongo as mg


def grava_videos_experimento(id_experimento, path_server):
    gravador_file = GravaVideo(path_server)


    dict_query =  {"id_experimento": ObjectId(id_experimento)}
    j = qf.Get_Juncoes(dict_query)
    cursor = j.get_cursor()
    for juncao in cursor:
        video_mongo_data = mg.Video().get_by_hash(juncao["id_video"]).cliente.data

        # vide_file = {"id":"123123","cadastroVideo":{"dadoOriginal": {"nomeOpencv":"./tests/examples/1e3z1h4.avi"}}}
        gravador_file.grava_video(video_mongo_data)



class GravaVideo():
    def __init__(self, path_server):
        self.path_server = path_server
        # self.usuario = usuario
        # self.experimento = experimento
    
    def grava_video(self, video_file_dict):
        copyfile(video_file_dict["cadastroVideo"]["dadoOriginal"]["nomeOpencv"], self.path_server + str(video_file_dict["_id"])+".avi" )
        