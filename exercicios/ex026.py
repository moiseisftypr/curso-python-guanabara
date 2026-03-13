# REVISADO
frase = str(input('DIGITE UMA FRASE: ')).strip().upper()
print(f'A letra "A" aparece {frase.count("A")} vez(es).')
print(f'Ela aparece a primeira vez na posição {frase.find("A") + 1}.')
# Somamos +1 para que a posição 0 apareça como 1 para o usuário
print(f'E a última vez na posição {frase.rfind("A") + 1}.')
# Utilizei o "rfind" para isso: ele começa a procurar da direita para a esquerda, encontrando a última ocorrência instantaneamente.
