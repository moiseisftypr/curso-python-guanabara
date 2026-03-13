# REVISADO:
# A lógica matemática (n // casa % 10) garante que o código funcione de 0 a 9999.
# Importante para Security: Manipulação direta de valores numéricos é mais performática e segura.
n = int(input('DIGITE UM NÚMERO: '))
uni = n // 1 % 10
dez = n // 10 % 10
cen = n // 100 % 10
mil = n // 1000 % 10
print(f'UNIDADE: {uni} \nDEZENA: {dez} \nCENTENA: {cen} \nMILHAR: {mil}')

# TENTATIVA COM STR (NÃO RECOMENDADA):
'''num = int(input('DIGITE UM NÚMERO : ')).strip()
n = str(num)
mil = num[0]
cen = num[1]
dez = num[2]
uni = num[3]
print(f'{mil}, {cen}, {dez}, {uni}')'''

'''n = str(num)
mil = n[0]  <-- Erro aqui se o número for "12" (não existe índice 0, 1, 2, 3 garantido)
...
ERRO: IndexError. 
Motivo: Sem laços de repetição ou conferência de tamanho (len), 
o acesso direto por índice falha em números com menos de 4 dígitos.
'''