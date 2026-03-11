r1 = int(input('Digite o comprimento da primeira reta: '))
r2 = int(input('Digite o comprimento da segunda reta: '))
r3 = int(input('Digite o comprimento da terceira reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r3 + r2 > r1:
  print('As retas informadas podem formar um triângulo.')
else:
  print('As retas informadas não podem formar um triângulo.')
