media = float(input("Digite a média: "))
presenca = int(input("Digite a porcentagem de presença: "))

if media >= 7.0 and presenca >= 75:
    print("Parabéns! Você foi aprovado.")
elif media < 7.0 and presenca < 75:
    print("Reprovado. Verifique sua nota ou frequência.")