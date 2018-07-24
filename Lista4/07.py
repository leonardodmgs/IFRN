'''7. Crie um programa que simule um painel eletrônico que organiza uma fila.
O programa exibe um menu com as seguintes opções:
1. Entrar na fila. / 2. Consultar a fila. / 3. Chamar próximo da fila.
Na opção 1, o usuário digita o nome da pessoa que está entrando no final da fila.
Na opção 2, o programa imprime a fila atual e diz *quantas pessoas há na fila*.
Na opção 3, o programa exibe uma mensagem chamando a pessoa da vez e remove seu nome da fila.
Se não houver pessoas na fila, mostre a mensagem "fila vazia".'''


print('1. Entrar na fila / 2. Consultar a fila /3. Chamar próximo da fila')

fila = []
opção = input('Escolha uma opção:')
while opção =='1':
    fila.append(input('Digite o nome da pessoa:'))
    opção = input('Deseja inserir outra pessoa na fila? [1/sair]')
else:
    opção = input('Escolha outra opção:')
while opção == '2':
    print(f'Temos {len(fila)} pessoa(s) na fila')
    opção = input('Deseja ver quantas pessoas estão na fila? [2/sair]')
else:
    opção = input('Escolha outra opção:')
while opção == '3' and not fila == []:
    print(f'É a sua vez {fila[0]}')
    del (fila[0])
    opção = input ('Deseja chamar outra pessoa? [3/sair]')
    if fila == []:
        print('Fila vazia')
else:
    print('Até a próxima')
