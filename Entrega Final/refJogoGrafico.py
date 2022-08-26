import pygame
from pygame.locals import *
from sys import exit
import time
import random

N = 50
B = 10
R = 10
j = 1
#len(lista_icones)== (10*onze)+(onze-3) or
lista_icones=[]
numero_icone=1
lista_icon_val = True

while lista_icon_val:
    try:
        if len(lista_icones) == 9 or len(lista_icones)==19 or len(lista_icones) ==30 or len(lista_icones)== 41 or len(lista_icones)== 52 or len(lista_icones)== 63 or len(lista_icones)== 74 or len(lista_icones)== 85 or len(lista_icones)== 96 or len(lista_icones)== 107 :
            lista_icones.append(pygame.image.load(f'icone_{numero_icone}.png'))
            lista_icones.append(pygame.image.load(f'icone_{numero_icone}.png'))
        else:
            lista_icones.append(pygame.image.load(f'icone_{numero_icone}.png'))
            numero_icone+=1
    except:
        lista_icones.append(pygame.image.load(f'icone_{numero_icone-1}.png'))
        lista_icones.append(pygame.image.load(f'icone_{numero_icone - 1}.png'))
        lista_icones.append(pygame.image.load(f'icone_{numero_icone - 1}.png'))
        lista_icones.append(pygame.image.load(f'icone_{numero_icone - 1}.png'))
        lista_icones.append(pygame.image.load(f'icone_{numero_icone - 1}.png'))
        lista_icones.append(pygame.image.load(f'icone_{numero_icone - 1}.png'))
        lista_icones.append(pygame.image.load(f'icone_{numero_icone - 1}.png'))
        lista_icones.append(pygame.image.load(f'icone_{numero_icone - 1}.png'))
        lista_icon_val = False



#############################

#setando variaveis da parte grafica
tabuleiro = pygame.image.load('12x6.png')
largura = 1416-118
altura = 708-8
x = 0
y = 0
peca = []
peca.append(pygame.image.load('peca_branca.png'))
peca.append(pygame.image.load('peca_preta.png'))
peca.append(pygame.image.load('peca_branca.png'))
peca.append(pygame.image.load('peca_preta.png'))

lista_usuario =[]
começar_continuar = input('deseja continuar um jogo (S/SIM)? ')


if começar_continuar.upper() == 'SIM' or começar_continuar.upper() == 'S':
    caminho = []
    caminho = formatar_dados_pegos_em_arquivo(caminho,'caminho')

    lista_usuario = formatar_dados_pegos_em_arquivo(lista_usuario,'lista_usuario')
    lista_bonus = sortear_posiçãoAndcadastrar_bonusAndReves('bonus')
    lista_reves = sortear_posiçãoAndcadastrar_bonusAndReves('reves')
    tela = pygame.display.set_mode((largura, altura))  # tela
    lista_usuario = vez_de_cada_jogador(lista_usuario)

else:
    lista_bonus = sortear_posiçãoAndcadastrar_bonusAndReves('bonus')
    lista_reves = sortear_posiçãoAndcadastrar_bonusAndReves('reves')
    caminho = gerar_caminho()

    lista_usuario = cadastrar_usuario(lista_usuario)
    print('jogadores',lista_usuario)
    tela = pygame.display.set_mode((largura, altura))  # tela
    lista_usuario = vez_de_cada_jogador(lista_usuario)

