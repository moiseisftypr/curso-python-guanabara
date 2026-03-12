# REVISÃO MUNDO 1 - MÓDULO: TRATAMENTO DE DADOS
# Aprendi: a função input() sempre retorna uma STRING.
# Para somar matematicamente, antes preciso converter (fazer o 'cast') para int ou float. 

n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
n3 = int(input('Digite mais um número:'))
s = n1 + n2 + n3

# Usando o f-string.
print(f'A soma de {n1}, {n2} e {n3} é {s}')
