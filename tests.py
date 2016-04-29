from mastermind import reportar


def test_reportar_1():
    real = reportar('1234', plenos=1, regulares=2)
    esperado = "El número 1234 tiene 1 pleno y 2 regulares. Dale que va"
    assert real == esperado


def test_reportar_2():
    real = reportar('1349', plenos=2, regulares=2)
    esperado = "El número 1349 tiene 2 plenos y 2 regulares: ya lo tenés!"
    assert real == esperado


def test_reporart_3():
    real = reportar('1092', plenos=0, regulares=1)
    esperado = "El número 1092 tiene 0 pleno y 1 regular: estás más lejos que Macri de la pobreza cero"
    assert real == esperado
