# Questão 3
'''Crie um programa em que o usuário digite a idade e o programa informa se ele já pode votar'''

nome = input('Qual o seu nome?')
idade = int(input(f'Olá, {nome}! Qual a sua idade?'))

if idade >= 16:
    print(f'{nome}, com {idade} anos você já pode votar!')
else:
    print(f'{nome}, com {idade} anos você ainda não pode votar!')
