n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
botao = 0
while botao != 5:
  print('''=========== PAINEL DE CONTROLE ===========
\n[ 1 ] SOMAR VALORES
[ 2 ] MULTIPLICAR VALORES
[ 3 ] IDENTIFICAR MAIOR VALOR
[ 4 ] SELECIONAR NOVOS VALORES
[ 5 ] SAIR\n''')
  botao = int(input('SELECIONE UM COMANDO: '))
  if botao == 1:
    print(f'A soma de {n1} e {n2} é {n1 + n2}')
  elif botao == 2:
    print(f'A multiplicação de {n1} com {n2} é {n1 * n2}')
  elif botao == 3:
    maior = max(n1, n2)
    print(f'O maior valor é {maior}')
  elif botao == 4:
    n1 = int(input('Digite o novo valor: '))
    n2 = int(input('Digite o outro novo valor: '))
  elif botao == 5:
    print('PROGRAMA ENCERRADO.')
  else:
    print('COMANDO INVÁLIDO. Tente novamente.')
