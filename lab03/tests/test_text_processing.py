from my_awesome_lib.text_processing import odwroc_tekst, policz_znaki

# odwracanie tekstu
def test_odwroc_tekst():
    assert odwroc_tekst("abc") == "cba"


def test_odwroc_tekst_pusty():
    assert odwroc_tekst("") == ""

# liczenie znaków
def test_policz_znaki():
    assert policz_znaki("hello") == 5


def test_policz_znaki_ze_spacja():
    assert policz_znaki("hello world") == 11
