# text_processing.py - operacje na tekście

# ------------ ODWRACANIE TEKSTU ------------

def odwroc_tekst(tekst):
    """
    Odwraca kolejność znaków w tekście.

    Argumenty:
        tekst (str) - tekst do odwrócenia

    Zwraca:
        odwrócony tekst (str)
    """
    return tekst[::-1]


# ------------ LICZENIE ZNAKÓW W TEKŚCIE ------------

def policz_znaki(tekst):
    """
    Liczy liczbę znaków w tekście.

    Argumenty:
        tekst (str) - tekst wejściowy

    Zwraca:
        liczbę znaków w tekście (int)
    """
    return len(tekst)
