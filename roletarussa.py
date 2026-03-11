senha = "admin123"
tentativa = int(input("Qual a tentativa ?: "))
insenha = input("Qual a senha ?: ")
token = input("Possui token ?(s/n):")
if insenha == senha and (tentativa % 3 == 0 or token == "s"):
    print(f"Tentativa nº{tentativa}: ACESO CONCEDIDO. ")
else:
    print(f"Tentativa nº{tentativa}: ACESSO BLOQUEADO POR PROTOCOLO.")