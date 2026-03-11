from datetime import datetime
from time import sleep
print(' ~~~~~~~~~ CADASTRO DE DADOS ~~~~~~~~~')
ano = datetime.now().year
cont18 = contm = contf = 0
while True:
  print('=-' * 21)
  nasc = int(input('ANO DE NASCIMENTO: '))
  sexo = "x"
  while sexo not in "MF":
    sexo = str(input('SEXO [M/F]: ')).upper().strip()[0]
  sleep(2)
  print('=-' * 21)
  print('DADOS COLETADOS COM SUCESSO!')
  print('=-' * 21)
  idade = ano - nasc
  if idade >= 18:
    cont18 += 1
  if sexo in "M":
    contm += 1
  if sexo in "F" and idade < 20:
    contf += 1
  resp = "x"
  while resp not in "NS":
   resp = str(input('QUER CONTINUAR [S/N]? ')).upper().strip()[0]
  if resp in "N":
   break
print('**' * 21)
print(f'MAIORES DE 18 ANOS = {cont18}')
print(f'HOMENS CADASTRADOS = {contm}')
print(f'MULHERES SUB-20 = {contf}')
