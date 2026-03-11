print('============ CAIXA ELETRÔNICO ============')
print('=-' * 21)
new_value = 0
value = int(input('VALOR DO SAQUE (R$): '))
cont50 = cont20 = cont10 = cont1 = 0
while True:
  while value >= 50:
    value -= 50
    cont50 += 1 
  while value >= 20:
    value -= 20
    cont20 += 1
  while value >= 10:
    value -= 10
    cont10 += 1
  while value >= 1:
    value -= 1
    cont1 += 1
  break
if cont50 > 0:
  print(f'{cont50} CÉDULA(S) de R$50')
if cont20 > 0:
  print(f'{cont20} CÉDULA(S) de R$20')
if cont10 > 0:
  print(f'{cont10} CÉDULA(S) de R$10')
if cont1 > 0:
  print(f'{cont1} CÉDULA(S) de R$1')
print('_' * 42)
print('SAQUE REALIZADO COM SUCESSO!')
