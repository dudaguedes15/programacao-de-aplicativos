nome = input("Qual o seu nome? ")
codigo = int(input("Qual o código secreto? "))
if nome == "admin" and codigo == 999:
    print("Acesso ao servidor liberado. Sistema online")
else:
    print("Falha na autenticação. Alerta de segurança ligado!")