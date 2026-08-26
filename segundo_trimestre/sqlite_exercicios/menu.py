from sociedades import cadastrar_sociedades, listar_sociedade, atualizar_sociedades, excluir_sociedades
from filiais import cadastrar_filiais, listar_filiais, atualizar_filiais, excluir_filiais
def menu():
    try:
        opcao = 0
        while opcao != 8:
            print("\n")
            print("-------------------- MENU ------------------")
            print("-- 1 Cadastrar sociedades -- 2 Cadastrar filiais -- 3 Listar sociedade -- 4 Listar filiais --  5 Atualizar sociedades -- 6 Atualizar filiais -- 7 Excluir sociedades -- 8 Excluir filiais -- 9 Fechar programa --")
            opcao = int(input("Digite o que você deseja fazer: "))

            if opcao == 1:
                cadastrar_sociedades()
            elif == 2:
                cadastrar_filiais()
            elif opcao == 3:
                listar_sociedade()
            elif opcao == 4:
                listar_filiais()
            elif opcao == 5:
                atualizar_sociedades()
            elif opcao == 6:
                atualizar_filiais()
            elif opcao == 7:
                excluir_sociedades()
            elif opcao == 8:
                excluir_filiais()
            elif opcao == 9:
                print("===== PROGRAMA ENCERRADO =====")
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