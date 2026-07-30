import sqlite3


def inserir_escola(nome): 
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor() 
    cursor.execute(f"INSERT INTO escolas (nome) VALUES {nomee}")
    conexao.commit() 

nome = input("Digite o nome da escola: ")
inserir_escola(nome)

# A conexão deve ser criada dentro da função para evitar problemas em projetos com vários módulos.