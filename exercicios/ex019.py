# REVISADO:
# 'choice': Escolhe um elemento aleatório de uma sequência.
# .upper(): Usei para padronizar a saída, independente de como o usuário digitou.
from random import choice
a1 = str(input('NOME 1: '))
a2 = str(input('NOME 2: '))
a3 = str(input('NOME 3: '))
a4 = str(input('NOME 4: '))
alunos = [a1, a2, a3, a4]
sorteado = choice(alunos)
print(f'O aluno sorteado foi: {sorteado.upper()}.')
