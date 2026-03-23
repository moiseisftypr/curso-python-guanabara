# REVISADO
r1 = int(input('MEDIDA DA PRIMEIRA RETA(M): '))
r2 = int(input('MEDIDA DA SEGUNDA RETA(M): '))
r3 = int(input('MEDIDA DA TERCEIRA RETA(M): '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
  print('Essas retas PODEM formar um TRIÂNGULO!')
  if r1 == r2 == r3:
    print('TRIÂNGULO EQUILÁTERO\nTodos os lados são iguais.')
  elif r1 == r2 and r1 != r3 or r2 == r3 and r2 != r1 or r1 == r3 and r1 != r2:
    print('TRIÂNGULO ISÓSCELES\nPossui dois lados iguais.')
  else:
    print('TRIÂNGULO ESCALENO\nTodos os lados são diferentes.')

else:
  print('Essas retas NÃO PODEM formar um TRIÂNGULO!')
