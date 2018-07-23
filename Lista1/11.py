"""Uma companhia de carros paga a seus empregados um salário de R$ 500,00 por mês mais uma comissão de R$ 50,00
para cada carro vendido e mais 5% do valor da venda. Elabore um algoritmo para calcular e imprimir o salário do vendedor
num dado mês recebendo como dados de entrada o nome do vendedor, o número de carros vendidos e o valor total das
vendas."""  

nome = input('Nome do vendedor:')
carros = int(input('Carros vendidos:'))
vendas = float(input('Valor total das vendas:'))
ns = 500 + (carros * 50) + (5 / 100 * vendas)
print(f'O salário de {nome} é de R${ns:.2f}')
