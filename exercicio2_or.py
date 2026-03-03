media = float(input("Digite a sua média "))
renda = float(input("Digite a sua renda "))
escola = input("Você veio de escola publica? S/N: ")

if media >= 8.0 and (renda < 2.000 or escola == "S"):
    print("Ganhou a bolsa")
else:
    print("Não atendeos requisitos.")