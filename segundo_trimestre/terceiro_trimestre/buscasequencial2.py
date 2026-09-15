def contar_valor():
    vetor = [10, 20, 10, 30, 10, 40, 50, 10]

    numero = 0

    for i in range(len(vetor)):
        if vetor[i] == numero:
            contador += 1

    print("O número aparece", contador, "vezes.")

contar_valor()