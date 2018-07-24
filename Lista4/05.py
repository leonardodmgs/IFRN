'''5. Crie um programa que o usuário digita os dados de duas listas com 3 elementos cada.
Depois crie uma terceira lista com a junção dos elementos das outras duas.
Imprima a nova lista.'''


lista1 = [] # a lista 1 começa vazia
x = 1
while x <= 3:  #inicia o laço
    lista1.append(input(f'Digite o {x}º elemento da lista 1:'))
    x = x + 1 # conta até 3 e encerra o laço
else:
    print(lista1)

lista2 = [] # a lista 2 começa vazia
x = 1
while x <= 3:  # inicia o laço
    lista2.append(input(f'Digite o {x}º elemento da lista 2:'))
    x = x + 1 # conta até 3 e encerra o laço
else:
    print(lista2)

lista3 = [lista1, lista2]
print(lista3)
