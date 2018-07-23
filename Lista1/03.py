"""Ler dois valores (inteiros, reais ou caracteres) para as variáveis A e B, e efetuar a troca dos valores de forma
que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A.
Apresentar os valores trocados.""" 

A = int(input('Valor de A:'))
B = int(input('Valor de B:'))
C = A
A = B
B = C
print(f'Valor de A = {A}')
print(f'Valor de B = {B}')
