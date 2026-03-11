from math import sqrt, trunc
c1 = int(input('Qual a medida do cateto oposto em metros? '))
c2 = int(input('Qual o medida do cateto adjacente em metros? '))
h2 = (c1 ** 2) + (c2 ** 2)
h = sqrt(h2)
print(f'A hipotenusa desse triângulo retângulo mede: {trunc(h)} metros.')
