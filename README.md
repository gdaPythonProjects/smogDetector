# smogDetector
Check smog and pollution level for given city. Alert when pollution level today is very high.


Application is searching for the nearest measuremenet point (MPoint) of the pollution.

It is searching a place from the arguments or from user input

Provides an information about place (latitude and longitude) and measures from the nearest point.

First arg - place, city where it should search for MPoint. Argument should be by one word or with quotation marks

### Examples
```sh 
$ main.py Gdansk
$ main.py "Gdansk, dluga"
$ main.py "Sopot, Haffnera 20"
```

Second arg - interval to repeat measurement request (in seconds)

### Examples
```sh 
$ main.py Gdansk, 10 
$ main.py "Gdansk, dluga", 60 
$ main.py "Sopot, Haffnera 20" , 900
```

Application without arguments will lead to menu which user can choose where to search for MPoints:

    Witamy w SmogDetektorze
    Wybierz jedną z opcji:

    1 - Wyszukiwanie proste
    2 - Wyszukiwanie zaawansowane
    3 - Ustawienia
    4 - Wyjscie
