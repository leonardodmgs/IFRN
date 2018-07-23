"""Digite as notas de um aluno para os 4 bimestres do ano e calcule a sua média aritmética""" 

nota1 = float(input('Nota 1:'))
nota2 = float(input('Nota 2:'))
nota3 = float(input('Nota 3:'))
nota4 = float(input('Nota 4:'))
media_aritmetica = (nota1 + nota2 + nota3 + nota4) / 4
print(f'A média para as 4 notas do aluno é de {media_aritmetica}')

# outra forma de resolver a questão
notas = []
x = 1

while x <= 4:
    nota = float(input(f'Nota {x}:'))
    notas.append(nota)  # adiciona as notas digitadas a lista
    x = x + 1

else:
    print(f'Média: {sum(notas)/len(notas)}')  # soma as notas da lista e divide pela quantidade de elementos nela.
