# REVISADO
from time import sleep

iniciar = int(input('DIGITE [0] P/ INICIAR A CONTAGEM REGRESSIVA: '))

if iniciar == 0:
  for c in range(10, 0, -1):
   print(f'{c}..')
   sleep(1)
  print('KABUUUUUUUM!')

else:
 print('TECLA INCORRETA, tente novamente.')
