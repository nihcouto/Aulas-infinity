 
# POO

# Programação orientada a objeto

nome = "João do Caminhão"
idade = 60
profissao = "Caminhoneiro"

class Pessoa:
    def __init__(self,nome,idade,profissao):# método Construtor
        self.nome = nome
        self.idade = idade 
        self.profissao = profissao 

    def falar(self):
        return "Esto Conversando Fiado"
# Abstração

p1 = Pessoa("João Caminhoreiro",45,"Desenvolvedor Full-Stack")
# p1 é um objeto da classe pessoa
print(p1.nome)  
print(p1.idade)  
print(p1.profissao)   

nome = str("Gabriel")# nome é um objeto da classe str
print(nome.upper())
print()
============================================================================================
class Animal:
    def __init__(self,especie,idade,cor):# Método Construtor
        self.especie = especie
        self.idade = idade 
        self.cor = cor
    
    def fazer_som(self):
        return "Estou fazendo som"
    
class Dogao(Animal):
    def __init__(self, especie, idade, cor,sexo):
        super().__init__(especie, idade, cor)
        self.sexo = sexo

class Gatao(Animal):
    def __init__(self, especie, idade, cor,raca):
        super().__init__(especie, idade, cor)
        self.raca = raca


d1 = Dogao("Cachorrão",10,"Caramelo")
print(vars(d1))
print(d1.fazer_som())
==================================================================
