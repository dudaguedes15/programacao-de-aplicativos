import sqlite3

def cadastrar_sociedades():
    try:
        conexao = sqlite3.connect('sistema_escritorio_adv.db')
        cursor = conexao.cursor()

        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS sociedades_advogados (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nome_banca TEXT NOT NULL,
                    registro_oab_juridico) 
                    ''') 
        nome_banca = input("Digite o nome da banca: ")
        registro_oab_juridico = int(input("Digite seu registro OAB: "))
        
        comando_inserir_sociedades_advogados = (f'''INSERT INTO sociedades_advogados (nome_banca, registro_oab_juridico) values ('{nome_banca}', '{registro_oab_juridico}')''')



        print("Cadastro realizado.")

    except sqlite3.IntegrityError as e:
        print(f"Esse ID não existe: {e}." )
    except ValueError:
        print("Digite um valor válido.")
    except Exception as e:
        print(e)
    finally:
        conexao.close()    


def listar_sociedade():
    try:
        conexao = sqlite3.connect('sistema_escritorio_adv.db')
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM sociedades_advogados")
        sociedades_advogados = cursor.fetchall()

        print("===== LISTA DE CADASTROS SOCIEDADES DE ADVOGADO =====")

        for s in sociedades_advogados:
            print(f"ID {s[0]}")
            print(f"Nome da banca {s[1]}")
            print(f"registro_oab_juridico {s[2]}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}.")
    finally:
        conexao.close()
    


def atualizar_sociedades():
    try:
        conexao = sqlite3.connect('sistema_escritorio_adv.db')
        cursor = conexao.cursor()

        print("===== ATUALIZAR SOCIEDADES =====")
        id_sociedades = int(input(" Qual seu ID: "))

        cursor.execute(f'''SELECT * FROM sociedades_advogados WHERE id = {id_sociedades}''')
        
        s = cursor.fetchone()

        if not s:
            print("Não encontrado.")
        else: 
            print(f"Nome atual da banca: {s[1]}")
            print(f"Registro oab atual: {s[2]}")
            

            nome_atualizado = input("Digite novo nome: ")
            registro_atualizado = int(input("Digite o novo registro de oab: "))

            cursor.execute(f'''UPDATE sociedades_advogados
                                    SET nome_banca = '{nome_atualizado}', registro_oab_juridico = '{registro_atualizado}'
                                WHERE id = {id_sociedades}   ''')
            conexao.commit()
            print("Sociedade atualizada com sucesso.")
    except ValueError:
        print("Erro de valor no cadastro tente novamente")
    except TypeError:
        print("Erro de tipo de dados")
        print(f"Ocorreu um erro: {e}.")
    finally:
        conexao.close() 

def excluir_sociedades():
    try:
        conexao = sqlite3.connect('sistema_escritorio_adv.db')
        cursor = conexao.cursor()
        listar_sociedade()

        id_sociedades = int(input("Digite o ID do cadastro que você deseja deletar: "))

        cursor.execute(f'''DELETE FROM sociedades_advogados WHERE id = {id_sociedades}''')

        conexao.commit()
        print("Sociedade excluida.")
        conexao.close()
    except ValueError:
        print("Erro de valor no cadastro tente novamente")
    except TypeError:
        print("Erro de tipo de dados")
    except Exception as e:
        print(f"Ocorreu um erro: {e}.")
    finally:
        conexao.close()

