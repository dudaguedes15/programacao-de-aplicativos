def busca_sequencial():
    vetor = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    numero = int(input("Digite o número que deseja procurar: "))

    for i in range(len(vetor)):
        if vetor[i] == numero:
            print("Número encontrado no índice:", i)

    print("Número não encontrado!")
