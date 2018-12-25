import variables
import location
import city
import airly

simpleChose = "Wybrales proste wyszukiwanie"


def printCityData(cityDict):
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
    if active == True:
        return 'Włączony'
    else:
        return 'Wyłączony'


def printAirlyNearest(airlyDict):
    print('\n\n Najbliższe punkty pomiarowe')
    print('*%-25s %-25s %10s*' % ('miejscowosc', 'ulica', 'aktywnosc'))
    for element in airlyDict:
        print('*%-25s %-25s %10s*'
              % (element['city'], element['street'], check(element['airly'])))


global airly_nearest


class GetData:

    def __init__(self):
        city = self.getCity()
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

            # for measure_element in airly_measure:
            # for k,v in measure_element.items():

    def getCity(self):
        return input("Podaj miejsce pomiaru smogu: ")

    def getCitydata(self, jsonData):
        return city.convertCityJsonData(jsonData)
