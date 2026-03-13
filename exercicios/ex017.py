# REVISADO
from math import sqrt, trunc
co = int(input('Informe a medida do cateto oposto(M): '))
ca = int(input('Informe a medida do cateto adjacente(M): '))
h2 = co **2 + ca **2
h = sqrt(h2)
print(f'A hipotenusa desse triângulo retângulo mede {trunc(h)} metros.')
