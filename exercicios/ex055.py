# REVISADO
maior = 0
menor = 0

for p in range(1, 6):
    # Entrada de dados com f-string para indicar a ordem da pessoa
    peso = float(input(f'Peso da {p}ª pessoa (Kg): '))

    # Lógica de Inicialização Especial:
    # Na primeira ocorrência (p == 1), o primeiro peso lido 
    # torna-se a nossa referência inicial para comparação.
    if p == 1:
        maior = peso
        menor = peso

    # Lógica de Comparação (Bloco de Processamento):
    else:
        # Verifica se o peso atual é maior que o recorde anterior
        if peso > maior:
            maior = peso

        # Verifica se o peso atual é menor que o recorde anterior
        if peso < menor:
            menor = peso

# Bloco de Saída (Exibição dos resultados formatados)
# :.1f garante que apenas uma casa decimal apareça (ex: 80.5)
print(f'\nO maior peso lido foi de {maior:.1f}Kg')
print(f'O menor peso lido foi de {menor:.1f}Kg')
