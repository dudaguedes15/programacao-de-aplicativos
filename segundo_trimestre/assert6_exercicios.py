def situacao_faltas(faltas):
    if faltas <=4:
        return "Regular"
    elif faltas > 10:
        return "Reprovado"
    elif faltas >= 5:
        return "Atenção"


situacao_faltas(15)
assert situacao_faltas(0) == "Regular"
assert situacao_faltas(4) == "Regular"
assert situacao_faltas(5) == "Atenção"
assert situacao_faltas(10) == "Atenção"
assert situacao_faltas(11) == "Reprovado"