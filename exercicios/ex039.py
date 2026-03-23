# REVISADO
from datetime import date
atual = date.today().year
nascimento = int(input('ANO DE NASCIMENTO: '))
idade = atual - nascimento
if idade > 18:
  print(f'{idade} ANOS.\nVocê ultrapassou a idade correta para o Alistamento Militar em {idade - 18} anos.')
elif idade < 18:
  print(f'{idade} ANOS.\nAinda faltam {18 - idade} ano(s) para o seu Alistamento Militar.')
else:
  print(f'18 ANOS.\nVocê está na idade adequada para o Alistamento Militar.')
