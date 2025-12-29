**Porównanie wyników**
| Smartfon   | Ocena TOPSIS | Ocena SPOTIS |
| ---------- | ------------ | ------------ |
| iPhone 15  | 0.435152     | 0.617688     |
| Galaxy S23 | 0.811002     | 0.204817     |
| Motorola   | 0.310871     | 0.677495     |
| Xiaomi     | 0.242440     | 0.763120     |

Wyniki są bardzo różne. Możliwe przyczyny:
- Różna skala oceny: TOPSIS zwraca wartości w przedziale [0, 1], gdzie wyższa wartość oznacza lepszą alternatywę (bliskość do ideału). SPOTIS natomiast mierzy odległość od rozwiązania idealnego, więc niższa wartość oznacza lepszy wynik (mniejszy dystans do ideału).
- Sposób normalizacji: TOPSIS bazuje na relatywnych odległościach od punktu idealnego i anty-idealnego wewnątrz danego zbioru, podczas gdy SPOTIS odnosi się do sztywnych granic (bounds), co czyni go odporniejszym na tzw. zjawisko zamiany rang (rank reversal).
- Geometria metod: TOPSIS używa miary euklidesowej w przestrzeni znormalizowanej, a SPOTIS sumuje znormalizowane dystanse bezpośrednio, co inaczej rozkłada "kary" za słabsze wyniki w poszczególnych kryteriach.

**Interpretacja wyników**  
Najlepszą alternatywą w obu metodach okazał się Galaxy S23.  
Obydwie metody są zgodne. W TOPSIS zdobył najwyższą notę (najbliżej ideału) - 0.811. W SPOTIS najniższą (najbliżej ideału) - 0.204.  
Galaxy S23 najprawdopodobniej oferuje najlepszy balans między ceną a parametrami (RAM, Bateria, Aparat).  

**Ranking końcowy**
1. Galaxy S23
2. iPhone 15
3. Motorola
4. Xiaomi
