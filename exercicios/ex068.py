from random import randint
from time import sleep
print('========== JOGO DO PAR OU ÍMPAR ===========')
print('=-' * 21)
count = 0
while True:
  poi = "x"
  while poi not in "PI":
    poi = str(input('PAR OU ÍMPAR [P/I]: ')).upper().strip()[0]
  numpc = randint(0, 10)
  numus = int(input('DIGITE UM NÚMERO (0 - 10): '))
  total = numpc + numus
  sleep(0.3)
  print('VAMOS COMEÇAR!!')
  sleep(0.7)
  print('DÓ..')
  sleep(0.7)
  print('LÁ..')
  sleep(0.7)
  print('SÍ..')
  sleep(0.7)
  print('JÁ!')
  print('_' * 42)
  if total % 2 == 0:
    print(f'JOGADOR = {numus}\nCOMPUTADOR = {numpc}')
    sleep(2)
    print(f'TOTAL = {total}, PAR!')
    if poi in "P":
      print('Parabéns, você GANHOU!!')
      sleep(2)
      print('Se prepare, vamos novamente.')
      count += 1
    else:
      print('Você PERDEU, mais sorte na próxima.')
      break
  else:
    print(f'JOGADOR = {numus}\nCOMPUTADOR = {numpc}')
    sleep(2)
    print(f'TOTAL = {total}, ÍMPAR!')
    if poi in "I":
      print('Parabéns, você GANHOU!!')
      sleep(2)
      print('Se prepare, vamos novamente.')
      count += 1
    else:
      print('Você PERDEU, mais sorte na próxima.')
      break
print(f'Você teve {count} vitórias consecutivas.')