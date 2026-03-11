a1 = int(input('Digite o Primeiro Termo: '))
r = int(input('Digite a Razão: '))
c = 1
while c < 11:
  an = a1 + (c - 1) * r
  print(f'{c}º Termo = {an}')
  c += 1
