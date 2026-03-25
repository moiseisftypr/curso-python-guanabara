# REVISADO
from time import sleep

s = 0

for c in range(1, 500):
  if c % 2 != 0 and c % 3 == 0:
    s += c

print(f'A SOMA de todos os números ímpares multiplos de 3 de 1 à 500:\n{s}')
