# REVISADO:
# 'from math import floor': Importação seletiva (economiza memória).
# floor(): Função que "arredonda para baixo", extraindo a parte inteira.
from math import floor
n = float(input('Digite um número real: '))
por = floor(n)
print(f'A porção inteira de {n} é {por}.')
# Alternativa: Poderia usar int(n) para o mesmo resultado sem importar módulos.
