print('SERVIÇO DE ALISTAMENTO MILITAR')
ano = int(input('Em que ano você nasceu? '))
idade = 2025 - ano
if idade < 18 and 18 - idade != 1:
  print(f'Você nasceu em {ano} e tem {idade} anos, ainda faltam {18 - idade} anos para o alistamento militar. Apenas em {ano + 18}.')
elif idade < 18:
  print(f'Você nasceu em {ano} e tem 17 anos, ainda falta 1 ano para o alistamento militar. Em 2026.')
if idade == 18:
  print(f'Você nasceu em {ano} e tem 18 anos, está na idade certa para o alistamento militar. Neste ano, 2025.')
if idade > 18 and idade - 18 != 1:
  print(f'Você nasceu em {ano} e tem {idade} anos, está {idade - 18} anos fora do prazo do alistamento militar. Foi em {ano + 18}.')
elif idade > 18:
  print(f'Você nasceu em {ano} e tem 19 anos, está 1 ano fora do prazo do alistamento militar. Foi em 2024.')
