opcao = int(input("1 - Café\n2 - Chá\n3 - Suco\nEscolha o seu pedido: "))
match opcao:
    case  1:
        pedido = "Café"
    case  2:
        pedido = "Chá"
    case  3:
        pedido = "Suco"
    case _:
        pedido = "uma opção inexistente."
print("Você escolheu", pedido)