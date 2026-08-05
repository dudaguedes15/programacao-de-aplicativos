import sqlite3


def cadastrar():
    try:

        cursor.execute('''CREATE TABLE IF NOT EXISTS hospitais(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    cidade TEXT    )   
                ''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS medicos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                crm TEXT UNIQUE NOT NULL,
                id_hospital INTEGER,
                FOREIGN KEY(id_hospital) REFERENCES hospitais(id)
                )

        ''')

        nome_hospital = input("Digite o nome do hospital: ")
        cidade = input("Digite o nome da cidade: ")
        nome_medico = input("Digite o nome do médico: ")
        crm = int(input("Digite o crm dele(a): "))
        id_hospital = int(input("digite o id do hospital: "))


        comando_inserir_hospitais = f'''INSERT INTO hospitais (nome, cidade) values ('{nome_hospital}', '{cidade}')'''
        comando_inserir_medicos = f'''INSERT INTO medicos (nome, crm, id_hospital) values ('{nome_medico}', '{crm}', '{id_hospital}')'''

        cursor.execute(comando_inserir_hospitais)
        cursor.execute(comando_inserir_medicos)

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