print('Mz Garage & Stock')
valor = float(input('Qual o valor total à ser pago? '))
formapag = str(input('Qual a forma de pagamento? ')).lower().strip()
if formapag in ["dinheiro" , "cheque" , "pix"]:
   print(f'À vista no {formapag} você recebe 10% de desconto.\nSua compra ficou no valor de R$ {valor - (valor * 0.10) :.2f}.')
elif formapag in ["1x" , "cartão 1x" , "1x no cartão" , "à vista no cartão" , "a vista no cartão"]:
   print(f'Para pagamento à vista no cartão, você recebe 5% de desconto. \nSua compra ficou no valor de R$ {valor - (valor * 0.05) :.2f}.')
elif formapag in ["2x no cartão" , "cartão em 2x" , "cartão 2x" , "2x"]:
   print(f'Em 2x no cartão, não tem acréscimo. \nSua compra ficou no valor de R$ {valor :.2f}.')
else:
   print(f'Parcelado no cartão à partir de 3x, tem um acréscimo de 20%. \nSua compra ficou no valor de R$ {valor + (valor * 0.20) :.2f}.')
