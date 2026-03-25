# REVISADO
s = 0

for c in range(0, 6):
  n = int(input('DIGITE UM NÚMERO: '))
  if n % 2 == 0:
    s += n

print(f'A SOMA dos números pares: {s}')
