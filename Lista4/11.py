'''11. Crie um programa que o usuário digite as notas de 10 alunos de uma turma.
Depois calcule e imprima a média das notas, a maior e a menor nota.'''

notas = []
x = 1
for i in range(10):
    nota = float(input(f'Digite a nota do {x}º aluno:'))
    notas.append(nota)
    x = x + 1
    max = notas [0]
    min = notas [0]
for no in notas:
    if no < min:
        min = no
    elif no > max:
        max = no
else:
    print(f'A média das notas da turma foi {sum(notas)/len(notas)}')
    print(f'A maior nota foi {max}')
    print(f'A menor nota foi {min}')
