import sqlite3

def vincular_aluno_turma():
    conexao = None

    nome = input("Nome do aluno: ")

    try:
        id_turma = int(input("Digite o ID numérico da turma: "))

        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO alunos (nome, id_turma) VALUES (?, ?)",
            (nome, id_turma)
        )

        conexao.commit()
        print("Aluno cadastrado com sucesso!")

    except ValueError:
        print("Erro: Digite apenas números!")

    except sqlite3.Error as erro:
        print("Erro no banco de dados:", erro)

    finally:
        if conexao:
            conexao.close()

vincular_aluno_turma()