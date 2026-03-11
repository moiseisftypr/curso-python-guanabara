print('=-' * 15)
print('SEQUÊNCIA DE FIBONACCI')
print('=-' * 15)
t1 = int(input('Digite um número: '))
qt = int(input('Quantos elementos mostrar: '))
t2 = t1 + 1
cont = 3
print(f'{t1} ~> {t2} ', end="")
while cont <= qt:
  t3 = t1 + t2
  print(f'~> {t3} ', end="")
  t1 = t2
  t2 = t3
  cont += 1
