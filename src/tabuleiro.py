import string
import random
from arv import *
__all__ = ['criaTabuleiro']

def criaTabuleiro():
    tab = [[None for i in range(6)] for j in range(6)]
    letras = string.ascii_lowercase
    palavraEscolhida = palavraAleatoria() #palavra aleatoria puxada da arvore

    while (len(palavraEscolhida) > 0): #garante que sempre vai ter uma palavra da arvore
        for i in range(6):
            for j in range(6):
                if len(palavraEscolhida) == 0:
                    break
                if tab[i][j] == None:
                    if random.randint(0,3) == 1:
                        tab[i][j] = palavraEscolhida[0]
                        palavraEscolhida = palavraEscolhida[1:]

        for i in range(6):
            for j in range(6):
                if tab[i][j] == None:
                    numAleatorio = random.randint(0, len(letras) - 1)
                    tab[i][j] = letras[numAleatorio]

    return tab

