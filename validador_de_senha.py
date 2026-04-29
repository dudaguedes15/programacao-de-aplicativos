def senha_valida(senha):
    while len(senha) < 6:
        print("Senha invalida!")
        senha = input("Digite a sua senha novamente: ")
    if len(senha) >= 6:
        print("Senha cadastratada com sucesso!")

validar_senha = input("Digite sua senha: ")
senha_valida(validar_senha)