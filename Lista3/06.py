'''6) Escreva um programa que pergunta o valor de depósito inicial para uma poupança, e a taxa de rendimento mensal
 Apresente o saldo dos próximos 24 meses, considerando o rendimento sobre o saldo atual de cada mês.''' 

deposito_inicial = float(input('Depósito inicial:'))
taxa_rendimento = float(input('Taxa de rendimento %:'))

mes = 1
saldo = deposito_inicial

while mes <= 24:
    saldo = saldo + (saldo * taxa_rendimento/100)
    print(f'Saldo no mês {mes} foi de R${saldo:.2f}')
    mes = mes + 1
