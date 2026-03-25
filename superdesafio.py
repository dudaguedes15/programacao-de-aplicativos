livros_disponiveis = ["Python Pro", "Banco de Dados", "Redes", "IA", "Hardware"]
livros_emprestados = [] 
livro = input("Digite o nome do livro que você deseja: ")

if livro in livros_disponiveis:

    posicao = livros_disponiveis.index(livro)
    livros_disponiveis.remove(livro)
    livros_emprestados.append(livro)
    print("Empréstimo realizado com sucesso!")
else:
    print("Desculpe, este livro não está no acervo.")

devolucao = input("Digite o nome do livro que você está com você: ")

if devolucao in livros_emprestados:
    livros_emprestados.remove(devolucao)
    livros_disponiveis.append(devolucao)
else:
    print("Este livro não consta como emprestado.")

del livros_disponiveis[0:2]
print(livros_disponiveis)
print(livros_emprestados)