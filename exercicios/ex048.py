s = 0
cont = 0
for c in range(1, 501, 2):
  if c % 3 == 0:
    print(c)
    s += c
    cont += 1
print(f'O somatório de todos esses valores foi: \n{s}.')
print(f'A quantidade de números foi: {cont}.')
