# REVISADO
print('======••• CALCUDADORA DE IMC •••======')
peso = float(input('PESO(KG): '))
altura = float(input('ALTURA(M): '))
imc = peso / (altura * altura)
print(f'Índice de Massa Corporal(IMC): {imc :.1f}')
if imc < 18.5:
  print('Abaixo do peso ideal')
elif 18.5 <= imc < 25:
  print('Peso ideal')
elif 25 <= imc < 30:
  print('Sobrepeso')
elif 30 <= imc < 40:
  print('Obesidade')
else:
  print('Obesidade mórbida')
  