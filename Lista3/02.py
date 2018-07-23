'''2) Modifique o programa anterior de maneira que
o usuário também digite o início e o fim da
tabuada, ao invés de ir de 1 a 10. Ex. Tabuada de: 2, início: 5, fim: 12. Vai imprimir: 2 x 5 = 10, 2 x 6
= 12, ... 2 x 12 = 24.'''
n = int(input('Tabuada do número:'))
inicio = int(input('Inicio da tabuada:'))
fim = int(input('Fim da tabuada:'))
x = inicio

print(f'Imprimindo a tabuada de número {n}:')
while x <= fim:
    print(f'{n} x {x} = {n*x}')
    x = x + 1
