#algoritimo que leia um número e mostre seu dobro seu triplo e raiz quadrada
n = float(input('digite um número:'))
nx2 = n*2
nx3 = n*3
raiz = n**(1/2)
print('O dobro é:{}\nO triplo é:{}\nA raiz quadrada é {:.3f}'.format(nx2,nx3,raiz))
