num = c = r = flag = 0
while flag != 999:
  num = int(input('Digite um número: '))
  if num != 999:
    r += num
    c += 1
    print(f'''Número {num} adicionado.\nPara PAUSAR digite: "999"''')
  elif num == 999:
    print(f'A somatória dos {c} valores é {r}.')
    flag = 999
