import requests
import variables
import urllib


class Airly:
    @staticmethod
    def getAirlyApiNearestData(lat, lon):
        """
        From longitude and latitude, getting json response file from airly api
        :param lat: latitude
        :param lon: longitude
        :return: response json
        """
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

    @staticmethod
    def getAirlyApiMeasureData(id):
        """
        getting specific data from airly api MPoint
        :param id: id of MPoing
        :return: response json
        """
        airly_measure_variables = {
            'apikey': variables.AIRLY_KEY,
            'Accept-Language': 'pl',
            'indexType': 'AIRLY_CAQI',
            'installationId': id,

        }
        # print(variables.airly_measure_url + urllib.parse.urlencode(airly_measure_variables))
        resp = requests.get(variables.airly_measure_url + urllib.parse.urlencode(airly_measure_variables))
        return resp.json()

    @staticmethod
    def convertAirlyNearestJsonData(airlyJson):
        """
        airly api json data is processing and is returning dictionary data
        :param airlyJson:
        :return: airly dictionary
        """
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

    @staticmethod
    def convertAirlyMeasureJsonData(airlyJson):
        """
                airly api json data is processing and is returning dictionary data
                :param airlyJson:
                :return: airly list
                """
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
