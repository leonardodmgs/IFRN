"""Faça um programa que leia a idade de um atleta e informa a qual categoria ele pertence:
Até 8 anos - pré-mirim
Até 11 anos - mirim
Até 14 anos - infantil
Até 17 anos - juvenil
18 ou mais - adulto"""

idade = int(input('Informe sua idade:'))
if idade <= 8:
    print(f'Você tem {idade} anos\nCategoria: pré-mirim')
elif idade <= 11:
    print(f'Você tem {idade} anos\nCategoria: mirim')
elif idade <= 14:
    print(f'Você tem {idade} anos\nCategoria: infantil')
elif idade <= 17:
    print(f'Você tem {idade} anos\nCategoria: juvenil')
else:
    print(f'Você tem {idade} anos\nCategoria: adulto')
