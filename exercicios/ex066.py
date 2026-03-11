s = c = 0
while True:
  num = int(input('Digite um número [999 p/ PARAR]: '))
  if num == 999:
    break
  s += num
  c += 1
print(f'Você digitou {c} números e a soma entre eles foi {s}')