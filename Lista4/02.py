'''2. Crie um programa em que o usuário digite 10 valores
em uma lista e depois imprima a lista.'''

lista = []
x = 1
while x <= 10: # iniciando o laço
    lista.append(input(f'Digite o {x}º valor:')) # os valores digitados são inseridos na lista por meio do append
    x = x + 1 # conta até 10 e encerra o laço
else:
    print(f'Os dez valores digitados na sua lista foram: {lista}')
