print('-'*50)
print('CALCULADORA')
print('-'*50)

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

print('Escolha a operação:')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')

opcao = int(input('Digite a opção: '))

if opcao == 1:
    resultado = num1 + num2
    print(f'Resultado: {resultado}')
elif opcao == 2:
    resultado = num1 - num2
    print(f'Resultado: {resultado}')
elif opcao == 3:
    resultado = num1 * num2
    print(f'Resultado: {resultado}')
elif opcao == 4:
    if num2 != 0:
        resultado = num1 / num2
        print(f'Resultado: {resultado}')
    else:
        print('Erro: divisão por zero')
else:
    print('Opção inválida')

print('-'*50)