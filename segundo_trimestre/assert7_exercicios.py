def brinde(carrinho):
    if carrinho >= 120:
 	    return  "Sim"
    return "Não"



brinde(99)
assert brinde(100) == "Não"
assert brinde(120) == "Sim"
assert brinde(121) == "Sim"

def hora_extra(horas):
    if horas > 5:
        return "Solicitar pagamento"
    return "Trabalhe mais"


hora_extra(4)
assert hora_extra(5) == "Trabalhe mais"
assert hora_extra(6) == "Solicitar pagamento"
assert hora_extra(8) == "Solicitar pagamento"



def safra(melancias):
    if melancias >= 100:
        return "Atacado"
    return "Varejo"


safra(120)
assert safra(99) == "Varejo"
assert safra(100) == "Atacado"
assert safra(101) == "Atacado"