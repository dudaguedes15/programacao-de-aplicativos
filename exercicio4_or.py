valorcompra = float(input("Digite o valaor da sua compra: "))
prime = input("Você é prime? S/N")

if valorcompra > 500.00 or (prime == "S" and valorcompra > 100.00):
    frete = 00.00 
    print("Você ganhou frete gratis")
    valorcompra + frete 
    print("o valor total é", valorcompra + frete)
else:
    frete = 50.00
    valorcompra + frete 
    print("voce nao ganhou frete gratis")