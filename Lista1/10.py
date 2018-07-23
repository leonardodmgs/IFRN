"""O cardápio de uma lanchonete é dado abaixo. Prepare um algoritmo que leia a quantidade de cada item que você
consumiu e calcule a conta final.
Hambúrguer................. R$ 3,00
Cheeseburger............... R$ 2,50
Fritas............................ R$ 2,50
Refrigerante................. R$ 1,00
Milkshake..................... R$ 3,00"""

Hamburguer = int(input('Quantidade de hamburguer consumida:'))
Cheeseburguer = int(input('Quantidade de cheeseburguer consumida:'))
Fritas = int(input('Quantidade de porções de fritas consumidas:'))
Refrigerante = int(input('Quantidade de refrigerante consumida:'))
Milkshake = int(input('Quantidade de milkshakes consumida:'))

conta = (Hamburguer * 3) + (Cheeseburguer * 2.50) + (Fritas * 2.50) + (Refrigerante * 1.00) + (Milkshake * 3.00)
print(f'O valor da sua conta é de R${conta:.2f}') 
