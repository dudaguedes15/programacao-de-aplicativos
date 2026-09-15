def maior_numero():
    vetor = [15, 8, 32, 45, 12, 60, 25]

    maior = vetor[0]
    posicao = 0

    for i in range(1, len(vetor)):
        if vetor[1] > maior:
            maior = vetor[i]
            posicao = i

    print("Maior número:", maior)
    print("Posição:", posicao)

maior_numero()
