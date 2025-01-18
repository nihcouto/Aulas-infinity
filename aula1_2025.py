#REVISAO
# Condicionais
#executa uma ação no caso do cumprimento 



# Exercícios - Lógica de programação em Python

# Condicionais:


# 31 - Crie um algoritmo que ao ser executado que verifica se um número é par ou ímpar 
# e exibe a mensagem "ímpar" se o número for ímpar e "par" se o número for par.

# Um número é par quando o resto da divisão por 2 é zero.
# Se o módulo de n % 2 for 0 este número é par.

'''
#n = int (input ('Informe um número:'))

#if n%2 == 0:
#    print ('Número par.')
#else:
#    print ('Número ímpar.')
'''

#Exercícios:

# 01 - Crie um algoritmo que ao ser executado verifica uma variável "chuva" e 
# se for verdadeiro exibe a mensagem: "Leve um guarda chuva"
# e se for falso exiba a mensagem: "Olha que dia bonito, nem precisa levar guarda-chuva"

'''
#        tempo = input ('Informe se hoje teremos chuva ou sol. ')
#        if tempo == 'chuva':
#            print ('Leve um guarda chuva!')
#        else:
#            print ('Olha que dia bonito, nem precisa levar guarda-chuva!')
'''


# 33 - Crie um algoritmo que ao ser executado verifica: Se está ensolarado e se é fim de semana, 
# caso seja fim de semana E esteja ensolarado exiba a mensagem: "Bora pra praia de mineiro?" 
# senão exiba a mensagem: "Bora ver um trem no Netflix?"

'''
#        tempo = input ('Hoje temos um dia ensolarado ou nublado?')
#        dia = input ('Informe o dia da semana atual: ')

#        if (tempo == 'ensolarado' and dia == 'sabado') or (dia == 'domingo'):
#            print ('Bora pra praia de mineiro?')
#        else:
#            print ('Bora ver um trem no Netflix?')
'''


# 34 - Crie um algoritmo que ao ser executado recebe dois valores númericos
# e imprime qual é o maior dos dois valores.

'''
        # n1 = int (input ('Informe um número: '))
        # n2 = int (input ('Informe outro número: '))10

        # if n1 > n2:
        #     print ('O primeiro número digitado,', n1, 'é maior que o segundo número,', n2)
        # elif n1 < n2:
        #     print ('O segundo número digitado,', n2, 'é maior que o primeiro número,', n1)
        # else:
        #     print ('Os números digitados são iguais.')
'''


# 35 - Crie um algoritmo que recebe três números e compare cada desses números e imprima: 
# Para o menor número a mensagem: "<numero1> é o menor entre os números fornecidos"
# Para o número intermediário: "<numero2> está entre <numero2> e <numero3>"
# Para o maior número: "<numero3> é o maior entre os números"


'''
        n1 = int (input ('Informe um número: '))
        n2 = int (input ('Informe outro número: '))
        n3 = int (input ('Informe um terceiro número: '))
                
        if n1 > n2 and n1 > n3:
            print ('O maior entre os números é o ', n1)
        elif (n1 > n2 and n1 < n3) or (n1 < n2 and n1 > n3):
            print ('O número ', n1 , 'está entre', n2,'e', n3)
        else:
            print ('O número ', n1, 'é o menor entre os números fornecidos.')
            

        if n2 > n1 and n2 > n3:
            print ('O maior entre os números é o ', n2)
        elif (n2 > n1 and n2 < n3) or (n2 < n1 and n2 > n3):
            print ('O número ', n2 , 'está entre', n1,'e', n3)
        else:
            print ('O número ', n2, 'é o menor entre os números fornecidos.')


        if n3 > n1 and n3 > n2:
            print ('O maior entre os números é o ', n3)
        elif (n3 > n1 and n3 < n2) or (n3 < n1 and n3 > n2):
            print ('O número ', n3 , 'está entre', n1,'e', n2)
        else:
            print ('O número ', n3, 'é o menor entre os números fornecidos.')
'''


# 36 - Crie um algoritmo que ao ser executado recebe uma palavra, verifica se a palavra se inicia com uma vogal
# e exibe a mensagem "Começa em vogal" caso a palavra se inice em vogal
# ou exibe a mensagem "Começa em consoante" caso a palavra não se inicie em vogal

