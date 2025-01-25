#permite que o computador faça selecões aleatórias dentro de uma lista
import random

#instruções de jogo
print ('Bem vindo ao jogo de Pedra, Papel e Tesoura! \nEsteja atento, você jogará contra o computador, seja esperto (a)!')
print ('No jogo PPT a ser iniciado temos as regras: \n\n- Pedra ganha de Tesoura. \n- Tesoura ganha de Papel. \n- Papel ganha de Pedra.')
print ('- Para sair, digite SAIR ao final da partida.\n')

#criação de lista para utilização do random
opc_pc = ['pedra' , 'papel' , 'tesoura']

cont_partida = 0
cont_vitoria = 0
cont_empate = 0

#menu de seleção para o usuário
print ('Para iniciar, escolha uma opção abaixo: \n')
while True:
    print('1. Pedra')
    print('2. Papel')
    print('3. Tesoura\n')

    #escolha do usuário
    escolha_usuario = input('Informe a opção selecionada:\n')

    #verifica a condição de saída pelo usuário
    if escolha_usuario.lower() == 'sair':
        print ('Volte sempre!')
        break  

    #INCREMENTANDO CONTADOR DE PARTIDAS
    cont_partida += 1 #o contador foi imputado apos a condição que determina saída, pois caso não seja acionada, ele entenderá que é uma partida a mais

    #VERIFICA A CONDIÇÃO ESCOLHIDA PELO USUÁRIO E VALIDA
    if escolha_usuario == '1' or escolha_usuario.lower() == 'pedra':
        print('Usuário selecionou Pedra.\n')
    elif escolha_usuario == '2' or escolha_usuario.lower() == 'papel':
        print('Usuário selecionou Papel.\n')
    elif escolha_usuario == '3' or escolha_usuario.lower() == 'tesoura':
        print('Usuário selecionou Tesoura.\n')
    else:
        print('Escolha inválida, selecione uma das opções fornecidas.\n')
        continue #se a escolha for invalida volta para o inicio do loop


    #SELECIONAR OPÇÃO ALEATORIA USANDO RANDOM CHOICE
    opc_pc_selec = random.choice(opc_pc)
    print ('O computador selecionou a opção ' , opc_pc_selec)

    #VERIFICANDO SE O USUÁRIO GANHOU
    if (escolha_usuario == '1' or escolha_usuario.lower() == 'pedra') and opc_pc_selec == 'tesoura':
        print ('O usuário venceu essa partida!\n')
        cont_vitoria += 1
    elif (escolha_usuario == '2' or escolha_usuario.lower() == 'papel') and opc_pc_selec == 'pedra':
        print ('O usuário venceu essa partida!\n')
        cont_vitoria += 1
    elif (escolha_usuario == '3' or escolha_usuario.lower() == 'tesoura') and opc_pc_selec == 'papel':
        print ('O usuário venceu essa partida!\n')
        cont_vitoria += 1

    #VERIFICANDO SE O COMPUTADOR GANHOU
    if opc_pc_selec == 'pedra' and (escolha_usuario == '3' or escolha_usuario.lower() == 'tesoura'):
        print ('O computador venceu essa partida!\n')
    elif opc_pc_selec == 'tesoura' and (escolha_usuario == '2' or escolha_usuario.lower() == 'papel'):
        print ('O computador venceu essa partida!\n')
    elif opc_pc_selec == 'papel' and (escolha_usuario == '1' or escolha_usuario.lower() == 'pedra'):
        print ('O computador venceu essa partida!\n')
    #DECLARANDO EMPATE
    else:
        print ('Houve em empate nessa rodada! \n')
        cont_empate += 1

#MOSTRANDO PLACAR

