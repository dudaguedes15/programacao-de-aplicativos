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
        comando_inserir_salas = f'''INSERT INTO cinemas (numero_sala, capacidade, id_cinemas) values ('{numero_sala}', '{capacidade}', {id_cinemas}')'''

        comando.execute(comando_inserir_cinemas)
        comando.execute(comando_inserir_hospitais)


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

cadastrar()