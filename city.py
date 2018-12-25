
def convertCityJsonData(cityData):
    cityDict = dict()

    for elements in cityData['results']:
        for key, value in elements.items():
            if key == 'locations':
                for element in elements[key]:
                    cityDict.update({'street': element['street']})
                    cityDict.update({'city': element['adminArea5']})
                    cityDict.update({'district': element['adminArea3']})
                    cityDict.update({'postCode': element['postalCode']})
                    for k, v in element['latLng'].items():
                        cityDict.update({k: v})
    return cityDict

