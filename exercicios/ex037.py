num = int(input('Digite um número: '))
conversao = int(input('Binário [1] \nOctal [2] \nHexadecimal [3] \nDigite o número da base de conversão escolhida:'))
if conversao == 1:
  print(f'{num} convertido para BINÁRIO: {bin(num)[2:]}.')
elif conversao == 2:
  print(f'{num} convertido para OCTAl: {oct(num)[2:]}.')
elif conversao == 3:
  print(f'{num} convertido para HEXADECIMAL: {hex(num)[2:]}.')
else:
  print('Opção inválida, tente novamente.')
