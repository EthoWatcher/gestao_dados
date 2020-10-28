
import cv2
import numpy as np
import base64

# vai ter que adaptar para rodar num servidor
class Tocador_video():
    def __init__(self, experimento_path, video_id):
        self.experimento_path = experimento_path
        self.video_id = video_id
        self.video_path_completo = self.experimento_path + self.video_id + ".avi"
        # self.vid = cv2.VideoCapture( self.video_path_completo)

    def get_list_quadros(self, q_inicio, q_fim):
        lis_imagem = []
        for quadro in range(q_inicio, q_fim):
            lis_imagem.append(self.get_quadro(quadro))
        return lis_imagem

    def get_video_gerador(self, q_inicio, q_fim):
        for imagem in self.get_list_quadros(q_inicio,q_fim):
            yield c_64_2_image(imagem)

    def get_quadro(self, quadro):
        vid = cv2.VideoCapture( self.video_path_completo)
        vid.set(1, quadro)
        ret, frame = vid.read()
        return c_image_2_64(frame)

# def gerador_video(quadro_inicio, quadro_fim)


def c_image_2_64(imagem):
    retval, buffer = cv2.imencode('.jpg', imagem)
    jpg_as_text = base64.b64encode(buffer)
    return jpg_as_text

def c_64_2_image(jpg_as_text):
    jpg_original = base64.b64decode(jpg_as_text)
    return jpg_original

def c_image_to_np(jpg_original):
    im_arr = np.frombuffer(jpg_original, dtype=np.uint8)  # im_arr is one-dim Numpy array
    img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
    return img 



# def abre_video(name_path):
#     cap = cv2.VideoCapture(name_path)
#     i = 0
#     while(1):
#         i +=1
#         _, frame = cap.read()
#         cv2.imshow("frame", frame)
#         k = cv2.waitKey(1)
#         if k == 27:
#             break
#         if i == 100:
#             break

#     cap.release()
#     cv2.destroyAllWindows()
#     return 0