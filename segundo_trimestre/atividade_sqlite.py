import sqlite3
def cadastrar_professores():
    try:
        conexao = sqlite3.connect('escola_demonstracao.db')
        cursor =  conexao.cursor()
        cursor.execute('''
                            CREATE TABLE IF NOT EXISTS professores (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        telefone TEXT,
                        materia TEXT,
                        idade INTEGER,
                        cpf TEXT UNIQUE NOT NULL,
                        salario REAL,
                        escola TEXT,
                        endereco TEXT
                    )
                    ''')

        nome_completo = input("Digite o nome do professor: ")
        telefone_professor = input("Digite o telefone do professor: ")
        materia = input("Digite a materia que esse professor da aula: ")
        idade_prof = int(input("Digite a idade: "))
        cpf_prof = input("Digite seu CPF: ")
        salario = float(input("Digite o salário dele: "))
        nome_escola = input("Digite o nome da escola: ")
        endereco_prof = input("Digite seu endereço: ")
        

        comando_inserir = f'''
            INSERT INTO  professores (nome, telefone, materia, idade, cpf, salario, escola, endereco)
            values ('{nome_completo}', '{telefone_professor}', '{materia}', '{idade_prof}', '{cpf_prof}', '{salario}', '{nome_escola}', '{endereco_prof}')
            '''
        cursor.execute(comando_inserir)

        conexao.commit()

        print("cadastro realizado")

    except ValueError:
        print("Digite um valor válido.")
    except TypeError:
        print("Tipo de dado errado.")
    except NameError:
        print("Erro de valor no cadastro tente novamente")
    except IndexError:
        print("Erro de indice fora dos limites")
    except KeyError:
        print("Chave não encontrada")
    except AttributeError:
        print("Atributo não existe")
    except sqlite3.IntegrityError:
        print("CPF já cadastrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}.")
    finally:
        conexao.close()

def listar():
    try:
        conexao = sqlite3.connect('escola_demonstracao.db')
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM professores") 
        professores = cursor.fetchall() 

        print("=== Lista de professores ===")

        for professor in professores:
            print(f"ID: {professor[0]}")
            print(f"Nome completo: {professor[1]}")
            print(f"Telefone: {professor[2]}")
            print(f"Materia: {professor[3]}")
            print(f"Idade do professor: {professor[4]}")
            print(f"CPF do professor: {professor[5]}")
            print(f"Salário: {professor[6]}")
            print(f"Nome da escola: {professor[7]}")
            print(f"Seu endereco: {professor[8]}")

    except IndexError:
        print("Erro de indice fora dos limites")
    except sqlite3.IntegrityError:
        print("CPF já cadastrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}.")
    finally:
        conexao.close()
def alterar():
    try:
        conexao = sqlite3.connect('escola_demonstracao.db')
        cursor = conexao.cursor()

        listar()
        id_professor = int(input("Digite o ID do professor que você deseja alterar: ")) 
        cursor.execute(f'''SELECT * FROM professores WHERE id = {id_professor}''')
        professor = cursor.fetchone()


        if not professor:
            print("Professor não cadastrado.")
        else: 
            print(f"Nome atual: {professor[0]}")
            print(f"Telefone atual: {professor[1]}")
            print(f"Materia atual: {professor[2]}")
            print(f"Idade atual: {professor[3]}")
            print(f"CPF atual: {professor[4]}")
            print(f"Salário: {professor[5]}")
            print(f"Escola atual: {professor[6]}")
            print(f"Endereço atual: {professor[7]}")

            nome_atualizado = input("Atualize o nome do professor: ")
            telefone_atualizado = input("Atualize seu telefone: ")
            materia_atualizada = input("Atualize a materia: ")
            idade_atualizada = int(input("Atualize a idade do professor: "))
            cpf_atualizado = input("Atualize o cpf: ")
            salario_atualizado = float(input("Digite o salário atualizado: "))
            escola_atualizada = input("Atualize o nome da escola: ")
            endereco_atualizado = input("Atualize seu endereço: ")

            cursor.execute(f'''
                        UPDATE professores
                        SET nome = '{nome_atualizado}', 
                        telefone = '{telefone_atualizado}', 
                        materia = '{materia_atualizada}', 
                        idade = '{idade_atualizada}',
                        CPF = '{cpf_atualizado}',
                        salario = '{salario_atualizado}',
                        escola = '{escola_atualizada}',
                        endereco = '{endereco_atualizado}'
                        WHERE id ={id_professor}
                        ''')
            conexao.commit()
            print("Dados alterados.")

            conexao.close()
    except ValueError:
        print("Erro de valor no cadastro tente novamente")
    except TypeError:
        print("Erro de tipo de dados")
    except sqlite3.IntegrityError:
        print("CPF já cadastrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}.")
    finally:
        conexao.close()        

def excluir():
    try:
        conexao = sqlite3.connect("escola_demonstracao.db")
        cursor = conexao.cursor()
        listar()
        id_professor = int(input(" Qual ID deseja deletar: " ))

        cursor.execute(f'''DELETE FROM professores WHERE Id = {id_professor}''')
        conexao.commit()
        conexao.close()
    except ValueError:
        print("Erro de valor no cadastro tente novamente")
    except TypeError:
        print("Erro de tipo de dados")
    except sqlite3.IntegrityError:
        print("CPF já cadastrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}.")
    finally:
        conexao.close()


def menu():
    try:
        opcao = 0

        while opcao != 5:
            print("\n")
            print("-------------------- MENU ------------------")
            print("-- 1 Cadastrar professor -- 2 Listar professores -- 3 Alterar professores --  4 Excluir professores -- 5 Fechar programa --")
            opcao = int(input("Digite o que você deseja fazer: "))
        
            if opcao == 1: 
                cadastrar_professores()

            elif opcao == 2:
                listar()

            elif opcao == 3:
                alterar()

            elif opcao == 4:
                excluir()

            elif opcao == 5:
                print("----PROGRAMA ENCERRADO.----")
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