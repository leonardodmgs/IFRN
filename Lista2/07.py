"""Informe a altura e o sexo de uma pessoa e calcule o peso ideal, utilizando as seguintes fórmulas:
Para homens: (72*altura)-58. Para mulheres: (62.1*altura-44.7 """

altura = float(input('Altura:'))
sexo = input('Sexo:')

if sexo == 'masculino' or sexo == 'Masculino' or sexo == 'MASCULINO':
    peso = (72 * altura) - 58
    print(f'Sexo: {sexo}')
    print(f'Seu peso ideal é {peso:.2f}kg')
else:
    peso = (62.1 * altura) - 44.7
    print(f'Sexo: {sexo}')
    print(f'Seu peso ideal é {peso:.2f}kg')