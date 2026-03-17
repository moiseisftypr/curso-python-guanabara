# REVISADO
n1 = int(input('DIGITE UM NÚMERO: '))
n2 = int(input('DIGITE OUTRO NÚMERO: '))
n3 = int(input('DIGITE MAIS UM NÚMERO: '))

# Descobrindo o maior número.
if n1 > n2 and n1 > n3:
  print(f'O maior número é: {n1}.')
elif n2 > n1 and n2 > n3:
  print(f'O maior número é: {n2}.')
else:
  print(f'O maior número é: {n3}.')

# Descobrindo o menor número.
if n1 < n2 and n1 < n3:
  print(f'O menor número é: {n1}.')
elif n2 < n1 and n2 < n3:
  print(f'O menor número é: {n2}.')
else:
  print(f'0 menor número é: {n3}.')
