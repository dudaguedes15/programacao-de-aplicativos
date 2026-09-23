letra = input("Digite uma letra para ver se é uma vogal: ")
match letra:
    case "a"|"e"|"i"|"o"|"u":
        print("É vogal.")
    case _:
        print("Não é vogal")