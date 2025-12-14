# data_utils.py - praca z listami danych

# ------------ USUWANIE DUPLIKATÓW ------------

def usun_duplikaty(lista):
    """
    Usuwa powtarzające się elementy z listy.

    Argumenty:
        lista (list) - lista wejściowa

    Zwraca:
        listę bez powtórzeń (list)
    """
    return list(set(lista))

# ------------ ZLICZANIE ELEMENTÓW ------------

def zlicz_elementy(lista):
    """
    Zlicza liczbę elementów w liście.

    Argumenty:
        lista (list) - lista wejściowa

    Zwraca:
        liczbę elementów w liście (int)
    """
    return len(lista)