""" Ler quatro notas de um aluno, calcular a média aritmética e imprimir a média e uma mensagem dizendo que o aluno foi aprovado,
se a média for maior ou igual a 6, ou reprovado para uma nota abaixo de 6. """

nota1 = float(input('Nota 1:'))
nota2 = float(input('Nota 2:'))
nota3 = float(input('Nota 3:'))
nota4 = float(input('Nota 4:'))

media_aritmetica = (nota1 + nota2 + nota3 + nota4) / 4  # soma as e divide

if media_aritmetica >= 6:  # condição para ser aprovado
    print(f'Aprovado\nMédia: {media_aritmetica:.2f}')
else:  # caso não atenda a primeira condição, ou seja, fique abaixo de 6, o aluno será reprovado
    print(f'Reprovado\nMédia: {media_aritmetica:.2f}')


# outra forma de resolver essa questão
notas = []
x = 1
while x <= 4:
    nota = float(input(f'Nota {x}:'))
    x = x+1
    notas.append(nota)
    media_aritmetica = (sum(notas)/len(notas))
if media_aritmetica >= 6:
    print(f'Aprovado\nMédia: {media_aritmetica:.2f}')
else:
    print(f'Reprovado\nMédia: {media_aritmetica:.2f}') 
