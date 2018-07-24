'''8. Crie um programa que sorteia 20 números e guarda-os numa lista.
Permita que o usuário faça pesquisas na lista.
Se o número pesquisado existe na lista, informe a sua posição.
Se o elemento não existe, mostre uma mensagem informando.
O usuário poderá repetir novas pesquisas quantas vezes quiser.'''

import random
lista = []

while len(lista) !=20:
    l = random.randint(1,100)
    if l not in lista:
        lista.append(l)

else:
    lista.sort()
    print(lista)
resposta = 'sim'
while resposta == 'sim':
    pesquisa = int(input('Digite o número:'))
    if pesquisa in lista:
        print(f'O número foi encontrado na posição {lista.index(pesquisa)}')
    else:
        print('O número digitado não existe na lista')
    resposta = input('Deseja consultar outro número na lista? [sim/não]')
print('Até a próxima')
