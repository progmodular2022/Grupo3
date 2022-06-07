import sys
path_to_module = "./src/"
sys.path.append(path_to_module)

import arv

def test_verificaPrefixo():
    assert arv.verificaPrefixo('aaaaaaaaa') == False
'''   
def test_wordInArq():
    assert arv.wordInArq('banana','frutas.txt') == True
'''
