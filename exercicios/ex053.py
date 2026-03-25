# REVISADO
# Entrada e Limpeza dos dados (Pré-processamento)
# .strip() remove espaços nas bordas, .upper() padroniza para maiúsculas
# .split() divide a frase em uma lista de palavras
frase = str(input('Digite uma frase: ')).strip().upper().split()


# ''.join() junta as palavras da lista em uma única string, sem espaços
junto = ''.join(frase)

# Inversão da String
# Criamos uma variável vazia para armazenar o texto de trás para frente
inverso = ''

# O laço 'for' percorre os índices da string 'junto' em ordem reversa
# range(início, fim, passo)
# Começa no último índice (tamanho - 1), vai até o primeiro (0) subtraindo 1
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

# Exibição dos Resultados
print(f'\nO inverso de {junto} é {inverso}.')

# Lógica de Decisão (Verificação do Palíndromo)
if junto == inverso:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada NÃO é um palíndromo.')
