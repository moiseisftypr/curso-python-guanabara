s = 0
cont = 0
for n in range(1, 7):
  n = int(input('Digite um número: '))
  if n % 2 == 0:
    s += n
    cont += 1
print(f'Você informou {cont} números PARES e a somatória foi {s}.')
