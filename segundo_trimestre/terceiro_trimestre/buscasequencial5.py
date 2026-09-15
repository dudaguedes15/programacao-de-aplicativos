def primeira_ultima_posicao():
    vetor = [5, 10, 20, 10, 30, 10, 40, 50]

    numero = int(input("Digite o número: "))

    primeira = -1
    ultima = -1

    for i in range(len(vetor)):
        if vetor[i] == numero:

            if primeira == -1:
                primeira = i

            ultima = i

    if primeira != -1:
        print("Primeira posição: ", primeira)
        print("Última posição: ", ultima)
    else:
        print("Número não encontrado!")

primeira_ultima_posicao()
