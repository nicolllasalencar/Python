#converta de real para dolar (US$:1,00 = R$:5,15)
real = float(input('Quantos R$ você tem?:'))
dolar = real / 5.15
print('seus R${0}, são US${1:.3}'.format(real,dolar))