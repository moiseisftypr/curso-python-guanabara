# REVISADO:
# .split(): Quebra o nome em "tokens" (palavras).
# [-1]: Acesso direto ao último elemento, independente do tamanho da lista.
# Engenharia: Uso de índices negativos evita cálculos de tamanho (len), 
# tornando o código mais limpo e menos propenso a erros de "Off-by-one".
nome = str(input('NOME COMPLETO: ')).strip().upper().split()
print(f'PRIMEIRO NOME: {nome[0]} \nÚLTIMO NOME: {nome[-1]}')
