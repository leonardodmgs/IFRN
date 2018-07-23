''''4  Digite as notas de uma prova para uma turma de 10 alunos e calcule a média da turma. Dica
: use uma variável para acumular a soma de todas as notas, por último, já fora do laço, faça a divisão para calcular a média'''

x = 1
soma = 0
while x <= 10:
    nota = float(input(f'Digite a {x} nota:'))
    soma = soma + nota
    x = x + 1
x = x - 1  # remove um valor de x, caso contrário, a divisão ficaria incorreta.
media = soma/x
print(f'A média para as 10 notas é igual a {media:.2f}')
