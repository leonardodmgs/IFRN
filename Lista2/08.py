""" Numa cidade litorânea há uma lei municipal que permite a produção de 50 Kg de pescados por dia.
Sempre que um pescador chega à praia, um fiscal pesa os peixes e aplica uma multa de R$ 4,00 por cada Kg excedente.
Faça um programa que leia o peso e informe o valor da multa, caso ultrapasse o peso permitido. """ 

peso = float(input('Peso do pescado:'))

if peso > 50:
    print(f'Você ultrapassou o limite!\nMulta: {(peso-50)*4:.2f}')
else:
    print(f'Você não ultrapassou o limite de {peso:.2f}kg. Portanto, não pagará multa!')
