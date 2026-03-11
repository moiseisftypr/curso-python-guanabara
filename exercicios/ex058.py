from random import randint
from time import sleep
num_us = 0
cont = 0
print('--------- JOGO DA ADIVINHAÇÃO ---------')
print('O Computador irá escolher um número de 1 a 10. \nPara ganhar o jogo, tente adivinhar o número escolhido pelo computador. ')
num_pc = randint(1, 10)
while num_pc != num_us:
  num_us = int(input('Qual o número correto? '))
  cont += 1
  print('PROCESSANDO...')
  sleep(2)
  if num_pc > num_us:
    print('Mais... Tente novamente.')
  if num_pc < num_us:
    print('Menos... Tente novamente.')
print('Você ACERTOU! Parabéns!')
print(f'O número correto, era o número {num_pc}, você acertou na {cont}ª tentativa')
