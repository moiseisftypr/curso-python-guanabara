# REVISADO
n = int(input('Digite um núnero: '))
c = n
f = 1

print(f'{n}! = ', end="")

while c > 0:
  print(f'{c}', end=" x " if c > 1 else " = ")
  f *= c
  c -= 1

print(f'{f}')


# De outra forma, utilizando o comando for:
'''n = int(input('Digite um núnero: '))
f = 1
print(f'{n}! = ' , end= "")

for c in range(n, 0, -1):
  print(f'{c}', end= " x " if c > 1 else " = ")
  f *= c

print(f'{f}')'''
