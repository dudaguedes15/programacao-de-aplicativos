import sqlite3

def cadastrar():
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
        
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS filiais_regionais(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    estado_uf TEXT,
                    id_sociedades INTEGER,
                    FOREIGN KEY (id_sociedades) REFERENCES sociedades_advogados (id))
                    ''')

        
        nome_banca = input("Digite o nome da banca: ")
        registro_oab_juridico = int(input("Digite seu registro OAB: "))
        estado_uf = input("Digite o estado da filial: ")
        id_sociedades = int(input("Digite o id da sociedade de advogados: "))

        comando_inserir_sociedades_advogados = (f'''INSERT INTO sociedades_advogados (nome_banca, registro_oab_juridico) values ('{nome_banca}', '{registro_oab_juridico}')''')
        comando_inserir_filiais_regionais = (f'''INSERT INTO filiais_regionais (estado_uf, id_sociedades) values ('{estado_uf}', '{id_sociedades}') ''')

        cursor.execute(comando_inserir_sociedades_advogados)
        cursor.execute(comando_inserir_filiais_regionais)
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

def listar_filiais():
    try:
        conexao = sqlite3.connect('sistema_escritorio_adv.db')
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM filiais_regionais")
        filiaias_regionais = cursor.fetchall()

        print("===== LISTA DE CADASTROS FILIAIS =====")

        for f in filiaias_regionais:
            print(f"ID {f[0]}")
            print(f"Estado UF {f[1]}")
            print(f"ID sociedades {f[2]}")
            print("-" * 30)

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

def atualizar_filiais():
    try:
        conexao = sqlite3.connect('sistema_escritorio_adv.db')
        cursor = conexao.cursor()

        print("===== ATUALIZAR FILIAIS =====")

        id_filiais = int(input(" Qual seu ID: "))

        cursor.execute(f'''SELECT * FROM filiais_regionais WHERE id = {id_filiais}''')
        f = cursor.fetchone()

        if not f:
            print("Não encontrado.")
        else:
            print(f"Estado atual: {f[1]}")
            print(f"Id sociedades atual: {f[2]}")

            estado_atualizado = input("Digite o novo eestado: ")
            id_sociedades_atualizado = int(input("Digite o novo ID: "))

            cursor.execute(f'''UPDATE filiais_regionais
                                            SET estado_uf = '{estado_atualizado}',
                                                id_sociedades = '{id_sociedades_atualizado}'
                                            WHERE id = {id_filiais}''')

            cursor.execute(f'''UPDATE filiais_regionais
                                    SET estado_uf = '{estado_atualizado}'
                                WHERE id_sociedades = '{id_sociedades_atualizado}'
                                    ''')
            conexao.commit()
            print("Filial atuzalizada com sucesso.")
    except ValueError:
        print("Erro de valor no cadastro tente novamente")
    except TypeError as e:
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

def excluir_filiais():
    try:
        conexao = sqlite3.connect('sistema_escritorio_adv.db')
        cursor = conexao.cursor()
        listar_filiais()

        id_filiais = int(input("Digite o ID do cadastro que você deseja deletar: "))

        cursor.execute(f'''DELETE FROM filiais_regionais WHERE id = {id_filiais}''')

        conexao.commit()
        print("Filial excluida.")
        conexao.close()
    except ValueError:
        print("Erro de valor no cadastro tente novamente")
    except TypeError:
        print("Erro de tipo de dados")
    except Exception as e:
        print(f"Ocorreu um erro: {e}.")
    finally:
        conexao.close()

def menu():
    try:
        opcao = 0
        while opcao != 8:
            print("\n")
            print("-------------------- MENU ------------------")
            print("-- 1 Cadastrar sociedades e filiais -- 2 Listar sociedade -- 3 Listar filiais --  4 Atualizar sociedades -- 5 Atualizar filiais -- 6 Excluir sociedades -- 7 Excluir filiais -- 8 Fechar programa --")
            opcao = int(input("Digite o que você deseja fazer: "))

            if opcao == 1:
                cadastrar()
            elif opcao == 2:
                listar_sociedade()
            elif opcao == 3:
                listar_filiais()
            elif opcao == 4:
                atualizar_sociedades()
            elif opcao == 5:
                atualizar_filiais()
            elif opcao == 6:
                excluir_sociedades()
            elif opcao == 7:
                excluir_filiais()
            elif opcao == 8:
                print("===== PROGRAMA ENCERRADO =====")
                break
            else: 
                print("Opção inválida.")
        
    except ValueError:
        print("Erro de valor no cadastro tente novamente")
    except TypeError:
        print("Erro de tipo de dados")
   
    except Exception as e:
        print(f"Ocorreu um erro: {e}.")        

menu()