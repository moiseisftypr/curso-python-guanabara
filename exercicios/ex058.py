# REVISADO
from random import randint
from time import sleep

pc_num = randint(0, 10)
cont = 0
acertou = False

print("-=-" * 15)
print("Vou pensar em um número entre 0 e 10.\nTente adivinhar!")
print("-=-" * 15)
sleep(1)

while not acertou:
    user_num = int(input('Qual é o seu palpite? '))
    cont += 1

    print('PROCESSANDO...')
    sleep(1)

    if user_num == pc_num:
        acertou = True
        print(f'PARABÉNS! Você acertou com {cont} tentativa(s).')

    else:

        if user_num < pc_num:
            print('Mais... Tente outra vez.')
        else:
            print('Menos... Tente outra vez.')
        print('-' * 44)

print('Fim de jogo!')
