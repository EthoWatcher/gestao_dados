
import deposito_watcher.grava_videos as gr_v 
# C:\Mestrado Oficial Marino\Videos cegados
def test_video_abre():
    gravador_file = gr_v.GravaVideo("./tests/examples/")
    vide_file = {"id":"123123","cadastroVideo":{"dadoOriginal": {"nomeOpencv":"./tests/examples/1e3z1h4.avi"}}}
    gravador_file.grava_video(vide_file)
