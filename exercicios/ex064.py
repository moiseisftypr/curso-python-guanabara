# REVISADO
c = 0
s = 0
fim = False

print('=' * 45)

while not fim:
  n = int(input('Digite um número: '))

  if n == 999:
    fim = True

  else:
    s += n
    c += 1
    print(f'Número {n} adicionado!')

    print('-' * 45)

    print('Digite 999 p/ FINALIZAR o programa.')

    print('-' * 45)

print('=' * 45)

print(f'* Quantidade de números informados: {c}')
print(f'* Soma de todos os valores: {s}')
