from datetime import datetime
ano = datetime.now().year
cont1 = 0
cont2 = 0
for c in range(1, 8):
  nasc = int(input(f'Ano de nascimento da {c}ª pessoa: '))
  idade = ano - nasc
  if idade >= 18:
    cont1 += 1
  elif idade < 18:
    cont2 += 1
print(f'O número de pessoas que já atingiram a maior idade é: {cont1}')
print(f'O número de pessoas que ainda não atingiram a maior idade é: {cont2}')
