import sqlite3

def criar_tabela_escola():

    conexao = sqlite3.connect('gestao_escolar.db')
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS escola(
                    id  INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    cidade TEXT NOT NULL)
                    ''')
    conexao.commit()
    conexao.close()

def criar_tabela_turma():

    conexao = sqlite3.connect('gestao_escolar.db')
    cursor = conexao.cursor()

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS turma(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_turma TEXT NOT NULL,
                id_escola INTEGER,
                FOREING KEY (id_sociedades) REFERENCES escola (id))
                ''')
    conexao.commit()
    conexao.close()

def criar_tabela_alunos():

    conexao = sqlite3.connect('gestao_escolar.db')
    cursor = conexao.cursor()

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS alunos(
                id INTEGER PRIMARY KEY AUTOINCREMENT
                nome TEXT NOT NULL,
                idade INTEGER,
                id_turma INTEGER,
                FOREING KEY (id_turma) REFERENCES turma (id))
                ''')
    conexao.commit()
    conexao.close()

criar_tabela_escola()