
import deposito_watcher.api as api



def test_senha_correta():
    assert api.get_usuario("jmarcolan", 1234)[0]

def test_senha_errada():
    assert api.get_usuario("jmarcolan", 12342)[0] == False