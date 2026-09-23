nota = input("Digite sua nota, de A a F: ")
match nota:
    case "A" | "B":
        print("Excelente Desempenho.")
    case "C" | "D":
        print("Desempenho Mediano.")
    case "E" | "F":
        print("Reprovado.")
    case _:
        print("Conceito inválido.")