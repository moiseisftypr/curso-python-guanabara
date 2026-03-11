sa = float(input('Qual o seu salário? '))
if sa > 1250.00:
  print(f'Parabéns, você recebeu um aumento salarial de 10%! \nSeu salário de R${sa :.2f} irá passar para R${sa * 1.10 :.2f}!')
else:
  print(f'Parabéns, você recebeu um aumento salarial de 15%! \nSeu salário de R${sa :.2f} irá passar para R${sa * 1.15 :.2f}!')
