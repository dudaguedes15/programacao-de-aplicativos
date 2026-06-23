import sqlite3
def cadastrar():
    try:
        conexao = sqlite3.connect('escola_demonstracao.db')
        cursor = conexao.cursor()

        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS alunos (
                    id  INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone TEXT,
                    turma TEXT,
                    idade INTERGER,
                    cpf TEXT UNIQUE NOT NULL,
                    endereco TEXT,
                    cidade TEXT,
                    estado TEXT,
                    id_professor INTEGER,
                    FOREIGN KEY (id_professor) REFERENCES professor(id)
                    )
                    ''')

        nome_aluno = input (" Digite o nome do aluno: ")
        telefone_aluno = input (" Digite o telefone do alunos: ")
        turma_aluno = input (" Digite qual a sua turma: ")
        idade_aluno = int(input(" Digite a sua idade: "))
        cpf_aluno = input(" Digite seu CPF: ")
        endereco = input("Digite o seu endereço: ")
        cidade = input("Digite a cidade:")
        estado = input("Digite o estado: ")
        id_professor = int(input("Digite o ID do professor: "))

        comando_inserir = f'''
            INSERT INTO  alunos (nome, telefone, turma, idade, cpf, endereco, cidade, estado, id_professor)
            values ('{nome_aluno}', '{telefone_aluno}', '{turma_aluno}', '{idade_aluno}', '{cpf_aluno}', '{endereco}', '{cidade}', '{estado}', '{id_professor}')
            '''

        cursor.execute(comando_inserir)

        conexao.commit()

        print("cadastro realizado")
    except: 
        print("Digite apenas números. ")
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
        print(f"endereco: {aluno[6]}")
        print(f"cidade: {aluno[7]}")
        print(f"estado: {aluno[8]}")
        print(f"ID do professor: {aluno[9]}")
        print("-" * 30)

def alterar():

    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    id_aluno = int(input(" Qual seu ID: "))

    cursor.execute(f'''SELECT * FROM alunos WHERE id = {id_aluno}''')
    
    aluno = cursor.fetchone()

    if not aluno:
        print(" Não encontrado ")
    else:
        print(f"Nome atual {aluno[1]} ")
        print(f"Telefone atual {aluno[2]} ")
        print(f"Turma atual {aluno[3]} ")
        print(f"Idade atual {aluno[4]} ")
        print(f"CPF atual {aluno[5]} ")
        print(f"endereço atual {aluno[6]}")
        print(f"cidade atual {aluno[7]}")
        print(f"estado atual {aluno[8]}")
        print(f"Professor atual: {aluno[9]}")
        
        

        nome_atualizado = input(" Atualize seu nome: ")
        telefone_atualizado = input(" Atualize se telefone: ")
        turma_atualizada = input(" Atualize sua turma: ")
        idade_atualizada = input(" Atualize sua idade: ")
        cpf_atualizado = input(" Atualize seu CPF: ")
        endereco_atualizado = input(" Atualize o endereço: ")
        cidade_atualizado = input(" Atualize a cidade: ")
        estado_atualizado = input(" Atualize o estado: ")
        professor_id_atualizado = input("Atualize o ID do professor: ")
        
        
        

        cursor.execute(f'''
                    UPDATE alunos
                        SET nome ='{nome_atualizado}', Telefone ='{telefone_atualizado}' ,Turma ='{turma_atualizada}', Idade ='{idade_atualizada}', endereco = '{endereco_atualizado}', cidade = '{cidade_atualizado}', estado = '{estado_atualizado}', CPF ='{cpf_atualizado}',    id_professor = '{professor_id_atualizado}'
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
    conexao.commit()
    conexao.close()
cadastrar()