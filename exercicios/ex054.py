# REVISADO
from datetime import date

atual = date.today().year
maior = 0
menor = 0

for c in range(1, 8):
  nasc = int(input('ANO DE NASCIMENTO: '))
  if atual - nasc >= 21:
    maior +=1
  else:
    menor +=1

print(f'TOTAL:\n{maior} pessoas JÁ atingiram a maior idade.\n{menor} pessoas, ainda NÃO atingiram.')
