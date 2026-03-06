seguranca = input("Você concluiu o curso de segurança? S/N: ")

if seguranca == "S":
    instrutor = input("O instrutor está presente na sala? S/N: ")
    if instrutor == "S":
        print("Acesso liberado: Operação iniciada.")
    else:
        print("Aguarde o instrutor para ligar a máquina.")

else: 
    print("Acesso negado. Faça o treinamento primeiro.")