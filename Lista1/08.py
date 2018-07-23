"""Digite as notas de um aluno para os 4 bimestres do ano e calcule a sua média ponderada. Os pesos para cada
bimestre são, respectivamente: 2, 3, 4, 6.""" 

nota1 = float(input('Nota 1:'))
nota2 = float(input('Nota 2:'))
nota3 = float(input('Nota 3:'))
nota4 = float(input('Nota 4:'))

media_ponderada = (nota1 * 2 + nota2 * 3 + nota3 * 4 + nota4 * 6) / 15
print(f'Média ponderada = {media_ponderada:.2f}')
