estado = input("Digite uma sigla de um estado da região sul(PR, SC ou RS): ")
match estado:
    case "PR":
        print("Paraná")
    case "SC":
        print("Santa Catarina")
    case "RS":
        print("Rio Grande do Sul")
    case _ :
        print("Inválido ou não é da região sul.")