# REVISADO
print('=========== EMPRESTIMO BANCÁRIO ===========')
casa = float(input('VALOR DO IMÓVEL(R$): '))
renda = float(input('RENDA ATUAL(R$): '))
anos = int(input('QUANTO TEMPO P/ QUITAÇÃO(ANOS): '))
parcela = casa / (anos * 12)
limite = renda * 0.30
if parcela > limite:
 print(f'EMPRÉSTIMO NEGADO!\nA prestação(R${parcela :.2f}) estimada excede 30% da sua renda atual(R${renda :.2f}), sendo um dos percalços para a não aceitação.')
else:
  print(f'EMPRÉSTIMO ACEITO!\nValor da prestação(mensal): R${parcela :.2f}\nPrazo p/ quitação(meses): {anos * 12}')
