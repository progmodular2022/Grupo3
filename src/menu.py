#o menu chama o jogo (game.py)
from game import *

#globais estaticas dos botoes do menu
x_botao = (LARG - 180) / 2 #meio
w_botao = 180
h_botao = 70

def botaoMenu(tela,texto,x_bt,n_botao):
    x = x_bt
    y = 100 * n_botao
    width = w_botao
    height = h_botao
    pg.draw.rect(tela, vermelho, (x, y, width, height), 0)
    texto = fonte.render(texto, True, (0, 0, 0))
    tela.blit(texto, (x + (width/2 - texto.get_width()/2),y + height/2 - texto.get_height()/2))

def clickouBotao(pos,x,n_botao):
    y = 100 * n_botao
    if pos[0] > x and pos[0] < x + w_botao:
        if pos[1] > y and pos[1] < y + h_botao:
            return True

def menu():
    running = True
    while running:
        tela.fill(branco)
        click = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        botaoMenu(tela, 'Frutas', x_botao, 1)
        botaoMenu(tela, 'Animais', x_botao, 2)
        botaoMenu(tela, 'Fixo', x_botao, 3)
        if click:
            mx,my = pg.mouse.get_pos()
            if clickouBotao((mx, my), x_botao, 1):
                clear() #"esvazia" a árvore caso tenha algo nela
                setPalavraFormada("")
                posicoes_marcadas = []
                insereArvore('frutas.txt')
                tela.fill(branco)
                game('frutas.txt')

            if clickouBotao((mx, my), x_botao, 2):
                clear()
                setPalavraFormada("")
                posicoes_marcadas = []
                insereArvore('animais.txt')
                tela.fill(branco)
                game('animais.txt')
            if clickouBotao((mx, my), x_botao, 3):
                clear()
                setPalavraFormada("")
                posicoes_marcadas = []
                insereArvore('fixo.txt')
                tela.fill(branco)
                game('fixo.txt')
        pg.display.update()
    pg.quit()

