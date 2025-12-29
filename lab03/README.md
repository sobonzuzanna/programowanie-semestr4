# My Awesome Lib

My Awesome Lib to biblioteka napisana w języku Python.
Biblioteka zawiera zestaw funkcji realizujących:
- podstawowe obliczenia matematyczne,
- operacje na tekście,
- pracę z listami danych.

---

## Instalacja

Sklonuj repozytorium i korzystaj z biblioteki bezpośrednio w swoim projekcie

git clone https://github.com/sobonzuzanna/programowanie-lab03.git

## Przykłady użycia

### Operacje matematyczne
from my_awesome_lib.math_tools import sumuj, odejmij, srednia

print(sumuj(2, 3))      # 5
print(odejmij(10, 4))   # 6
print(srednia(4, 6))    # 5.0

### Operacje na tekście

from my_awesome_lib.text_processing import odwroc_tekst, policz_znaki

print(odwroc_tekst("Python"))        # "nohtyP"
print(policz_znaki("Hello world"))   # 11

### Praca z listami danych

from my_awesome_lib.data_utils import usun_duplikaty, zlicz_elementy

print(usun_duplikaty([1, 2, 2, 3]))  # [1, 2, 3]
print(zlicz_elementy([5, 7, 9]))     # 3


## Autor

Zuzanna Soboń

## Wersja

1.0.0

## Licencja

MIT