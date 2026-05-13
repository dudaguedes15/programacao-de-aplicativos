print("\n----SISTEMA CRUD MODULARIZADO----")

estoque = []
usuario = 0

def adicionar_produto(nome, estoque):
    estoque.append(nome)

def listar_produtos(estoque):
    for item in estoque:
        indice = estoque.index(item)
        print(f"\nPosição do produto:{indice}, Nome do produto:{item}")

def atualizar_produto(nome, novo_nome, estoque):
    indice = estoque.index(nome)
    estoque[indice] = novo_nome

def remover_produto(nome, estoque):
    indice = estoque.index(nome)
    estoque.pop(indice)


def exibir_menu(usuario):
    while usuario != 5:
        print("\n1-Adicionar produtos ao estoque")
        print("2-Listar produtos")
        print("3-Atualizar produtos")
        print("4-Remover produtos")
        print("5-Sair")

        usuario = int(input("\nDigite a opção que deseja: "))
        
        if usuario == 1:
            nome = input("\nDigite o produto que deseja adicionar ao estoque: ")
            adicionar_produto(nome, estoque)
        
        elif usuario == 2:
            listar_produtos(estoque)

        elif usuario == 3:
            nome = input("\nDigite o produto que deseja remover: ")
            novo_nome = input("\nDigite o produto que deseja adicionar: ")
            atualizar_produto(nome, novo_nome, estoque)

        elif usuario == 4:
            nome = input("\nDigite o produto que deseja remover: ")
            remover_produto(nome, estoque)

        elif usuario == 5:
            print("\nEncerrando programa...")
            break

exibir_menu(usuario)