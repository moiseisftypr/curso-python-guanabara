# REVISADO
from time import sleep

sexo = str(input('INFORME O SEXO [M/F]: ')).upper().strip()[0]
sleep(0.5)

while sexo != "M" and sexo != "F":
  print('Algo deu errado, tente novamente!')
  sexo = str(input('INFORME O SEXO [M/F]: ')).upper().strip()[0]
  sleep(0.5)


print('Sexo registrado com SUCESSO!')
