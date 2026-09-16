numeros = list(range(1, 101))

valores = [10, 50, 90]


for valor in valores:

    # Busca sequencial

    comparacoes_sequencial = 0

    for i in range(len(numeros)):

        comparacoes_sequencial += 1

        if numeros[i] == valor:
            break


    # Busca binária

    inicio = 0
    fim = len(numeros) - 1

    comparacoes_binaria = 0

    while inicio <= fim:

        meio = (inicio + fim) // 2

        comparacoes_binaria += 1

        if numeros[meio] == valor:
            break

        elif numeros[meio] < valor:
            inicio = meio + 1

        else:
            fim = meio - 1


    print("\nValor procurado:", valor)
    print("Busca sequencial:", comparacoes_sequencial, "comparações")
    print("Busca binária:", comparacoes_binaria, "comparações")
