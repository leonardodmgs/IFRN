'''5) Faça um programa que calcula a potência a partir de dois
valores digitados pelo usuário. Não use o operador de potência,
faça apenas multiplicações. Se o usuário digitar: base = 2, expoente = 3,
o programa deve repetir a multiplicação 2 x 2 x 2 para obter o resultado.'''

base = int(input('Digite a base:'))
expoente = int(input('Digite o expoente:'))
pot = 1
x = 0
while x < expoente:
    pot = pot * base
    x = x + 1
print(f'{base} elevado a {expoente} = {pot}')
