import sqlite3
def cadastrar_professores():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor =  cursor = conexao.cursor()
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS professores (
                nome TEXT NOT NULL,
                telefone TEXT,
                materia TEXT
                idade_prof INTERGER,
                cpf TEXT UNIQUE NOT NULL,
                salario REAL,
                nome_escola TEXT
                )
                ''')
    nome_completo = input(" Digite o nome do professor: ")
    telefone_professor = input(" Digite o telefone do professor: ")
    materia = input("Digite a materia que esse professor da aula: ")
    idade_prof = int(input(" Digite a idade: "))
    cpf_prof = input(" Digite seu CPF: ")
    salario = float(input("Digite o salário dele: "))
    nome_escola = input("Digite o nome da escola: ")

    comando_inserir = f'''
        INSERT INTO  professores (nome, telefone, turma, idade, cpf)
        values ('{nome_completo}', '{telefone_professor}', '{materia}', '{idade_prof}', '{cpf_prof}', '{salario}', '{nome_escola}')
        '''
    cursor.execute(comando_inserir)

    conexao.commit()

    print("cadastro realizado")

    conexao.close()

def listar():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM professores") 
    professores = cursor.fetchall() 

    print("=== Lista de professores ===")

    for professor in professores:
        print(f"Nome completo: {professor[0]}")
        print(f"Telefone: {professor[1]}")
        print(f"Materia: {professor[2]}")
        print(f"Idade do professor: {professor[3]}")
        print(f"CPF do professor: {professor[4]}")
        print(f"Salário: {professor[5]}")
        print(f"Nome da escola: {professor[6]}")

