print('Calculadora de IMC')
peso = float(input('Quanto você pesa?  '))
altura = float(input('Qual é a sua altura?  '))
imc = peso / (altura ** 2)
if imc < 18.5:
  print(f'Seu IMC é de {imc :.1f}, você está abaixo do peso.')
elif 18.5 <= imc < 25:
  print(f'Seu IMC é de {imc :.1f}, você está no peso ideal.')
elif 25 <= imc < 30:
  print(f'Seu IMC é de {imc :.1f}, você está com sobrepeso.')
elif 30 <= imc < 40:
  print(f'Seu IMC é de {imc :.1f}, você está com obesidade.')
else:
  print(f'Seu peso é de {imc :.1f}, você está com obesidade mórbida.')
