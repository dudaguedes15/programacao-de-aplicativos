def calcular_frete(valor_compra):
    if valor_compra >= 200:
        return 0
    elif valor_compra >= 100:
        return 10
    return 20


def test_compra_abaixo_de_100():
    assert calcular_frete(99.99) == 20


def test_compra_exatamente_100():
    assert calcular_frete(100) == 10


def test_compra_entre_100_e_199_99():
    assert calcular_frete(150) == 10


def test_compra_exatamente_200():
    assert calcular_frete(200) == 0


def test_compra_acima_de_200():
    assert calcular_frete(250) == 0

