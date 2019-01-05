import variables
import simple
import advanced
import settings
import exceptions
import sys

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


