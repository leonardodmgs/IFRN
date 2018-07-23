# Questão 5
'''Crie um programa que o usuário digita dois valores e o programa escreve a sequência de números entre eles'''

n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))

if n2 < n1:
    print(n2)
else:
    print(n1)
while n1 < n2:
    n1 = n1 + 1
    print(n1)
while n2 < n1:
    n2 = n2 + 1
    print(n2)
