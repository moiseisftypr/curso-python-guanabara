# REVISADO
from random import randint
from time import sleep
velo = randint(40, 120)
print('=========== RADAR DE VELOCIDADE ============')
sleep(3)
multa = (velo - 80) * 7
print(f'Você ultrapasou a uma velocidade de {velo}KM/H.')
if velo > 80:
  print(f'Você estava acima do limite de velocidade permitido de 80KM/H.\nSua multa será de R${multa :.2f}.')
else:
  print('Você estava dentro de limite de velocidade permitido de 80KM/H.\nTenha uma boa viagem!')
