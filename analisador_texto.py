def contar_caracteres(palavra):
    return len(palavra)

nome_de_usuario = input("Digite o nome de usuário: ")
while contar_caracteres < 5:
    print("Nome de usuário muito curto")
else:
    print( "Nome aceito")