import sys
from tabuleiro import *
from palavra import *
from config import *
from arv import *

tab = ''

###tamanho dos retangulos
ret_alt = 83
ret_larg = 88

def inicializar(arq):
    global tab
    global posicoes_marcadas
    insereArvore(arq)
    tab = criaTabuleiro()
    setPalavraFormada("")
    posicoes_marcadas = []

#####
posicoes_marcadas = []

def desenhaTabuleiro(tela,ret_lar,ret_al):
    linha_y = 0
    linha_x = 0
    for i in range(7):
        pg.draw.line(tela, preto, (0, linha_y), (ret_lar*6, linha_y), width=2)
        linha_y += ret_alt
    for i2 in range(7):
        pg.draw.line(tela, preto, (linha_x, 0), (linha_x, ret_al*6), width=2)
        linha_x += ret_larg
    return

def preencheLetras(tela,ret_lar,ret_al):
    i = 0
    aux2 = 1
    while (i < 6):
        aux = 1
        for j in range(6):
            txt_x = ret_larg / 2 * aux
            txt_y = ret_alt / 2 * aux2
            text_surface = fonte.render(tab[i][j], False, preto)
            text_rect = text_surface.get_rect(center=(txt_x, txt_y))
            tela.blit(text_surface, text_rect)
            aux += 2
        aux = 1
        aux2 += 2
        i+= 1

def posMouseClick(mx,my):
        posicao_tab = int(my // (ret_alt*6/6)), int(mx // (ret_larg*6 /6))
        r = posicao_tab[0]
        c = posicao_tab[1]
        if r >= 0 and r <=5 and c >= 0 and c <=5:
            return posicao_tab
        return

def letraMouseClick(pos):
    return tab[pos[0]][pos[1]]

def desenhaQuad(tela,pos_tab_linha,pos_tab_coluna,transparencia): #isso ta funcionando mas nao sei como
    if transparencia:
        rect = pg.Surface((ret_larg, ret_alt), pg.SRCALPHA, 32)
        rect.fill((23, 100, 255, 50))
    else:
        rect = pg.Surface((ret_larg, ret_alt))
        rect.fill(branco)

    dist_x = ret_larg * pos_tab_coluna
    dist_y = ret_alt * pos_tab_linha
    tela.blit(rect, (dist_x, dist_y))
    return posMouseClick(pos_tab_linha,pos_tab_coluna)

def botaoLimpar(tela):
    x = LARG - 200
    y = 100
    width = 180
    height = 70
    pg.draw.rect(tela, verde, (x, y, 180, 70), 0)
    texto = fonte.render("Limpar", True, (0, 0, 0))
    tela.blit(texto, (x + (width/2 - texto.get_width()/2),y + height/2 - texto.get_height()/2))

def clickouBotaoLimpar(pos,x,y,width,height):

    if pos[0] > x and pos[0] < x + width:
        if pos[1] > y and pos[1] < y + height:
            return True

def game(arq):
    global posicoes_marcadas
    inicializar(arq)
    running = True
    while running:

        click = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
        desenhaTabuleiro(tela,ret_larg,ret_alt)
        preencheLetras(tela,ret_larg,ret_alt)
        botaoLimpar(tela)

        if click:
            mx,my = pg.mouse.get_pos()
            pos = posMouseClick(mx,my)
            if clickouBotaoLimpar((mx,my),LARG-200,100,180,70):
                tela.fill(branco)
                setPalavraFormada("")
                posicoes_marcadas = []
            else:
                if pos != None:
                    if [pos[0],pos[1]] in posicoes_marcadas:
                        if [pos[0],pos[1]] == posicoes_marcadas[-1]:
                            desenhaQuad(tela,pos[0],pos[1],False)
                            posicoes_marcadas.remove([pos[0],pos[1]])
                            removeUltimoCaracter()
                            text_surface = fonte.render(getPalavraFormada(), False, preto)
                            tela.blit(text_surface, (0, 520))
                            tela.fill(branco)
                            for el in posicoes_marcadas:
                                desenhaQuad(tela,el[0],el[1],True)
                    else:
                        desenhaQuad(tela,pos[0],pos[1],True)
                        posicoes_marcadas.append([pos[0],pos[1]])
                        letra = letraMouseClick(pos)
                        adicionaCaracter(letra)
        if verificaPrefixo(getPalavraFormada()):
            if procuraArv(getPalavraFormada()) == False:
                text_surface = fonte.render(getPalavraFormada(), False, preto)
            else:
                text_surface = fonte.render(getPalavraFormada(), False, verde)

        else:
            text_surface = fonte.render(getPalavraFormada(), False, vermelho)
        tela.blit(text_surface, (0,ret_alt * 6))

        pg.display.update()

    return