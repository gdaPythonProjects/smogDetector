import variables
import json
import location
import os
import airly


# def check(active):
#     if active == True:
#         return 'Włączony'
#     else:
#         return 'Wyłączony'
#
airlyValues = dict()
airlyIndexes = dict()
airlyStandards = dict()
airlyEnd = dict()
airlyD = []
airlyApiGet = airly.Airly()
airlyData = airlyApiGet.getAirlyApiMeasureData(204)
# print(json.dumps(airlyData, ensure_ascii=False, indent=4 * ' '))
# print(len(airlyData['current']['values']))
if len(airlyData['current']['values']) == 0:
    airlyIndexes = airlyData['current']['indexes']
    airlyD.append(airlyIndexes)
    status = {'working': 'False'}
    airlyD[0].append(status)
    print('cos')
else:
    airlyIndexes = airlyData['current']['indexes']
    airlyValues = airlyData['current']['values']
    airlyStandards = airlyData['current']['standards']
    airlyD.append(airlyIndexes)
    airlyD.append(airlyValues)
    airlyD.append(airlyStandards)
    airlyD.append({'working': 'True'})
    print(airlyValues)

print(len(airlyD))
for element in airlyD[0]:
    for k, v in element.items():
        airlyEnd.update({k: v})
't' \
''
# for element in airlyD[1]:
#     key = element['name']
#     value = element['value']
#     airlyEnd.update({key: value})

print(airlyEnd)


# i = 0
# for element in airlyData:
#     airlyD.append({
#         'id': element['id'],
#         'airly': element['airly'],
#     })
#     for k, v in element['address'].items():
#         airlyD[i].update({k: v})
#     i += 1
# print(airlyD)
# print('*%-25s %-25s %10s*' % ('miejscowosc', 'ulica', 'aktywnosc'))
# for element in airlyD:
#     print('*%-25s %-25s %10s*'
#           % (element['city'], element['street'], check(element['airly'])))
#
#
# # for elements in cityData['results']:
# #     for key, value in elements.items():
# #         if key == 'locations':
# #             for element in elements[key]:
# #                 cityDict.update({'street': element['street']})
# #                 cityDict.update({'city': element['adminArea5']})
# #                 cityDict.update({'district': element['adminArea3']})
# #                 cityDict.update({'postCode': element['postalCode']})
# #                 for k, v in element['latLng'].items():
# #                     cityDict.update({k: v})
# # print(cityDict)

#
# def is_palindrome(word):
#     word = word.lower()
#     i=0
#     for iss in word:
#         letter = -len(word)
#         if iss != word[-(len(word))+i]:
#             return False
#         i += 1
#     return True
# print(is_palindrome('deleveled'))