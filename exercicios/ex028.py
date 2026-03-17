# REVISADO
from random import randint
from time import sleep
pc_num = randint(0,5)
print("O Computador pensou em um número de 0 a 5...")
sleep(2)
user_num = int(input('Qual seria esse número? '))
print('Um momento, PROCESSANDO...')
sleep(2)
print(f'Você escolheu o número: {user_num}\nNúmero pensado pelo Computador: {pc_num}')
if pc_num == user_num:
  print('PARABÉNS, você acertou!!!')
else:
  print('VOCÊ ERROU, boa sorte na próxima vez!')
