import sqlite3

def cadastrar_filiais():
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
    

def cadastrar_filiais():
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