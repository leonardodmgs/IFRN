'''10. Crie um programa em que o usuário digite 10 valores em uma lista.
Ao final o programa deve informar o maior e o menor valor digitado
e suas posições na lista.'''

lista = []
x = 1
for i in range(10):
    lista.append(int(input(f'Digite o {x}º valor:')))
    x = x + 1
    min = lista[0]
    max = lista[0]
for no in lista:
    if no <min:
        min = no
    elif no > max:
        max = no
else:
    print(lista)
    print(f'O maior valor da lista é: {max}')
    print(f'O menor valor da lista é: {min}')
    print(f'A posição do maior valor na lista é: {lista.index(max)}')
    print(f'A posição do menor valor da lista é: {lista.index(min)}')
