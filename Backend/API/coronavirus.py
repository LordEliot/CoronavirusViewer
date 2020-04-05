# encoding: utf-8
import requests

request = requests.get('https://www.datos.gov.co/resource/gt2j-8ykr.json')
response = request.json()

print("Coronavirus project: Colombia")
print("Current cases: " + str(len(response)))

counter = 0

for case in response:
    if case["ciudad_de_ubicaci_n"] == u"Ibagué":
        counter = counter + 1

print("Cases in Ibague: " + str(counter))
