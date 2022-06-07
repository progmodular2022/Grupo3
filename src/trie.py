from random import choice
from json import dumps


__trie: dict = {} #arvore dicionario

def insert(word,fromWhere,isWord) -> bool: 
    if isWord(word,fromWhere)!=False and len(word)!=0: #se nao for palavra vazia e se existir a palavra
        __insertRec(__trie,word,0) #insere a palavra na arvore
        return True
    else:
        return False


def __insertRec(dictTree,word,index) -> None:
    current = dictTree #no atual
    if index == len(word): #se chegar no final da palavra
        current['isWord'] = True #marca como palavra
        return
    else:
        if word[index] not in current: #se ainda nao existir a letra cria novo no
            current[word[index]] = {}
        __insertRec(current[word[index]],word,index+1) #chama recursivamente
    return

def search(word) -> bool:
    if len(word)==0: #se for palavra vazia retorna falso
        return False
    else:
        return __searchRec(__trie,word,0)
    
def __searchRec(dictTree,word,index) -> bool:
    current = dictTree #no atual
    if index == len(word): #se chegar no final da palavra
        if 'isWord' in current: #se for palavra retorna verdadeiro
            return True
        else:
            return False
    else:
        if word[index] in current: #se ainda nao existir a letra retorna falso
            return __searchRec(current[word[index]],word,index+1) #chama recursivamente
        else:
            return False
    
def delete(word) -> bool:
    if len(word)==0: #se for palavra vazia retorna False
        return False
    else:
        return False if __deleteRec(__trie,word,0) == -1 else True #se retornar -1 retorna False se nao retorna True
         

def __deleteRec(dictTree,word,index) -> int:
    current = dictTree #no atual
    lenDict = len(current) #numero de nos filhos
    if len(word)==index and 'isWord' in current: #se chegar no final da palavra e for palavra
        del current['isWord'] #deleta marcador de palavra
        return lenDict #retorna numero de nos filhos
    if word[index] not in list(current.keys()): #se ainda nao existir a letra retorna -1
        return -1
    res = __deleteRec(current[word[index]],word,index+1) #chama recursivamente
    if res == -1: #se nao existir letra so retorna que nao achou letra
        return -1
    if lenDict==1 and res==1: #se so tem um filho e deletou
        del current[word[index]] #deleta no
        return 1 #retorna que deletou no com tamanho 1
    return 0 # para quebrar o loop quando encontrar primeiro no que faz parte de outra palavra que n seja a deletada

def showAllWords() -> None: #mostra as palavras da arvore
    print(__generateArray(__trie,"",[]))
    return 

def __generateArray(dictTree,currentString,words) -> list:
    current = dictTree #no atual
    if 'isWord' in current.keys(): #se for palavra adiciona a palavra a lista
        words.append(currentString)
        if len(current)==1: #retorna se so houver nao possuir mais palavra no caminho
            return words
    for key in current.keys(): #percorre os nos filhos
        if key!='isWord': #se nao for palavra
            words = __generateArray(current[key],currentString+key,words)
    return words
    
def __insertPrefix(prefix,word) -> str:
    return prefix+word

def __iterateList(words,prefix) -> list:
    res = []
    for word in words:
        res.append(__insertPrefix(prefix,word))
    return res

def wordsWith(prefix) -> list:
    if len(prefix)==0: #se for palavra vazia retorna todas as palavras
        return __generateArray(__trie,"",[])
    else:
        return __iterateList(__getSubTreeAt(__trie,prefix,0),prefix)


def __getSubTreeAt(dictTree,word,index) -> list:
    current = dictTree #no atual
    if index!=len(word) and word[index] not in current:
        return []
    if index == len(word): #se chegar no final do prefixo
        return __generateArray(current,"",[]) #retorna todas as palavras que possuem prefixo
    else:
        return __getSubTreeAt(current[word[index]],word,index+1) #chama recursivamente

def random() -> str: #retorna uma palavra aleatoria
    return __randomRec(__trie)

def __randomRec(dictTree) -> str:
    current = dictTree  #no atual
    currentChar = choice(list(current.keys())) #pega uma letra aleatoria do no atual
    if currentChar=='isWord': #se for palavra retorna 
        return ''
    else:
        return currentChar+__randomRec(current[currentChar]) #adiciona letra a palavra e chama recursivamente

def __debuggingDict() -> None: # função de debugging que mostra o esquema da arvore formatada
    print(dumps(__trie,indent=4))
    return

def clear() -> None:
    __trie.clear()

####
