import sys
path_to_module = "./src/"
sys.path.append(path_to_module)

import palavra

def test_removeUltimoCaracter():
    palavra.adicionaCaracter('a')
    palavra.adicionaCaracter('s')
    palavra.removeUltimoCaracter()
    assert palavra.getPalavraFormada() == 'a'
    
def test_adicionaCaracter():
    palavra.setPalavraFormada('oi')
    palavra.adicionaCaracter('a')
    assert palavra.getPalavraFormada() == 'oia'


