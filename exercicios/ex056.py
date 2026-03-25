# REVISADO
from time import sleep

soma_idade = 0
idade_hmv = 0
nome_hmv = ''
m_sub20 = 0

for p in range(1, 5):

  nome = str(input(f'NOME DA {p}ª PESSOA: ')).strip().capitalize()
  idade = int(input(f'IDADE DA {p}ª PESSOA: '))
  sexo = str(input(f'SEXO DA {p}ª PESSOA [F/M]: ')).strip().upper()

  if 'M' in sexo[0] and idade > idade_hmv:
    idade_hmv = idade
    nome_hmv = nome


  if 'F' in sexo[0] and idade < 20:
    m_sub20 += 1


  soma_idade += idade

if nome_hmv == '':
  nome_hmv = 'Não foram encontrados homens no grupo.'


print('•' * 44)
print('FILTRANDO...')
print('•' * 44)
sleep(3)
print('FILTRAGEM REALIZADA COM SUCESSO!')
sleep(2)
print('•' * 44)
print('RESULTADO DA PESQUISA:')
print('•' * 44)
sleep(2)


print(f'MÉDIA DE IDADE: {soma_idade / 4 :.0f} ANOS')
sleep(2)
print(f'NOME DO HOMEM MAIS VELHO: {nome_hmv}')
sleep(2)
print(f'MULHERES SUB-20: {m_sub20} MULHER(ES)')
