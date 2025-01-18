# Laços de Repetição
#
# 1 - Crie um algoritmo que receba um número e imprima no terminal todos os valores em ordem crescente até o valor do número informado.
# Ex: n = 5, a saída no terminal devera ser:
# 1
# 2
# 3
# 4
# 5
#
# codigo aqui
#

# number = int(input("Digite um número: "))

# for i in range(1, number + 1):
#     print(i)

#
#------------------------------------
#
# 2 - Crie um algoritmo que receba um número e imprima no terminal todos os valores em ordem decrescente até o valor do número informado.
# Ex: n = 6, a saída no terminal devera ser:
# 6
# 5
# 4
# 3
# 2
# 1
#
# codigo aqui
#

# number = int(input("Digite um número: "))

# for i in range(number,0, -1):
#     print(i)

#
#------------------------------------
#
# 3 - Crie um algoritmo que ao receber uma palavra conte o número de letras dessa palavra e imprima esse valor no terminal.
#
# codigo aqui

# palavra = input("Digite uma Palavra: ")

# qtd_letra= len(palavra)
# print(f"Sua palavra tem: ", qtd_letra ," Letras!" )

#
#------------------------------------
#
# 4 - Crie um algoritmo que recebe 5 nomes e imprime no terminal todos aqueles iniciados em uma letra à sua escolha:
# Ex: 'Ana', 'Julia', 'Pedro', 'Amanda' , letra = "A", a saída no terminal dever ser:
# Ana
# Amanda
# Obs: Se atentem para o uso de letras maiúsculas ou minúsculas
#
# codigo aqui
#

# pessoas = ['Ana', 'Julia', 'Pedro', 'Amanda']

# letra = input("Digite a letra para filtrar os nomes: ")

# for pessoa in pessoas:
#     if pessoa[0].upper() == letra.upper(): 
#         print(pessoa)

#
#------------------------------------
#
# 5 - Crie um algoritmo que receba um número de usuário e informe a soma de todos os números anteriores ao valor informado:
# Ex: 3 , o resultado devera ser: 1 + 2 + 3 = 6 , então no terminal deverá ser exibido o número 6.
#

number = int(input("Digite um número: "))

for i in range(2, number + 1):
    print(i)