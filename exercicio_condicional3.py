valor_total = float(input("Digite o valor total da compra: "))
cupom = input("Digite o nome do cupom: ")

if cupom == "DEV10":
    desconto = valor_total - (0.10 * valor_total)
    print("O valor a ser pago é:", desconto)
else:
    print("Dados invalidos.")