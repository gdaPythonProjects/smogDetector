"""
Created by Piotr R. 2018-2019
Application is searching for the nearest measuremenet point (MPoint) of the pollution.
It is searching a place from the arguments or from user input
Provides an information about place (latitude and longitude) and measures from the nearest point.
running script without arguments will lead to menu which user can choose search for MPoints
First arg - place, city where it should search for MPoint. Argument should be by one word or with quotation marks
Example 1: main.py Gdansk
Example 2: main.py "Gdansk, dluga"
Example 3: main.py "Sopot, Haffnera 20"
Second arg - interval to repeat measurement request (in seconds)
Example 1: main.py Gdansk, 10
Example 2: main.py "Gdansk, dluga", 60
Example 3: main.py "Sopot, Haffnera 20", 900

"""
import sys

import advanced
import settings
import simple
import variables

z = 0
if len(sys.argv) == 1:
    print(variables.menuIntro)
    print(variables.menuOptions)
    while z != 4:
        try:
            z = int(input(variables.yourChoice))
        except ValueError:
            print("Podana wartość nie jest liczbą")

        if z == 1:
            print(simple.simpleChose)
            simple.GetData()
        elif z == 2:
            print(advanced.advancedChose)
        elif z == 3:
            print(settings.settingChose)
        elif z == 4:
            print(variables.menuEnd)
            break
        else:
            print("nie wybrano poprawnej cyfry, wybierz jedną z opcji")

else:
    arguments = sys.argv[1:]
    try:
        simple.GetData(*arguments)
    except Exception:
        print("niepoprawne parametry")

