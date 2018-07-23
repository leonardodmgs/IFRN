"""Elaborar um programa que efetue a leitura de um número inteiro e apresentar uma mensagem informando se o número é par ou ímpar"""

print('Vamos descobrir se o número é par ou ímpar')
numero = int(input('Digite um número:'))
if numero % 2 == 0:
    print(f'O número {numero} é par!')
else:
    print(f'O número {numero} é ímpar!')

# outra forma de descobrir se é par ou ímpar, mas usando um laço
resposta = 'sim'
while resposta == 'sim':
    numero = int(input('Digite um número:'))
    if numero % 2 == 0:
        print(f'O número {numero} é par!')
    else:
        print(f'O número {numero} é ímpar!')
    resposta = input('Deseja consultar outro número? [sim/não]')  # se digitar 'não' o laço é encerrado
    print('Ok! Até a próxima.') 
