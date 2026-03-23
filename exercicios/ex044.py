# REVISADO
print('======••• MERCADO PYTHON •••======')
valor = float(input('VALOR DO PRODUTO(R$): '))
pagamento = int(input('FORMA DE PAGAMENTO: \nÀ VISTA DINHEIRO/CHEQUE = [1]\nÀ VISTA CARTÃO = [2]\nCARTÃO EM 2x = [3]\nCARTÃO EM 3x OU MAIS = [4]\nDigite o número de acordo com a opção que gostaria de selecionar: '))
if pagamento == 1:
  print(f'Você recebeu 10% de desconto.\nVALOR TOTAL À PAGAR: R${valor - (valor * 0.10) :.2f}')
elif pagamento == 2:
  print(f'Voce recebeu 5% de desconto.\nVALOR TOTAL À PAGAR: R${valor - (valor * 0.05) :.2f}')
elif pagamento == 3:
  print(f'Não houve nenhum desconto ou acréscimo.\nVALOR TOTAL À PAGAR: R${valor :.2f}')
elif pagamento == 4:
  print(f'Na forma de pagamento selecionada será acrescido 20% de juros.\nVALOR TOTAL À PAGAR: R${valor + (valor * 0.20) :.2f}')
else:
   print('OPÇÃO INVÁLIDA, tente novamente.')