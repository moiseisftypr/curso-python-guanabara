from random import randint
from time import sleep
num_us = int(input('O computar escolheu um número entre 0 e 5 \nQual seria esse número? '))
num_pc = randint(0, 5)
print('PROCESSANDO...')
sleep(2)
print(f'O número escolhido pelo computador foi {num_pc}. \nE o número que você escolheu foi {num_us}.')
if num_us == num_pc:
  print('PARABÉNS, você acertou!!')
else:
  print('Você errou! :(')
