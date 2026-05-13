def criar_arquivo():
    open ('viagem.txt','w').close()

def criar():
    nome = input("Adicione o seu destino: ")
    with open('viagem.txt', 'a') as f:
        f.write(nome + '\n')
    print("Local adicionado!")

def ler():
    with open('viagem.txt', 'r') as f:
        viagens = f.readlines()

        i = 0
        for viagem in viagens:
            print(f"{i} - {viagem.strip()}") 
            i += 1 

def atualizar():
    ler() 
    idx = int(input("Digite o ID do local que deseja alterar: "))
    novo_nome = input("Novo local: ")

    with open('viagem.txt', 'r') as f:
        linhas = f.readlines()

    linhas[idx] = novo_nome + '\n'

    with open('viagem.txt', 'w') as f:
        f.writelines(linhas)
    print("Local atualizado!")

def deletar():
    ler()
    idx = int(input("Digite o ID do local que deseja excluir: "))

    with open('viagem.txt', 'r') as f:
        linhas = f.readlines()

    del linhas[idx]

    with open('viagem.txt', 'w') as f:
        f.writelines(linhas)
    print("Local removido!")

while True:
    print("\n1-Adicionar local | 2-Listar | 3-Editar | 4-Excluir | 5-Sair")
    opcao = input("Escolha: ")

    if opcao == '1': criar()
    elif opcao == '2': ler()
    elif opcao == '3': atualizar()
    elif opcao == '4': deletar()
    elif opcao == '5': break






open ("viagens.txt", 'w') . close ()

def adicionar ():
    lugar = input("Sugere um lugar: ")
    with open("viagens.txt", 'a') as arquivo:
        arquivo.write(lugar + '\n')
        print("Lugar adicionado! ")


def ler():
    with open ("viagens.txt", 'r') as arquivo:
        viagens = arquivo.readlines()

    soma = 0
    for viagem in viagens:
        print(f"{soma} - {viagem.strip()}")
        soma += 1

def editar():
    ler()
    editar_destino = input("Digite o destino que deseja alterar: ")
    novo_destino = input("Digite o novo destino: ")

    with open("viagens.txt", 'r') as arquivo:
        linhas = arquivo.readlines()

    editar_destino = novo_destino + '\n'
    with open("viagens.txt", 'w') as arquivo:
        arquivo.writelines(linhas)
        print("lugar atualizado atualizado! ")

def deletar():
    ler()
    destino = input("Digite o nome do destino que deseja excluir: ")
    with open("viagens.txt", 'r') as arquivo:
        linhas = arquivo.readlines()
    del linhas[destino]
    with open("viagens.txt", 'w') as arquivo:
        arquivo.writelines(linhas)
        print("Aluno removido! ")

while True:
    print("------PLANEJADOR DE VIAGENS--------")
    print(" 1-Cadastrar | 2-Ler | 3-Editar |4-Deletar | 5-Encerrar sessão") 
    opcao = input("Digite a opção desejada: ")
    if opcao == '1': adicionar()
    elif  opcao == '2': ler()
    elif opcao == '3': editar()
    elif opcao == '4': deletar()
    else:
        print("Saindo do programa! ")
