print('Simulacão de Empréstimo Bancário.')
casa = float(input('Qual o valor do imóvel? '))
salario = float(input('Qual o salário do comprador? '))
prazo = float(input('Em quantos anos pretende quitar o bem? '))
prestacao = casa / (prazo * 12)
if prestacao > salario * 0.30:
  print(f'Infelizmente, seu empréstimo foi NEGADO.\nPois sua prestação (R$ {prestacao :.2f}) excederia o valor máximo permitido, de acordo com seu salário (R$ {salario :.2f}).')
else:
  print(f'PARABÉNS, seu empréstimo foi APROVADO!\nSua prestação ficará no valor de R$ {prestacao :.2f} mensais')
