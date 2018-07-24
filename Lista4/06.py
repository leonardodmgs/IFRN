'''6. Crie um programa que sorteie números aleatórios entre 1 e 100.
Preencha uma lista com 20 elementos *diferentes*,
organize em ordem decrescente e imprima na tela.'''

import random
lista = []
while len(lista) !=20:
    l = random.randint(1,100)
    if l not in lista:
        lista.append(l)
else:
    lista.sort()
    lista.reverse()
    print(lista)
