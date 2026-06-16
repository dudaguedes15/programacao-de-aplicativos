import sqlite3
def cadastrar():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS alunos (
                id  INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT,
                turma TEXT,
                idade INTERGER,
                cpf TEXT UNIQUE NOT NULL
                )
                ''')

    nome_aluno = input (" Digite o nome do aluno: ")
    telefone_aluno = input (" Digite o telefone do alunos: ")
    turma_aluno = input (" Digite qual a sua turma: ")
    idade_aluno = int(input(" Digite a sua idade: "))
    cpf_aluno = input(" Digite seu CPF: ")

    comando_inserir = f'''
        INSERT INTO  alunos (nome, telefone, turma, idade, cpf)
        values ('{nome_aluno}', '{telefone_aluno}', '{turma_aluno}', '{idade_aluno}', '{cpf_aluno}')
        '''

    cursor.execute(comando_inserir)

    conexao.commit()

    print("cadastro realizado")

    conexao.close()

def listar():
    
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos") 
    alunos = cursor.fetchall() 

    print("=== Lista de Aluno ===")

    for aluno in alunos: 
        print(f"ID: {aluno[0]}")
        print(f"Nome: {aluno[1]}")
        print(f"Telefone: {aluno[2]}")
        print(f"Turma: {aluno[3]}")
        print(f"Idade: {aluno[4]}")
        print(f"CPF: {aluno[5]}")
        print("-" * 30)

def alterar():

    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    id_aluno = int(input(" Qual seu ID: "))

    cursor.execute(f'''SELECT nome , cpf , telefone , idade , turma FROM alunos WHERE id = {id_aluno}''')
    
    aluno = cursor.fetchone()

    if not aluno:
        print(" Não encontrado ")
    else:
        print(f" Nome atual {aluno[0]} ")
        print(f" CPF atual {aluno [1]} ")
        print(f" Telefone atual {aluno[2]} ")
        print(f" Idade atual {aluno [3]} ")
        print(f" Turma atual {aluno [4]} ")

        nome_atualizado = input(" Atualize seu nome: ")
        cpf_atualizado = input(" Atualize seu CPF: ")
        telefone_atualizado = input(" Atualize se telefone: ")
        idade_atualizada = input(" Atualize sua idade: ")
        turma_atualizada = input(" Atualize sua turma: ")

        cursor.execute(f'''
                        UPDATE alunos
                        SET nome ='{nome_atualizado}', CPF ='{cpf_atualizado}', Telefone ='{telefone_atualizado}', Idade ='{idade_atualizada}', Turma ='{turma_atualizada}'
                    WHERE id ={id_aluno}
                        ''')
        conexao.commit()
        print(" Dados alterados ")

        conexao.close()


def deletar():


    conexao = sqlite3.connect("escola_demonstracao.db")
    cursor = conexao.cursor()
    listar()
    id_aluno = int(input(" Qual ID deseja deletar: " ))

    cursor.execute(f'''DELETE FROM Alunos WHERE Id = {id_aluno}''')
    conexao.commit
    conexao.close

alterar()