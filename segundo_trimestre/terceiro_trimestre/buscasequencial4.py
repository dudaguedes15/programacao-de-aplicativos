def buscar_aluno():
    alunos = ["Ana", "Carlos", "João", "Maria", "Pedro"]

    nome = input("Digite o nome do aluno: ")

    encontrado = False

    for i in range(len(alunos)):
        if alunos[i] == nome:
            encontrado = True
            break

    if encontrado:
        print("Aluno encontrado!")
    else:
        print("Aluno não encontrado!")

buscar_aluno()
