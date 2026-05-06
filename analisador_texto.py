def contar_caracteres(palavra):
    while len(palavra) <5:
        print("Nome de usuário muito curto")
        palavra = input("Digite o seu nome de usuário novamente: ")
    print( "Nome aceito")
    
nome_de_usuario = input("Digite o nome de usuário: ")
contar_caracteres(nome_de_usuario)