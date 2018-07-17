"""Em uma eleição sindical concorreram ao cargo de presidente três candidatos (A, B e C). Durante a apuração
dos votos foram computados votos nulos e votos em branco, além dos votos válidos para cada candidato. Deve
ser criado um programa de computador que efetue a leitura da quantidade de votos válidos para cada
candidato, além de efetuar também a leitura da quantidade de votos nulos e votos em branco. Ao final o
programa deve apresentar o número total de eleitores, considerando votos válidos, nulos e em branco; o
percentual correspondente de votos válidos em relação à quantidade de eleitores; o percentual correspondente
de votos válidos de cada candidato em relação à quantidade de eleitores, além do percentual de votos brancos
e votos nulos;"""

A = int(input('Votos de A:'))
B = int(input('Votos de B:'))
C = int(input('Votos de C:'))
branco = int(input('Votos em branco:'))
nulo = int(input('Votos nulos:'))

total_de_eleitores = A + B + C + branco + nulo
votos_válidos = (A + B + C) / total_de_eleitores * 100

print(f'Total de eleitores = {total_de_eleitores}')
print(f'Total de votos válidos = {votos_válidos:.0f}%')
print(f'Total de votos válidos de A = {A/total_de_eleitores*100:.0f}%')
print(f'Total de votos válidos de B = {B/total_de_eleitores*100:.0f}%')
print(f'Total de votos válidos de C = {C/total_de_eleitores*100:.0f}%')
print(f'Percentual de votos em branco = {branco/total_de_eleitores*100:.0f}%')
print(f'Percentual de votos nulos = {nulo/total_de_eleitores*100:.0f}%')
