codigo = int(input("Qual o código do pacote ?: "))
peso = float(input("Qual o peso do pacote ?: "))

if peso < 5 and codigo % 10 == 0:
    print(f"Pacote {codigo}: Autorizado para entrega.")
elif peso > 50 and codigo % 10 == 0:
    print(f"Pacote {codigo}: Carga pesada.")
else:
    print(f"Pacote {codigo}: Carga não Encontrada/Autorizada. ")
    