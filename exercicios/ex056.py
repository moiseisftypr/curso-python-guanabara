somaidade = 0
mediaidade = 0
nomehmv = ''
idadehmv = 0
cont20 = 0
for c in range(1, 5):
  print(f'------ {c}ª PESSOA ------')
  nome = str(input('NOME: ')).strip().capitalize()
  idade = int(input('IDADE: '))
  sexo = str(input('SEXO: (Responda com [M/F]) ')).upper().strip()
  somaidade += idade
  if sexo == "M" and c == 1:
    idadehmv = idade
    nomehmv = nome
  if sexo == "M" and idade > idadehmv:
    idadehmv = idade
    nomehmv = nome
  if sexo == "F" and idade < 20:
    cont20 += 1
mediaidade = somaidade / 4
print(f'\nA média de idade do grupo é de {mediaidade :.0f} anos.')
print(f'\nO nome do homem mais velho é {nomehmv} e ele tem {idadehmv} anos.')
print(f'\nO número de mulheres que tem menos de 20 anos é {cont20}.')
