from datetime import datetime
atual = datetime.now().year
ano = int(input('Qual ano você nasceu? '))
idade = atual - ano
if idade > 20:
  print(f'Você tem {idade} anos. \nEstá na Categoria MASTER.')
elif idade == 20:
  print(f'Você tem {idade} anos. \nEstá na Categoria SÊNIOR')
elif idade > 14 <= 19:
  print(f'Você tem {idade} anos. \nEstá na Categoria JUNIOR')
elif idade > 9 <= 14:
  print(f'Você tem {idade} anos. \nEstá na Categoria INFANTIL')
else:
  print(f'Você tem {idade} anos. \nEstá na Categoria MIRIM')
