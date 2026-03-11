n1 = float(input('Qual foi sua primeira nota? '))
n2 = float(input('Qual foi sua segunda nota? '))
media = (n1 + n2) / 2
if media >= 7.0:
  print(f'Sua média foi: {media :.1f}\nParabéns, você foi APROVADO!!')
elif media >= 5.0 <= 6.9:
  print(f'Sua média foi: {media :.1f}\nVocê está de RECUPERAÇÃO.')
else:
  print(f'Sua média foi: {media :.1f}\nInfelizmente, você foi REPROVADO.')
