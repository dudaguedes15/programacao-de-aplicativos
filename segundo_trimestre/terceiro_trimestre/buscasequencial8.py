palavras = ["abacaxi", "banana", "cachorro", "casa", "escola", "gato", "livro", "mesa"]

palavra = input("Digite a palavra que deseja procurar: ")

inicio = 0
fim = len(palavras) - 1

comparacoes = 0
encontrou = False

while inicio <= fim:

    meio = (inicio + fim) // 2

    comparacoes += 1

    if palavras[meio] == palavra:
        encontrou = True
        break

    elif palavras[meio] < palavra:
        inicio = meio + 1

    else:
        fim = meio - 1


if encontrou:
    print("A palavra foi encontrada.")
    print("Quantidade de comparações:", comparacoes)
else:
    print("A palavra não foi encontrada.")
    print("Quantidade de comparações:", comparacoes)
