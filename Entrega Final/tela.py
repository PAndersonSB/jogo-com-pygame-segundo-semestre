import pygame
from pygame.locals import *
from sys import exit
import time
import random
import modelo

lista_bonus = modelo.cadastrarBonusReves('bonus')
lista_reves = modelo.cadastrarBonusReves('reves')
caminho = modelo.gerar_caminho()

N = 50 #caminho
B = 10 #bonus
R = 10 #reves


tabuleiro = pygame.image.load('12x6.png')
largura = 1416-118
altura = 708-8

tela = pygame.display.set_mode((largura, altura))


x = 0
y = 0
peca = []
peca.append(pygame.image.load('peca_branca.png'))
peca.append(pygame.image.load('peca_preta.png'))
peca.append(pygame.image.load('peca_branca.png'))
peca.append(pygame.image.load('peca_preta.png'))

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

def texto(x,y,tamanho_da_fonte,string): #x,y,

    #def que pego a posição , tamanho da fonte e o texto e com isso ploto o texto na tela

    fonte = pygame.font.SysFont('arial', tamanho_da_fonte, True, False)
    mensagem = f'{string}'
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))
    tela.blit(texto_formatado,(x,y))
    #pygame.display.update()

    return texto_formatado

def escolher_icone(jogador):
    complemento = 0  # variavel para pular o valor de 1 do indice da lista para 11
    c = 0
    texto((2 * 118) , (5 * 118), 30,f'aperte 0 para ver mais icones')
    while True:

        for event in pygame.event.get():
            posicao = 21 #posição inicial a ser plotado na tela em X e Y
            numero_na_tela = 1 #enumerando cada icone

            while c != complemento + 9: #complemento começa com 0 então temos 0+9
                #calculo de posição XY
                linha = 10
                while posicao > linha: linha += 10

                coluna = posicao

                while coluna > 10: coluna -= 10

                linha = (linha // 10) - 1

                tela.blit(lista_icones[c], ((coluna * 118), linha * 118)) #ploto icone no indice de C(contador)
                texto((coluna * 118) + 59, (linha * 118), 50, numero_na_tela) #enumerando os icones
                c += 1
                numero_na_tela += 1
                posicao += 2 #2 para ter mais espaço de um icone para o outro na tela

            pygame.display.update()

            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_KP_1:
                    peca[jogador]=lista_icones[0+complemento]
                    #se apertou 1 , pegaremos o icone no indice 0+complemento(inicialmente é 0)
                    #jogador é o indice que veio da def anterior
                    return
                elif event.key == K_KP_2:
                    peca[jogador]=lista_icones[1+complemento]
                    return
                elif event.key == K_KP_3:
                    peca[jogador]=lista_icones[2+complemento]
                    return
                elif event.key == K_KP_4:
                    peca[jogador]=lista_icones[3+complemento]
                    return
                elif event.key == K_KP_5:
                    peca[jogador] = lista_icones[4 + complemento]
                    return
                elif event.key == K_KP_6:
                    peca[jogador] = lista_icones[5 + complemento]
                    return
                elif event.key == K_KP_7:
                    peca[jogador] = lista_icones[6 + complemento]
                    return
                elif event.key == K_KP_8:
                    peca[jogador] = lista_icones[7 + complemento]
                    return
                elif event.key == K_KP_9:
                    peca[jogador] = lista_icones[8 + complemento]
                    return
                elif event.key == K_KP_0:
                    #se 0 , aumenta o contador em 2(para passar de 9 para 11)
                    #numero na tela é resetado para 1
                    #complemento vai de 0 para 11
                    if len(lista_icones) >= complemento+18:
                        #condição para ver se tem icone suficiente para uma nova tela

                        c += 2
                        numero_na_tela = 1
                        complemento += 11
                    else:
                        #caso não tenha ele reseta os valores a zero e começam do indice 0

                        c=0
                        numero_na_tela = 1
                        complemento =0

def trocar_icone():
    indice_icone=0
    #peca[jogador]=lista_icones[indice_icone]

    while True:
        pygame.draw.rect(tela, (255, 255, 255), (0, 0, (12 * 118), (6 * 118))) # pinta tela de branco
        texto((2 * 118), (5 * 118)+59, 30, f'aperte 0 para sair') #texto

        posicionar_as_pecas(2, 0, 0) #def de posicionar a peça aonde eu quero com o sorteio em 0
        texto((3*118)-59,59,50,1) #texto "1" para enumarar cada icone de jogador
        posicionar_as_pecas(4, 1, 0)
        texto(5*118, 59, 50, 2)
        posicionar_as_pecas(6, 2, 0)
        texto((7*118)-59, 0, 50, 3)
        posicionar_as_pecas(8, 3, 0)
        texto(9 * 118, 0, 50, 4)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_KP_0: #sair do loop
                    return
                elif event.key == K_KP_1:
                    escolher_icone(0) #apertando o botão 1 ele escolhe o jogador 1 que tem indice 0 na lista
                elif event.key == K_KP_2:
                    escolher_icone(1)
                elif event.key == K_KP_3:
                    escolher_icone(2)
                elif event.key == K_KP_4:
                    escolher_icone(3)

def plotar_vencedor(lista_usuario):
    #plotar antes do while
    xis = 5
    yplis = 1
    for c, i in enumerate(lista_usuario):
        if yplis == 2: xis = 4
        elif yplis == 3: xis = 6
        elif yplis == 4: xis = 3

        tela.blit(peca[c], ((xis * 118) + 29, (yplis * 118) + 29))
        texto((xis * 118) + 5, (yplis * 118) + 5, 28, lista_usuario[c][0])
        texto((xis * 118) + 5, ((yplis) * 118) + 110, 30, f'{c+1}°')
        texto((xis* 118) + 5, ((yplis) * 118) + 80, 30, f'${lista_usuario[c][1]}')

        yplis +=1

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:  # BUTÃO 1 , INICIAR RODADA ?
                if event.key == K_KP_0:
                    return

def plotar_ranking():
    lista_pr = []
    xpr= 10
    ypr= 10

    lista_pr = []#formatação dos dados pegos no arquivo

    for c , i in enumerate(lista_pr):
        if c // 5 == 15: #limitador para parar de plotar na tela
            break

        texto(xpr,ypr,20,f'{c+1}° {lista_pr[c][0]}, {lista_pr[c][1]}, {lista_pr[c][2]}')
        #chama def que plota nome saldo e posição
        ypr+= 40 #aumenta 40 na vertical

        if c == 15 or c == 30 or c == 45 or c == 60: #significa fim de uma coluna do rank
            xpr += 230 #soma 230 na horizontal para inicial mais uma coluna
            ypr= 10 #reseta na vertical

    pygame.display.update()
    #atualiza tela e inicia clico esperando apertar um botão para sair da tela de ranking
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_KP_0:
                    return

def plotar_saldo(c,lista_usuario):
    if c <2:
        tela.blit(peca[c], ((0 * 118) + 29, ((c+1) * 118) + 29))
        texto((0 * 118) + 5, ((c+1) * 118) + 5, 28, lista_usuario[c][0])
        texto((0 * 118) + 5, ((c+1) * 118) + 80, 30, f'${lista_usuario[c][1]}')
    else:
        tela.blit(peca[c], ((0 * 118) + 29, ((c+2) * 118) + 29))
        texto((0 * 118) + 5, ((c+2) * 118) + 5, 28, lista_usuario[c][0])
        texto((0 * 118) + 5, ((c+2) * 118) + 80, 30, f'${lista_usuario[c][1]}')
    return

def plotar_numero_sorteado(numero):

    animado = 1
    pygame.draw.rect(tela, (255, 255, 255), (0 + 10, (3 * 118) + 10, (1 * 118) - 10, (1 * 115) - 10))
    #pintar um lugar de branco

    while animado != numero+1:
        #primeiro ciclo onde ele vai printar o número
        #no final ele acrescenta um ao contador e termina quando chega no número sorteado

        yanimado = 0
        texto((0 * 118)+ 25, (3 * 118)+ 25 ,70,animado)

        while yanimado < 120:
            #segundo ciclo que pinta o numero sorteado de branco ao poucos
            #a cada ciclo vai aumentando o tamanho do rect(retangulo) até chegar no tamanho maximo

            pygame.draw.rect(tela,(255,255,255),(0+10,(3*118)+10,(1*118)-10,(1*yanimado)-10 ))
            pygame.time.delay(30)
            pygame.display.update()
            yanimado+=5

        animado +=1

    texto((0 * 118) + 25, (3 * 118) + 25, 70, numero)
    pygame.display.update()

    return

def posicionar_as_pecas(posicao, contador,sorteio):
    #def que pega a posição e soma com o numero sorteado e plota a peça no lugar certo
    # o contador é necessario para saber qual jogador é
    contador += 1
    linha = 10

    if (sorteio + posicao) > 50:
        sorteio = (50 - posicao)


    while (sorteio + posicao) > linha:
        linha += 10

    coluna = (sorteio + posicao)

    while coluna > 10:
        coluna -= 10

    linha = (linha // 10) - 1

    if contador == 1:
        tela.blit(peca[0], ((coluna * 118)+10, (linha * 118)+10))
    if contador == 2:
        tela.blit(peca[1], ((coluna * 118) + 59, (linha * 118)+10))
    if contador == 3:
        tela.blit(peca[2], ((coluna * 118)+10, (linha * 118) + 59))
    if contador == 4:
        tela.blit(peca[3], ((coluna * 118) + 59, (linha * 118) + 59))

    return

def plotar_numeros(posicao):
    #def que plota os numeros e simbolos B R no tabuleiro

    while posicao != 51:
        linha = 10
        while posicao > linha: linha += 10

        coluna = posicao

        while coluna > 10: coluna -= 10

        linha = (linha // 10) - 1
        #
        xnum = 10
        ynum = 10
        fonte = pygame.font.SysFont('arial', 30, True, False)

        mensagem = f'{posicao}'

        texto_formatado = fonte.render(mensagem, True, (0, 0, 0))
        tela.blit(texto_formatado, ((coluna * 118) + xnum, (linha * 118) + ynum))

        if caminho[posicao - 1] == 'B':
            mensagem = 'B'
            texto_formatado = fonte.render(mensagem, True, (32, 32, 240))
            tela.blit(texto_formatado, ((coluna * 118) + 45, (linha * 118) + 45))

        elif caminho[posicao - 1] == 'R':
            mensagem = 'R'
            texto_formatado = fonte.render(mensagem, True, (240, 32, 32))
            tela.blit(texto_formatado, ((coluna * 118) + 45, (linha * 118) + 45))

        posicao += 1

    return

def tela_inicial(lista_usuario): #lista_usuario

    #def onde atualizo a tela toda depois de uma rodada

    tela.blit(tabuleiro, (0, 0))
    posicao = 0
    plotar_numeros(posicao) #numeros e simbolos na tela

    for c, i in enumerate(lista_usuario): #jogadores 'lista usuario puxando a def posicionar com sorteio 0'
        posicionar_as_pecas(lista_usuario[c][2], c, 0)

    for c,i in enumerate(lista_usuario): #def que plota a parte esquerda com icone nome e saldo dos jogadores
        plotar_saldo(c,lista_usuario)

    texto((0 * 118) + 25, (3 * 118) + 25, 70, 'l>') #apenas estetica , plota um simbolo de play
    #dados , nome , saldo
    pygame.draw.rect(tela, (255, 255, 255), (118 + 10, (5 * 118) + 10, (10 * 118) - 12, (1 * 115) - 10))
    return


########################################################

def vez_de_cada_jogador(lista_usuario):

    len_da_lista = len(lista_usuario)
    parametro_de_vitoria = 'nao'

    pygame.init()
    tela = pygame.display.set_mode((largura, altura))


    while True:
        for event in pygame.event.get():
            #pygame.time.delay(5)
            tela_inicial(lista_usuario)  # plotar tela inicial "de preferencia dentro do loop né anderson"
            pygame.display.update()

            if event.type == QUIT:
                pygame.quit()
                exit()

            elif event.type == KEYDOWN: #BUTÃO 1 , INICIAR RODADA ?
                if event.key == K_KP_0:
                    c = 0

                    while c != len_da_lista:

                        lista_usuario[c] = andar(lista_usuario[c], caminho, lista_bonus, lista_reves, c)

                        if lista_usuario[c][2] == N:
                            parametro_de_vitoria = 'sim'

                        c += 1

                        #tela_inicial(lista_usuario)  # plotar tela inicial "de preferencia dentro do loop né anderson"
                        pygame.display.update()


                elif event.key == K_KP_1:  # para o jogo e salvar

                    return lista_usuario

                elif event.key == K_KP_2:
                    pygame.draw.rect(tela, (255, 255, 255), (0, 0 , (12 * 118) , (6 * 118) ))
                    plotar_ranking()

                elif event.key == K_KP_3:
                    trocar_icone()

            elif parametro_de_vitoria == 'sim':

                pygame.draw.rect(tela, (255, 255, 255), (0, 0, (12 * 118), (6 * 118)))
                #pinta a tela de branco e puxa def de ranking final do jogo
                plotar_vencedor(lista_usuario)

                lista_ranking = []
                if len(lista_ranking) >1:
                    for c , i in enumerate(lista_ranking):
                        lista_usuario.append(lista_ranking[c])

                #ordenar
                # ordena a lista_usuario do jogo atual
                #salvar

                pygame.quit()
                exit()

    return lista_usuario

def andar(lista_usuario,caminho,lista_bonus,lista_reves,contador):

    sorteio = roleta(5) # puxar def de animação do sorteio

    sorteio2 = 1
    while sorteio2 != sorteio+1:
        #ciclo que adiciona +1 na posição da peça e printa na tela a peça em cada uma dessas posições

        posicionar_as_pecas(lista_usuario[2],contador,sorteio2)
        pygame.time.delay(150)
        pygame.display.update()
        sorteio2+=1

    lista_usuario[2] = lista_usuario[2] + sorteio

    #aqui paramentro para fim de game
    if lista_usuario[2] > N:
        lista_usuario[2] = N


    if caminho[(lista_usuario[2])-1] == 'B':
        sorteio = roleta(24)

        lista_usuario[1] = lista_usuario[1] + lista_bonus[sorteio][1]

        texto(118+5, 5 * 118, 25, f'você caiu numa casa bonus: {lista_bonus[sorteio][0]}\n')
        texto(118+5, (5 * 118) + 30, 25, f'saldo atual : , {lista_usuario[1]}')
        pygame.display.update()
        pygame.time.delay(5000)


    if caminho[(lista_usuario[2])-1] == 'R':
        sorteio = roleta(24)

        lista_usuario[1] = lista_usuario[1] - lista_reves[sorteio][1]

        texto(118+5, 5 * 118, 25, f'você caiu numa casa reves: {lista_reves[sorteio][0]}\n')
        texto(118+5, (5 * 118)+30, 25, f'saldo atual : , {lista_usuario[1]}')
        pygame.display.update()
        pygame.time.delay(5000)

    return lista_usuario

def roleta(n):
    numero_sorteado =random.randint(1, n)
    if n != 24:
        pass
        plotar_numero_sorteado(numero_sorteado)

    return numero_sorteado