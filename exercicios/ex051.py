# REVISADO
from time import sleep

print(' ====== ••• PROGRESSÃO ARITMÉTICA ••• ======')

n = int(input('PRIMEIRO TERMO: '))
r = int(input('RAZÃO: '))

print('=-' * 20)

for c in range (1, 11):
  print(f'{c}º termo: {n}')
  n += r # += significa: "pegue o valor atual e some algo a ele".
  sleep(0.5)

print('=-' * 20)
