nivel = int(input("Fale seu nível atual: "))
esferas = int(input("Fale a quantidade de esferas coletadas: "))

if nivel >= 20 and esferas >= 50:
    print("Habilidade Super Salto desbloqueda!")
elif nivel < 20 and esferas < 50:
    print("Requisitos insuficientes para nova habilidade")
elif nivel >= 20 and esferas < 50: 
    print("Requisitos insuficientes para nova habilidade")
elif nivel < 20 and esferas > 50:
    print("Requisitos insuficientes para nova habilidade")