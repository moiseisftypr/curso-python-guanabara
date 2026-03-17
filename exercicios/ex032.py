# REVISADO
from datetime import date
from time import sleep
ano = int(input('Qual ANO gostaria de analisar? Digite "0" para analisar o ano atual: '))
if ano == 0:
  ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print(f'O ano de {ano} é um ano BISSEXTO.')
else:
  print(f'O ano de {ano} não é um ano BISSEXTO.')
