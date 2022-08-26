import random
import PySimpleGUI as sg
import pandas as pd

N = 50 #caminho
B = 10 #bonus
R = 10 #reves

def cadastrarBonusReves(nome): #cadastra os texots e valores dos bonus e reves que serão sorteados.
    lista_bonus = []
    lista_reves = []

    if nome == 'bonus':
        while len(lista_bonus) < 25:
            valor = random.randint(500, 1000)
            lista_bonus.append((f'hoje é dia de pagamento. Receba R${valor}', valor))
            valor = random.randint(300, 1150)
            lista_bonus.append((f'hoje é dia de pagamento. Receba R${valor}', valor))
            valor = random.randint(100, 1300)
            lista_bonus.append((f'hoje é dia de pagamento. Receba R${valor}', valor))
            valor = random.randint(650, 850)
            lista_bonus.append((f'hoje é dia de pagamento. Receba R${valor}', valor))
            valor = 700
            lista_bonus.append((f'hoje é dia de pagamento. Receba R${valor}', valor))

        return lista_bonus

    if nome == 'reves':
        while len(lista_reves) < 25:
            valor = random.randint(500, 1000)
            lista_reves.append((f'hoje é dia de pagamento do aluguel. Perca R${valor}', valor))
            valor = random.randint(300, 1150)
            lista_reves.append((f'hoje é dia de pagamento do IPTU. Perca R${valor}', valor))
            valor = random.randint(100, 1300)
            lista_reves.append((f'hoje é dia de pagamento do IPVA. Perca R${valor}', valor))
            valor = random.randint(650, 850)
            lista_reves.append((f'hoje é dia de pagamento de emprestimo. Perca R${valor}', valor))
            valor = 700
            lista_reves.append((f'hoje é dia de pagamento de emprestimo. Perca R${valor}', valor))

        return lista_reves

def sortear_posição(caminho): #sorteia as posicoes de bonus e reves
    cont = 0
    cont2 = 0

    while (cont < B):
        posição = random.randint(0,N-1)
        if caminho[posição] == 'N':
            caminho[posição] = 'B'
            cont += 1

    while (cont2 < R):
        posição = random.randint(0, N - 1)
        if caminho[posição] == 'N':
            caminho[posição] = 'R'
            cont2 += 1

    return caminho

def gerar_caminho(): #gera o caminho de tamanho N
    caminho = ['N']*N
    sortear_posição(caminho)

    return caminho

# usuario
# depois criar um tela

def cadastrar_numerod_de_usuario():
    # All the stuff inside your window.
    layout = [  [sg.Text('Numero de jogadores:') , sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'Ok':
            window.close()
            return (values[0])

    window.close()

def valida_numero_jogadores():
    while True:
        quantidade_de_jogadores =cadastrar_numerod_de_usuario()

        if quantidade_de_jogadores.isnumeric() == True:
            quantidade_de_jogadores = int(quantidade_de_jogadores)

            if quantidade_de_jogadores > 0 and quantidade_de_jogadores < 5:
                return quantidade_de_jogadores

def cadastrar_nome_de_usuario():
    # All the stuff inside your window.
    layout = [  [sg.Text('Nome do jogador:') , sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'Ok':
            window.close()
            return (values[0])

    window.close()

def valida_nome():
    c = 0
    numero_de_jogadores =valida_numero_jogadores()
    lista_usuario = []

    while c < numero_de_jogadores:
        validacao = True

        while validacao:
            nome = cadastrar_nome_de_usuario()

            if len(nome) <= 7:
                # nome , saldo , ponto inicial
                lista_usuario.append([nome, 1000, 0])
                validacao= False

        c+=1

    lista_usuario = sortear_jogadores(lista_usuario)
    return lista_usuario

def sortear_jogadores(lista_usuario):
    c = len(lista_usuario) - 1
    nova_lista = []
    while c != 0:
        sorteio = random.randint(0, c)
        nova_lista.append(lista_usuario[sorteio])
        del lista_usuario[sorteio]

        c -= 1

    nova_lista.append(lista_usuario[0])

    return nova_lista

def salvar_arquivo(nome_do_arquivo,lista):
    df = pd.DataFrame(lista)
    df.to_csv(f'{nome_do_arquivo}.csv')

def acessar_arquivo(nome_do_arquivo):
    return pd.read_csv(f'{nome_do_arquivo}.csv')
