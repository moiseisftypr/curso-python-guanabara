d = float(input('Qual a distância em KM da sua viagem? '))
if d > 200:
  print(f'Sua viagem é de {d} KM, terá o valor de R$ {d * 0.45 :.2f}.')
else:
  print(f'Sua viagem é de {d} KM, terá o valor de R$ {d * 0.50 :.2f}.')
