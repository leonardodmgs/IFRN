'''1  Crie  um  programa  que  imprime  a  tabuada  de  um  número  digitado  pelo  usuário.  Ex.  Usuário
digitou "2", o programa imprime: 2 x 1 = 2, 2 x 2 = 4, 2 x 3 = 6 ...'''

n = int(input('Digite o número desejado:'))
x = 1
print(f'Imprimindo a tabuada do número {n}:')
while x <= 10:

    print(f'{n} x {x} = {n*x}')
    x = x + 1 
    
