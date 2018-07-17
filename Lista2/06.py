"""Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
Pergunte a quantidade de kWh consumidas e
o tipo de instalação: R para residências, I para indústrias e C para comércios.
Calcule o preço a pagar de acordo com a tabela a seguir.

Tipo 			Faixa (kWh) 	Preço
Residêncial
				Até 500 		R$ 0,40
				Acima de 500 	R$ 0,65
Comercial
				Até 1000 		R$ 0,55
				Acima de 1000 	R$ 0,60
Industrial
				Até 5000 		R$ 0,55
				Acima de 5000 	R$ 0,60
"""
try:
    kwh = float(input('Quantidade de kWh:'))
except:
    print('Opção inválida')

tipo = input('Tipo de instalação [R/I ou C]:')
if tipo == 'R':
    if kwh <= 500:
        print(f'O preço da conta da sua residência é de {kwh*0.40:.2f} reais')
    else:
        print(f'O preço da conta da sua residência é de {kwh*0.65:.2f} reais')
if tipo == 'C':
    if kwh <= 1000:
        print(f'O preço da conta do seu estabelecimento é de {kwh*0.55:.2f} reais')
    else:
        print(f'O preço da conta do seu estabelecimento é de {kwh*0.60:.2f} reais')
if tipo == 'I':
    if kwh <= 5000:
        print(f'O preço da conta da sua fábrica é de {kwh*0.55:.2f} reais')
    else:
        print(f'O preço da conta da sua fábrica é de {kwh*0.60:.2f} reais')
else:
    print('Tipo de instalação desconhecida')