# REST_API
Jednoduché API pre správu textových príspevkov, API podporuje `GET`, `PUT`, `PATCH` a `DELETE` request. Dáta z prichádzajúcich PUT requestov sú ukladané do databázového systému SQLAlchemy.

Formát textového príspevku: 
```
[{"userId": 1, "id": 1, "title": "TITLE", "body": 'BODY'}]
```

## Potrebné balíčky

Pred spustením aplikácie je potrebné nainštalovať balíčky, ktoré sú dôležite pre správnu funkciu aplikácie. Balíčky sa nachádzajú v textovom súbore `req.txt`, ktorý je možné jednoducho nainštalovať pomocou príkazu `pip/pip3 install -r req.txt`.

## Spustenie

Pre správne fungovanie aplikácie treba spustiť dva súbory pomocou príkazu `python3` a to v nasledovnom poradí: 
```
python3 main.py
python3 apiReq.py
```

### main.py
Obsahuje kód, ktorý vytvára lokálny server, vytvorenie databázového súboru a funkcie na spracovanie prichádzajúcich requestov. Po prijatí requestu sa následne spracuje aj zmena v databázovom súbore. Napríklad po GET requeste sa na základe ID z databázového súboru odošlú informácie ktore sú spojené s daným ID.  


### apiReq.py
V súbore je definovaný zdroj dát, ktoré pochádzajú z externej API ďalej sa v ňom nachádzajú `GET`, `PUT`, `PATCH` a `DELETE` requesty, ktoré sú následne spracované a odoslané do súboru `main.py` kde sa spracujú a vykonajú príslušné úkony v databázovom súbore. Príkazy pre requesty sa vykonávajú samostatne prvý príkaz sa vykoná automaticky po spustení súboru ostatné príkazy sa vykonávajú po stlačení klávesy ENTER. 

Príkazy sú v nasledovnom poradí:

- **GET** - získa dáta z externej api
- **PUT** - dáta uloží na server
- **GET** - pošle dotaz pre databázu na získanie dát pod ID 4
- **PATCH** - pošle dotaz na update dát pod ID 2
- **DELETE** - pošle dotaz na delete dát pod ID 3
- **GET** - pošle dotaz na získanie dát pod ID 3, následne vypíše ERROR

