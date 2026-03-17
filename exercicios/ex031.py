# REVISADO
from time import sleep
distancia = int(input('DISTÂNCIA DA VIAGEM(KM): '))
print('CALCULANDO...')
sleep(2.5)
if distancia > 200:
  print(f'O valor total da viagem será:\nR${distancia * 0.45 :.2f}.')
else:
 print(f'O valor total da viagem será:\nR${distancia * 0.50 :.2f}.')
