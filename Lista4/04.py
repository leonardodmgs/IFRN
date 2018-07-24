'''4. Crie um programa que cadastre os alunos de uma escola.
Pergunte ao usuário o nome, o curso e a série de um aluno.
Salve esses 3 dados como uma (sub)lista e depois acrescente esta (sub)lista em uma lista principal.
O programa deve repetir quantas vezes o usuário desejar.
Ao finalizar os cadastros, imprima todos os alunos cadastrados.'''

lista = [] #a lista começa vazia
resposta = 'sim'
while resposta == 'sim': #enquanto o usuário digitar "sim", o laço será executado pedindo nome, curso e série
    nome = input('Digite o nome do aluno:')
    curso = input('Digite o curso do aluno:')
    serie = input('Digite a série do aluno:')
    escola = [nome, curso, serie] #aninhando as variáveis
    lista.append(escola) #adiciona os itens de escola em lista vazia.
    resposta = input('Deseja cadastrar outro aluno? [sim/não]') #pode encerrar o laço ou não.
else:
    print(f'Alunos cadastrados: {lista}')
