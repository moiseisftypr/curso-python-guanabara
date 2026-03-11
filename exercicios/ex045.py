from random import choice
from time import sleep
print('Te desafio a me ganhar no JOKENPÔ! ;)')
resposta = str(input('Você aceita o desafio? Sim ou não? ')).capitalize().strip()
if resposta == "Sim":
  print('Haha, beleza! Vamos começar!')
  sleep(1)
else:
    print('Poxa, que pena! Deixa para a próxima.')
    sleep(100000)

jok_list = ["Pedra", "Papel", "Tesoura"]
jok_pc = choice(jok_list)
jok_user = str(input('Escolha um! \nPedra, Papel ou Tesoura? ')).capitalize().strip()
sleep(1)
print('Vamos lá!')
sleep(0.7)
print('JO..')
sleep(1)
print('KEN..')
sleep(1)
print('PÔÔ!!..')
sleep(1)

print(f'Você escolheu {jok_user} e eu escolhi {jok_pc}.')

if jok_pc == "Pedra":

   if jok_user == "Pedra":
      print('Putz, deu EMPATE!')

   elif jok_user == "Papel":
      print('você VENCEU! Parabéns, você é bom!')

   elif jok_user == "Tesoura":
      print('Eu VENCI! Haha')

   else:
      print('Opção inválida, tente novamente.')


elif jok_pc == "Papel":

   if jok_user == "Pedra":
      print('Eu VENCI! Haha')

   elif jok_user == "Papel":
      print('Putz, deu EMPATE!')

   elif jok_user == "Tesoura":
      print('Você VENCEU! Parabéns, você é bom!')

   else:
      print('Opção inválida, tente novamente.')


elif jok_pc == "Tesoura":

   if jok_user == "Pedra":
      print("Você VENCEU! Parabéns, você é bom!")

   elif jok_user == "Papel":
      print('Eu VENCI! Haha')

   elif jok_user == "Tesoura":
      print('Putz, deu EMPATE!')

   else:
      print('Opção inválida, tente novamente.')
