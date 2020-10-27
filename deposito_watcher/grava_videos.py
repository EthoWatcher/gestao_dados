from shutil import copyfile

class GravaVideo():
    def __init__(self, path_server):
        self.path_server = path_server
        # self.usuario = usuario
        # self.experimento = experimento
    
    def grava_video(self, video_file_dict):
        copyfile(video_file_dict["cadastroVideo"]["dadoOriginal"]["nomeOpencv"], self.path_server +video_file_dict["id"]+".avi" )
        