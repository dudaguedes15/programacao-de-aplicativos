cliente = input("Digite o seu nome: ")
valortotal = float(input("Digite o valor total da compra: "))
distancia = int(input("Digite a distância em km: "))
cupom = input("Você deseja cumpom? S ou N: " )
frete = 40.00
TOTAL = 0.00

if valortotal >= 1000.00 and cupom == "S":
    desconto = 0.20 * valortotal
    total = valortotal - desconto
    print("Parabéns! Você ganhou um Mouse pad Gamer de brinde!")
elif valortotal > 500.00 and valortotal < 1000.00 and cupom == "S":
    desconto = 0.10 * valortotal
    total = valortotal - desconto


if distancia <= 50 and total >= 200.00:
    frete = 0.00 
    valorfinal = total + frete 
else: 
    valorfinal = total + frete

    print("Nome do cliente:", cliente)
    print("Valor original", valortotal)
    print("valor do desconto aplicado", desconto)
    print("Total Final a pagar", valorfinal)