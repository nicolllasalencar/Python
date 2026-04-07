print('-'*50)
print('CALCULADORA DE MÉDIA DE NOTAS')
print('-'*50)

soma = 0
quantidade = 0

while True:
    nota = float(input('Digite uma nota (ou -1 para finalizar): '))

    if nota == -1:
        break

    soma += nota
    quantidade += 1

if quantidade > 0:
    media = soma / quantidade

    print('-'*50)
    print('Quantidade de notas:', quantidade)
    print('Média final: {:.2f}'.format(media))

    if media >= 7:
        print('Situação: APROVADO')
    elif media >= 5:
        print('Situação: RECUPERAÇÃO')
    else:
        print('Situação: REPROVADO')

else:
    print('Nenhuma nota foi digitada.')

print('-'*50)