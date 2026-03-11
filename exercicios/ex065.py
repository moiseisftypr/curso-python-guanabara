from time import sleep
m = t = c = max = min = 0
r = "S"
while r == "S":
  num = int(input('Digite um número: '))
  if c == 0:
    max = min = num
  else:
   if num > max:
    max = num
   if num < min:
    min = num
  t += num
  c += 1
  sleep(1)
  r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
  sleep(1)
sleep(1)
print('Processando...')
sleep(2)
print('Programa FINALIZADO.')
m = t / c
print(f'A média dos {c} valores foi {m :.1f}')
print(f'O maior valor foi {max} e o menor foi {min}')
