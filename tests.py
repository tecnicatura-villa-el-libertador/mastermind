from mastermind import reportar, crear_numero


def test_reportar_1():
    real = reportar('1234', plenos=1, regulares=2)
    esperado = "El número 1234 tiene 1 pleno y 2 regulares. Dale que va"
    assert real == esperado


def test_reportar_2():
    real = reportar('1349', plenos=2, regulares=2)
    esperado = "El número 1349 tiene 2 plenos y 2 regulares: ya lo tenés!"
    assert real == esperado


def test_reportar_3():
    real = reportar('1092', plenos=0, regulares=1)
    esperado = "El número 1092 tiene 0 pleno y 1 regular: estás más lejos que Macri de la pobreza cero"
    assert real == esperado


def test_crear_numero():
    for x in range(1000):
        numero = crear_numero()
        assert numero.isdigit()
        assert len(numero) == 4
        assert set(numero).issubset(set(map(str, range(10))))


def test_validar_1():
    assert validar('1234')


def test_validar_no_acepta_repetidos():
    assert not validar('1134')
    assert not validar('1334')
    assert not validar('1133')
    assert not validar('1111')
    assert not validar('0122')


def test_validar_no_acepta_letras():
    assert not validar('a123')
    assert not validar('123v')


def test_validar_no_acepta_letras():
    assert not validar('a123')
    assert not validar('123v')


def test_validar_largo_4():
    assert not validar('123')
    assert not validar('2')


def test_evaluar():
    assert evaluar('1234', '1234') == (4, 0)
    assert evaluar('1234', '2134') == (2, 2)
    assert evaluar('1234', '1243') == (2, 2)
    assert evaluar('1234', '9871') == (0, 1)
    assert evaluar('1234', '9831') == (1, 1)


