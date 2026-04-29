def converter_km_para_ms(km):
    if velocidade > 80:
        ms = km / 3.6
        print("Reduza a velocidade!")
        return ms
    else:
        print("Você está na velocidade correta")

velocidade = int(input("Qual sua velocidade? "))
mensagem = converter_km_para_ms(velocidade)
