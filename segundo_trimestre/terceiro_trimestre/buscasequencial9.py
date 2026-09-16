numeros = [10, 20, 30, 40, 50, 60, 70]

novo_numero = int(input("Digite o número que deseja inserir: "))

inicio = 0
fim = len(numeros)

while inicio < fim:

    meio = (inicio + fim) // 2

    if numeros[meio] < novo_numero:
        inicio = meio + 1

    else:
        fim = meio


print("O número deve ser inserido na posição:", inicio)

numeros.insert(inicio, novo_numero)

print("Lista ordenada:")
print(numeros)