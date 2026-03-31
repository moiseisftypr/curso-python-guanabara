# REVISADO
fim = False

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro núnero: '))

while not fim:

  print("=" * 45)

  print('[1] Somar')
  print('[2] Multiplicar')
  print('[3] Maior')
  print('[4] Novos Números')
  print('[5] Sair')

  print("=" * 45)

  opcao = int(input('Qual operação gostaria de relizar? '))

  print("-" * 45)

  if opcao == 1:
    print(f'SOMA: {n1} + {n2} = {n1 + n2}')

  elif opcao == 2:
    print(f'MULTIPLICAÇÃO: {n1} x {n2} = {n1 * n2}')

  elif opcao == 3:
    print(f'MAIOR NÚMERO: {max(n1, n2)}')

  elif opcao == 4:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))

  elif opcao == 5:
    fim = True

  else:
    print('Opção inválida, tente novamente!')

print('Programa finalizado!')
