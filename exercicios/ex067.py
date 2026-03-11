print('================= TABUADA ================')
while True:
  print('_' * 42)
  num = int(input('DIGITE UM NÚMERO: '))
  if num < 0:
    print('TABUADA ENCERRADA.')
    break
  count = 1
  print('_' * 42)
  while count < 11:
   print(f'{num} x {count} = {num * count}')
   count += 1
