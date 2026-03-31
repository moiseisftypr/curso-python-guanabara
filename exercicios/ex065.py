# REVISADO
cont = soma = maior = menor = 0
fim = False

print('=' * 45)

while not fim:
  n = int(input('Digite um número: '))
  print(f'{n} adicionado!')

  soma += n
  cont += 1

  if cont == 1:
    maior = menor = n

  else: 
    if n > maior:
      maior = n

    if n < menor:
      menor = n

  print('-' * 45)

  resp = " "

  while resp not in "SN":
    resp = str(input('Quer adicionar mais algum número? [S/N] ')).strip().upper()[0]

    if resp not in "SN":
      print('Resposta inválida, tente novamente.')

  if resp == "N":
    fim = True

    print("-" * 45)

print("=" * 45)

print(f'* Média dos valores: {soma / cont :.1f}')
print(f'* Maior número: {maior}')
print(f'* Menor número: {menor}')
