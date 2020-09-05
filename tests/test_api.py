
import deposito_watcher.api as api



def test_senha_correta():
    assert api.get_usuario("jmarcolan", 1234)[0]

def test_senha_errada():
    assert api.get_usuario("jmarcolan", 12342)[0] == False


def test_get_list_experimento():
    r_saida, documentos = api.get_list_experimento("5f4f8f39c66cad3eb1dd0d4d")