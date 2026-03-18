print('olá mundo')

print(7+4)
print('7+4')
print('7' + '4') #CONCATENANDO STRINGS

# VARIÁVEIS
nome = "Léo" # str
idade = 18 # int
peso = 82.0 # float

print(nome, idade, peso)
print(f'Oiiiii {nome}!!!')

# INPUT = SIMULAÇÃO DE UM FORMS NO CMD
nome = input('Digite o seu nome:')
idade = int(input('Digite a sua idade:'))
peso = float(input('Digite o seu peso:'))
print(nome, idade, peso)
print(idade + 1)

ano_nascimento = 2007
ano_atual = 2026
idade = ano_atual - ano_nascimento
print(idade)