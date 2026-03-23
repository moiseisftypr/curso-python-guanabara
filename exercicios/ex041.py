# REVISADO
from datetime import date
atual = date.today().year
nascimento = int(input('ANO DE NASCIMENTO: '))
idade = atual - nascimento
print(f'IDADE: {idade} ANOS')
if idade <= 9:
  print('CATEGORIA MIRIM')
elif 9 < idade <= 14:
  print('CATEGORIA INFANTIL')
elif 14 < idade <= 19:
  print('CATEGORIA JUNIOR')
elif idade == 20:
  print('CATEGORIA SÊNIOR')
else: 
  print('CATEGORIA MASTER')
