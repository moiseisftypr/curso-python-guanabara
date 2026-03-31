# REVISADO
from time import sleep

print(' ====== ••• PROGRESSÃO ARITMÉTICA ••• ======')

t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
total_termos = 10

print('=' * 45)

while c <= total_termos:
  print(f'{c}º termo = {t}')
  t += r
  c += 1
  sleep(0.5)

print('=' * 45)
