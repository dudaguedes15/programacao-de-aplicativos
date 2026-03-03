nome = input("Digite o seu noem: ")
usuario = input("Qual o seu usuario? ")
senha = int(input("Digite a senha: "))

if (usuario == "Admin" or usuario == "Root") and senha == 12345:
    print("acesso liberado")
else:
    print("acesso negado")