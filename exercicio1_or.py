cliente = int(input("Digite sua idade: "))
vip = input("Você tem ingresso? S/N ")
lista_convidados = input("Você está na lista? S/N ")

if cliente >= 18 and (vip == "S" or lista_convidados == "S"):   
    print("Seja bem vindo")
