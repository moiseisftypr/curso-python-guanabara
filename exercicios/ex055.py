  maior = 0
  menor = 0
  for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
      maior = peso
      menor = peso
    else:
      if peso > maior:
        maior = peso
      if peso < menor:
        menor = peso
  print(f'O maior peso lido foi {maior :.1f}Kg')
  print(f'O menor peso lido foi {menor :.1f}Kg')
