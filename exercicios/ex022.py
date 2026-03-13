# REVISADO:
# .strip(): Limpeza de ruído (espaços) nas extremidades.
# .split(): Transformação da string em lista (Tokenização).
# ''.join(): Reagrupamento de elementos para contagem líquida de caracteres.
nome = str(input('NOME COMPLETO: ')).strip()
print(f'MAIÚSCULO: {nome.upper()}')
print(f'minúsculo: {nome.lower()}')
dividido = nome.split()
# Conta o total sem considerar espaços unindo a lista
print(f'Total de letras: {len("".join(dividido))}')
# O primeiro item da lista é sempre o primeiro nome
print(f'Letras no primeiro nome: {len(dividido[0])}')
