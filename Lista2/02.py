"""Modifique o programa anterior para solicitar a nota da recuperação se o aluno ficou abaixo de 6.
Calcule a média final usando a primeira média e a nota da recuperação.
O aluno será aprovado se a média final for 5 ou mais, caso contrário, será reprovado. Mostre a média final e a mensagem"""

nota1 = float(input('Nota 1:'))
nota2 = float(input('Nota 2:'))
nota3 = float(input('Nota 3:'))
nota4 = float(input('Nota 4:'))

media_aritmetica = (nota1 + nota2 + nota3 + nota4)/4

if media_aritmetica >= 6:
    print(f'Aprovado!\nMédia: {media_aritmetica:.2f}')
else:
    print(f'Você ficou na recuperação!\nMédia: {media_aritmetica:.2f}')
    recuperacao = float(input('Nota da recuperação:'))
    media_final = (media_aritmetica + recuperacao)/2
    if media_final >= 5:
        print(f'Aprovado!\nMédia final: {media_final:.2f}')
    else:
        print(f'Reprovado!\nMédia final: {media_final:.2f}')

# outra forma de resolver essa questão:
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
    print(f'Você ficou na recuperação\nMédia: {media_aritmetica:.2f}')
    recuperacao = float(input('Nota da recuperação:'))
    media_final = (media_aritmetica + recuperacao)/2
    if media_final >= 5:
        print(f'Aprovado!\nMédia final: {media_final:.2f}')
    else:
        print(f'Reprovado!\nMédia final: {media_final:.2f}')