cargo = input("Qual o seu cargo? ")
codigo = int(input("Digite o código de acesso: "))
botaoemergencia = input("O botão de emergência foi pressionado? S/N ")
equipamentos = input("Você esta com o EPI completo? S/N ")

if cargo == "engenheiro" or (cargo == "tecnico" and codigo == 1234) or (botaoemergencia == "S" and equipamentos == "S"): 
                                                                      print("ACESSO LIBERADO")

else:
        print("ACESSO NEGADO: RISCO DE SEGURANÇA")