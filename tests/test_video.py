
import deposito_watcher.video as v 
import cv2
# C:\Mestrado Oficial Marino\Videos cegados
# experimento path 
PATH_SERVIDOR = "./tests/examples/arquivos_gerados/"

def test_video_abre():
    tocador = v.Tocador_video(PATH_SERVIDOR, "5f8f5517d3d64947e0da2425" )
    for imagem in tocador.get_video_gerador(100,300):
        np_image = v.c_image_to_np(imagem)
        cv2.imshow("teste", np_image)
        k = cv2.waitKey(int(1/30*1000))

    cv2.destroyAllWindows()

