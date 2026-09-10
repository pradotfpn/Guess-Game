# programa de inserir usuário com senha
nome = input('Digite seu nome de usuário:')
senha = input('Digite sua senha: ')
while senha == nome:
    print("Sua senha não pode ser o mesmo nome de usuário!")
    senha = input("Digite novamente sua senha: ")
print(f"Nome:{nome}\nSenha: {senha}")