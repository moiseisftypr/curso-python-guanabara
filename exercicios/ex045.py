# REVISADO
from time import sleep
from random import randint
print('========= ••• JOKENPÔ ••• =========')
inicio = str(input('Olá! Gostaria de jogar Jokenpô [S/N]? ')).upper().strip()

if "S" in inicio[0]:
  print('BOA! Vamos começar, então!')

  sleep(2)

  user = int(input('ESCOLHA UMA OPÇÃO:\nPEDRA = [1]\nPAPEL = [2]\nTESOURA = [3]\nDigite o número de acordo com a opção que gostaria de selecionar: '))
  if 1 <= user <= 3:
    pc = randint(1, 3)
    print('JO..')
    sleep(1)
    print('KEN..')
    sleep(1)
    print('PÔÔÔÔ!!!')
    sleep(1)

    if pc == 1:
      print('O Computador escolheu PEDRA')
    elif pc == 2:
      print('O Computador escolheu PAPEL')
    else:
      print('O Computador escolheu TESOURA')
      sleep(1)

    if user == 1:
      print('Você escolheu PEDRA')
    elif user == 2:
      print('Você escolheu PAPEL')
    elif user == 3:
      print('Você escolheu TESOURA')

    sleep(1) 

    if user == 1 and pc == 3 or user == 2 and pc == 1 or user == 3 and pc == 2:
      print('VOCÊ GANHOU! Parabéns!')
    elif user == 1 and pc == 2 or user == 2 and pc == 3 or user == 3 and pc == 1:
      print('VOCÊ PERDEU, que pena, mais sorte na próxima.')
    elif user == 1 and pc == 1 or user == 2 and pc == 2 or user == 3 and pc == 3:
      print('EMPATE, ninguém ganhou.')
  else:
    print('ALGO DEU ERRADO, tente novamente!')


elif "N" in inicio[0]:
  print('Poxa, beleza! Deixa pra próxima.')

else:
  print('Não deu pra entender, repita por favor.')