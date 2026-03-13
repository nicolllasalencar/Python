#aplicar desconto em um produto e mostrar o quanto foi descontado
print('-'*100)
valor = float(input('Digite o valor do produto em R$:'))
porcentagem_desconto = float(input('Digite o valor do desconto em %:'))
desconto = valor*porcentagem_desconto / 100
resultado = valor - desconto
print('o valor de {}R$ com o desconto de {}% caiu para {:.2f}R$\nfoi descontado {}R$ do valor inicial do protudo'.format(valor,porcentagem_desconto,resultado,desconto))
print('-'*100)