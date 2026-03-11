num = int(input('Digite um número: '))
print(f'{num}! =', end="")
cont = num
fator = 1
while cont > 0:
  print(f' {cont} ', end= "")
  print('x' if cont > 1 else '= ', end="")
  fator *= cont
  cont -=1
print(fator)
