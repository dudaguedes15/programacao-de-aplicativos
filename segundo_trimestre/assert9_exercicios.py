def buscar_nome(lista, nome):
    return nome in lista

def tem_senha_valida(senha):
    if len(senha) >= 8:
        return True
    return False

senha = "abec"
tem_senha_valida(senha)
assert tem_senha_valida("aaaaaaa") == False
assert tem_senha_valida("aaaaaaaa") == True
assert tem_senha_valida("aaaaaaaaa") == True