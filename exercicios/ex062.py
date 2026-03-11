a1 = int(input('Digite o Primeiro Termo: '))
r = int(input('Digite a Razão: '))
c = 1
add = 0
while c < 11:
  an = a1 + (c - 1) * r
  print(f'{c}º Termo = {an}')
  c += 1
while c > 9:
  add = int(input('Quantos termos quer adicionar: '))
  if add > 0:
    add += c
    while add > c:
      an = a1 + (c - 1) * r
      print(f'{c}º Termo = {an}')
      c += 1
  elif add == 0:
   c = 9
   print('PROGRAMA ENCERRADO.')
