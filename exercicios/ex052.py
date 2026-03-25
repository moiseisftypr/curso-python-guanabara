# REVISADO
n = int(input('DIGITE UM NÚMERO: '))

cont = 0

for c in range(1, n + 1):
  if n % c == 0:
    cont += 1

if cont == 2:
  print(f'O número {n} é um número PRIMO.')

else:
  print(f'O número {n} não é um número PRIMO.')
