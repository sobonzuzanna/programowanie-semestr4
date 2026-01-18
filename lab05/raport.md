**WYBRANA DZIEDZINA**
Web Scraping - proces automatycznego pozyskiwania danych ze stron internetowych.



**OPIS BIBLIOTEK**



**1. Requests**



Ta biblioteka jest najpopularniejszym narzędziem w Pythonie służącym do wysyłania zapytań HTTP. Jej głównym przeznaczeniem jest komunikacja z serwerami WWW i pobieranie zawartości stron internetowych w sposób uproszczony, bez konieczności ręcznej konfiguracji połączeń. Jest to fundament większości projektów typu web scraping, ponieważ pozwala w kilku linijkach kodu uzyskać dostęp do surowego kodu źródłowego witryny.



**Główne funkcje:**

* requests.get() - pobieranie danych z serwera.
* response.status\_code - weryfikacja poprawności połączenia.
* response.text - odczyt pobranej zawartości jako tekst.



**Zalety:**

* Niezwykła intuicyjność i składnia typu "human-readable".
* Bardzo bogata dokumentacja i ogromne wsparcie społeczności.
* Stabilność i standard rynkowy w projektach Python.



**Ograniczenia:**

* Brak możliwości renderowania skryptów JavaScript (pobiera tylko statyczny kod).
* Nie potrafi samodzielnie obsługiwać interakcji z przeglądarką (np. klikania w przyciski).



**Dokumentacja:** https://requests.readthedocs.io/en/latest/



**Repozytorium:** https://github.com/psf/requests



**2. BeautifulSoup4**



To biblioteka przeznaczona do analizy i przetwarzania dokumentów HTML oraz XML. Po pobraniu surowego kodu strony (np. za pomocą biblioteki Requests), BeautifulSoup tworzy z niego strukturę drzewiastą, która pozwala na łatwe i szybkie wyciąganie konkretnych informacji, takich jak nagłówki, linki czy tabele danych.



**Główne funkcje:**

* BeautifulSoup(html, 'html.parser') - transformacja tekstu HTML w obiekt strukturalny.
* find\_all() - wyszukiwanie wszystkich elementów o zadanych parametrach.
* get() - dostęp do konkretnych atrybutów tagu (np. adresu URL).



**Zalety:**

* Duża elastyczność w radzeniu sobie z błędnym lub niechlujnym kodem HTML.
* Wiele intuicyjnych metod nawigacji po strukturze dokumentu.
* Bardzo lekka i szybka w działaniu przy parsowaniu tekstu.



**Ograniczenia:**

* Nie potrafi sama pobierać danych z sieci (wymaga współpracy z Requests).
* Podobnie jak Requests, nie współpracuje z treścią generowaną dynamicznie przez JavaScript.



**Dokumentacja:** https://www.crummy.com/software/BeautifulSoup/bs4/doc/



**Repozytorium:** https://pypi.org/project/beautifulsoup4/

