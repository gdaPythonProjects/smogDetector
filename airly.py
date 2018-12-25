import requests
import variables
import urllib



class Airly:
    def getAirlyApiNearestData(self, lat, lon):
        airly_nearest_variables = {
            'apikey': variables.AIRLY_KEY,
            'Accept-Language': 'pl',
            'lat': lat,
            'lng': lon,
            'maxDistanceKM': 50,
            'maxResults': 1,

        }
        # print(variables.airly_nearest_url + urllib.parse.urlencode(airly_nearest_variables))
        resp = requests.get(variables.airly_nearest_url + urllib.parse.urlencode(airly_nearest_variables))
        return resp.json()

    def getAirlyApiMeasureData(self, id):
        airly_measure_variables = {
            'apikey': variables.AIRLY_KEY,
            'Accept-Language': 'pl',
            'indexType': 'AIRLY_CAQI',
            'installationId': id,

        }
        # print(variables.airly_measure_url + urllib.parse.urlencode(airly_measure_variables))
        resp = requests.get(variables.airly_measure_url + urllib.parse.urlencode(airly_measure_variables))
        return resp.json()

    def convertAirlyNearestJsonData(self, airlyJson):
        airlyD = []
        i = 0
        for element in airlyJson:
            airlyD.append({
                'id': element['id'],
                'airly': element['airly'],
            })
            for k, v in element['address'].items():
                airlyD[i].update({k: v})
            i += 1
        return airlyD

    def convertAirlyMeasureJsonData(self, airlyJson):
        airlyD = list()
        airly_v = dict()
        if len(airlyJson['current']['standards']) == 0:
            airly_indexes = airlyJson['current']['indexes']
            airlyD.append(airly_indexes)
            return airlyD
        else:
            airly_indexes = airlyJson['current']['indexes']
            airly_values = airlyJson['current']['values']
            airly_standards = airlyJson['current']['standards']
            airlyD += airly_indexes
            for element in airly_values:
                airly_v.update({element['name']: element['value']})
            airlyD.append(airly_v)
            airlyD += airly_standards
            return airlyD


