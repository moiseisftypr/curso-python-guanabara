sexo = ''
while sexo not in ["M", "F"]:
  sexo = str(input('SEXO [M/F]: ')).upper().strip()
  if sexo not in ["M", "F"]:
   print('ERRO! Digite novamente.')
print('PRONTO! Registrado.')