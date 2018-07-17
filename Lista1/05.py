"""Ler o valor correspondente ao salário mensal (variável SM) de um trabalhador e também o valor do
percentual de reajuste (variável PR) a ser atribuído. Apresentar o valor do novo salário (variável NS)."""

SM = float(input('Salário mensal R$:'))
PR = float(input('Reajuste %:'))
NS = SM + (PR / 100 * SM)
print(f'O novo salário é de R${NS:.2f}')
