import sqlite3
conexao = sqlite3.connect('sistema_escola.db')
cursor = conexao.cursor()

def cadastrar_tabela():


    cursor.execute('''
                CREATE TABLE IF NOT EXISTS series(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_serie TEXT NOT NULL,
                id_escola INTEGER,
                FOREIGN KEY (id_escola) REFERENCES escolas(id)

                )''')


cadastrar_tabela()
    
conexao.commit()
