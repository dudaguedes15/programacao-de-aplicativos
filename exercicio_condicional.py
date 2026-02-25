nome = input("Digite seu nome ")
altura = float(input("Digite sua altura "))

if altura < 1.50:
    print("Você não está liberado", nome)
elif altura >= 1.50:
    print("Acesso liberado! Divirta-se na queda livre", nome)