'''
        palavra = input ('Informe uma palavra:')

        if palavra [0].lower() in 'aeiou':
            print ('Começa em vogal')
        else:
            print ('Começa em consoante')
'''


# 37 - Crie um algoritmo que ao ser executado recebe a velocidade de dois veículos  em km/h
# e exibe no terminal qual dos veículos está se deslocando mais rápido.
# Se algum dos veículos estiver a mais de 80km/hora deve ser exibida a mensagem: "<veiculo> está acima da velocidade permitida"
# Se algum dos veículos estiver parado deve exibir a mensagem: "<veiculo> não está em movimento"

'''
veic1 = int (input ('Informe a velocidade de veículo 1 em Km/h: '))
veic2 = int (input ('Informe a velocidade de veículo 2 em Km/h: '))

if veic1 > veic2:
    print ('O veículo 1 está mais rápido que o veículo 2.')
else:
    print ('O veículo 2 está mais rápido que o veículo 1.')

if veic1 > 80:
    print ('Veículo1 acima da velocidade permitida.')
elif veic2 > 80:
    print ('Veículo2 acima da velocidade permitida.')

if veic1 == 0:
    print ('Veículo1 não está em movimento.')
elif veic2 == 0:
    print ('Veículo2 não está em movimento.')
'''



# 38 - Crie um algoritmo que ao ser executado recebe uma frase, 
# e verifica se uma letra escolhida por você está presente na frase
# caso a frase contenha a letra escolhida deve ser exibida a mensagem "A letra <letra> está presente na frase"
# caso contrário deve ser exibida a frase "A letra <letra> não está contida na frase"

'''
frase = input ('Digite uma frase: ')
letra = input ('Informe uma letra a ser analisada: ')

if letra.lower() in frase.lower():
    print (f'A letra {letra} está presente na frase.')
else:
    print (f'A letra {letra} não está contida na frase.')
'''


# 39 - Desafio: Crie um algoritmo para calcular a velocidade de um veículo
# o calculo da velocidade é: velocidade = distância/tempo 
# os valores devem ser recebidos através de inputs.
# Caso valores não númericos sejam recebidos o deve ser exibida uma mensagem de erro:
# "Os valores inseridos não são números"
# Caso valores corretos sejam informados o algoritmo deve imprimir o valor da velocidade calculada.

'''
distancia = input ('informe a distância percorrida em metros:')
tempo = input ('Informe o tempo gasto em segundos:')

if not distancia.isnumeric() or not tempo.isnumeric():
    print ("Os valores inseridos não são números.")
else:
    velocidade = (distancia / tempo)
    print ('A velocidade do carro é de: ', velocidade , 'm/s')
'''
'''
    O erro no código está na linha onde ocorre o cálculo da velocidade:

    velocidade = (distancia / tempo)

    Motivo do erro:

        As variáveis distancia e tempo são recebidas como strings pelo input(). Mesmo verificando com isnumeric(), elas continuam sendo str.
        Ao tentar realizar a operação de divisão entre strings, o Python levantará um erro de TypeError.

    Correção:

        Converter as entradas para float ou int antes do cálculo.
        isnumeric() não aceita números decimais. Para cobrir esses casos, a abordagem com try...except é mais apropriada.

    Código corrigido:

    distancia = input('Informe a distância percorrida em metros: ')
    tempo = input('Informe o tempo gasto em segundos: ')

    try:
        distancia = float(distancia)
        tempo = float(tempo)

        if tempo <= 0:
            print("O tempo deve ser maior que zero.")
        else:
            velocidade = distancia / tempo
            print('A velocidade do carro é de: ', velocidade, 'm/s')

    except ValueError:
        print("Os valores inseridos não são números válidos.")

    Melhorias implementadas:

        Conversão explícita com float(): Garante que valores decimais sejam aceitos.
        try...except para validação: Lida com erros ao tentar converter a string.
        Validação de tempo positivo: Adicionada para evitar divisão por zero.

    Essa versão está corrigida e mais robusta.
'''