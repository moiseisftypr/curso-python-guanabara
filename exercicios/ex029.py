from random import randint
from time import sleep
velo = randint(60, 100,)
print('A velocidade na pista é de até 80 KM/H.')
print('Verificando sua velocidade...')
sleep(2.5)
if velo > 80:
  print(f'Sua velocidade atual é de {velo} KM/H. \nVocê foi multado em R${(velo - 80) *7 :.2f}.')
else:
  print(f'Sua velocidade atual é de {velo} KM/H, está OK!')
