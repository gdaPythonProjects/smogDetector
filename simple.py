import variables
import location
import city
import airly
import time

simpleChose = "Wybrales proste wyszukiwanie"


def printCityData(cityDict):
    """
    function is receiving dictionary with the data of selected place and prints their details
    :param cityDict:
    :return None:
    """
    if cityDict['street'] != '':
        print("\nUlica: ", cityDict['street'])
    else:
        print('\n')
    print("Miejscowość: ", cityDict['city'])
    print("Województwo: ", cityDict['district'])
    if cityDict['postCode'] != '':
        print("Kod pocztowy: ", cityDict['postCode'])
    print('Długość geograficzna', cityDict['lng'])
    print('Szerokosc geograficzna', cityDict['lat'])


def check(active):
    """
    Check if specifig MPoint is active or not
    :param bool active:
    :return translation if Mpoint is running or not:
    """
    if active == True:
        return 'Włączony'
    else:
        return 'Wyłączony'


def printAirlyNearest(airlyDict):
    """
    Function print nearest MPoint (for default now is 1)
    :param airlyDict:
    :return None:
    """
    print('\n\n Najbliższe punkty pomiarowe')
    print('*%-25s %-25s %10s*' % ('miejscowosc', 'ulica', 'aktywnosc'))
    for element in airlyDict:
        print('*%-25s %-25s %10s*'
              % (element['city'], element['street'], check(element['airly'])))


global airly_nearest



class GetData:
"""
This class is getting data from MAP API and AIRLY API and printing all important information about air pollution
"""
    def __init__(self, city=None, interval=None):
        if interval is not None:
            while True:

                if city is None:
                    city = self.getCity()

                self.receiveAndPrintData(city)
                print(f'kolejny pomiar za {interval}s')
                time.sleep(int(interval))
        else:
            if city is None:
                city = self.getCity()
            self.receiveAndPrintData(city)


            # for measure_element in airly_measure:
            # for k,v in measure_element.items():

    def getCity(self):
        return input("Podaj miejsce pomiaru smogu: ")

    def getCitydata(self, jsonData):
        return city.convertCityJsonData(jsonData)

    def receiveAndPrintData(self, city):

        mapApiGet = location.Location()
        cityJsonData = mapApiGet.getMapApiData(city)
        cityDict = self.getCitydata(cityJsonData)
        printCityData(cityDict)
        airlyApiGet = airly.Airly()
        airlyJsonData = airlyApiGet.getAirlyApiNearestData(cityDict['lat'], cityDict['lng'])
        airly_nearest = airlyApiGet.convertAirlyNearestJsonData(airlyJsonData)
        printAirlyNearest(airly_nearest)
        for element in airly_nearest:
            airly_json_measure = airlyApiGet.getAirlyApiMeasureData(element['id'])
            airly_measure = airlyApiGet.convertAirlyMeasureJsonData(airly_json_measure)
            print(f"Poziom zanieczyszczeń: {airly_measure[0]['level']}")
            print(f"Wskazówka: {airly_measure[0]['advice']}")
            names = ''
            values = ''
            for k, v in airly_measure[1].items():
                names += "{:>15}".format(k)
                values += "{:15}".format(v)
            print(names)
            print(values)

