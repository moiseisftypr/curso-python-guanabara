print('========= CAIXA INTELIGENTE ==========')
print('=-' * 21)
total = cont = cheap = cont_c = 0
name_cheap = ""
while True:
  name = str(input('NOME DO PRODUTO: ')).strip().upper()
  value = float(input('VAlOR: '))
  if value > 1000:
    cont += 1
  if cont_c == 0:
    cheap = value
    cont_c += 1
  if value <= cheap:
    cheap = value
    name_cheap = name
  total += value
  print('-=' * 21)
  resp = "x"
  while resp not in "SN":
    resp = str(input('ADICIONAR MAIS PRODUTOS [S/N]: ')).upper().strip()[0]
  if resp in "S":
    print('=-' * 21)
  elif resp in "N":
    print('_' * 42)
    print('COMPRA FINALIZADA!')
    print('_' * 42)
    break
print(f'TOTAL GASTO: {total :.2f}')
print(f'{cont} PRODUTOS CUSTAM MAIS DE R$ 1000.00')
print(f'{name_cheap} É O PRODUTO MAIS BARATO')
