# Questão 4
'''Crie um programa que pergunta se o usuário é homem ou mulher. Se for homem, em seguida pergunta qual time de
futebol ele torce, e mostre uma mensagem, se ele responder “nenhum”, mostre outra mensagem. Se for mulher,
pergunte se ela gosta de maquiagem e mostre uma mensagem se ela responder sim e outra mensagem se responder
não.'''

sexo = input('Qual o seu sexo? [F/M]')

if sexo == 'M':
    time = input('Pra qual time você torce?')
    if time =='nenhum':
        print('Eu também não torço pra nenhum time!')
    else:
        print(f'Legal! também torço para o {time}')
if sexo == 'F':
    maquiagem = input('Você gosta de maquiagem?')
    if maquiagem == 'não':
        print('Você fica linda sem maquiagem')
    else:
        print('Você fica bem bonita maquiada')

# ou


sexo=input('Você é homem ou mulher?')
if sexo =='homem':
  time = input('Pra qual time de futebol você torce?')
  if time!='nenhum':
    print('Que bom! Também torço pelo',time)
  else:
    print('Também não gosto de futebol')
elif sexo=='mulher':
  maquiagem=input('Você gosta de maquiagem?[sim/não]')
  if maquiagem!='não':
    print('Você fica bem bonita maquiada')
  else:
    print('Nem precisa!Você é naturalmente bonita')
