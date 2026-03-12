# REVISADO
print('======= ALUGUEL DE CARROS =======')
dias = int(input('DIAS ALUGADOS: '))
km = float(input('DISTÂNCIA PERCORRIDA(KM): '))
print(f'{dias} dia(s) de aluguel \n{km :.1f}KM percorridos \nValor total à pagar: R$ {(60 * dias) + (km * 0.15) :.2f}.')
