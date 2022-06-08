#responsável por fazer o "meio de campo" entre o módulo do grupo 1 e a aplicação.
from trie import *

__all__ = ['wordInArq', 'insereArvore','verificaPrefixo','procuraArv','clear','palavraAleatoria']

def wordInArq(word,arq):
    file = open(arq, 'r')
    list = []
    for line in file:
        list.append(line.strip())
    file.close()
    if word in list:
        return True
    return False

def insereArvore(arq):
    file = open(arq, 'r')
    for line in file:
        line = line.strip()
        if wordInArq(line,arq):
            insert(line,arq,wordInArq)
    file.close()
    return

def verificaPrefixo(pr):
   if wordsWith(pr) == []:
       return False
   return True

def procuraArv(s):
    return search(s)

def limpaArv():
    clear()
    return

def palavraAleatoria():
    return random()
