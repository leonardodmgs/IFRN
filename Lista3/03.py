'''3 Crie um programa em que o usuário digite 10 números e o programa apresente a soma desses números. Dica: use uma variável para
acumular a soma dos números, como no exemplo: soma = soma + numero''' 

x = 1
soma = 0

while x <= 10:
    numero = int(input(f'Digite o {x} número:'))
    soma = soma + numero
    x = x + 1
print(f'A soma dos números é igual a {soma}')
