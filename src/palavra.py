#responsável pela palavra que será formada no jogo.
__all__ = ['getPalavraFormada','setPalavraFormada','adicionaCaracter','removeUltimoCaracter']

palavraFormada = ""

def getPalavraFormada():
    global palavraFormada
    return palavraFormada

def setPalavraFormada(palavra):
    global palavraFormada
    palavraFormada = palavra
    return

def adicionaCaracter(c):
    palavra = getPalavraFormada()
    palavra += c
    setPalavraFormada(palavra)
    return

def removeUltimoCaracter():
    palavra = getPalavraFormada()
    palavra = palavra[:-1]
    setPalavraFormada(palavra)
    return
