# REVISADO
from time import sleep

n = int(input('Digite um número: '))

print('=' * 20)

for c in range (1, 11):
 print(f'{n} x  {c} = {n * c}')
 sleep(1)

print('=' * 20)
