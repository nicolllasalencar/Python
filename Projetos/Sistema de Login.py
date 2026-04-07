print('-'*50)
print('SISTEMA DE LOGIN')
print('-'*50)

usuario_correto = "admin"
senha_correta = "1234"

usuario = input('Digite o usuário: ')
senha = input('Digite a senha: ')

if usuario == usuario_correto and senha == senha_correta:
    print('Acesso PERMITIDO')
else:
    print('Acesso NEGADO')

print('-'*50)