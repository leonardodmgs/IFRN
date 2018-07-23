"""O custo ao consumidor de um carro novo é a soma do custo de fábrica com a porcentagem do distribuidor e dos
impostos, ambos aplicados ao custo de fábrica. Supondo que a porcentagem do distribuidor seja de 12% e a dos impostos
de 45%, prepare um algoritmo para ler o custo de fábrica do carro e imprimir o custo ao consumidor.""" 

custo_fabrica = float(input('Custo de fábrica R$:'))
distribuidor = (12 / 100) * custo_fabrica
impostos = (45 / 100) * custo_fabrica
consumidor = custo_fabrica + distribuidor + impostos
print(f'Custo ao consumidor: R${consumidor:.2f}')

# ou

custo_fabrica = float(input('Custo de fábrica R$:'))
preco = custo_fabrica + (custo_fabrica * 12 / 100) + (custo_fabrica * 45 / 100)
print(f'Custo ao consumidor: R${preco:.2f}')
