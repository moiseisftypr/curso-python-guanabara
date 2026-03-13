# REVISADO
# Transformei as strings em maiúsculo logo na entrada.
from random import shuffle
a1 = str(input('NOME 1: ')).upper()
a2 = str(input('NOME 2: ')).upper()
a3 = str(input('NOME 3: ')).upper()
a4 = str(input('NOME 4: ')).upper()
alunos = [a1, a2, a3, a4]
shuffle(alunos)
# Embaralhei a lista com shuffle, que já está em maiúsculo.
print(f'A ordem será:\n{" ~> ".join(alunos)}')
# Em seguida quebrei a linha com "\n"  e utilizei o método .join() para ficar mais agradável, a visualização.
