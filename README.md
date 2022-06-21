# REST_API


### Spustenie

Prvý krok spustenia je zapnutie súboru `main.py` - tento súbor spustí lokálny server na ktorom beží databáza do ktorej sa ukladajú dáta. Následnepo  spustení súboru sa vytvorí databázový súbor `test.db` do ktorého sa ukladajú všetky dáta získané `GET requestom`. Následne sú dáta získavané a upravované pomocou requestov priamo v databazovom súbore. 

Pre načítanie dát z externej `API` je potrebné spustiť druhý súbor s názvom `apiReq.py`, v súvore sa nachádzajú requesty `PUT, GET, PATCH a DELETE`.

### Potrebné balíčky
Balíčky potrebné k spusteniu programu sa nachádzajú v textovom súbore `req.txt`. Tieto balíčky nainštalujeme príkazom `pip/pip3 install -r req.txt`
