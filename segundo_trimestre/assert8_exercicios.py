def pode_votar(idade):
    if idade >= 16:
        return True
    return False


    
pode_votar(12)
assert pode_votar(15) == False
assert pode_votar(16) == True
assert pode_votar(17) == True