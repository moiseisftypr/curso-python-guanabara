a1 = int(input('Digite o Primeiro Termo: '))
r = int(input('Digite a Razão: '))
for n in range(1, 11):
  an = a1 + (n - 1) * r
  print(f'{n} Termo = {an}')
