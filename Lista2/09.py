"""Uma empresa paga R$ 12,50 por hora trabalhada (até 40 horas) e 18,50 por hora extra.
Leia o número de horas semanais de um funcionário e informe o valor do pagamento da semana."""

horas = int(input('Horas semanal trabalhadas:'))
if horas <= 40:
    print(f'O seu salário é de: {horas * 12.50:.2f} reais')
else:
    print(f'O seu salário é de {(horas - 40) * 18.50 + (40*12.50):.2f} reais')