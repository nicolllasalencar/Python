#fazer a tábua formatada a partir de um número inteiro digitado.
num = int(input('Digite um número para ver sua tabuada: '))
print('_' * 12)
print('{0} x 01 = {1}\n{0} x 02 = {2}\n{0} x 03 = {3}\n{0} x 04 = {4}\n{0} x 05 = {5}\n{0} x 06 = {6}\n{0} x 07 = {7}\n{0} x 08 = {8}\n{0} x 09 = {9}\n{0} x 10 = {10}'
.format(num, num*1, num*2, num*3, num*4, num*5, num*6, num*7, num*8, num*9, num*10))
print('_' * 12)