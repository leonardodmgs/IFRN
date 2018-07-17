'''3) Efetuar a leitura de três valores (variáveis A, B e C) e
apresentá-los dispostos em ordem crescente. '''

a = int(input("Valor de A: "))
b = int(input("Valor de B: "))
c = int(input("Valor de C: "))

# usando if encadeados/aninhados

if a > b and a > c :    # A é o maior
  if b > c :
    print(a, b, c)
  else:
    print(a, c, b)
else :
  if b > a and b > c :  # B é o maior
    if a > c :
      print(b, a, c)
    else :
      print(b, c, a)
  else :				# C é o maior
    if a > b :
      print(c, a, b)
    else :
      print(c, b, a)