mes = int(input("Digite um numero de 1 a 12 para mostrar a estação correspondente: "))
match mes:
    case 12|1|2:
        print("Verão")
    case 3|4|5:
        print("Outono")
    case 6|7|8:
        print("inverno")
    case 9|10|11:
        print("primavera")
    case _:
        print("Mes nao encontrado.")