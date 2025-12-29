from my_awesome_lib.data_utils import usun_duplikaty, zlicz_elementy

# usuwanie duplikatów
def test_usun_duplikaty():
    wynik = usun_duplikaty([1, 2, 2, 3])
    assert set(wynik) == {1, 2, 3}


def test_usun_duplikaty_pusta_lista():
    assert usun_duplikaty([]) == []

# zliczanie elementów
def test_zlicz_elementy():
    assert zlicz_elementy([1, 2, 3]) == 3


def test_zlicz_elementy_pusta_lista():
    assert zlicz_elementy([]) == 0
