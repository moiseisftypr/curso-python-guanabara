# REVISADO
salario = float(input('SALÁRIO ATUAL(R$): '))
if salario <= 1250.00:
  print(f'PARABÉNS! Você recebeu um aumento salarial de 15%.\nSeu novo salário será: R${salario * 1.15 :.2f}.')
else:
  print(f'PARABÉNS! Você recebeu um aumento salarial de 10%.\nSeu novo salário será: R${salario * 1.10 :.2f}')
