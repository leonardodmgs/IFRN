
"""Escreva um programa que informa sobre a aprovação de um empréstimo habitacional.
O usuário informa o valor da casa, a renda e a quantidade de anos a pagar.
O valor da prestação não pode ser superior a 30% do salário. Informe o valor da prestação e se o empréstimo será aprovado ou não.
 Não são considerados juros neste exemplo."""

valor_casa = float(input('Valor da casa R$:'))
renda = float(input('Renda R$:'))
anos = int(input('Anos para pagar:'))

prestacao = valor_casa/(anos*12)
porcentagem = renda * (30/100)

if prestacao < porcentagem:
    print(f'Valor da prestação: {prestacao:.2f}\nEmpréstimo aprovado!')
else:
    print(f'Valor da prestação: {prestacao:.2f}\nEmpréstimo reprovado!')
