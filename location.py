import requests
import variables
import urllib


class Location:
    def getMapApiData(self, place):
        mapVariables = {
            'key': variables.MAP_API_KEY,
            'location': place+ ',pl',
            'thumbMaps': 'false',
            'maxResults': 1
        }
        resp = requests.get(variables.map_url + urllib.parse.urlencode(mapVariables))
        return resp.json()


