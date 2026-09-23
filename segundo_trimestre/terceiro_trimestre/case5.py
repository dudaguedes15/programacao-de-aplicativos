numeroum = int(input("Digite o primeiro numero da conta: "))
numerodois = int(input("Digite o segndo numero da conta: "))
operacao = input("Digite a operação desejada(+ ou -): ")
match operacao:
    case "+":
        resultado = numeroum + numerodois
    case "-":
        resultado = numeroum - numerodois
    case _:
        resultado = "Operação inválida"
print(resultado)