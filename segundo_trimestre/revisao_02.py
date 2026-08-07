import sqlite3

def cadastrar():
    try:
        conexao = sqlite3.connect('sistema_cinema.db')
        cursor = conexao.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS cinemas(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    shopping TEXT   )
                    
                    ''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS salas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                numero_sala TEXT NOT NULL,
                capacidade TEXT,
                id_cinemas INTEGER,
                FOREIGN KEY(id_cinemas) REFERENCES cinemas(id)
                )
                ''')

        nome_cinema = input("Digite o nome do cinema: ")
        shopping = input("Digite o nome do shopping: ")
        numero_sala = int(input("Digite o número da sala: "))
        capacidade = input("Digite a capacidades da sala: ")
        id_cinemas = int(input("Digite o ID do cinema: "))

        comando_inserir_cinemas = f'''INSERT INTO cinemas (nome, shopping) values ('{nome_cinema}', '{shopping}')'''
        comando_inserir_salas = f'''INSERT INTO salas (numero_sala, capacidade, id_cinemas) values ('{numero_sala}', '{capacidade}', {id_cinemas})'''

        cursor.execute(comando_inserir_cinemas)
        cursor.execute(comando_inserir_salas)


        conexao.commit()
        print("Médico cadastrado.")
        
    except sqlite3.IntegrityError as e:
        print(f"Cadastro já realisado: {e}." )
    except ValueError:
        print("Digite um valor válido.")
    except Exception as e:
        print(e)
    finally:
        conexao.close()



def listar():
    try: 
        conexao = sqlite3.connect('sistema_cinema.db')
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM salas")
        salas = cursor.fetchall()

        print("===== LISTA DE SALAS ===")

        for sala in salas:
            print
            print(f"ID: {sala[0]}")
            print(f"Número da sala: {sala [1]}")
            print(f"Capacidade de pessoas: {sala[2]}")
            print(f"ID do cinema: {sala[3]}")
            print("-" * 30)

    except Exception as e:
        print(f"Ocorreu um erro: {e}.")
    finally:
        conexao.close()

def menu():
    try:
        opcao = 0
        while opcao != 5:

            print("-------------------- MENU ------------------")
            print("-- 1 Cadastrar cinema -- 2 Listar salas -- 3 Fechar programa -- ")
            opcao = int(input("Digite o que você deseja fazer: "))
        
            if opcao == 1:
                cadastrar()
            elif opcao == 2:
                listar()
            elif opcao == 3:
                print("---------- PROGRAMA ENCERRADO ----------")
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