import sqlite3
from banco import criar_tabela_escola

def cadastrar():
    conexao = None
    try:
        conexao = sqlite3.connect("gestao_escolar.db")
        cursor = conexao.cursor()

        nome_escola = input("Digite o nome da escola: ")
        cidade_escola = input("Digite a cidade da escola: ")

        assert nome_escola != "", "O nome da escola não pode estar vazio."
        assert cidade_escola != "", "A cidade da escola não pode estar vazia."
        
        comando_inserir_escola = (f'''INSERT INTO escola (nome, cidade) values ('{nome_escola}', '{cidade_escola}')''')
        
        cursor.execute(comando_inserir_escola)
        conexao.commit()
        print("Cadastro realizado.")
    except sqlite3.IntegrityError as e:
        print(f"Esse ID não existe: {e}." )
    except ValueError:
        print("Digite um valor válido.")
    except Exception as e:
        print(e)
    finally:
        conexao.close()

def listar():
    try:
        conexao = sqlite3.connect('gestao_escolar.db')
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM escola")
        escola = cursor.fetchall()

        print("===== LISTA DE CADASTROS ESCOLA =====")
        
        for s in escola:
            print(f"ID {s[0]}")
            print(f"Nome da escola {s[1]}")
            print(f"Cidade da escola {s[2]}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}.")
    finally:
        conexao.close()
cadastrar()
listar()
    