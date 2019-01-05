import requests
import variables
import urllib


class Location:
    @staticmethod
    def getMapApiData(place):
        """
        this function is getting place from user and creating query for MAP_API
        :param place:
        :return: json response from MAP_API
        """
        mapVariables = {
            'key': variables.MAP_API_KEY,
            'location': place + ',pl',
            'thumbMaps': 'false',
            'maxResults': 1
        }
        resp = requests.get(variables.map_url + urllib.parse.urlencode(mapVariables))
        return resp.json()
