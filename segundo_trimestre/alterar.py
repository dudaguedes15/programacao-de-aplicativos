import sqlite3
def cadastrar_professores():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor =  cursor = conexao.cursor()
    cursor.execute('''ALTER TABLE alunos ADD COLUMNS
                   endereco TEXT,
                   cidade TEXT,
                   estado TEXT''')