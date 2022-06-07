import pygame as pg
pg.init()
#cores
preto = (0,0,0)
branco = (255,255,255)
azul_claro = (150,150,255)
verde = (0,255,0)
vermelho = (255,0,0)

#dimensoes da janela
ALT = 600
LARG = 800

#texto
pg.font.init()
fonte = pg.font.SysFont('Comic Sans MS', 40)

#tela pygame
tela = pg.display.set_mode((LARG,ALT))
tela.fill(branco)
#pg.display.update()