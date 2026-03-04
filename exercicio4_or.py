valorcompra = float(input("Digite o valaor da sua compra: "))
prime = input("Você é prime? S/N ")
frete = 50.00
if valorcompra > 500.00 or (prime == "S" and valorcompra > 100.00):
    frete = 00.00 
    print("Você ganhou frete gratis")
    valor_total = valorcompra + frete 
    print("o valor total é", valorcompra + frete)
else:
    frete = 50.00
    valor_total = valorcompra + frete 
    print("voce nao ganhou frete gratis")
    print("o seu valor total é", valorcompra)