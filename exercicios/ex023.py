n = int(input('Digite um número de 0 a 9999: '))
print(f'Analisando o número: {n}')
un = n // 1 % 10
de = n // 10 % 10
ce = n // 100 % 10
mi = n // 1000 % 10
print(f'Unidade: {un}')
print(f'Dezena: {de}')
print(f'Centena: {ce}')
print(f'Milhar: {mi}')
