import json  #importa do python para json
import os #ve se o arquivo existe 

BANCO_DADOS = 'alunos.json' #isso é uma variável que guarda o nome do arquivo

def cadastrar(): #cria uma função
    print("\n--- Novo Cadastro ---")  #quebra a linha e mostra de um jeito organizado no terminal
    
    if os.path.exists(BANCO_DADOS):  #se existir um arquivo chamado banco_dados 
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f: #ele abre o arquivo banco_dados em modo de leitura, usando o utf-8 para conseguir usar acentuação, e coloca tudo isso como a variável f
            alunos = json.load(f)  #ele pega o que tem no arquivo f e transforma em um objeto python e guarda na variável alunos
    else: #se não existir um arquivo chamado banco_dados
        alunos = [] #ai ele cria uma nova lista

    novo_aluno = { #abre um dicionario que armazena os dados chamado 'novo_aluno'
        "nome": input("Nome: "), # da linha 16 até a linha 20 tem as chaves e os valores que estão dentro do objeto
        "telefone": input("Telefone: "),  # ex: "telefone" é a chave e o usuário que irá digitar o telefone é o valor
        "turma": input("Turma: "),
        "idade": int(input("Idade: ")),
        "cpf": input("CPF: ")
    }  # fecha o dicionário 
    
    alunos.append(novo_aluno)  #adiciona  o dicionario novo_aluno dentro da lista de alunos 

    with open(BANCO_DADOS, 'w', encoding='utf-8') as f:  #abre o arquivo de texto no modo de escrita para salvar as informações 
        json.dump(alunos, f, indent=4, ensure_ascii=False)   #salva a lista de alunos no formato json, mantendo o arquivo organizado com recuo e acentos
        
    print("Aluno cadastrado com sucesso!") #exibe essa mensagem no terminal avisando que o cadastro deu certo

def listar(): #mantem o foco na criação
    print("\n--- Lista de Alunos ---") #quebra a linha e deixa o terminal organizado
    
    if os.path.exists(BANCO_DADOS): #se existir um arquivo chamado banco_dados 
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f:  #ele abre o arquivo banco_dados em modo de leitura, usando o utf-8 para conseguir usar acentuação, e coloca tudo isso como a variável f
            alunos = json.load(f)  #ele pega o que tem no arquivo f e transforma em um objeto python e guarda na variável alunos
    else:  #se não existir um arquivo chamado banco_dados
        alunos = []  #ai ele cria uma nova lista

    if not alunos:  #se não tiver alunos 
        print("Nenhum aluno cadastrado.")  #mostrar no terminal uma mensagem que o aluno não foi cadastrado
        return  #ele encerra uma função

    for aluno in alunos: #percorre cada aluno dentro da lista
        print(f"ID: {aluno['id']} | Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}")  #essa linha pega os dados do objeto aluno e monta uma frase

def atualizar(): #mantem o foco na criação
    print("\n--- Atualizar Aluno ---") #quebra a linha e deixa o terminal organizado
    if not os.path.exists(BANCO_DADOS):  #se não existir o arquivo banco_dados 
        print("Nenhum aluno cadastrado no sistema.")  #mostrar no terminal que não tem alunos cadastrados no sistema
        return #encera um função

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f: #ele abre o arquivo banco_dados em modo de escrita, usando o utf-8 para conseguir usar acentuação, e coloca tudo isso como a variável f
        alunos = json.load(f)  #ele pega o que tem no arquivo f e transforma em um objeto python e guarda na variável alunos
        
    cpf_busca = int(input("Digite o CPF do aluno que deseja editar: ")) #aqui a pessoa digita o cpf para buscar ele 
    
    for aluno in alunos: #percorre cada aluno dentro da lista
        if aluno['cpf'] == cpf_busca: #ele percorre a lista aluno e ve se tem algum cpf igual ao cpf que a pessoa digitou em cpf_busca
            print(f"Editando dados de: {aluno['nome']}")
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome']
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone']
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma']
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade'])
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf']
            
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
                json.dump(alunos, f, indent=4, ensure_ascii=False)
            print("Dados atualizados com sucesso!")
            return
            
    print("Aluno não encontrado.")

def excluir():
    print("\n--- Excluir Aluno ---")
    if not os.path.exists(BANCO_DADOS):
        print("Nenhum aluno cadastrado no sistema.")
        return

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
        alunos = json.load(f)
        
    id_busca = int(input("Digite o ID do aluno que deseja remover: "))
    
    nova_lista = [a for a in alunos if a['id'] != id_busca]
    
    if len(nova_lista) < len(alunos):
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
            json.dump(nova_lista, f, indent=4, ensure_ascii=False)
        print("Aluno removido com sucesso!")
    else:
        print("Aluno não encontrado.")

def menu():
    if not os.path.exists(BANCO_DADOS):
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
            json.dump([], f)

    while True:
        print("\n=== SISTEMA ESCOLAR ===")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Aluno")
        print("4. Excluir Aluno")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1': cadastrar()
        elif opcao == '2': listar()
        elif opcao == '3': atualizar()
        elif opcao == '4': excluir()
        elif opcao == '5': break
        else: print("Opção inválida!")

menu()