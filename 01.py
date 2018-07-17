"""Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit.
A fórmula de conversão é F ← (9 * C + 160) / 5, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius."""

celsius = float(input('Temperatura em ºC:'))
fahrenheit = (9 * celsius + 160) / 5
print(f'Temperatura em ºC = {celsius:.2f}\nTemperatura em Fahrenheit = {fahrenheit:.2f}')