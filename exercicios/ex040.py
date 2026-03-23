# REVISADO
p1 = float(input('NOTA P1: '))
p2 = float(input('NOTA P2: '))
media = (p1 + p2) / 2
print(f'MÉDIA: {media :.1f}')
if media < 5.0:
  print(f'Você foi REPROVADO!\nEstude com mais afinco na próxima vez.')
elif 5.0 <= media <= 6.9:
  print(f'Você ficou em RECUPERAÇÃO!\nVoce terá outra chance, se prepare!')
else:
  print(f'Você foi APROVADO!\nParabéns, você conseguiu uma ótima nota!')
