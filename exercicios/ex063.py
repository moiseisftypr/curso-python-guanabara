# REVISADO
print('====== ••• SEQUÊNCIA DE FIBONACCI ••• ======')

total_termos = int(input('Digite quantos termos gostaria de mostrar: '))

c = 3
t1 = 0
t2 = 1

print('=' * 45)
print('')

print(f'{t1} -> {t2} ', end= "")

while c <= total_termos:
  t3 = t1 + t2

  print(f'-> {t3} ', end= "")

  t1 = t2
  t2 = t3
  c += 1

print('-> FIM')

print('')
print('=' * 45)
