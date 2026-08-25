def pode_entrar(idade, acompanhado):
    if idade >= 18 or acompanhado:
        return True
    return False


def test_maior_de_idade_desacompanhada():
    assert pode_entrar(20, False) is True


def test_menor_de_idade_acompanhada():
    assert pode_entrar(16, True) is True


def test_menor_de_idade_desacompanhada():
    assert pode_entrar(16, False) is False


def test_exatamente_18_anos():
    assert pode_entrar(18, False) is True


def test_17_anos_acompanhada():
    assert pode_entrar(17, True) is True
