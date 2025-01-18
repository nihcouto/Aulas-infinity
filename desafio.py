print ('Bem vindo ao jogo de Pedra, Papel e Tesoura! \nEsteja atento, você jogará contra o computador, seja esperto (a)!')
print ('No jogo PPT a ser iniciado temos as regras: \n\n- Pedra ganha de Tesoura. \n- Tesoura ganha de Papel. \n- Papel ganha de Pedra.')
print ('- Para sair, digite SAIR ao final da partida.\n')

print ('Para iniciar, escolha uma opção abaixo: \n')
while True:
    print('1. Pedra')
    print('2. Papel')
    print('3. Tesoura\n')
    
    escolha = input('Informe a opção selecionada:')

    if escolha == '1' or escolha.lower() == 'pedra':
        print('Usuário selecionou Pedra.')
    elif escolha == '2' or escolha.lower() == 'papel':
        print('Usuário selecionou Papel.')
    elif escolha == '3' or escolha.lower() == 'tesoura':
        print('Usuário selecionou Tesoura.')
    elif escolha.lower() == 'sair':
        print ('Voltei sempre!')
        break
    else:
        print('Escolha inválida, selecione uma das opções fornecidas\n')

#CRIAR LISTA DAS OPÇÕES E ARMAZENAR EM UMA VARIAVEL
#SELECIONAR NUMERO ALEATORIO ENTRE 0 E 2 USANDO RANDOM CHOICE
