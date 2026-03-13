#Aplicar aumento em porcentagem de um salário
print('-' * 100)
sal = float(input('Digite o valor do salário em R$:'))
aumento_porcentagem = float(input('Digite o valor do aumento em %:'))
aumento_valor = sal * aumento_porcentagem / 100
resultado = sal + aumento_valor
print('com aumento de {}% o salário de R${} foi para {:.2f}'.format(aumento_porcentagem,sal,resultado,))
print('-' * 100)