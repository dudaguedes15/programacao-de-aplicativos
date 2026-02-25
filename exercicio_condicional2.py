
poder_de_ataque = int(input("Digite o seu poder de ataque: "))
pontos_de_defesa = int(input("Digite os pontos de defesa do vilão: "))

dano = poder_de_ataque - pontos_de_defesa
if dano <= 0: 
    print("O vilão bloqueou ataquqe! Dano: 0. ")
elif dano > 0:
    print("Ataque crítico! Você causou dano ao vilão de", dano)
