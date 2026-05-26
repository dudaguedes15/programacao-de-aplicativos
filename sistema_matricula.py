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
            print(f"Editando dados de: {aluno['nome']}") #vai mostrar a mensagem no termianl falando o nome do aluno que foi encontrado, confirmando que ele esta alterando a pessoa certa
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome'] #pede um novo nome de aluno
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone'] #pede um novo telefone 
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma'] #pede uma nova turma
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade']) #pede uma nova idade
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf'] #pede um novo cpf
            
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f:   #Essa linha abre o arquivo do meu bande dados no modo de escrita ('w'),
                json.dump(alunos, f, indent=4, ensure_ascii=False)  #salvar a lista alunos em formato json, atendendo o arquivo e organizando
            print("Dados atualizados com sucesso!") #mostra a mensagem no terminal
            return   #Essa linha encerra a execução da função imediatamente e volta para o ponto onde ela foi chamada
            
    print("Aluno não encontrado.") #mostra essa mensagem no terminal

def excluir(): #mantem o foco na criação
    print("\n--- Excluir Aluno ---") #quebra a linha e deixa o terminal organizado
    if not os.path.exists(BANCO_DADOS): #se não existir o arquivo banco_dados
        print("Nenhum aluno cadastrado no sistema.") #mostrar no terminal que não tem alunos cadastrados no sistema
        return  #encera um função

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:  #ele abre o arquivo banco_dados em modo de escrita, usando o utf-8 para conseguir usar acentuação, e coloca tudo isso como a variável f
        alunos = json.load(f)  #ele pega o que tem no arquivo f e transforma em um objeto python e guarda na variável alunos
        
    id_busca = int(input("Digite o ID do aluno que deseja remover: ")) #aqui a pessoa digita o id para buscar ele 
    
    nova_lista = [a for a in alunos if a['id'] != id_busca] # cria uma nova lista onde vai adicionar um novo id e o outro vai ser excluido 
    
    if len(nova_lista) < len(alunos): # o if cria uma nova função e dentro dela tem o len e ele conta quantas pessoas tem dentro da nova_lista 
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:  # abre o arquivo banco_dados em modo de escrita, usando o utf-8 para conseguir usar acentuação
            json.dump(nova_lista, f, indent=4, ensure_ascii=False) # salva a lista de alunos no formato json, mantendo o arquivo organizado com recuo e acentos
        print("Aluno removido com sucesso!")   # mostra essa mensagem no terminal quando remover um aluno
    else:   # se a opção não existir vai para o else
        print("Aluno não encontrado.") # mostra essa mensagem se não encontrar aluno cadastrado

def menu():  # de cria a função, e o nome da função(menu) onde a função vai executar comando
    if not os.path.exists(BANCO_DADOS):   # o comando if not verifica se o arquivo existe ou não dentro da variável
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:   # abre o arquivo banco_dados em modo de escrita, usando o utf-8 para conseguir usar acentuação
            json.dump([], f)  # o json.dump aqui armazena uma lista vazia ([]) no arquivo representado por f

    while True:   # laço de repetição que faz ele executar todas as opções
        print("\n=== SISTEMA ESCOLAR ===")  #mostra a mensagem, quebra a lista e começa a mostrar as opções
        print("1. Cadastrar Aluno")  #print com a priemira opção
        print("2. Listar Alunos")  #print com a segunda opção
        print("3. Atualizar Aluno")  #print com a terceira opção
        print("4. Excluir Aluno")  #print com a quarta opção
        print("5. Sair")  #ultimo print para sair das opções
        
        opcao = input("Escolha uma opção: ")  # uma nova variavel, com o input para armazenar ela e para o usuário digitar uma das opções do print
        
        if opcao == '1': cadastrar()  #o if cria uma função para o cadastro
        elif opcao == '2': listar()  #o elif cria outra função igual a opção para listar
        elif opcao == '3': atualizar()#o elif cria oura função igual para atualizar
        elif opcao == '4': excluir()   #o elif cria outra função igual a opção para excluir
        elif opcao == '5': break  #o break serve para quebrar o loop
        else: print("Opção inválida!") #cria um else já com a mensagem e com a opção inválida

menu() #criada para mostrar o menu no terminal